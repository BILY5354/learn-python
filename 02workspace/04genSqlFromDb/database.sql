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
CREATE TABLE `rep_lot` (
  `GUID` char(36) NOT NULL,
  `lotNo` varchar(100) NOT NULL,
  `machineID` varchar(100) NOT NULL,
  `lotRunType` smallint NOT NULL DEFAULT '0' COMMENT 'to separate production / engineering / sampling',
  `lotStatus` smallint NOT NULL DEFAULT '0' COMMENT '1 for runnning, 2 for stopped, 3 for machine finish lot, 4 for offline end lot, 5 stripmap uploading, 6 stripmap all uploaded',
  `startTime` datetime NOT NULL,
  `endTime` datetime DEFAULT NULL,
  `DBID` varchar(100) DEFAULT NULL COMMENT 'Die Bond ID',
  `WBID` varchar(100) DEFAULT NULL COMMENT 'Wire Bond ID',
  `deviceName` varchar(100) DEFAULT NULL COMMENT '设备名称',
  `product` varchar(100) DEFAULT NULL COMMENT '产品名称',
  `framePerMag` int DEFAULT NULL COMMENT 'FramePerMagazine',
  `blockSize` int NOT NULL COMMENT '料片规格-块',
  `rowSize` int NOT NULL COMMENT '料片规格-行',
  `colSize` int NOT NULL COMMENT '料片规格-列',
  `lotSize` int DEFAULT NULL,
  `magCount` int DEFAULT NULL COMMENT '料盒总数',
  `visionRecipe` varchar(100) NOT NULL COMMENT '视觉配方',
  `motionRecipe` varchar(100) NOT NULL COMMENT '运控配方',
  `operatorID` varchar(100) DEFAULT NULL COMMENT '操作员ID',
  `package` varchar(100) DEFAULT NULL COMMENT '封装形式',
  `defects` json NOT NULL COMMENT '缺陷类别',
  `detections` json NOT NULL COMMENT '检测项目',
  `NG` int NOT NULL DEFAULT '0',
  `OK` int NOT NULL DEFAULT '0',
  `frameCount` int DEFAULT NULL COMMENT '批次料片总数',
  `archived` tinyint NOT NULL DEFAULT '0' COMMENT '存档标志位',
  `imgSaveType` tinyint NOT NULL DEFAULT '0' COMMENT '图片保存类型-1. 不保存图片 / 2. 仅保存失败图片 / 3. 保存所有图片',
  `saveImgPath` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '保存图片路径',
  `imgSuffix` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '保存图片后缀',
  `upload` tinyint NOT NULL DEFAULT '0' COMMENT '上传标志位',
  `motionVer` varchar(100) NOT NULL COMMENT '运控版本号',
  `visionVer` varchar(100) NOT NULL COMMENT '视觉版本号',
  `camVer` varchar(100) NOT NULL COMMENT '相机模块版本号',
  `exeVer` varchar(100) NOT NULL COMMENT '主程序版本号',
  `vRecipeVer` varchar(100) NOT NULL COMMENT '视觉配方版本号',
  `mRecipeVer` varchar(100) NOT NULL COMMENT '运控配方版本号',
  `equipmentID` varchar(100) NOT NULL COMMENT '计算机唯一ID',
  `insertTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据插入时间(默认)',
  `info` json DEFAULT NULL COMMENT '预留字段',
  PRIMARY KEY (`GUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `rep_result` (
  `GUID` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `frameID` int NOT NULL,
  `blockID` int NOT NULL COMMENT '块',
  `rowID` int NOT NULL COMMENT '行',
  `colID` int NOT NULL COMMENT '列',
  `objID` int NOT NULL,
  `appID` int NOT NULL,
  `taskID` int NOT NULL,
  `resultID` tinyint NOT NULL,
  `defectID` varchar(100) DEFAULT NULL COMMENT '缺陷类型',
  `draw` json DEFAULT NULL COMMENT '在图上的绘制信息',
  `duration` int NOT NULL,
  `type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `isMeasure` tinyint(1) NOT NULL COMMENT '该检测项是否为测量项',
  `meaValue` float DEFAULT NULL,
  `log` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `insertTime` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '数据插入时间(默认)',
  `updateTime` datetime(6) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '数据更新时间(默认)',
  `info` json DEFAULT NULL,
  PRIMARY KEY (`GUID`,`frameID`,`blockID`,`rowID`,`colID`,`appID`,`objID`,`taskID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  PRIMARY KEY (`GUID`,`frameID`,`blockID`,`rowID`,`colID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
