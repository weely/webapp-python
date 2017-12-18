python中文文档：http://docs.pythontab.com/python/python3.4/

## OS模块
  # 简介：是python的一个系统编程的操作模块，可以对系统文件与目录进行操作
  # 1.交互式方式下通过下面代码可查看os模块的帮助文档
  >>>import os
  >>>help(os)
  # 2.重要函数及变量
  os.sep 更改操作系统中的路径分布
  os.getcwd()获取当前执行路径
  os.listdir() 列出当前目录下的所有文件及文件夹
  os.remove() 可删除指定文件
  os.system() 用来运行shell命令
  os.chdir() 改变当前目录到指定目录
  # os模块函数作用详解
  os.system函数可运行shell命令外
  也还有一些函数可执行外部程序，包括execv，它会退出python解析器，并将控制权交给被执行的程序
  os.变量主要用于系统路径中的分隔符
  # os.path 详解
  1. os.path.absPath(filename) 返回文件的绝对路径
  2. os.path.split(path)  将path分割成目录和文件名的二元组返回  path = e:/test/test.png  返回 e:/test, test.png
  3. os.path.dirname(path) 返回path的目录，就是 os.path.split(path) 的第一个元素
  4. os.path.commonprefix(list) 返回list中所有path共有的最长路径
      os.path.commomprefix(['/home/td', '/home/td/ff', '/home/td/fff'])   -> '/home/td'
  5. os.path.basename(path) 返回path最后的文件名，如果path以/或\结尾，就返回空值，即 os.path.split(path) 的第二个元素
  6. os.path.exists(path) 判断path是否存在，存在返回True，不存在返回False
  7. os.path.isabs(path) 如果path是绝对路径，返回True
  8. os.path.isfile(path) 如果path是存在的文件，返回True
  9. os.path.isdir(path) 判断是否为目录
  10. os.path.join(path1[,path2[,...]])  组合路径并返回
  11. os.path.normcase(path) window系统下将路径转换为小写返回
  12. os.path.normpath(path) 规范化路径
  13. os.path.splitdrice(path)  返回(drivername, fpath) 元组
  14. os.path.splitext(path) 分割文件路径和后缀名并返回对应元组
  15. os.path.getsize(path)  返回path文件大小(字节数)
  16. os.path.getatime(path) 返回文件最后存取时间(时间戳)
  17. os.path.getmtime(path) 返回最后修改时间(时间戳)
  18. os.path.islink(path)    
  19. os.path.realpath(path)  返回规范绝对路径  eg:os.path.realpath(test.txt)   返回 e:test/test.txt  (不论test.txt是否存在)

  # eg:
  import os
  print(os.getcwd())                  #获取当前路径
  print(os.listdir('c:\window'))      #列出目录下所有文件及文件夹，window下相当于 dir
  print(os.mkdir("test"))             #创建test目录
  print(os.rmdir('c))                 #删除 c目录
  print(os.rename('abc.txt', 'newname.txt'))      #重命名文件

## SYS模块
  # 简介：用来处Python 运行时配置及资源，从而可与当前程序外的系统环境交互
  * 导入模块：
  >>>import sys
  >>>dir(sys)        #查看模块中的可用方法
  # sys模块常用函数变量
  * 变量
  sys.stdin 标准输入流
  sys.stdout 标准输出流
  sys.stderr 标准错误流
  sys.path 查找模块所在目录的目录列表名
  sys.argv 命令行的参数，  sys.argv[0] 表示脚本名称
  sys.platform 返回当前系统平台，eg：win32,linux
  * 函数方法
  sys.exit([arg]) 方法可以退出当前程序，可提供整数类型参数
  /sys.modules 方法可将模块的名字映射到实际存在的模块上，只应用于目前导入的模块
  /sys.getdefaultencoding() 获取系统当前编码，一般默认ascii
  /sys.setdefaultencoding() 设置系统默认编码，dir(sys)不可见，执行不通过时可以先执行 reload(sys)

## re 正则表达式
  # 简介: 
  # python re 正则表达式语法
  * 匹配字符
  1. '.'  匹配任意除换行符，即除 "\n" 以外的任意字符
  2. '\'  转义符
  3. '[]' 中括号用来创建字符集， 第一个出现字符如果是 ^ ,表示反向匹配
  * 预定义字符集
  \d   匹配数字，eg: [0,9]
  \D   与 \d 相反，匹配所有非数字字符
  \s   空白字符， eg: 空格， \t\r\n\f\v
  \S   非空白字符
  \w   单词字符(数字及字母)，eg: A~Z, a~z, 0~9
  \W   非单词字符
  * 
  '*'        0次及以上
  '+'        1次及以上
  '?'        0或1次
  '{m}'      m次
  '{m,n}'    m至n次
  * 常用函数
  re.compile()  创建
  re.search()   查询
  re.match()    匹配
  re.split()    分割
  re.findall()  
  re.sub(old,new)   替换
  re.escape()   转义

## time模块
  # 可以使用时间戳 、 格式化的时间(str) 、 元组(struct_time)及calendar表示时间
  # 元组struct_time 有9个元素
  time.localtime([secs])  返回time.struct_time() 元组
  time.struct_time(tm_year=2017, tm_mon=5, tm_mday=25, tm_hour=15, tm_min=24, tm_sec=43, tm_wday=3, tm_yday=145, tm_isdst=0)
  # 常用函数
  time.localtime([secs])    将时间戳转换成当前时区的时间结构，返回的是一个元组，参数默认为当前时间
  time.time()   返回纪元开始的总秒数(float值)
  time.ctime()  将一个时间戳转换为时间字符串   
      eg: time.ctime(time.time()) ->'Thu May 25 15:20:36 2017'
  time.sleep()  暂停程序，参数以秒计
  time.clock() 返回浮点数可计算程序的总运行时间，也可以计算两次clock()的间隔
  time.strftime() 将struct_time元组按照规定输出字符串
  #时区相关 pytz: tz1 = pytz.timezone('Asiz/Shanghai) (pytz为python2版本的)



## pickle持久化
  # pickle模块将任意一个Python对象转换成系统字节的过程叫做串行化对象
  # pickle 与 cpickle对比
  前者用pickle模块，后者用c实现，速度比pickle快几倍，推荐使用cpickle
  # 常用方法： 
  序列化/反序列化
  * pickle.dump(obj, file, protocol=None, *, fix_imports=True) 提示持久化的对象，保存到文件，使用的协议，默认为0->ASCII,1->旧式2进制，2->新式2进制，2比1高效
      Write a pickled representation of obj to the open file object file. This is equivalent to Pickler(file, protocol).dump(obj)
  * pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict")  与dump相反
      Read a pickled object representation from the open file object file and return the reconstituted object hierarchy specified therein. This is equivalent to Unpickler(file).load().
  # eg：
  import pickle



## random 随机
  # 生成随机浮点数、整数、字符串、随机选择列表中的元素，打乱数据等等
  # 重要函数
  random.random() 返回 0 <= n < 1 之间的随机浮点数
  random.uniform(a,b) 可以设定浮点数的范围，设置上下限(选取a~b中的浮点数,a、b为任意实数)
  random.randint(a,b) 随机生成a~b中的一个整数int(a,b为整数, a <= b)
  random.choice(seq) 从序列中返回随机元素, seq可以为list, tuple, set
  random.getrandbits(n) 以长整数形式返回n个随机位
  random.shuffle(seq[,random]) 原地指定seq序列
  random.sample(seq, n) 从序列seq中选择n个随机且独立的元素
  # eg:
  random.uniform(-1.43, -423)  输出-423 到 -1.43之间的浮点数

## csv模块
  python内置模块，导入： import csv
  #主要函数
  csv.reader(csvfile, dialect='excel', **fmtparams) 读取csv文件数据
  csv.writer(csvfile, dialect='excel', **fmtparams) 写入csv文件数据
  # eg:
  with open('csv_test.csv', newline="") as csvfile:
      reader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
      for row in reader:
          print(','.join(row))
          print(row)
  with open('csv_test.csv', 'w', newline="") as csvfile:
      writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(['Spam'] * 5 + ['Baked Beans'])
      writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

## logging模块
  http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
  调用：
  import logging
  logging 日志级别： critical > error > warning > info > debug > noset
  默认的日志级别为 warning
  level：CRITICAL   Numeric value：50(CRITICAL/50)、
          ERROR/40、WARNING/30、INFO/20、DEBUG/10、NOTSET/0
  logging.basicConfig函数对日志的输出格式及方式做相关配置：
  logging.basicConfig(level=logging.DEBUG, 
      format='%(asctime)s % (filename) s [line:%(lineno)d] % (levelname)s %(message)s',
      datefmt='%a, %d %b %Y %H:%M:%S',
      filename='myapp.log',
      filemode='w')

## Socket 套接字模块
  模块支持TCP/IP,UDP/IP, ICMP/IP协议，创建服务端与客户端套接字
  import socket
## Json模块/ json encoder and decoder
  import json
  json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
  #
  * json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
      Serialize obj to a JSON formatted str using this conversion table. The arguments have the same meaning as in dump().
  * json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
      Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object using this conversion table.

## urlparse 模块： 将一个普通的URl解析成6个部分，返回的数据类型都是元组，同时可将分解的组合成url
  * 注意: The urlparse module is renamed to urllib.parse in Python 3. 
          The 2to3 tool will automatically adapt imports when converting your sources to Python 3.
      import urlparse
  # 方法：
  urlparse.urlparse() 分解url，返回元组
  urlparse.urlunparse()  接受元组，组合成url
  urlparse.urlsplit(url) 
  urlparse.unjoin(base, url)
## urllib模块/python 3.5
  参考博客：http://www.cnblogs.com/Lands-ljk/p/5447127.html
  官方文档： https://docs.python.org/3.5/library/urllib.html
  urllib.request for opening and reading urls
  urllib.error containing the exceptions raised by urllib.request
  urllib.parse for parsing URLS
  urllib.robotparser for parsing robots.txt

  # urllib.request:
    urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
      data: 发送到服务器的data必须是bytes对象,或者是指定的可迭代的在头部指定了content-Lenght的对象; 
        eg: req_data = parse.urlencode([("email", r"lm220930@163.com"),])
      timeout: 可选参数，设置请求访问时响应超时时间
      context: 如果指定了上下文，则它是描述各种SSL选项的ssl.SSLContext实例
      The optional cafile and capath parameters specify a set of trusted CA certificates for HTTPS requests
      The cadefault parameter is ignored
      通过context manager 返回的对象返回以下几个可供调用的函数
      function:
        geturl() :返回访问的url
        info() :返回访问的头部信息
        getcode(): 返回响应的状态码
      Note that None may be returned if no handler handles the request
      如果代理*_proxy变量设置时，proxyhandler需要被安装，请求需要通过代理来处理
    urllib.request.install_opener(opener)
    urllib.request.builder_opener(opener)
    urllib.request.pathname2url(path):     把本地路径转换为url路径,联合quote()
    urllib.request.url2pathname(path):     把url路径转换为本地路径 ,unquote()
    urllib.request.getproxies(): 返回proxy的一个 dict
    hanler...
    Request Objects:
      * urllib.request.Request(url, data=None, headers={}, method=None)
      Request.full_url  /  Request.type  /  Request.host  /  Request.selector  /  Request.data  /method  /  unverifiable 
      Request.get_method()  /  add_header(key, val)  / add_unredirected_header(key, header)  /  has_header(header)  / remove_header(header)  /  get_full_url()
      Request.set_proxy(host, type)  /  Request.get_header(header_name, default=None)  /  Request.header_items()
    OpenerDirector Objects:
      OpenerDirector.add_handler(handler)  /  OpenerDirector.open(url, data=None[, timeout])  /  OpenerDirector.error(proto, *args)
    BaseHandler Objects:
      BaseHandler.add_parent(director) :Add a director as parent.  
      BaseHandler.close(): remove any parents
    HTTPRedirectHandler Objects:
      HTTPRedirectHandler.redirect_request(req, fp, code, msg, hdrs, newurl)
    HTTPCookieProcessor Objects:
      HTTPCookieProcessor.cookiejar:  存储cookie
  * URL Parsing:
    urllib.parse.urlparse(urlstring, scheme='',allow_fragments=True):
      转换url为6个元素
      >>> o = parse.urlparse("http://www.baidu.com")
      >>>o
      ParseResult(scheme='http', netloc='www.baidu.com', path='', params='', query='', fragment='')
      >>>o.scheme
      'http'
    urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
    ...
## urllib2模块

## robotparser解析


## Cookie模块


## smtplib模块

## Base64模块

## xmlrpclib客户端

## string文本

## queue模块
  调用模块：import queue

## math数学计算

## linecache缓存

## threading多线程

## sqlite3数据库

## gzip压缩解压


## tkinter
  图表网站：http://matplotlib.org/users/screenshots.html
  matplotlib.org/downloads.html
  window下安装matplotlib:注意python版本：
  python -m pip install -U pip setuptools
  python -m pip install matplotlib

  import tkinter as tk
  from tkinter import ttk
  relief样式属性值：tk.SOLID,tk.SUNKEN,tk.RAISED,tk.FLAT,tk.GROOVE,tk,RIDGE,
  justify样式属性值：tk.LEFT,tk.RIGHT,tk.TOP,tk.BOTTOM
  borderwidth: 控件边框线宽度
  font: 控件字体样式 
  标签：
  Label(father_widget,text='label'[,width=0,height=0,textvariable,background(bg)='blue',relief=tk.FLAT,justify=tk.LEFT,\
          borderwidth=1,font=('tahoma','8','normal')])

  输入框：
  Entry(father_widget,textvariable,...)
  按钮：
  Button(father_widget, text='button',command=command,...)
  下拉框：
  ttk.Combobox(father_widget,textvariable=tk.IntVar(),values=[...])
  多行文本框：
  from tkinter.srcolledtext import Scrolledtext
  Scrolledtext
  标签框架：
  LabelFrame(father_widget, text='labelframe')
  菜单：
  from tkinter import Menu
  菜单栏： menuBar = Menu(root)
  初始化菜单对象： menuitem = Menu(menuBar,tearoff=0)
  添加菜单到菜单栏： mebuBar.add_cascade(label='',menu=menuitem)
  添加子菜单项： menuitem.add_command(label='item',command=command)
  spinbox:
  from tkinter import Spinbox
  spinbox = tk.Spinbox(father_widget,from_=1,to=10,bd=10,[command=command,values=(1,2,...10)])

## ipython
  # 安装：
  linux：
    ubuntu: sudo apt-get install ipython
  # 使用：
    %logstart  ->  开启日志记录
    %logoff    ->  关闭日志记录
    使用ipython执行系统shell命令时，需在命令前加上！
      eg:  !date  ->  输出系统时间，   !dir  ->  即shell命令下的dir
      实际上是以！为前缀的任何内容都会被发送到系统shell
    %hist：该命令显示历史记录， 使用 -g选项可以对%hist进行搜索
      eg: %hist -g a  :搜索历史输入的指令中包含a的行并返回
    Magic函数：Magic函数以% 符号开始，如果只用作单行命令，可省略%
    
    numpy库常用函数：
      sqrt:计算素组元素的算术平方根
      log:计算数组元素的自然对数
      arange:生成一个指定范围的数组
      astype:把数组元素转换为指定数据类型
      sum：计算数组元素之和
      ceil：对数组元素向上取整
      modf：返回浮点数的小数部分及整数部分
      where：返回取值符合条件的数组元素的索引值
      ravel：返回一个展开的一维数组
      take：从数组取出指定元素
      sort:对数组元素排序
      outer：返回两个数组的外积
      diff：计算离散差分，默认计算一阶差分
      sign：返回数组元素的符号
      eig：返回数组元素的特征值及特征向量
      histogram,ployfit
      compress,randint