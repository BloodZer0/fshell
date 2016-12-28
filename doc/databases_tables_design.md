
### fshell 数据库表设计文档v1.0

fshell系统数据库采用MySQL存储，大致可分为6个数据存数单元，分别是：

- dbu_conf Agent信息基本配置单元
- dbu_user  用户数据/Server配置信息数据单元
- dbu_sample_lib  特征样本库数据单元
- dbu_data  Agent上报的元数据单元
- dbu_feature  特征向量化数据单元
- dbu_result  检测结果数据单元

-------


** dbu_conf  Agent配置 数据单元 **

* agent基本配置信息表
```
CREATE TABLE `tb_conf_base` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `agent_id` int(11) NOT NULL,
      `dev_name` varchar(30) NOT NULL,
      `server_ip` varchar(20) NOT NULL,
      `server_port` int(11) NOT NULL,
      `web_enum` varchar(10) NOT NULL,
      `web_dir` varchar(50) NOT NULL,
      `cache_dir` varchar(50) NOT NULL,
      `log_dir` varchar(50) NOT NULL,
      `log_level` int(2) NOT NULL DEFAULT '1',
      `log_prefix` varchar(20) NOT NULL DEFAULT '',
      `ctr_log` int(2) NOT NULL DEFAULT '1',
      PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `tb_conf_danfunc` (
      `id` int(11) NOT NULL,
      `agent_id` int(11) NOT NULL,
      `dev_name` varchar(30) NOT NULL,
      `run_time` varchar(50) NOT NULL,
      `result_output` varchar(30) NOT NULL,
      `scan_file_ext` varchar(30) NOT NULL

)
```



