https://devcenter.heroku.com/start

### python内置函数： https://docs.python.org/3/library/functions.html
### 开启shell
	1、os.system(path)
	2、subprocess.Popen(args, bufsize=0, executable=None, \
							 stdin=None, stdout=None, stderr=None, \
                             preexec_fn=None, close_fds=False, shell=False, \
                             cwd=None, env=None, universal_newlines=False,\
                             startupinfo=None, creationflags=0)
### 搭建自己的vpn
	http://ilinuxkernel.com/?p=1594

### python量化学习
	https://www.ricequant.com/courses/?utm_source=tab

###  SQLite
	SQLite数据库中的信息存在于一个内置表sqlite_master中，在查询器中可以用
	select * from sqlite_master来查看，如果只要列出所有表名的话，则只要一个语句:
	SELECT name FROM sqlite_master WHERE type='table' order by name，因为表的列type固定为'table'

### git
	git使用：
	下载安装git
	配置git: git config --global user.name "..."
			git config --global user.email "..."
			git config --list 查看配置信息
	git init初始化
	本地建立库
	git clone ....
	http://blog.jobbole.com/78960/
### 模块
	在Python中，一个.py文件就称之为一个模块（Module）
	包的引用：mycompany.abc    	mycompany->目录，abc.py表示Python文件
	每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包
	__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
	如果包中的 __init__.py 代码定义了一个名为 __all__ 的列表，就会按照列表中给出的模块名进行导入

### json
	对象表示为键值对
	数据由逗号分隔
	花括号保存对象
	方括号保存数组

### apache安装
	apache官网未提供window编译好的安装包，可在apachehus网站上下载
	下载后解压放到相应位置即可，在执行 httpd.exe -k install 配置服务器名，修改配置文件 root变量名为相应apache的路径
### apache删除
	先停止Apache服务，具体进入windows下的服务，apache24服务，手动停止其服务。（也可以通过ApacheMonitor.exe来关闭其服务）
	<!--然后以管理员运行CMD窗口，在窗口中输入sc delete apache。回车后会告知Apache服务已经被删除，这时就可以手动删除Apache目录了。-->
	配置了服务器名的apache需要以管理员身份打开cmd，执行 httpd.exe -k uninstall [服务器名]
	以上windows下的Apache的下载、安装配置与卸载都以完毕
### flask配置apache
	http://www.bkjia.com/xtzh/1014628.html
	http://blog.csdn.net/meloyi/article/details/55684507
	http://blog.csdn.net/kaka20099527/article/details/52191370
	配置文档：https://github.com/GrahamDumpleton/mod_wsgi/blob/develop/win32/README.rst
	文档中均有对应的下载链接
	下载相同vc编译的apache，python，mod_wsgi
	下载网站：
	apache:http://www.apachehaus.com/cgi-bin/download.plx;  (warn：v10编译的apache在文档中提供了下载链接)
	mod_wsgi: http://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
	下载好编译的apache，python，直接安装；
	apache安装好后，配置服务器名(以管理员身份打开cmd，执行 httpd.exe -k install [服务器名],方括号表示可以缺省)
	使用pip install mod_wsgi.whl  (为python安装对应的mod_wsgi包)
	使用vc编译下载的mod_wsgi,生成mod_wsgi.so文件(正常会自动加载到apache的mod文件夹下，(apache配置好路径))
	编译过程： 下载mod_wsgi源码，非python的mod_wsgi安装包
	mod_wsgi-4.5.15链接：http://modwsgi.readthedocs.org/en/latest/release-notes/version-4.5.15.html
	安装好对应版本vc编译器，设置好vc编译器的环境变量
	设置 include，lib环境变量(导入vc包的头文件)
	以管理员身份打开cmd，执行 cmdnmake -f ap24py34-win32-VC10.mk install  (编译成功会生成mod_wsgi.so文件到apache的模块文件夹下)
	apache配置，http.conf 配置文件添加 LoadModule wsgi_module modules/mod_wsgi.so
	添加app.wsgi文件，链接python及apache，修改apaceh虚拟端口文件如下：
		<VirtualHost *:80>
				ServerName  example.com
				WSGIScriptAlias / C:\pyAutoTradeSystem\app.wsgi
				DocumentRoot "C:\pyAutoTradeSystem"
				<Directory "C:\pyAutoTradeSystem">
					Order allow,deny  
					Allow from all
				</Directory>
		</VirtualHost>

