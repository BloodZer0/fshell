### fshell 基于机器学习的分布式webshell检测系统
------
#### 项目简介
baba



#### 项目整体架构设计
** fshell系统逻辑架构图**
![fshell-system-framework]http://www.s0nnet.com/wp-content/uploads/2016/12/fshell.png)

* fs_agent模块：fshell的agent模块，主要实现：（1）对web_log, statistics, file_attribute, danger_func, fuzz_hash元数据的采集，并发送到fs_server；（2）对server下发到agent配置信息进行更新；（3）读取server的文件读取指令，并将文件内容回传给server。

* fs_server模块：fshell在Server端的数据通信模块，该模块采用TCP socket 长连接和短连接的方式，监听3个端口。与agent模块实现：元数据data_srv接收入库，配置更新下发，agent上文件读取回传三个功能。

* fs_stand_srv模块：fshell的标准化srv模块，主要实现对已经入库的元数据进行特征向量化处理，使机器学习算法能够直接使用。

* fs_kernel模块：fshell的机器学习算法的核心模块。该模块采用支持向量机（SVM）和决策树（DT）等算法对特征向量进行监督学习，从而实现webshell与正常文件的分类。

* fs_manager模块：fshell的主控制模块。该模块实现：对agent配置管理；用户UI的管理；样本特征库的管理；机器学习检测模块相关配置以及结果的管理；以及其他预警通知、文件传输等的管理。


#### 相关博文链接

- [基于机器学习的分布式Webshell检测系统-绪论篇](http://www.s0nnet.com/archives/fshell)

- [基于机器学习的分布式webshell检测系统-特征工程（1）](http://www.s0nnet.com/archives/fshell-feature-1)
