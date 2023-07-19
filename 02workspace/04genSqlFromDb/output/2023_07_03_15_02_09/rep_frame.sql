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
INSERT INTO rep_frame VALUES ("FB12882A649C478EA406C295D6D48075", "1", "None", "None", "None", "None", "None", "None", "15", "2023-07-03 10:04:50", "2023-07-03 10:05:27", "2023-07-03 10:04:50", "None");