### python字符转换及其他转换：
	print(str.upper())          # 把所有字符中的小写字母转换成大写字母
	print(str.lower())          # 把所有字符中的大写字母转换成小写字母
	print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
	print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

	int(x [,base ])         将x转换为一个整数    		int()函数提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
	long(x [,base ])        将x转换为一个长整数    
	float(x )               将x转换到一个浮点数    
	complex(real [,imag ])  创建一个复数    
	str(x )                 将对象 x 转换为字符串    
	repr(x )                将对象 x 转换为表达式字符串    
	eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
	tuple(s )               将序列 s 转换为一个元组    
	list(s )                将序列 s 转换为一个列表    
	chr(x )                 将一个整数转换为一个字符    		
	unichr(x )              将一个整数转换为Unicode字符    
	ord(x )                 将一个字符转换为它的整数值    
	hex(x )                 将一个整数转换为一个十六进制字符串    
	oct(x )                 将一个整数转换为一个八进制字符串   

	ljust(width[,fillchar]) 左对齐
	rjust(width[,fillchar])  右对齐函数
	center(width[,fillchar]) 
	print('hello'.center(10,'*'))
	输出： **hello***

	#  chr(65) = 'A'
	#  int('2') = 2
	#  str(2) = '2'

### print格式化输出（输出注意空格个数）
	* 1.打印字符串
	print("His name is %s" % ("xiaoming"))
	输出: His name is xiaoming
	* 2.打印整数
	print("He is %d years old" % (18))
	输出: He is 18 years old
	* 3.打印浮点数(默认6位小数)
	print("His weight is %f kg" % (62.5))
	输出: His weight is 62.500000 kg
	* 4.打印指定小数位浮点数
	print("His height is %.2f m" % (1.80))
	输出: His height is 1.80 m
	* 5.指定占位符宽度
	print("Name:%6s Age:%4d Height:%4.2f"%("David",25,1.83))
	! 变量s占6个字符，不足的用空格补充
	输出: Name: David Age:    25 Height:    1.83
	* 6.指定占位符宽度(左对齐)
	print("Name:%-8s Age:%-8d Height:%-8.2f"%("Dviad",25,1.83))
	输出: Name:David    Age:25       Height:1.83
	* 7.指定占位符
	print("Name:%-4s Age:%04d Height:%04.2f"%("Dviad",25,1.83))
	输出: Name:Dviad Age:00000025 Height:00001.83
	* 8.科学计数法
	print(format(0.000015, '.2e'))
	输出结果为字符串: '1.50e-04'

### 字符串的相关方法
	eg: a = 'apple'
	a = a.replace('a','A')
	a输出为Apple
	## 字符转数组
	str = '1,2,3'
	arr = str.split(',')
	#数组转字符
	arr = ['a','b']
	str = ','.join(arr)
	##
	str为字符串 
	str.isalnum() 所有字符都是数字或者字母 
	str.isalpha() 所有字符都是字母 
	str.isdigit() 所有字符都是数字 
	str.islower() 所有字符都是小写 
	str.isupper() 所有字符都是大写 
	str.istitle() 所有单词都是首字母大写，像标题 
	str.isspace() 所有字符都是空白字符、\t、\n、\r


### 编码问题
	f.open(filename, encoding='utf-8')来解决，一般选择utf-8编码
	strTest = strTxt.decode('utf-8', 'ignore')
	默认的参数就是strict，代表遇到非法字符时抛出异常；
	如果设置为ignore，则会忽略非法字符； 
	如果设置为replace，则会用?号取代非法字符； 
	如果设置为xmlcharrefreplace，则使用XML的字符引用

