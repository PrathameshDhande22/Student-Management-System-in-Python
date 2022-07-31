-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: students_db
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `fees`
--

DROP TABLE IF EXISTS `fees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fees` (
  `id` varchar(8) NOT NULL,
  `fullyearpaid` enum('Y','N') DEFAULT NULL,
  `year_` year NOT NULL,
  `jan` enum('Y','N') DEFAULT NULL,
  `feb` enum('Y','N') DEFAULT NULL,
  `mar` enum('Y','N') DEFAULT NULL,
  `april` enum('Y','N') DEFAULT NULL,
  `may` enum('Y','N') DEFAULT NULL,
  `june` enum('Y','N') DEFAULT NULL,
  `july` enum('Y','N') DEFAULT NULL,
  `aug` enum('Y','N') DEFAULT NULL,
  `sept` enum('Y','N') DEFAULT NULL,
  `oct` enum('Y','N') DEFAULT NULL,
  `nov` enum('Y','N') DEFAULT NULL,
  `dece` enum('Y','N') DEFAULT NULL,
  KEY `id` (`id`),
  KEY `year_` (`year_`),
  CONSTRAINT `fees_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fees_ibfk_2` FOREIGN KEY (`year_`) REFERENCES `store_fees` (`year_`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fees`
--

LOCK TABLES `fees` WRITE;
/*!40000 ALTER TABLE `fees` DISABLE KEYS */;
INSERT INTO `fees` VALUES ('ST10000','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10004','N',2020,'Y','Y','Y','Y','Y','N','N','N','N','N','N','N'),('ST10001','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10002','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10003','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10005','Y',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10006','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10010','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10011','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10012','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10013','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10014','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10015','N',2020,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10016','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10017','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10018','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10019','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10020','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10021','N',2019,'N','N','N','N','N','N','N','N','N','N','N','N'),('ST10004','N',2021,'N','N','N','N','N','N','N','N','N','N','N','N');
/*!40000 ALTER TABLE `fees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-31 13:20:53
