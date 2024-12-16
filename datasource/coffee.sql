-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: coffee
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chitetoder`
--


DROP TABLE IF EXISTS `chitetoder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitetoder` (
  `MAODER` varchar(20) NOT NULL,
  `MANV` varchar(10) NOT NULL,
  `MASP` varchar(10) NOT NULL,
  `SOLUONG` int NOT NULL,
  `GIATIEN` int NOT NULL,
  PRIMARY KEY (`MAODER`,`MANV`,`MASP`),
  KEY `FK_CHITETODER_MASP` (`MASP`),
  CONSTRAINT `FK_CHITETODER_MASP` FOREIGN KEY (`MASP`) REFERENCES `sanpham` (`MASP`),
  CONSTRAINT `FK_CHITETODER_ORDER_MANV` FOREIGN KEY (`MAODER`, `MANV`) REFERENCES `datmon` (`MAODER`, `MANV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitetoder`
--

LOCK TABLES `chitetoder` WRITE;
/*!40000 ALTER TABLE `chitetoder` DISABLE KEYS */;
INSERT INTO `chitetoder` VALUES ('ORD-1','ST001','SP001',1,72000),('ORD-10','ST001','SP001',1,72000),('ORD-10','ST001','SP002',2,112500),('ORD-11','ST001','SP001',1,72000),('ORD-11','ST001','SP002',2,112500),('ORD-12','ST001','SP001',1,72000),('ORD-12','ST001','SP002',2,112500),('ORD-13','ST001','SP001',2,72000),('ORD-14','ST001','SP001',2,72000),('ORD-14','ST001','SP002',4,112500),('ORD-15','ST002','SP001',4,72000),('ORD-15','ST002','SP002',3,112500),('ORD-16','ST002','SP002',4,112500),('ORD-2','ST001','SP001',1,72000),('ORD-3','ST001','SP001',1,72000),('ORD-3','ST001','SP002',1,112500),('ORD-4','ST001','SP001',4,72000),('ORD-5','ST001','SP001',2,72000),('ORD-5','ST001','SP002',4,112500),('ORD-6','ST001','SP001',2,72000),('ORD-6','ST001','SP002',3,112500),('ORD-7','ST001','SP002',2,0),('ORD-8','ST001','SP001',1,0),('ORD-8','ST001','SP002',111,0),('ORD-9','ST001','SP001',2,72000),('ORD-9','ST001','SP002',2,112500);
/*!40000 ALTER TABLE `chitetoder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitietxuatnhapkho`
--

DROP TABLE IF EXISTS `chitietxuatnhapkho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietxuatnhapkho` (
  `STT` int NOT NULL AUTO_INCREMENT,
  `MANL` varchar(20) NOT NULL,
  `MANV` varchar(10) NOT NULL,
  `SOLUONG` int NOT NULL,
  `NGAY` datetime NOT NULL,
  `XUATNHAP` bit(1) DEFAULT NULL,
  `MANCC` varchar(10) NOT NULL,
  PRIMARY KEY (`STT`,`MANL`,`MANV`,`MANCC`),
  KEY `FK_CHITIETXUATNHAPKHO_MANV` (`MANV`),
  KEY `FK_CHITIETXUATNHAPKHO_KHO` (`MANL`,`MANCC`),
  CONSTRAINT `FK_CHITIETXUATNHAPKHO_KHO` FOREIGN KEY (`MANL`, `MANCC`) REFERENCES `kho` (`MANL`, `MANCC`),
  CONSTRAINT `FK_CHITIETXUATNHAPKHO_MANV` FOREIGN KEY (`MANV`) REFERENCES `nhanvien` (`MANV`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietxuatnhapkho`
--