### 详解Python中的下划线：http://python.jobbole.com/81129/
	# 单下划线：
	* 1.在解释器中：在这种情况下，“_”代表交互解释器会话上一条执行的语句的结果
	* 2.作为一个名称：此时“_”作为临时性的名称使用
	* 3.国际化：“_”作为函数使用
	* （2与3存在冲突，避免国际化时使用）

	# 名称前的下划线：(_egg)
	* 使用该下划线表示名称属性“私有”
	* 通过"from <模块/包名> import *" 引入的，以“_”开头的名称不会被导入，除非模块或包中
	* 的“__all__”列表显示的包含了他们

	# 名称前的双下划线"__"：
	* 避免与子类定义的名称冲突

	# 名称前后的双下划线(__init__)：

### 训练字体：
	# 1.将图片转换成tif格式，用于生成box文件：
	*	更改图片名称，tif文件命名格式[lang].[fontname].exp[num].tif
	*	lang->语言，fontname->字体
	# 2.生成box文件
	*	tesseract mjorcen.normal.exp0.jpg mjorcen.normal.exp0 -l chi_sim batch.nochop makebox
	*	
	*	tesseract mjorcen.order.exp0.jpg mjorcen.order.exp0 -l chi_sim batch.nochop makebox
	# 3.打开JTessBoxEditor矫正错误并训练
	# 4.训练
	* tesseract  mjorcen.testt.exp0.jpg mjorcen.testt.exp0  nobatch box.train
	* unicharset_extractor mjorcen.testt.exp0.box
	# 新建font_properties文件
	* 输入  normal 0 0 0 0 0   表示默认普通字体
	# 命令行执行以下语句
	* shapeclustering -F font_properties -U unicharset mjorcen.testt.exp0.tr  
	* mftraining -F font_properties -U unicharset -O unicharset mjorcen.testt.exp0.tr  
	* cntraining mjorcen.testt.exp0.tr
	# 将新生成的5个文件合并
	* combine_tessdata  testt.
	# 得到训练的字库

### os._exit() && sys.exit()比较
	* os._exit()直接退出python，其后代码不会执行，
	* sys.exit()引发SystemExit异常，若没有捕获异常，python解析器直接退出，捕获异常可以做些清理工作，0为正常退出，其他数字（1—127）为不正常
	* 一般os._exit()用于线程退出，sys.exit()用于主线程退出

### #!/usr/bin/env python3  与 #!/usr/bin/python 区别
	* （目的就是指定脚本用什么可执行程序执行）
	* #!/usr/bin/python 是告诉操作系统执行脚本的时候是调用 /usr/bin  下的python解释器
	* #!/usr/bin/env python3 这种写法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里，
	* 当系统看见该行时，首先会到env设置里查找python安装路径，再调用对应路径下解析器
	# 推荐使用 #!/usr/bin/env python 这种写法

### python安装：
	# Mac：自带python2.7，python3.6官网下载安装，或安装了Homebrew的话直接通过brew install python3
	# linux:
	# window：下载相应版本安装
	* 注意选择  install  launcher for ... 和 add Python 3.5 to path(添加环境变量)，以及添加pip

### python解析器：
	* CPython：CPython  为C语言开发的自带的官方的python解析器（命令行下运行python就是启动CPython解析器）
	* IPython：基于CPython之上的交互式解析器（只是在交互式上有所增强，其他与CPython一样）
	* PyPy：目标是执行熟读，采用JIT技术，对python代码动态编译，可显著增强python代码的执行速度，
	*	大多python代码均可在pypy上执行，但有部分与cpython有差异，需要清楚两者的不同之处
	* Jython：运行在java平台上的python解析器，可直接将python代码编译成java字节码
	* IronPython与Jython类似，不过是运行在微软.net平台上的python解析器，可直接将python代码编译成.net字节码

	## 在mac与linux上，可以直接运行python文件，前提是添加了权限（chmod a+x hello.py）	./hello.py就可以执行

### python输入与输出：
	输出：	用print() 输出字符串，字符串可通过‘，’逗号连接，逗号处会输出空格， print也可以打印整数
		print('100 + 200 =', 100+200) =>输出  100 + 200 = 300    逗号为300前的空格
	输入： input() 函数输入字符串

