### fshell 基于机器学习的分布式webshell检测系统
------


#### 1. 项目简介
该项目从web服务器日志、统计学分析、文件属性分析、静态特征检测以及文件fuzz hash的检测这5个维度对webshell进行了基于支持向量机（SVM）和决策树（DT）的监督学习的机器学习算法，从而分类出支持文件和恶意webshell。
通过在业务web server上安装agent，将采集到的数据定时/实时传输到Server端,经过对采集的元数据加工处理，形成机器学习算法可以处理的特征向量化数据。在机器学习模块将采用SVM和决策树进行机器学习，形成针对webshell的二分类，达到检测效果。
#### 2. 项目整体架构
**fshell Agent端技术架构**
![fshell-Agent](http://www.s0nnet.com/wp-content/uploads/2016/12/fshell-Agnet.png)

**fshell Server端技术架构**
![fshell-Server](http://www.s0nnet.com/wp-content/uploads/2016/12/fshell_Server.png)

**fshell 模块功能说明**
* fs_agent模块：fshell的agent模块，主要实现：（1）对web_log, statistics, file_attribute, danger_func, fuzz_hash元数据的采集，并发送到fs_server；（2）对server下发到agent配置信息进行更新；（3）读取server的文件读取指令，并将文件内容回传给server。

* fs_server模块：fshell在Server端的数据通信模块，该模块采用TCP socket 长连接和短连接的方式，监听3个端口。与agent模块实现：元数据data_srv接收入库，配置更新下发，agent上文件读取回传三个功能。

* fs_data_sync模块：fshell的元数据标准化srv模块，主要实现对已经入库的元数据进行特征向量化处理并存入mysql中，便于机器学习算法能够直接使用。

* fs_kernel模块：fshell的机器学习算法的核心模块。该模块采用支持向量机（SVM）和决策树（DT）等算法对特征向量进行监督学习，从而实现webshell与正常文件的分类。

* fs_manager模块：fshell的主控制模块。该模块实现：对agent配置管理；用户UI的管理；样本特征库的管理；机器学习检测模块相关配置以及结果的管理；以及其他预警通知、文件传输等的管理。

* fs_deploy模块：fshell的安装部署脚本。该模块实现对fs_agent和fs_server的自动化一键脚本部署，基于Nginx、mysql、python-virtualenv的底层基础环境，采用supervisor托管fs_server的各进程稳定运行。

#### 3. 机器学习核心算法
（待完善。。。）

#### 4. 相关博文链接

- [基于机器学习的分布式Webshell检测系统-绪论篇](http://www.s0nnet.com/archives/fshell)

- [基于机器学习的分布式webshell检测系统-特征工程（1）](http://www.s0nnet.com/archives/fshell-feature-1)