LOCK TABLES `chitietxuatnhapkho` WRITE;
/*!40000 ALTER TABLE `chitietxuatnhapkho` DISABLE KEYS */;
INSERT INTO `chitietxuatnhapkho` VALUES (1,'NL002','MN001',1,'2024-12-08 00:00:00',_binary '','NCC001'),(2,'NL002','MN001',1,'2024-12-08 00:00:00',_binary '','NCC001'),(3,'NL002','MN001',4,'2024-12-08 00:00:00',_binary '\0','NCC001'),(4,'NL002','MN001',4,'2024-12-08 00:00:00',_binary '\0','NCC001'),(5,'NL002','MN001',10,'2024-12-08 00:00:00',_binary '\0','NCC001'),(6,'NL002','MN001',2,'2024-12-09 00:00:00',_binary '\0','NCC001');
/*!40000 ALTER TABLE `chitietxuatnhapkho` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_kho_after_insert` AFTER INSERT ON `chitietxuatnhapkho` FOR EACH ROW BEGIN
    -- Check if XUATNHAP is 1 (Export) or 0 (Import)
    IF NEW.XUATNHAP = 1 THEN
        -- Ensure that stock in KHO does not go negative when exporting
        IF EXISTS (
            SELECT 1
            FROM KHO
            WHERE MANL = NEW.MANL AND MANCC = NEW.MANCC
            AND SOLUONG >= NEW.SOLUONG
        ) THEN
            -- If enough stock exists, update the KHO table (export: subtract stock)
            UPDATE KHO
            SET SOLUONG = SOLUONG - NEW.SOLUONG
            WHERE MANL = NEW.MANL AND MANCC = NEW.MANCC;
        ELSE
            -- If there is not enough stock, raise an error
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough stock in KHO to perform this operation';
        END IF;
    ELSEIF NEW.XUATNHAP = 0 THEN
        -- When importing (XUATNHAP = 0), add the stock to KHO
        UPDATE KHO
        SET SOLUONG = SOLUONG + NEW.SOLUONG
        WHERE MANL = NEW.MANL AND MANCC = NEW.MANCC;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `datmon`
--

DROP TABLE IF EXISTS `datmon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datmon` (
  `MAODER` varchar(20) NOT NULL,
  `NGAYODER` datetime DEFAULT NULL,
  `MANV` varchar(10) NOT NULL,
  `HOANTHANH` bit(1) DEFAULT NULL,
  PRIMARY KEY (`MAODER`,`MANV`),
  UNIQUE KEY `MAODER` (`MAODER`),
  KEY `FK_ORDER_MANV` (`MANV`),
  CONSTRAINT `FK_ORDER_MANV` FOREIGN KEY (`MANV`) REFERENCES `nhanvien` (`MANV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datmon`
--

LOCK TABLES `datmon` WRITE;
/*!40000 ALTER TABLE `datmon` DISABLE KEYS */;
INSERT INTO `datmon` VALUES ('ORD-1','2024-12-08 17:17:31','ST001',_binary '\0'),('ORD-10','2024-12-08 20:01:19','ST001',_binary '\0'),('ORD-11','2024-12-08 20:01:48','ST001',_binary '\0'),('ORD-12','2024-12-08 20:15:10','ST001',_binary ''),('ORD-13','2024-12-08 20:15:51','ST001',_binary ''),('ORD-14','2024-12-08 20:19:32','ST001',_binary ''),('ORD-15','2024-12-08 20:43:21','ST002',_binary ''),('ORD-16','2024-12-08 23:05:02','ST002',_binary ''),('ORD-2','2024-12-08 17:29:26','ST001',NULL),('ORD-3','2024-12-08 17:38:03','ST001',NULL),('ORD-4','2024-12-08 18:00:10','ST001',NULL),('ORD-5','2024-12-08 18:00:33','ST001',NULL),('ORD-6','2024-12-08 18:02:27','ST001',NULL),('ORD-7','2024-12-08 18:57:29','ST001',_binary ''),('ORD-8','2024-12-08 19:07:39','ST001',_binary ''),('ORD-9','2024-12-08 19:57:26','ST001',NULL);
/*!40000 ALTER TABLE `datmon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kho`
--

DROP TABLE IF EXISTS `kho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kho` (
  `MANL` varchar(20) NOT NULL,
  `TENNL` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `SOLUONG` int NOT NULL,
  `DONVI` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `XUATXU` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `MANCC` varchar(10) NOT NULL,
  PRIMARY KEY (`MANL`,`MANCC`),
  UNIQUE KEY `MANL` (`MANL`),
  KEY `FK_KHO_NHACUNGCAP` (`MANCC`),
  CONSTRAINT `FK_KHO_NHACUNGCAP` FOREIGN KEY (`MANCC`) REFERENCES `nhacungcap` (`MANCC`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kho`
--

LOCK TABLES `kho` WRITE;
/*!40000 ALTER TABLE `kho` DISABLE KEYS */;
INSERT INTO `kho` VALUES ('NL001','Arabica',100,'kg','Vietnam','NCC001'),('NL002','Sữa Brother',16,'lon','Vietnam','NCC001'),('NL003','Đường Trung Nguyên',10,'bao','Vietnam','NCC001'),('NL004','Robusta',0,'kg','VietNam','NCC001');
/*!40000 ALTER TABLE `kho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhacungcap`
--

DROP TABLE IF EXISTS `nhacungcap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhacungcap` (
  `MANCC` varchar(10) NOT NULL,
  `TENNCC` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `SODT` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `DIACHI` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`MANCC`),
  UNIQUE KEY `MANCC` (`MANCC`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhacungcap`
--

LOCK TABLES `nhacungcap` WRITE;
/*!40000 ALTER TABLE `nhacungcap` DISABLE KEYS */;
INSERT INTO `nhacungcap` VALUES ('NCC001','Trung Nguyen','sale@trungnguyenlegend.com','19006011','82-84 Bùi Thị Xuân, P. Bến Thành, Q.1, Tp Hồ Chí Minh'),('NCC002','Buôn Mê','sale@rangxaycaphe.com.vn','0918555302','35/4A Ao Đôi, Bình Trị Đông A, Quận Bình Tân, Tp.HCM');
/*!40000 ALTER TABLE `nhacungcap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `MANV` varchar(10) NOT NULL,
  `MANAGER` varchar(10) DEFAULT NULL,
  `TEN` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `SODT` varchar(10) NOT NULL,
  `CCCD` varchar(10) NOT NULL,
  `DIACHI` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `PHUONG` varchar(10) NOT NULL,
  `QUAN` varchar(10) NOT NULL,
  `NGAYSINH` datetime NOT NULL,
  `CHINHANH` varchar(10) NOT NULL,
  `NGAYTHAMGIA` datetime NOT NULL,
  `HOATDONG` bit(1) NOT NULL,
  `CHUCVU` varchar(10) NOT NULL,
  `PASS` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MANV`),
  UNIQUE KEY `MANV` (`MANV`),
  UNIQUE KEY `SODT` (`SODT`),
  UNIQUE KEY `CCCD` (`CCCD`),
  KEY `FK_MANAGER` (`MANAGER`),
  CONSTRAINT `FK_MANAGER` FOREIGN KEY (`MANAGER`) REFERENCES `nhanvien` (`MANV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
INSERT INTO `nhanvien` VALUES ('MN001',NULL,'Lý Văn A','09011113','10000003','54 Nguyễn Chí Thanh','7','10','1999-10-20 00:00:00','CH2','2024-12-07 00:00:00',_binary '','manager','man@123'),('ST001','MN001','Nguyễn Văn A','09011111','10000001','52 Nguyễn Chí Thanh','7','10','1999-10-20 00:00:00','CH1','2024-12-07 00:00:00',_binary '','staff','sta@123'),('ST002','MN001','Nguyễn Văn B','09011112','10000002','53 Nguyễn Chí Thanh','7','10','1999-10-20 00:00:00','CH1','2024-12-07 00:00:00',_binary '','staff','sta@123'),('ST003','MN001','Lý Văn E','23456789','23000001','34 Lý Phong','8','10','2000-12-08 00:00:00','CH2','2024-12-08 00:00:00',_binary '','staff','sta@123');
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanpham`
--

DROP TABLE IF EXISTS `sanpham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sanpham` (
  `MASP` varchar(10) NOT NULL,
  `TENSP` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `GIATIEN` int NOT NULL,
  `HINH` blob,
  PRIMARY KEY (`MASP`),
  UNIQUE KEY `MASP` (`MASP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanpham`
--

LOCK TABLES `sanpham` WRITE;
/*!40000 ALTER TABLE `sanpham` DISABLE KEYS */;
INSERT INTO `sanpham` VALUES ('SP001','Espresso',72000,NULL),('SP002','Latte',112500,NULL),('SP003','Cappuccino',10000,NULL),('SP004','Coffee milk tea',20000,NULL);
/*!40000 ALTER TABLE `sanpham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'coffee'
--

--
-- Dumping routines for database 'coffee'
--
/*!50003 DROP PROCEDURE IF EXISTS `FindMatchingNhanVien` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `FindMatchingNhanVien`(
    IN p_MANV VARCHAR(10),
    IN p_PASS VARCHAR(10),
    IN p_CHUCVU VARCHAR(10),
    OUT p_Result VARCHAR(3)
)
BEGIN
    -- Check for matching rows
    IF EXISTS (
        SELECT 1
        FROM NHANVIEN
        WHERE MANV = p_MANV
          AND PASS = p_PASS
          AND CHUCVU = p_CHUCVU
    ) THEN
        SET p_Result = 'Yes';  -- Match found
    ELSE
        SET p_Result = 'No';   -- No match found
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateNhanVienPass` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateNhanVienPass`(
    IN p_MANV VARCHAR(10),
    IN p_NewPass VARCHAR(10),
    OUT p_Result VARCHAR(20)
)
BEGIN
    -- Check if the record exists
    IF EXISTS (
        SELECT 1
        FROM NHANVIEN
        WHERE MANV = p_MANV
    ) THEN
        -- Update the PASS column
        UPDATE NHANVIEN
        SET PASS = p_NewPass
        WHERE MANV = p_MANV;
        
        SET p_Result = 'Success';
    ELSE
        SET p_Result = 'not found';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-09 12:19:20