### python是大小写敏感的
### 常见规则
	可以通过转义字符\来输入特殊字符，eg： \'  ->输入  ',
	python允许用  r''  表示 ‘’ 内部的字符串默认不转义
	python允许用  '''...'''  的格式表示多行内容，多行字符前也可以添加  r
	布尔值True，False，可以用 and、or和not运算
	空值  用None表示
	变量名必须是大小写的英文、数字和_ 组合，且不能以数字开头
	python中常量通常全部大写的变量表示，但实际上表示的常量仍为变量
	地板除//与除/，

	python对bytes类型的数据用带b的前缀的单引号或双引号表示（bytes的每个字符只占一个字节）
	以unicode表示的str通过encode()方法可以编码为指定的bytes（字符码变字节码）
	decode()与encode()相反（字节变字符）
	可用len()函数测定字符长度
	%d  ->整数
	%f  ->浮点数
	%s  ->字符串
	%x  ->十六进制整数
	只有一个占位符 %?   ,括号可以省了
	list有序集合 lists = ['a','b','c']  ,取  lists[i-1]，取第i个,  反向取  lists[-i], 倒数第 i 个，  使用append()函数添加元素到末尾，
		使用insert(i,value)插入到i位置, 使用pop()删除末尾元素, 使用pop(i)删除第i处元素, list.sort(),使用sort()方法对list进行排序
	tuple元组，不变的list
	tupledemo = (1,2,3)
	dict(dictionary)类似于字典，查询速度快：  dictdemo = {'a':1, 'b':2}    dictdemo['key'] = value  添加元素
	取dict中的元素可以直接使用dict[key],还可通过get()方法，使用get()如果key不存在，返回None
		删除key用pop(key)方法
	dict内部存放的顺序与key放入的顺序无关
	通过“ key in dict ” 可以判断键是否存在于dict中
	dict相当于java中的map(映射)
	dict的key必须是不可变对象，list是可变的，因此不能作为key
	* 和list比较，dict有以下几个特点：
		1、查找和插入的速度极快，不会随着key的增加而变慢；
		2、需要占用大量的内存，内存浪费多。
	set   setdemo = ([1,2,3])
	set中没有重复的key，
	添加元素用add(key)方法
	删除元素使用remove(key)
	set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

### 函数
	abs(-10)是函数调用，而abs是函数本身
	函数名是一个指向函数对象的引用，可以把函数名赋值给一个变量，相当于取了一个别名
	a = abs   a(-1)  返回1
	定义函数时，确定函数名及参数
	有必要的话可以对参数进行检查
	函数体内部可以用return随时返回函数结果
	函数执行完毕没return时，自动返回return None
	函数可以同时返回对个参数，但其实是一个tuple
	默认参数：1、必选在前，默认在后，否则报错；2、当函数有多个参数时，把变化大的放前，变化小的放后    
	可变参数，参数前面加 *
	关键字参数， 参数前加 **
	对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
	*args是可变参数，args接收的是一个tuple；

	**kw是关键字参数，kw接收的是一个dict。

### 递归函数 ：函数自己调用自己
### 高级特性：切片 slice   eg: L = [1,2,3,4]   取前3个  L[0:3]  L[0:3] 表示从索引0开始，直到索引3为止，但不包括3，
		如果第一个索引是0，可以省略， L[:3]  等效于  L[0:3];也可以倒数切片， L[-2:] ，注意倒数第一个索引是-1
		L[:10:2]  ->表示前10个，每两个取一次， 取5个
		L[::5] ->取所有，每5个取一次
		L[:] ->复制list
	tuple、字符string 也可以切片
		L[起始位置:结束位置:(方向)步长]
		方向大于0， 起始位置  <  结束位置
		方向小于0， 结束位置  >  起始位置
		
	orderIds = map(int, request.args.get('orderIds').split(r','))
	print(list(orderIds))		-> 有值
	print(list(orderIds))		-> 为空的list
	orderIds初始处理的有值，之后就为空了

### 迭代:
	from collections import Counter:
		对序列的各元素进行计数，
		Counter([1,2,3,4,1,2,1,1,2,3]) = Counter(({1:4, 2:3, 3:2, 4:1}))
	for迭代dict， 迭代dict过程中不按次序出牌
		d = {'a':1, 'b':2, 'c':3}
		for key in d: 			->迭代键
		for value in d.values(): 	->迭代值
		for k,v in d.items()：		->迭代键、值 
	判断是否可迭代，使用collections模块的iterable类型判断
	使用zip()函数可以迭代多个数组
	>>> from collections import Iterable
	>>> isinstance('abc', Iterable)
	True
	使用enumerate函数可以将list变成索引-元素对
		for i,value in enumerate(list)：
			print(i,value)
		for x,y in [(1,2),(3,4),(5,6)]:
