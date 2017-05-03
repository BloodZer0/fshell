#### pySSDeep模块
ssdeep python 模块 (roject: https://github.com/bunzen/pySSDeep)

#### Requirements
SSDeep library/tool : http://ssdeep.sourceforge.net


#### 安装

先安装ssdeep库：
```
解压ssdeep-2.13.tar.gz；
$ ./configure
$ make & sudo make install
```
下载源码,并运行:
```
$ python setup.py build
$ sudo python setup.py install
```
如安装后，使用时报如下错误：
```
ImportError: libfuzzy.so.2: cannot open shared object file: No such file or directory
```
其错误原因是：
```
sys.path is only searched for Python modules. For dynamic linked libraries, the paths searched must be in LD_LIBRARY_PATH. Check if your LD_LIBRARY_PATH includes /usr/local/lib, and if it doesn't, add it and try again.
```
解决办法：
通过echo  $LD_LIBRARY_PATH命令查看$LD_LIBRARY_PATH是否为空，如果为空，执行命令：
```
export LD_LIBRARY_PATH=/usr/local/lib
```
如果不为空，则执行：
```
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```


#### 使用样例
```
>>> import pyssdeep
>>> sig1 = pyssdeep.fuzzy_hash_filename("ls_test1")
>>> sig2 = pyssdeep.fuzzy_hash_buf(open("ls_test2").read())
>>> pyssdeep.fuzzy_compare(sig1, sig2)
99
>>>
``` 
