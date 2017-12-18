#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio
from aiohttp import web
import os
from coroweb import get, post
from apis import APIValueError, APIResourceNotFoundError, APIError, APIPermissionError, Page
from models import User, Comment, Blog, next_id
from config import configs
import markdown2

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

def user2cookie(user, max_age):
    '''
    Generate cookie by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.password, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

async def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.password, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.password = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@get('/')
async def index(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    page = Page(num, page_index, page_size=5)
    if num == 0:
        blogs = []
    else:
        blogs = await Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

@get('/about/home')
async def about_home():
    return {
        '__template__': 'about_home.html',

    }

@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_comment = text2html(c.content)
    # blog.html_comment = text2html(blog.content)
    blog.html_comment = markdown2.markdown(blog.content)
    return {
        '__template__' : 'blog.html',
        'blog': blog,
        'comments': comments
    }

@get('/note')
async def get_note():
    file = os.path.join(os.path.split(__file__)[0], r'static\\python_study.md')
    if os.path.exists(file):
        update_time = os.path.getmtime(file)
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
            html = markdown2.markdown(data)
            res = {
                "update_time": update_time,
                "html": html
            }
    else:
        res = {
            "update_time": 0,
            "html": None
        }
    return {
        '__template__': 'note.html',
        'note': res
    }

@get('/register')
def register():
    return {
        '__template__' : 'register.html'
    }

@get('/signin')
def signin():
    return {
        '__template__' : 'signin.html'
    }

@get('/user/{id}')
async def user_edit(id):
    # user = request.__user__
    user = await User.find(id)
    user.password = '******'
    return {
        '__template__': 'user.html',
        'user': user
    }

@post('/api/authenticate')
async def authenticate(*, email, password):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not password:
        raise APIValueError('password', 'Invalid password.')
    users = await User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # check password
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(password.encode('utf-8'))
    if user.password != sha1.hexdigest():
        raise APIValueError('password', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.password = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r

@get('/show/user/img/{id}/edit')
async def show_user_img_edit_(id):
    user = await User.find(id)
    return {
        '__template__': 'user_img_edit.html',
        'user': user
    }


@post('/user/img/{id}/edit')
async def user_img_edit(id, request):
    reader = await request.multipart()
    # /!\ Don't forget to validate your inputs /!\
    # reader.next() will `yield` the fields of your form
    field = await reader.next()
    filename = field.filename
    filepath = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static/img/', filename);
    if os.path.exists(filepath):  filepath = os.path.normpath(filepath)

    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'static/img/', filename), 'wb') as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)
    user = await User.find(id)
    blogs = await Blog.findAll("user_id=?", [id])
    comments = await Comment.findAll("user_id=?", [id])
    for comment in comments:
        comment.user_image = "/static/img/{}".format(filename)
        await comment.update()
    for blog in blogs:
        blog.user_image = "/static/img/{}".format(filename)
        await  blog.update()
    user.image = "/static/img/{}".format(filename)
    await user.update()
    return dict({"msg": '{} sized of {} successfully stored'.format(filename, size)})
    # return web.Response(text='{} sized of {} successfully stored'.format(filename, size))


@get('/manage/')
def manage():
    return 'redirect:/manage/blogs'

@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__' : 'manage_blogs.html',
        'page_index' : get_page_index(page)
    }

@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__' : 'manage_blog_edit.html',
        'id' : '',
        'action': '/api/blogs'
    }

@get('/manage/blogs/edit')
def manage_blogs_edit(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id
    }

@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

@get('/api/comments')
async def api_comments(*, page='1'):
    page_index = get_page_index(page)
    num = await Comment.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = await Comment.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

@post('/api/blogs/{id}/comments')
async def api_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = await Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.name, user_image=user.image, content=content.strip())
    await comment.save()
    return comment

@post('/api/comments/{id}/delete')
async def api_delete_comments(id, request):
    check_admin(request)
    c = await Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    await c.remove()
    return dict(id=id)

@get('/api/users')
async def api_get_users(*, page='1'):
    page_index = get_page_index(page)
    num = await User.findNumber('count(id)')
    # print(num, type(num))
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = await User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.password = '******'
    return dict(page=p, users=users)

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@post('/api/users')
async def api_register_user(*, email, name, password):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not password or not _RE_SHA1.match(password):
        raise APIValueError('password')
    users = await User.findAll("email=?", [email])
    if len(users) > 0:
        raise APIError('register failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' %  (uid, password)
    user = User(id=uid, name=name, email=email, password=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), \
            image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    await user.save()
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user,86400), max_age=86400, httponly=True)
    user.password ='******'
    r.content_type='application/json'
    r.body=json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@post('/api/user/{id}/edit')
async def api_user_edit(id, *, email, name, password):
    if not name or not name.strip():
        raise APIValueError('name')
    if not password or not _RE_SHA1.match(password):
        raise APIValueError('password')
    user = await User.find(id)
    comments = await Comment.findAll("user_id=?", [id])
    blogs = await Blog.findAll("user_Id=?", [id])
    user.name = name
    sha1_passwd = '%s:%s' % (user.id, password)
    user.password = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
    await user.update()
    for comment in comments:
        comment.user_name = name
        await comment.update()
    for blog in blogs:
        blog.user_name = name
        await  blog.update()
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user,86400), max_age=86400, httponly=True)
    user.password ='******'
    r.content_type='application/json'
    r.body=json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@post('/api/manage/user/{id}/admin')
async def api_manage_user_admin(id, *, admin):
    user = await User.find(id)
    user.admin = admin
    await user.update()
    # users = User.findAll()
    # r = web.Response()
    return dict({"msg": 'update user info successful!'})

@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    blog = await Blog.find(id)
    return blog

@get('/api/blogs')
async def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = await Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)

@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image,\
                name=name.strip(), summary=summary.strip(), content=content.strip())
    await blog.save()
    return blog

@post('/api/blogs/{id}')
async def api_update_blog(id, request, *, name, summary, content):
    check_admin(request)
    blog = await Blog.find(id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    await blog.update()
    return blog

@post('/api/blogs/{id}/delete')
async def api_delete_blog(request, *, id):
    check_admin(request)
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id])
    for comment in comments:
        await comment.remove()
    await blog.remove()
    # await comments.remove()
    return dict(id=id)