### 列表生成式,即List Comprehensions
	[x * x for x in range(1,11) if x % 2 == 0]
	生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
	把list、dict、str等Iterable变成Iterator可以使用iter()函数：
	>>> isinstance(iter([]), Iterator)
	True
	##
	* 凡是可作用于for循环的对象都是Iterable类型；
	* 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
	* 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
	* Python的for循环本质上就是通过不断调用next()函数实现的
	eg:
		# 首先获得Iterator对象:
		it = iter([1, 2, 3, 4, 5])
		# 循环:
		while True:
			try:
				# 获得下一个值:
				x = next(it)
			except StopIteration:
				# 遇到StopIteration就退出循环
				break


### map()/reduce()函数
	map()接收两个参数，一个是函数，一个是Iterable;map将传入的函数依次作用到序列的每个元素，并把结果作为新的iterator返回
	reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
### filter: Python内建的filter()函数用于过滤序列：和map()类似，filter()也接收一个函数和一个序列。
	和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回
	值是True还是False决定保留还是丢弃该元素。
### sorted: sorted可以对list进行排序；
	sort() 改变了原来序列的顺序，而sorted()没有，(sort()排序后原来的序列被覆盖)
	sorted(iterable, cmp=None, key=None, reverse=False)--> 
			new sorted list terable：是可迭代类型; 
			cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项; 
			key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项; 
			reverse：排序规则. reverse = True 或者 reverse = False，有默认值。 
			* 返回值：是一个经过排序的可迭代类型，与iterable一样
	sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序；eg
	>>> sorted([36, 5, -12, 9, -21], key=abs)
	[5, 9, -12, -21, 36]
		默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
		要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
	>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
	['Zoo', 'Credit', 'bob', 'about']
	datas = [{},{}]: 通过键排序： datas.sort(key=lambda d:d[key])


### 匿名函数
	匿名函数lambda x: x * x实际上就是：
	def f(x):
		return x * x
	关键字lambda表示匿名函数，冒号前面的 x 表示函数参数；
	匿名函数有一个限制，只能有一个表达式，不能写return，返回值就是表达式的结果
### 装饰器Decorator：函数对象有一个__name__属性，可以拿到函数的名字
	functools.partial就是帮助我们创建一个偏函数的
	int2 = functools.partial(int, base=2)
	functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
### 偏函数
	使用 functools模块实现偏函数功能(import functools)
		eg： int()函数
		>>>int('1234')
		1234
		>>>int('1234', base=8)
		5349
		>>>int('1234', 16)
		74565
		int2 = functools.partial(int, base=2)
		int2 相当于函数
		def int2(x, base=2):
			return int(x, base)

### 模块，一个 .py 文件就是一个模块，可以使用__name__ 访问模块名
 	from fibo import *	  -> 可以导出所有除以  (_)  开头的命名
 	#出于性能考虑，每个模块在每个解析器中只导入一遍，（交互式下可以用  imp.reload()重新加载）
### 类Class
	所有的 new-style 类继承自 object
	继承：
	isinstance()函数用于检查实例类型
	issubclass()用于检查类继承：issubclass(bool,int)为True，因为bool是int的子类
	多继承：多继承的同一父类值加载一次， object只加载一次
	私有变量：实际的私有变量在python中是不存在的，变通的方法是：
		以一个下划线开头的命名（例如 _spam ）会被处理为 API 的非公开部分（无论它是一个函数、方法或数据成员）
		任何形如 __spam 的标识（前面至少两个下划线，后面至多一个），被替代为 _classname__spam
	Python是动态语言，根据类创建的实例可以任意绑定属性。

### 使用__slots__
	可以使用特殊的__slots__变量，来限制该class实例能添加的属性：
	class Test(object):
		# 用tuple定义允许绑定的属性名称
		__slots__ = ('name','score')
	限制添加属性
