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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` varchar(8) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `middle_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `roll_no` int NOT NULL,
  `division` char(1) NOT NULL,
  `address` text NOT NULL,
  `father_name` varchar(100) NOT NULL,
  `mother_name` varchar(100) NOT NULL,
  `std` int NOT NULL,
  `dob` date DEFAULT NULL,
  `bloodgroup` char(4) DEFAULT NULL,
  `doa` date DEFAULT NULL,
  `father_occ` varchar(100) DEFAULT NULL,
  `mother_occ` varchar(100) DEFAULT NULL,
  `father_phoneno` bigint NOT NULL,
  `sex` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('ST10000','Sairin','Abdul','Khan',1,'A','Boisar near ostwal empire\n\n\n\n','Abdul Khan','Shayna Khan',7,'2005-10-02','B+','2020-10-12','Service','Housewife',9845103287,'Female'),('ST10001','Naitik','chandan','jha',3,'A','Borivali\n','Chandan Jha','Khusboo Jha',7,'2007-07-07','AB+','2020-08-12','Service','Service',4512369874,'Male'),('ST10002','Dhiraj','Sudhakar','gajare',4,'A','Ahemdabad\n','Sudhakar Gajare','Siddhi Gajare',7,'2006-03-27','A+','2020-09-14','Service','Housewife',9856321475,'Male'),('ST10003','Antra','Harshal','Yadav',5,'A','Anand\n','Harshal Yadav','Pooja Yadav',7,'2007-08-12','B+','2020-10-24','Service','Housewife',7895326412,'Female'),('ST10004','Priyanka','Hanumant','Naikwadi',2,'A','near dattawadi palghar \n','Hanumant Naikwadi','Pradnya',7,'2008-03-12','O-','2020-07-11','Service','Service',4523698741,'Female'),('ST10005','charulata','Prakash','Bharate',6,'A','Vadodara\n','Prakash Barahate','Anuradha Barhate',7,'2004-09-27','A-','2020-09-18','Business','Housewife',8452139745,'Female'),('ST10006','Mantasha','Saif','Shaikh',7,'A','Chennai\n','Saif Shaikh','Soumya Shaikh',7,'2004-12-23','O-','2019-02-12','Service','Service',7458963214,'Female'),('ST10010','Jayesh','Kanhaiya','Yadav',8,'A','Tamil\n','Kanhaiya Yadav','Kanishka Yadav',7,'2008-04-25','O+','2020-12-10','Business','Housewife',9853214756,'Male'),('ST10011','Aayush','Kuldeep','Singh',9,'A','Umroli\n','Kuldeep Singh','Bhoomika',7,'2007-10-08','AB-','2020-01-12','Service','Housewife',7852314895,'Male'),('ST10012','Namrata','Deepak','Jadav',1,'B','Palghar\n','Deepak Jadav','Harshala Jadav',7,'2003-09-10','B+','2020-10-03','Service','Housewife',9654128753,'Female'),('ST10013','Rashmi','Hemant','Jadav',2,'B','Kelva Road\n','Hemant Jadav','Lata Jadav',7,'2009-12-12','AB+','2020-12-04','Service','Housewife',7854213985,'Female'),('ST10014','Abdul','Atique','Khan',3,'B','near tvm school\n','Atique Khan','Tanisha Khan',7,'2007-01-23','B-','2020-04-12','Service','Housewife',8512364798,'Male'),('ST10015','Harshal','Vedant','Sarode',4,'B','near panchmarg\n','Vedant Sarode','Dhanvi Sarode',7,'2008-04-12','B+','2020-03-13','Business','Service',8412369547,'Male'),('ST10016','Mahesh','Chinmay','Shelke',5,'B','mumbai central\n','Chinmay Shelke','Divyani Shelke',7,'2009-12-27','A+','2019-09-20','Service','Service',9654123970,'Male'),('ST10017','Komal','Vishwas','Tamore',1,'A','dadar\n','Vishwas Tamore','Anamika Tamore',8,'2007-12-28','B-','2019-04-23','Service','Housewife',7423698501,'Female'),('ST10018','Fatima','Atique ','Shaikh',2,'A','grant road\n','Atique Shaikh','Isma Shaikh',8,'2006-01-23','Ab+','2019-05-28','Business','Service',2874103698,'Female'),('ST10019','Rehan','Tanmay','Shejwal',3,'A','lamingron road\n','Tanmay Shejwal','Snehal Shejwaal',8,'2006-02-12','B+','2019-05-27','Service','Housewife',8741203698,'Male'),('ST10020','Ravindranath','Rakesh','Mishra',4,'A','bhayandar\n','Rakesh Mishra','Rakhi mishra',8,'2006-12-23','Ab+','2019-02-10','Service','Housewive',8523169077,'Male'),('ST10021','Priya','Prince','Sarode',5,'A','Naingoan\n','Prince Sarode','Khushi Sarode',8,'2006-12-23','B-','2019-12-12','Service','Housewife',9652103654,'Female');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `auto_add_fees` AFTER INSERT ON `student` FOR EACH ROW begin
insert into fees values (new.id,"N",year(new.doa),"N","N","N","N","N","N","N","N","N","N","N","N");
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `dele_student_login` AFTER DELETE ON `student` FOR EACH ROW begin
delete from login_details where id=old.id;
end */;;
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

-- Dump completed on 2022-07-31 13:20:53
