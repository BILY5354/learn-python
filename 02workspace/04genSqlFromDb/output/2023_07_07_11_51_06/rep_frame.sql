CREATE TABLE `rep_frame` (
  `GUID` char(36) NOT NULL,
  `frameID` int NOT NULL,
  `slotID` int DEFAULT NULL COMMENT '料槽序号',
  `frameCode` varchar(100) DEFAULT NULL,
  `inMagIndex` int DEFAULT NULL COMMENT '入料料盒序号',
  `outMagIndex` int DEFAULT NULL COMMENT '下料料盒序号',
  `inMagCode` varchar(100) DEFAULT NULL COMMENT '入料料盒码',
  `outMagCode` varchar(100) DEFAULT NULL COMMENT '下料料盒码',
  `unitsTotal` int NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `insertTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据插入时间(默认)',
  `info` json DEFAULT NULL,
  PRIMARY KEY (`GUID`,`frameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:16", "2023-07-04 15:29:19", "2023-07-04 15:29:16", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:24", "2023-07-04 15:29:31", "2023-07-04 15:29:24", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:31", "2023-07-04 15:29:38", "2023-07-04 15:29:32", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:38", "2023-07-04 15:29:44", "2023-07-04 15:29:39", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:44", "2023-07-04 15:29:51", "2023-07-04 15:29:45", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:29:51", "2023-07-04 15:30:00", "2023-07-04 15:29:52", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "7", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:00", "2023-07-04 15:30:07", "2023-07-04 15:30:00", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "8", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:07", "2023-07-04 15:30:13", "2023-07-04 15:30:07", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "9", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:13", "2023-07-04 15:30:19", "2023-07-04 15:30:13", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "10", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:19", "2023-07-04 15:30:25", "2023-07-04 15:30:19", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "11", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:25", "2023-07-04 15:30:32", "2023-07-04 15:30:25", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "12", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:32", "2023-07-04 15:30:40", "2023-07-04 15:30:32", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "13", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:40", "2023-07-04 15:30:46", "2023-07-04 15:30:41", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "14", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:46", "2023-07-04 15:30:52", "2023-07-04 15:30:47", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "15", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:30:52", "2023-07-04 15:31:00", "2023-07-04 15:30:53", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "16", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:31:00", "2023-07-04 15:31:09", "2023-07-04 15:31:01", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "17", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:31:09", "2023-07-04 15:31:16", "2023-07-04 15:31:09", "None");
INSERT INTO rep_frame VALUES ("229052128F1E47C38B53B2D6F40DB2A6", "18", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:31:16", "2023-07-04 15:31:19", "2023-07-04 15:31:17", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:40:16", "2023-07-03 17:41:15", "2023-07-03 17:40:17", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:41:21", "2023-07-03 17:42:29", "2023-07-03 17:41:22", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:42:29", "2023-07-03 17:43:34", "2023-07-03 17:42:30", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:43:34", "2023-07-03 17:44:38", "2023-07-03 17:43:35", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:44:38", "2023-07-03 17:45:50", "2023-07-03 17:44:39", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:45:50", "2023-07-03 17:46:54", "2023-07-03 17:45:51", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "7", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:46:54", "2023-07-03 17:47:59", "2023-07-03 17:46:55", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "8", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:47:59", "2023-07-03 17:49:18", "2023-07-03 17:48:00", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "9", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:49:18", "2023-07-03 17:50:52", "2023-07-03 17:49:19", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "10", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:50:52", "2023-07-03 17:53:27", "2023-07-03 17:50:53", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "11", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:53:27", "2023-07-03 17:54:57", "2023-07-03 17:53:28", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "12", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:54:57", "2023-07-03 17:56:41", "2023-07-03 17:54:58", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "13", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:56:41", "2023-07-03 17:59:33", "2023-07-03 17:56:41", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "14", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 17:59:33", "2023-07-03 18:01:16", "2023-07-03 17:59:34", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "15", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 18:01:16", "2023-07-03 18:02:32", "2023-07-03 18:01:17", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "16", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 18:02:32", "2023-07-03 18:03:36", "2023-07-03 18:02:33", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "17", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 18:03:36", "2023-07-03 18:04:39", "2023-07-03 18:03:37", "None");
INSERT INTO rep_frame VALUES ("791F01C3893046A683C5FF7FB6C6CE42", "18", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 18:04:39", "2023-07-03 18:05:43", "2023-07-03 18:04:39", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:38:42", "2023-07-04 15:38:45", "2023-07-04 15:38:43", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:38:49", "2023-07-04 15:38:55", "2023-07-04 15:38:49", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:38:55", "2023-07-04 15:39:00", "2023-07-04 15:38:55", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:39:00", "2023-07-04 15:39:06", "2023-07-04 15:39:01", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:39:06", "2023-07-04 15:39:13", "2023-07-04 15:39:07", "None");
INSERT INTO rep_frame VALUES ("8D385EFC034B48038DE95E98A929F4F9", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:39:13", "2023-07-04 15:39:15", "2023-07-04 15:39:13", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:23:52", "2023-07-04 16:25:01", "2023-07-04 16:23:52", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:25:05", "2023-07-04 16:26:17", "2023-07-04 16:25:05", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:26:17", "2023-07-04 16:27:27", "2023-07-04 16:26:18", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:27:27", "2023-07-04 16:28:32", "2023-07-04 16:27:28", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:28:32", "2023-07-04 16:29:35", "2023-07-04 16:28:33", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:29:35", "2023-07-04 16:30:31", "2023-07-04 16:29:36", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "7", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:30:31", "2023-07-04 16:31:18", "2023-07-04 16:30:31", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "8", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:31:18", "2023-07-04 16:32:16", "2023-07-04 16:31:18", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "9", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:32:16", "2023-07-04 16:33:10", "2023-07-04 16:32:16", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "10", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:33:10", "2023-07-04 16:34:15", "2023-07-04 16:33:11", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "11", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:34:15", "2023-07-04 16:35:22", "2023-07-04 16:34:15", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "12", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:35:22", "2023-07-04 16:36:51", "2023-07-04 16:35:23", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "13", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:36:51", "2023-07-04 16:37:53", "2023-07-04 16:36:52", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "14", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:37:53", "2023-07-04 16:39:09", "2023-07-04 16:37:54", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "15", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:39:09", "2023-07-04 16:40:15", "2023-07-04 16:39:09", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "16", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:40:15", "2023-07-04 16:41:21", "2023-07-04 16:40:16", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "17", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:41:21", "2023-07-04 16:42:27", "2023-07-04 16:41:22", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "18", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:42:27", "2023-07-04 16:43:26", "2023-07-04 16:42:27", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "19", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 16:43:26", "2023-07-04 16:44:32", "2023-07-04 16:43:26", "None");
INSERT INTO rep_frame VALUES ("90373FD6D6254AAB95BB935D46458D3C", "20", "None", "None", "None", "None", "None", "None", "-1", "2023-07-04 16:44:32", "2023-07-04 16:44:32", "2023-07-04 16:44:33", "None");
INSERT INTO rep_frame VALUES ("907D8B3991094EF1B8D12865683BD23B", "1", "None", "None", "None", "None", "None", "None", "15", "2023-07-03 14:21:23", "2023-07-03 14:21:59", "2023-07-03 14:21:23", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:27:10", "2023-07-03 14:27:35", "2023-07-03 14:27:10", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:27:36", "2023-07-03 14:28:03", "2023-07-03 14:27:36", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:28:03", "2023-07-03 14:28:32", "2023-07-03 14:28:03", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:28:32", "2023-07-03 14:28:59", "2023-07-03 14:28:32", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:28:59", "2023-07-03 14:29:25", "2023-07-03 14:28:59", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:29:25", "2023-07-03 14:29:52", "2023-07-03 14:29:25", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "7", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:29:52", "2023-07-03 14:30:19", "2023-07-03 14:29:52", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "8", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:30:19", "2023-07-03 14:30:46", "2023-07-03 14:30:19", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "9", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:30:46", "2023-07-03 14:31:13", "2023-07-03 14:30:46", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "10", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:31:13", "2023-07-03 14:31:40", "2023-07-03 14:31:13", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "11", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:31:40", "2023-07-03 14:32:07", "2023-07-03 14:31:40", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "12", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:32:07", "2023-07-03 14:32:34", "2023-07-03 14:32:07", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "13", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:32:34", "2023-07-03 14:33:01", "2023-07-03 14:32:34", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "14", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:33:01", "2023-07-03 14:33:28", "2023-07-03 14:33:01", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "15", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:33:28", "2023-07-03 14:33:56", "2023-07-03 14:33:28", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "16", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:33:56", "2023-07-03 14:34:23", "2023-07-03 14:33:56", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "17", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:34:23", "2023-07-03 14:34:50", "2023-07-03 14:34:23", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "18", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:34:50", "2023-07-03 14:35:17", "2023-07-03 14:34:50", "None");
INSERT INTO rep_frame VALUES ("A342E5B172DB4F48BD7D2E113F97C19C", "19", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:35:17", "2023-07-03 14:35:43", "2023-07-03 14:35:17", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:45:00", "2023-07-03 09:45:25", "2023-07-03 09:45:00", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:45:27", "2023-07-03 09:45:52", "2023-07-03 09:45:27", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:45:52", "2023-07-03 09:46:19", "2023-07-03 09:45:52", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "4", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:46:19", "2023-07-03 09:46:45", "2023-07-03 09:46:19", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "5", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:46:45", "2023-07-03 09:47:11", "2023-07-03 09:46:45", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "6", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:47:11", "2023-07-03 09:47:37", "2023-07-03 09:47:11", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "7", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:47:37", "2023-07-03 09:48:03", "2023-07-03 09:47:37", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "8", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:48:03", "2023-07-03 09:48:29", "2023-07-03 09:48:03", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "9", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:48:29", "2023-07-03 09:48:56", "2023-07-03 09:48:29", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "10", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:48:56", "2023-07-03 09:49:22", "2023-07-03 09:48:56", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "11", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:49:22", "2023-07-03 09:49:50", "2023-07-03 09:49:22", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "12", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:49:50", "2023-07-03 09:50:17", "2023-07-03 09:49:50", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "13", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:50:17", "2023-07-03 09:50:43", "2023-07-03 09:50:17", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "14", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:50:43", "2023-07-03 09:51:09", "2023-07-03 09:50:43", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "15", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:51:09", "2023-07-03 09:51:35", "2023-07-03 09:51:09", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "16", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:51:35", "2023-07-03 09:52:01", "2023-07-03 09:51:35", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "17", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:52:01", "2023-07-03 09:52:28", "2023-07-03 09:52:01", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "18", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:52:28", "2023-07-03 09:52:55", "2023-07-03 09:52:28", "None");
INSERT INTO rep_frame VALUES ("A6E5DCAA14F84DD58DF7E7B02A4E46C6", "19", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 09:52:55", "2023-07-03 09:53:20", "2023-07-03 09:52:55", "None");
INSERT INTO rep_frame VALUES ("AA8422746B1E445D8A55EEF1BE93C01F", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:01:13", "2023-07-03 14:02:06", "2023-07-03 14:01:14", "None");
INSERT INTO rep_frame VALUES ("AA8422746B1E445D8A55EEF1BE93C01F", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-03 14:02:11", "2023-07-03 14:02:59", "2023-07-03 14:02:12", "None");
INSERT INTO rep_frame VALUES ("AA8422746B1E445D8A55EEF1BE93C01F", "3", "None", "None", "None", "None", "None", "None", "-1", "2023-07-03 14:02:59", "2023-07-03 14:02:59", "2023-07-03 14:03:00", "None");
INSERT INTO rep_frame VALUES ("BA9E9DCF915049A3A311E438A504FF14", "1", "None", "None", "None", "None", "None", "None", "15", "2023-07-03 10:08:36", "2023-07-03 10:09:12", "2023-07-03 10:08:36", "None");
INSERT INTO rep_frame VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "1", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:41:40", "2023-07-04 15:42:43", "2023-07-04 15:41:41", "None");
INSERT INTO rep_frame VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "2", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:42:47", "2023-07-04 15:44:02", "2023-07-04 15:42:47", "None");
INSERT INTO rep_frame VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "3", "None", "None", "None", "None", "None", "None", "1", "2023-07-04 15:44:02", "2023-07-04 15:45:12", "2023-07-04 15:44:03", "None");
INSERT INTO rep_frame VALUES ("BAA6A99777D1406E9F7A13F3533F351D", "4", "None", "None", "None", "None", "None", "None", "-1", "2023-07-04 15:45:12", "2023-07-04 15:45:12", "2023-07-04 15:45:13", "None");
INSERT INTO rep_frame VALUES ("E76A17F5F1734F3883F71636C2FA166C", "1", "None", "None", "None", "None", "None", "None", "15", "2023-07-03 17:49:36", "2023-07-03 17:51:31", "2023-07-03 17:49:35", "None");
INSERT INTO rep_frame VALUES ("FB12882A649C478EA406C295D6D48075", "1", "None", "None", "None", "None", "None", "None", "15", "2023-07-03 10:04:50", "2023-07-03 10:05:27", "2023-07-03 10:04:50", "None");
