


#### 数据库设计



* dbu_conf  Agent配置 数据单元
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



