
### fshell 网络通信协议设计文档v1.0

fshell系统中Agent与Server的数据通信采用TCP socket的方式进行通信，使用TCP长连接+短连接的方式进行元数据上报、配置更新和文件传输。其中，对web日志的数据上报基本是实时的，故采用长连接方式，其他数据传输采用短连接方式。


#### 1. 消息通用协议（基于TCP层） 

```
{ 
    /*  消息ID  */
    task_id: $uuid  //建立任务上下文对应，可选字段

    /* 消息发给/接收者 */
    dev_name:  // 标示设备身份（可为ip）
    agent_id:  // 标示agent编号（int）

    /*  消息协议  */
    msg_protocol:  //消息协议类型， 下行/上报消息
    msg_type:  // 消息类型， 表示具体消息类型（数据/文件/配置）

    /*  消息数据  */
    data:  {}
}
```
注意：
1. 消息协议类型(msg_protocol)目前定义四类：data_up, file_req, file_rsp, conf_req, conf_rsp  
2. 消息响应结果：data = {code：xxx ,val: xxx}  code:  成功为0, 失败为-1 。  
3. 解决二进制传输问题: msgJson.data[key] = value  
如果value中存在二进制数据，则转化成：  

> msgJson.data[key_base64] = true
> msgJson.data[key] = base64(value)
4. 该协议数据组装一般在bean层的网络拆/解包时进行。  

#### 2. 网络协议头（网络框架底层封装）
```
NetHead {
    int start;  // 定义起始值 0x11111111
    char type;  // 定义协议类型 0
    int pkgLen;  // 协议数据长度
}
```
注： 该协议头在net层被封装成应用层的数据包头，并被TCP层封包发送，它一般在/net/fs_nethead.py中定义。  

#### 3. 应用层协议定义
- msg_protocol定义：
```
F_RESULT_UP    =  0x01
F_RESULT_DOWN  =  0x02
F_FILE_REQ     =  0x03
F_FILE_RSP     =  0x04
F_CONF_REQ     =  0x05
F_CONF_RSP     =  0x06
```


- msg_type定义：

* data_type上报数据类型(0x01 ~ 0x20)
```
F_DATA_WEBLOG   =  0x01
F_DATA_STATICS  =  0x02
F_DATA_FILEATT  =  0x03
F_DATA_DANFUNC  =  0x04
F_DATA_FUZZHASH =  0x05 
```

* conf_type 通信数据类型(0x30 ~ 0x50)
```
F_CONF_BASE     =  0x30
F_CONF_WEBLOG   =  0x31
F_CONF_STATICS  =  0x32
F_CONF_FILEATT  =  0x33
F_CONF_DANFUNC  =  0x34
F_CONF_FUZZHASH =  0x35
```

* file_type 通信数据类型(0x60 ~ 0x80)
```
F_FILE_REQ      =  0x60
F_DATA_RSP      =  0x61
```
