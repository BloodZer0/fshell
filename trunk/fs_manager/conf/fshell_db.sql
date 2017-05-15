-- Adminer 4.2.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `tb_conf_base`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_conf_danfunc`;
CREATE TABLE `tb_conf_danfunc` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `run_time` varchar(50) NOT NULL,
  `result_output` varchar(30) NOT NULL,
  `scan_file_ext` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_conf_fileatt`;
CREATE TABLE `tb_conf_fileatt` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `run_time` varchar(50) NOT NULL,
  `result_ouput` varchar(30) NOT NULL,
  `scan_file_ext` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_conf_fuzzhash`;
CREATE TABLE `tb_conf_fuzzhash` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `run_time` varchar(50) NOT NULL,
  `result_output` varchar(30) NOT NULL,
  `scan_file_ext` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_conf_statics`;
CREATE TABLE `tb_conf_statics` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `run_time` varchar(50) NOT NULL,
  `smallest_filezise` int(5) NOT NULL DEFAULT '50',
  `result_ouput` varchar(30) NOT NULL,
  `scan_file_ext` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_conf_weblog`;
CREATE TABLE `tb_conf_weblog` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `log_file` varchar(50) NOT NULL,
  `time_wait` int(3) NOT NULL DEFAULT '5',
  `log_seek` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_data_danfunc`;
CREATE TABLE `tb_data_danfunc` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `weight_sum` int(5) NOT NULL,
  `functions` text NOT NULL,
  `insert_tm` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_data_fileatt`;
CREATE TABLE `tb_data_fileatt` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `file_ctime` int(11) NOT NULL,
  `file_mtime` int(11) NOT NULL,
  `file_mode` int(5) NOT NULL,
  `file_owner` varchar(20) NOT NULL,
  `insert_tm` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_data_fuzzhash`;
CREATE TABLE `tb_data_fuzzhash` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `fuzz_hash` varchar(300) NOT NULL,
  `insert_tm` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_data_statics`;
CREATE TABLE `tb_data_statics` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `text_ic` varchar(10) NOT NULL,
  `text_ent` varchar(10) NOT NULL,
  `text_lw` int(11) NOT NULL,
  `text_cmp` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_data_weblog`;
CREATE TABLE `tb_data_weblog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `client_ip` varchar(20) NOT NULL,
  `time_local` datetime NOT NULL,
  `method` varchar(6) NOT NULL,
  `url` varchar(200) NOT NULL,
  `req_body` text NOT NULL,
  `referer` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_feature_danfunc`;
CREATE TABLE `tb_feature_danfunc` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(100) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_feature_fileatt`;
CREATE TABLE `tb_feature_fileatt` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(100) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_feature_fuzzhash`;
CREATE TABLE `tb_feature_fuzzhash` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(100) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_feature_statics`;
CREATE TABLE `tb_feature_statics` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(100) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_feature_weblog`;
CREATE TABLE `tb_feature_weblog` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(100) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_danfunc`;
CREATE TABLE `tb_result_danfunc` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_fileatt`;
CREATE TABLE `tb_result_fileatt` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_fuzzhash`;
CREATE TABLE `tb_result_fuzzhash` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_statics`;
CREATE TABLE `tb_result_statics` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_sum`;
CREATE TABLE `tb_result_sum` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result_sum` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_result_weblog`;
CREATE TABLE `tb_result_weblog` (
  `id` varchar(20) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `result` varchar(10) NOT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_sample_lib_func`;
CREATE TABLE `tb_sample_lib_func` (
  `id` int(11) NOT NULL,
  `enum_type` varchar(10) NOT NULL,
  `class` int(2) NOT NULL,
  `function` varchar(50) NOT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `insert_tm` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_sample_lib_shell`;
CREATE TABLE `tb_sample_lib_shell` (
  `id` int(11) NOT NULL,
  `shell_name` varchar(50) NOT NULL,
  `enum_type` varchar(10) NOT NULL,
  `fuzz_hash` varchar(50) NOT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `insert_tm` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_session`;
CREATE TABLE `tb_session` (
  `session_id` char(128) NOT NULL,
  `atime` datetime NOT NULL,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_sys_agent`;
CREATE TABLE `tb_sys_agent` (
  `id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  `agent_ip` varchar(20) NOT NULL,
  `dev_name` varchar(30) NOT NULL,
  `web_enum` varchar(10) NOT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `edit_tm` datetime DEFAULT NULL,
  `action_tm` datetime DEFAULT NULL,
  `insert_tm` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_sys_log`;
CREATE TABLE `tb_sys_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `log_content` varchar(255) NOT NULL,
  `log_attr` text,
  `log_result` varchar(32) NOT NULL,
  `log_reason` varchar(255) DEFAULT NULL,
  `referee` varchar(255) NOT NULL,
  `remote_addr` varchar(32) NOT NULL,
  `insert_tm` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_sys_send`;
CREATE TABLE `tb_sys_send` (
  `id` int(11) NOT NULL,
  `event_conf` varchar(100) NOT NULL,
  `event_class` int(2) NOT NULL DEFAULT '1',
  `event_tpl` varchar(100) DEFAULT '',
  `event_msg` text NOT NULL,
  `event_send` varchar(20) DEFAULT '',
  `insert_tm` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_user_pwd`;
CREATE TABLE `tb_user_pwd` (
  `user_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `priv` int(2) NOT NULL DEFAULT '1',
  `remark` varchar(50) DEFAULT NULL,
  `insert_tm` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 2017-05-15 23:03:02