### 使用@property
	isinstance函数判断值是否是其子集
	if not isinstance(value, int):
    	raise ValueError('score must be an integer!')
	Python内置的 @property装饰器就是负责把一个方法变成属性使用的
### 定制类
	__str__
	__iter__
	def __iter__(self):
		return self
	def __next__(self):
		pass
		return self.*
	__getitem__
	__getattr__
	只有在没有找到属性的情况下，才调用__getattr__，已有的属性，类定义存在的，不会在__getattr__中查找
	__call__
### 使用元类
	使用type()方法创建类
	要创建一个class对象，type()函数依次传入3个参数：
		1. class的名称；
		2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
		3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
	metaclass 	元类
	metaclass 允许你创建类及修改类，可以将类看成是metaclass创建出来的‘实例’

### 调试：
	try
	except 
	else
	finally
	断点： assert

		启动Python解释器时可以用-O参数来关闭assert

### collections
	namedtuple:是一个函数，它用来创建一个自定义的tuple对象; 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
		from collections import namedtuple
		Point = namedtuple('Point',['x','y'])
		>>>p = Point(1,2)
		>>>p.x
		1
	deque:可固定大小的队列；deque(maxlen=N)
	defaultdict:
		>>>from collections import defaultdict
		>>>dd = defaultdict(lambda : 'N/A')
		>>>dd['key1'] = 'aad'
		>>>dd['key1']
		'aad
		>>>dd['key2']
		'N/A
	OrderedDict

### 线程及进程
	进程：
	from multiprocessing import Poll,Process
	启用大量进程时 ，启用线程池Poll
	进程数  
	count = 4
	p = Poll(count)
	for i in range(count):
		p.apply_async(task, args=(i,))
	p.close()
	p.join()
	使用Process
	p = Process(target=task, args=(...))
### subprocess
	根据文档，推荐使用subprocess创建子进程 替代  os.system/os.spawn*/os.popen*/popen2.*/commamds  创建子进程的方法
	subprocess.call(args,*,stdin=None,stdout=None,stderr=None,shell=False)
	运行由args描述的命令。 等待命令完成，然后返回returncode属性。
	>>>subprocess.call(['ls','-l'])
	subprocess.check_call(...)
	用参数运行命令。 等待命令完成。 如果返回代码为零，则返回，否则会引发CalledProcessError。 CalledProcessError对象将在returncode属性中具有返回码。
	subprocess.check_output(args,*,stdin=None,stdout=None,stderr=None,shell=False,universal_newlines=False)
	On Windows kill() is an alias for terminate().

	Popen.poll()
	检查子进程是否被终止，没有返回None
	Popen.kill()  /  window下等同  Popen.terminate()
	终止子进程
	Popen.communicate(input=None)   需要设置stdin=subprocess.PIPE，发送数据才有效， 设置stdout=subprocess.PIPE,stderr=subprocess.STDOUT读取数据才有效，否则返回空的tuple，(None,None)
	发送数据到stdin，读取数据到stdout,stderr
	communicate()只有子进程返回数据后主进程才继续





