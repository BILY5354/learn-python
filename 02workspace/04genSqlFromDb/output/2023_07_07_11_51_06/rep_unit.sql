CREATE TABLE `rep_unit` (
  `GUID` char(36) NOT NULL,
  `frameID` int NOT NULL,
  `blockID` int NOT NULL COMMENT '块',
  `rowID` int NOT NULL COMMENT '行',
  `colID` int NOT NULL COMMENT '列',
  `unitCode` varchar(100) DEFAULT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `resultID` tinyint NOT NULL,
  `defectID` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `process` tinyint DEFAULT NULL COMMENT '后续处理标志位',
  `insertTime` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '数据插入时间(默认)',
  `updateTime` datetime(6) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '数据更新时间(默认)',
  `info` json DEFAULT NULL,
  PRIMARY KEY (`GUID`,`frameID`,`blockID`,`rowID`,`colID`),
  KEY `rep_unit_insertTime_IDX` (`insertTime` DESC) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "1", "0", "0", "0", "1", "2023-07-04 15:29:19", "2023-07-04 15:29:19", "1", "0", "None", "2023-07-04 15:29:20.078975", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "2", "0", "0", "0", "1", "2023-07-04 15:29:26", "2023-07-04 15:29:26", "1", "0", "None", "2023-07-04 15:29:26.817040", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "3", "0", "0", "0", "1", "2023-07-04 15:29:33", "2023-07-04 15:29:33", "1", "0", "None", "2023-07-04 15:29:34.189674", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "4", "0", "0", "0", "1", "2023-07-04 15:29:40", "2023-07-04 15:29:40", "1", "0", "None", "2023-07-04 15:29:41.221875", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "5", "0", "0", "0", "1", "2023-07-04 15:29:47", "2023-07-04 15:29:47", "1", "0", "None", "2023-07-04 15:29:47.626023", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "6", "0", "0", "0", "1", "2023-07-04 15:29:54", "2023-07-04 15:29:54", "1", "0", "None", "2023-07-04 15:29:54.533765", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "7", "0", "0", "0", "1", "2023-07-04 15:30:02", "2023-07-04 15:30:02", "1", "0", "None", "2023-07-04 15:30:02.537406", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "8", "0", "0", "0", "1", "2023-07-04 15:30:09", "2023-07-04 15:30:09", "1", "0", "None", "2023-07-04 15:30:10.080979", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "9", "0", "0", "0", "1", "2023-07-04 15:30:15", "2023-07-04 15:30:15", "1", "0", "None", "2023-07-04 15:30:15.641584", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "10", "0", "0", "0", "1", "2023-07-04 15:30:21", "2023-07-04 15:30:21", "1", "0", "None", "2023-07-04 15:30:21.637986", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "11", "0", "0", "0", "1", "2023-07-04 15:30:27", "2023-07-04 15:30:27", "1", "0", "None", "2023-07-04 15:30:28.237129", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "12", "0", "0", "0", "1", "2023-07-04 15:30:36", "2023-07-04 15:30:36", "0", "111", "None", "2023-07-04 15:30:36.756560", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "13", "0", "0", "0", "1", "2023-07-04 15:30:42", "2023-07-04 15:30:42", "1", "0", "None", "2023-07-04 15:30:43.376586", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "14", "0", "0", "0", "1", "2023-07-04 15:30:48", "2023-07-04 15:30:48", "1", "0", "None", "2023-07-04 15:30:49.428529", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "15", "0", "0", "0", "1", "2023-07-04 15:30:55", "2023-07-04 15:30:55", "1", "0", "None", "2023-07-04 15:30:55.883303", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "16", "0", "0", "0", "1", "2023-07-04 15:31:03", "2023-07-04 15:31:03", "1", "0", "None", "2023-07-04 15:31:03.916000", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "17", "0", "0", "0", "1", "2023-07-04 15:31:11", "2023-07-04 15:31:11", "1", "0", "None", "2023-07-04 15:31:12.308840", "None", "{}");