### subprocess创建子进程
	1.os.system()
	缺点：
	A. os.system() 是新起一个shell去干活的，对系统的开销比较大
	B. 获得输出等信息比较麻烦,不能与外部命令或工具交互
	C. 无法控制，（如果调用的外部命令，挂死或者执行时间很长），主进程无法控制os.system(), 因为调用os.system(cmd) 调用进程会block， until os.system() 自己退出
	2.commands
	优点：
	A. 容易获得外部命令的输出，已经退出状态
	缺点：
	同os.system()中的A,C

	3.os.popen()
	同commands命令

	4.subprocess
	优点：
	A.支持和子进程交互
	B.支持同步/异步方式执行子进程
	C.可以子进程通信
	D.可自定义IO管道
	E.可控制是否开启新的shell工作

	subprocess.Popen(args, bufsize=0, executable=None, \
								stdin=None, stdout=None, stderr=None, \
								preexec_fn=None, close_fds=False, shell=False, \
								cwd=None, env=None, universal_newlines=False,\
								startupinfo=None, creationflags=0)
	参数说明：

	args：可以是字符串或者序列类型（如：list，元组），用于指定进程的可执行文件及其参数。如果是序列类型，第一个元素通常是可执行文件的路径。我们也可以显式的使用executeable参数来指定可执行文件的路径。在windows操作系统上，Popen通过调用 CreateProcess()来创建子进程,CreateProcess接收一个字符串参数，如果args是序列类型，系统将会通过 list2cmdline()函数将序列类型转换为字符串。
	bufsize：指定缓冲。到目前为止没用过。
	executable：用于指定可执行程序。一般情况下我们通过args参数来设置所要运行的程序。如果将参数shell设为True，executable将指定程序使用的shell。在windows平台下，默认的shell由COMSPEC环境变量来指定。
	stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
	preexec_fn只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用。
	Close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。我们不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
	shell设为true，程序将通过shell来执行。
	cwd用于设置子进程的当前目录。如果运行子进程需要在指定目录下运行，可以在此设置。
	env是字典类型，用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
	Universal_newlines:不同操作系统下，文本的换行符是不一样的。如：windows下用’/r/n’表示换，而Linux下用’/n’。如果将此参数设置为True，Python统一把这些换行符当作’/n’来处理。
	startupinfo与creationflags只在windows下用效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等。如果需要在新的CMD窗口运行，Windows下需要设置 creationflags =subprocess.CREATE_NEW_CONSOLE。

### pyc文件编译及运行
	# 单个文件
	>>> import py_compile
	>>> py_compile.compile(r'filepath')
	# 多个文件
	>>> import compileall
	>>> compileall.compile_dir(r'dirpath')
	# 直接通过命令编译文件
	cmd下： python -m py_compile test.py
	python -O -m py_compile test.py
	-o 优化成字符串
	-m 将后面的文件当成脚本运行
	# 编译后的pyc文件可直接通过命令行运行

### wsgi
	https://segmentfault.com/a/1190000003069785

### __name__与__main__:
	if __name__ == "__main__":
	1、当单独执行时，相当于程序的入口；
	2、当改module引入其他module时，__name__ 值为module的名字；
	3、因此，在python中，当一个module作为整体被执行时,moduel.__name__的值将是"__main__"；而当一个 module被其它module引用时，module.__name__将是module自己的名字，当然一个module被其它module引用时，其本身并不需要一个可执行的入口main了。

### sqlite3
	sqlite3为轻量级数据库，python内置
	使用直接导入库即可
	import sqlite3
	sqlite3 创建连接
	sqlite3.connect(db_path)
	db_path	
	数据库路径最好写成绝对路径，并且目录要存在
	db文件所在的目录需要有访问权限才能进行操作
	如果访问的路径为'C:\Users\Lux\Desktop\History' 路径 有时候要写成 'C:\\Users\\Lux\\Desktop\\History'；
	某些时候你的数据库文件后缀名不是 db 也不行，需要改名为 xxx.db
	对数据库文件要有读写的权限

### python 使用mysql
	* mysql-conncetor
	安装：pip install mysql-connector-python  --allow-external mysql-connector-python
	或 pip install mysql-connector
	或 在 https://dev.mysql.com/downloads/connector/python/  网站下载相应的连接器版本
	使用pip安装出错一般是版本的问题，建议使用对应网站下载对应版本包安装
	* mysql-python
	安装：pip install mysql-python 
	或 http://www.lfd.uci.edu/~gohlke/pythonlibs/  下载whl文件安装

### python import机制及实现
### python 类库引入机制
	http://python.jobbole.com/82604/
	* 相对引入 relative import：
	这种引入方式使用一个点号来标识引入类库的精确位置。与linux的相对路径表示相似，一个点表示当前目录，每多一个点号则代表向上一层目录
	eg:
		from .string import a
		from ..string import a
		from ...string import a
	相对引用使用引入库的__name__ 属性来决定该文件在整个包结构中的位置
	* 完全引入 absolute import

### next

###for循环语句后可以接else语句，类似于try;
###函数的默认参数只初始化一次
    >>>i=5
    >>>def f(arg=i):
    ...		print(arg)
    >>>f()
    5
    >>>i=100
    >>>f()
    5