INSERT INTO rep_unit VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "18", "0", "0", "0", "1", "2023-07-04 15:31:19", "2023-07-04 15:31:19", "1", "0", "None", "2023-07-04 15:31:19.439106", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "1", "0", "0", "0", "1", "2023-07-03 17:41:15", "2023-07-03 17:41:15", "0", "1", "None", "2023-07-03 17:41:16.575450", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "2", "0", "0", "0", "1", "2023-07-03 17:42:22", "2023-07-03 17:42:22", "0", "0", "None", "2023-07-03 17:42:23.576888", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "3", "0", "0", "0", "1", "2023-07-03 17:43:28", "2023-07-03 17:43:28", "0", "65", "None", "2023-07-03 17:43:29.936715", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "4", "0", "0", "0", "1", "2023-07-03 17:44:34", "2023-07-03 17:44:34", "0", "0", "None", "2023-07-03 17:44:35.060778", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "5", "0", "0", "0", "1", "2023-07-03 17:45:44", "2023-07-03 17:45:44", "0", "0", "None", "2023-07-03 17:45:45.209685", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "6", "0", "0", "0", "1", "2023-07-03 17:46:50", "2023-07-03 17:46:50", "0", "36", "None", "2023-07-03 17:46:51.603567", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "7", "0", "0", "0", "1", "2023-07-03 17:47:54", "2023-07-03 17:47:54", "0", "0", "None", "2023-07-03 17:47:55.788625", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "8", "0", "0", "0", "1", "2023-07-03 17:49:14", "2023-07-03 17:49:14", "0", "65", "None", "2023-07-03 17:49:15.517764", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "9", "0", "0", "0", "1", "2023-07-03 17:50:46", "2023-07-03 17:50:46", "0", "1", "None", "2023-07-03 17:50:47.635270", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "10", "0", "0", "0", "1", "2023-07-03 17:53:19", "2023-07-03 17:53:19", "0", "0", "None", "2023-07-03 17:53:20.732211", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "11", "0", "0", "0", "1", "2023-07-03 17:54:48", "2023-07-03 17:54:48", "0", "0", "None", "2023-07-03 17:54:49.011792", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "12", "0", "0", "0", "1", "2023-07-03 17:56:33", "2023-07-03 17:56:33", "0", "65", "None", "2023-07-03 17:56:34.441397", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "13", "0", "0", "0", "1", "2023-07-03 17:58:51", "2023-07-03 17:58:51", "0", "1", "None", "2023-07-03 17:58:52.854084", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "14", "0", "0", "0", "1", "2023-07-03 18:01:09", "2023-07-03 18:01:09", "0", "1", "None", "2023-07-03 18:01:10.106329", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "15", "0", "0", "0", "1", "2023-07-03 18:02:27", "2023-07-03 18:02:27", "0", "65", "None", "2023-07-03 18:02:28.174093", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "16", "0", "0", "0", "1", "2023-07-03 18:03:32", "2023-07-03 18:03:32", "0", "0", "None", "2023-07-03 18:03:33.222934", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "17", "0", "0", "0", "1", "2023-07-03 18:04:34", "2023-07-03 18:04:34", "0", "0", "None", "2023-07-03 18:04:35.112254", "None", "{}");
INSERT INTO rep_unit VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "18", "0", "0", "0", "1", "2023-07-03 18:05:43", "2023-07-03 18:05:43", "0", "1", "None", "2023-07-03 18:05:44.610596", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "1", "0", "0", "0", "1", "2023-07-04 15:38:45", "2023-07-04 15:38:45", "1", "0", "None", "2023-07-04 15:38:45.842928", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "2", "0", "0", "0", "1", "2023-07-04 15:38:51", "2023-07-04 15:38:51", "1", "0", "None", "2023-07-04 15:38:51.836811", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "3", "0", "0", "0", "1", "2023-07-04 15:38:57", "2023-07-04 15:38:57", "1", "0", "None", "2023-07-04 15:38:57.607527", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "4", "0", "0", "0", "1", "2023-07-04 15:39:03", "2023-07-04 15:39:03", "1", "0", "None", "2023-07-04 15:39:03.543028", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "5", "0", "0", "0", "1", "2023-07-04 15:39:09", "2023-07-04 15:39:09", "1", "0", "None", "2023-07-04 15:39:09.705796", "None", "{}");
INSERT INTO rep_unit VALUES ("8D385EFC034B48038DE95E98A929F4F9", "6", "0", "0", "0", "1", "2023-07-04 15:39:15", "2023-07-04 15:39:15", "1", "0", "None", "2023-07-04 15:39:15.749710", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "1", "0", "0", "0", "1", "2023-07-04 16:25:01", "2023-07-04 16:25:01", "0", "0", "None", "2023-07-04 16:25:01.855423", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "2", "0", "0", "0", "1", "2023-07-04 16:26:13", "2023-07-04 16:26:13", "0", "1", "None", "2023-07-04 16:26:14.051205", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "3", "0", "0", "0", "1", "2023-07-04 16:27:24", "2023-07-04 16:27:24", "0", "0", "None", "2023-07-04 16:27:24.436971", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "4", "0", "0", "0", "1", "2023-07-04 16:28:28", "2023-07-04 16:28:28", "0", "1", "None", "2023-07-04 16:28:28.934924", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "5", "0", "0", "0", "1", "2023-07-04 16:29:31", "2023-07-04 16:29:31", "0", "1", "None", "2023-07-04 16:29:32.003355", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "6", "0", "0", "0", "1", "2023-07-04 16:30:27", "2023-07-04 16:30:27", "0", "1", "None", "2023-07-04 16:30:28.257526", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "7", "0", "0", "0", "1", "2023-07-04 16:31:14", "2023-07-04 16:31:14", "0", "65", "None", "2023-07-04 16:31:14.903593", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "8", "0", "0", "0", "1", "2023-07-04 16:32:12", "2023-07-04 16:32:12", "0", "1", "None", "2023-07-04 16:32:12.794921", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "9", "0", "0", "0", "1", "2023-07-04 16:33:07", "2023-07-04 16:33:07", "0", "65", "None", "2023-07-04 16:33:07.363490", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "10", "0", "0", "0", "1", "2023-07-04 16:34:10", "2023-07-04 16:34:10", "0", "1", "None", "2023-07-04 16:34:11.174667", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "11", "0", "0", "0", "1", "2023-07-04 16:35:18", "2023-07-04 16:35:18", "0", "0", "None", "2023-07-04 16:35:18.894546", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "12", "0", "0", "0", "1", "2023-07-04 16:36:46", "2023-07-04 16:36:46", "0", "65", "None", "2023-07-04 16:36:46.598498", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "13", "0", "0", "0", "1", "2023-07-04 16:37:49", "2023-07-04 16:37:49", "0", "0", "None", "2023-07-04 16:37:49.627738", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "14", "0", "0", "0", "1", "2023-07-04 16:39:04", "2023-07-04 16:39:04", "0", "65", "None", "2023-07-04 16:39:04.774229", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "15", "0", "0", "0", "1", "2023-07-04 16:40:12", "2023-07-04 16:40:12", "0", "1", "None", "2023-07-04 16:40:12.479696", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "16", "0", "0", "0", "1", "2023-07-04 16:41:17", "2023-07-04 16:41:17", "0", "1", "None", "2023-07-04 16:41:17.856201", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "17", "0", "0", "0", "1", "2023-07-04 16:42:23", "2023-07-04 16:42:23", "0", "1", "None", "2023-07-04 16:42:23.959095", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "18", "0", "0", "0", "1", "2023-07-04 16:43:22", "2023-07-04 16:43:22", "0", "1", "None", "2023-07-04 16:43:22.981119", "None", "{}");
INSERT INTO rep_unit VALUES ("90373FD6D6254AAB95BB935D46458D3C", "19", "0", "0", "0", "1", "2023-07-04 16:44:29", "2023-07-04 16:44:29", "0", "0", "None", "2023-07-04 16:44:29.815989", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "0", "0", "1", "2023-07-03 14:21:24", "2023-07-03 14:21:24", "0", "2", "None", "2023-07-03 14:21:24.664680", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "0", "1", "1", "2023-07-03 14:21:36", "2023-07-03 14:21:36", "0", "2", "None", "2023-07-03 14:21:36.997809", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "0", "2", "1", "2023-07-03 14:21:39", "2023-07-03 14:21:39", "0", "2", "None", "2023-07-03 14:21:39.414815", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "0", "3", "1", "2023-07-03 14:21:51", "2023-07-03 14:21:51", "0", "2", "None", "2023-07-03 14:21:51.588190", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "0", "4", "1", "2023-07-03 14:21:54", "2023-07-03 14:21:54", "0", "1", "None", "2023-07-03 14:21:54.569697", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "1", "0", "1", "2023-07-03 14:21:27", "2023-07-03 14:21:27", "0", "2", "None", "2023-07-03 14:21:27.152829", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "1", "1", "1", "2023-07-03 14:21:34", "2023-07-03 14:21:34", "0", "2", "None", "2023-07-03 14:21:34.589123", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "1", "2", "1", "2023-07-03 14:21:41", "2023-07-03 14:21:41", "0", "2", "None", "2023-07-03 14:21:41.863247", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "1", "3", "1", "2023-07-03 14:21:49", "2023-07-03 14:21:49", "0", "2", "None", "2023-07-03 14:21:49.194592", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "1", "4", "1", "2023-07-03 14:21:57", "2023-07-03 14:21:57", "0", "1", "None", "2023-07-03 14:21:57.232486", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "2", "0", "1", "2023-07-03 14:21:29", "2023-07-03 14:21:29", "0", "2", "None", "2023-07-03 14:21:29.747817", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "2", "1", "1", "2023-07-03 14:21:32", "2023-07-03 14:21:32", "0", "2", "None", "2023-07-03 14:21:32.242732", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "2", "2", "1", "2023-07-03 14:21:44", "2023-07-03 14:21:44", "0", "2", "None", "2023-07-03 14:21:44.295996", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "2", "3", "1", "2023-07-03 14:21:46", "2023-07-03 14:21:46", "0", "1", "None", "2023-07-03 14:21:46.826148", "None", "{}");
INSERT INTO rep_unit VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "0", "2", "4", "1", "2023-07-03 14:21:59", "2023-07-03 14:21:59", "0", "1", "None", "2023-07-03 14:21:59.970063", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "1", "0", "0", "0", "1", "2023-07-03 14:27:34", "2023-07-03 14:27:34", "0", "1", "None", "2023-07-03 14:27:34.853252", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "2", "0", "0", "0", "1", "2023-07-03 14:28:01", "2023-07-03 14:28:01", "0", "1", "None", "2023-07-03 14:28:01.702104", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "3", "0", "0", "0", "1", "2023-07-03 14:28:30", "2023-07-03 14:28:30", "0", "1", "None", "2023-07-03 14:28:30.308576", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "4", "0", "0", "0", "1", "2023-07-03 14:28:57", "2023-07-03 14:28:57", "0", "1", "None", "2023-07-03 14:28:57.026281", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "5", "0", "0", "0", "1", "2023-07-03 14:29:23", "2023-07-03 14:29:23", "0", "1", "None", "2023-07-03 14:29:23.782787", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "6", "0", "0", "0", "1", "2023-07-03 14:29:50", "2023-07-03 14:29:50", "0", "1", "None", "2023-07-03 14:29:50.822071", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "7", "0", "0", "0", "1", "2023-07-03 14:30:17", "2023-07-03 14:30:17", "0", "1", "None", "2023-07-03 14:30:17.623769", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "8", "0", "0", "0", "1", "2023-07-03 14:30:44", "2023-07-03 14:30:44", "0", "1", "None", "2023-07-03 14:30:44.396428", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "9", "0", "0", "0", "1", "2023-07-03 14:31:11", "2023-07-03 14:31:11", "0", "1", "None", "2023-07-03 14:31:11.294643", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "10", "0", "0", "0", "1", "2023-07-03 14:31:38", "2023-07-03 14:31:38", "0", "1", "None", "2023-07-03 14:31:38.528416", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "11", "0", "0", "0", "1", "2023-07-03 14:32:05", "2023-07-03 14:32:05", "0", "1", "None", "2023-07-03 14:32:05.287767", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "12", "0", "0", "0", "1", "2023-07-03 14:32:32", "2023-07-03 14:32:32", "0", "1", "None", "2023-07-03 14:32:32.387390", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "13", "0", "0", "0", "1", "2023-07-03 14:32:59", "2023-07-03 14:32:59", "0", "1", "None", "2023-07-03 14:32:59.173020", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "14", "0", "0", "0", "1", "2023-07-03 14:33:26", "2023-07-03 14:33:26", "0", "1", "None", "2023-07-03 14:33:26.062407", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "15", "0", "0", "0", "1", "2023-07-03 14:33:54", "2023-07-03 14:33:54", "0", "1", "None", "2023-07-03 14:33:54.260626", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "16", "0", "0", "0", "1", "2023-07-03 14:34:21", "2023-07-03 14:34:21", "0", "1", "None", "2023-07-03 14:34:21.132946", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "17", "0", "0", "0", "1", "2023-07-03 14:34:48", "2023-07-03 14:34:48", "0", "1", "None", "2023-07-03 14:34:48.185061", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "18", "0", "0", "0", "1", "2023-07-03 14:35:15", "2023-07-03 14:35:15", "0", "1", "None", "2023-07-03 14:35:15.131035", "None", "{}");
INSERT INTO rep_unit VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "19", "0", "0", "0", "1", "2023-07-03 14:35:43", "2023-07-03 14:35:43", "0", "1", "None", "2023-07-03 14:35:43.014526", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "1", "0", "0", "0", "1", "2023-07-03 09:45:24", "2023-07-03 09:45:24", "0", "1", "None", "2023-07-03 09:45:24.872918", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "2", "0", "0", "0", "1", "2023-07-03 09:45:50", "2023-07-03 09:45:50", "0", "1", "None", "2023-07-03 09:45:50.904493", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "3", "0", "0", "0", "1", "2023-07-03 09:46:16", "2023-07-03 09:46:16", "0", "1", "None", "2023-07-03 09:46:16.962431", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "4", "0", "0", "0", "1", "2023-07-03 09:46:43", "2023-07-03 09:46:43", "0", "1", "None", "2023-07-03 09:46:43.249315", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "5", "0", "0", "0", "1", "2023-07-03 09:47:09", "2023-07-03 09:47:09", "0", "1", "None", "2023-07-03 09:47:09.434240", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "6", "0", "0", "0", "1", "2023-07-03 09:47:35", "2023-07-03 09:47:35", "0", "1", "None", "2023-07-03 09:47:35.638085", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "7", "0", "0", "0", "1", "2023-07-03 09:48:01", "2023-07-03 09:48:01", "0", "1", "None", "2023-07-03 09:48:01.749208", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "8", "0", "0", "0", "1", "2023-07-03 09:48:27", "2023-07-03 09:48:27", "0", "1", "None", "2023-07-03 09:48:27.798524", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "9", "0", "0", "0", "1", "2023-07-03 09:48:54", "2023-07-03 09:48:54", "0", "1", "None", "2023-07-03 09:48:54.215486", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "10", "0", "0", "0", "1", "2023-07-03 09:49:20", "2023-07-03 09:49:20", "0", "1", "None", "2023-07-03 09:49:20.505005", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "11", "0", "0", "0", "1", "2023-07-03 09:49:47", "2023-07-03 09:49:47", "0", "1", "None", "2023-07-03 09:49:47.989150", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "12", "0", "0", "0", "1", "2023-07-03 09:50:15", "2023-07-03 09:50:15", "0", "1", "None", "2023-07-03 09:50:15.216042", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "13", "0", "0", "0", "1", "2023-07-03 09:50:41", "2023-07-03 09:50:41", "0", "1", "None", "2023-07-03 09:50:41.501425", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "14", "0", "0", "0", "1", "2023-07-03 09:51:07", "2023-07-03 09:51:07", "0", "1", "None", "2023-07-03 09:51:07.609095", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "15", "0", "0", "0", "1", "2023-07-03 09:51:33", "2023-07-03 09:51:33", "0", "1", "None", "2023-07-03 09:51:33.729297", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "16", "0", "0", "0", "1", "2023-07-03 09:51:59", "2023-07-03 09:51:59", "0", "1", "None", "2023-07-03 09:51:59.729332", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "17", "0", "0", "0", "1", "2023-07-03 09:52:25", "2023-07-03 09:52:25", "0", "1", "None", "2023-07-03 09:52:25.999733", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "18", "0", "0", "0", "1", "2023-07-03 09:52:53", "2023-07-03 09:52:53", "0", "1", "None", "2023-07-03 09:52:53.062794", "None", "{}");
INSERT INTO rep_unit VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "19", "0", "0", "0", "1", "2023-07-03 09:53:19", "2023-07-03 09:53:19", "0", "1", "None", "2023-07-03 09:53:19.796994", "None", "{}");
INSERT INTO rep_unit VALUES ("AA8422746B1E445D8A55EEF1BE93C01F", "1", "0", "0", "0", "1", "2023-07-03 14:02:06", "2023-07-03 14:02:06", "0", "87", "None", "2023-07-03 14:02:07.731740", "None", "{}");
INSERT INTO rep_unit VALUES ("AA8422746B1E445D8A55EEF1BE93C01F", "2", "0", "0", "0", "1", "2023-07-03 14:02:54", "2023-07-03 14:02:54", "0", "87", "None", "2023-07-03 14:02:55.887583", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "0", "0", "1", "2023-07-03 10:08:37", "2023-07-03 10:08:37", "0", "2", "None", "2023-07-03 10:08:37.587023", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "0", "1", "1", "2023-07-03 10:08:49", "2023-07-03 10:08:49", "0", "2", "None", "2023-07-03 10:08:49.781240", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "0", "2", "1", "2023-07-03 10:08:52", "2023-07-03 10:08:52", "0", "2", "None", "2023-07-03 10:08:52.303214", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "0", "3", "1", "2023-07-03 10:09:04", "2023-07-03 10:09:04", "0", "2", "None", "2023-07-03 10:09:04.415072", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "0", "4", "1", "2023-07-03 10:09:07", "2023-07-03 10:09:07", "0", "1", "None", "2023-07-03 10:09:08.034609", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "1", "0", "1", "2023-07-03 10:08:39", "2023-07-03 10:08:39", "0", "2", "None", "2023-07-03 10:08:40.099791", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "1", "1", "1", "2023-07-03 10:08:47", "2023-07-03 10:08:47", "0", "2", "None", "2023-07-03 10:08:47.323037", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "1", "2", "1", "2023-07-03 10:08:54", "2023-07-03 10:08:54", "0", "2", "None", "2023-07-03 10:08:54.582693", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "1", "3", "1", "2023-07-03 10:09:01", "2023-07-03 10:09:01", "0", "2", "None", "2023-07-03 10:09:02.059804", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "1", "4", "1", "2023-07-03 10:09:10", "2023-07-03 10:09:10", "0", "1", "None", "2023-07-03 10:09:10.197432", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "2", "0", "1", "2023-07-03 10:08:42", "2023-07-03 10:08:42", "0", "2", "None", "2023-07-03 10:08:42.403227", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "2", "1", "1", "2023-07-03 10:08:44", "2023-07-03 10:08:44", "0", "2", "None", "2023-07-03 10:08:44.828212", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "2", "2", "1", "2023-07-03 10:08:57", "2023-07-03 10:08:57", "0", "2", "None", "2023-07-03 10:08:57.067495", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "2", "3", "1", "2023-07-03 10:08:59", "2023-07-03 10:08:59", "0", "1", "None", "2023-07-03 10:08:59.618026", "None", "{}");
INSERT INTO rep_unit VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "0", "2", "4", "1", "2023-07-03 10:09:12", "2023-07-03 10:09:12", "0", "1", "None", "2023-07-03 10:09:12.881217", "None", "{}");
INSERT INTO rep_unit VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "1", "0", "0", "0", "1", "2023-07-04 15:42:42", "2023-07-04 15:42:42", "0", "65", "None", "2023-07-04 15:42:43.203226", "None", "{}");
INSERT INTO rep_unit VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "2", "0", "0", "0", "1", "2023-07-04 15:43:58", "2023-07-04 15:43:58", "0", "65", "None", "2023-07-04 15:43:58.658225", "None", "{}");
INSERT INTO rep_unit VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "3", "0", "0", "0", "1", "2023-07-04 15:45:07", "2023-07-04 15:45:07", "1", "0", "None", "2023-07-04 15:45:07.982984", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "0", "0", "1", "2023-07-03 17:49:39", "2023-07-03 17:49:39", "0", "7", "None", "2023-07-03 17:49:38.983324", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "0", "1", "1", "2023-07-03 17:50:24", "2023-07-03 17:50:24", "0", "7", "None", "2023-07-03 17:50:23.785566", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "0", "2", "1", "2023-07-03 17:50:30", "2023-07-03 17:50:30", "0", "5", "None", "2023-07-03 17:50:30.164584", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "0", "3", "1", "2023-07-03 17:51:08", "2023-07-03 17:51:08", "0", "7", "None", "2023-07-03 17:51:07.695991", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "0", "4", "1", "2023-07-03 17:51:16", "2023-07-03 17:51:16", "0", "7", "None", "2023-07-03 17:51:15.492891", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "1", "0", "1", "2023-07-03 17:49:47", "2023-07-03 17:49:47", "1", "0", "None", "2023-07-03 17:49:46.867198", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "1", "1", "1", "2023-07-03 17:50:14", "2023-07-03 17:50:14", "0", "7", "None", "2023-07-03 17:50:14.041615", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "1", "2", "1", "2023-07-03 17:50:38", "2023-07-03 17:50:38", "0", "7", "None", "2023-07-03 17:50:38.086704", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "1", "3", "1", "2023-07-03 17:51:01", "2023-07-03 17:51:01", "0", "7", "None", "2023-07-03 17:51:00.622893", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "1", "4", "1", "2023-07-03 17:51:26", "2023-07-03 17:51:26", "0", "7", "None", "2023-07-03 17:51:25.659800", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "2", "0", "1", "2023-07-03 17:49:57", "2023-07-03 17:49:57", "0", "1", "None", "2023-07-03 17:49:56.422901", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "2", "1", "1", "2023-07-03 17:50:05", "2023-07-03 17:50:05", "1", "0", "None", "2023-07-03 17:50:05.029464", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "2", "2", "1", "2023-07-03 17:50:46", "2023-07-03 17:50:46", "0", "5", "None", "2023-07-03 17:50:45.792347", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "2", "3", "1", "2023-07-03 17:50:53", "2023-07-03 17:50:53", "0", "7", "None", "2023-07-03 17:50:52.200236", "None", "{}");
INSERT INTO rep_unit VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "0", "2", "4", "1", "2023-07-03 17:51:31", "2023-07-03 17:51:31", "0", "7", "None", "2023-07-03 17:51:30.954055", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "0", "0", "1", "2023-07-03 10:04:52", "2023-07-03 10:04:52", "0", "2", "None", "2023-07-03 10:04:51.995873", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "0", "1", "1", "2023-07-03 10:05:04", "2023-07-03 10:05:04", "0", "2", "None", "2023-07-03 10:05:04.226988", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "0", "2", "1", "2023-07-03 10:05:06", "2023-07-03 10:05:06", "0", "2", "None", "2023-07-03 10:05:06.724699", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "0", "3", "1", "2023-07-03 10:05:18", "2023-07-03 10:05:18", "0", "2", "None", "2023-07-03 10:05:19.050981", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "0", "4", "1", "2023-07-03 10:05:21", "2023-07-03 10:05:21", "0", "1", "None", "2023-07-03 10:05:21.964942", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "1", "0", "1", "2023-07-03 10:04:54", "2023-07-03 10:04:54", "0", "2", "None", "2023-07-03 10:04:54.586575", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "1", "1", "1", "2023-07-03 10:05:01", "2023-07-03 10:05:01", "0", "2", "None", "2023-07-03 10:05:01.789209", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "1", "2", "1", "2023-07-03 10:05:09", "2023-07-03 10:05:09", "0", "2", "None", "2023-07-03 10:05:09.278963", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "1", "3", "1", "2023-07-03 10:05:16", "2023-07-03 10:05:16", "0", "2", "None", "2023-07-03 10:05:16.505066", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "1", "4", "1", "2023-07-03 10:05:24", "2023-07-03 10:05:24", "0", "1", "None", "2023-07-03 10:05:24.559386", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "2", "0", "1", "2023-07-03 10:04:56", "2023-07-03 10:04:56", "0", "2", "None", "2023-07-03 10:04:57.069833", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "2", "1", "1", "2023-07-03 10:04:59", "2023-07-03 10:04:59", "0", "2", "None", "2023-07-03 10:04:59.395113", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "2", "2", "1", "2023-07-03 10:05:11", "2023-07-03 10:05:11", "0", "2", "None", "2023-07-03 10:05:11.654648", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "2", "3", "1", "2023-07-03 10:05:14", "2023-07-03 10:05:14", "0", "1", "None", "2023-07-03 10:05:14.138008", "None", "{}");
INSERT INTO rep_unit VALUES ("FB12882A649C478EA406C295D6D48075", "1", "0", "2", "4", "1", "2023-07-03 10:05:27", "2023-07-03 10:05:27", "0", "1", "None", "2023-07-03 10:05:27.132505", "None", "{}");
