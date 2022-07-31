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
-- Table structure for table `login_details`
--

DROP TABLE IF EXISTS `login_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_details` (
  `id` varchar(12) NOT NULL,
  `uname` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `typeofuser` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_details`
--

LOCK TABLES `login_details` WRITE;
/*!40000 ALTER TABLE `login_details` DISABLE KEYS */;
INSERT INTO `login_details` VALUES ('AD1000','pratham','3ea33a234a07056fcfa972497019c1e3cfcaadf1','admin'),('AD1001','sushant','f73a8ff808ea0a4304ad80fb70cd2fb851e1a54f','admin'),('AD1002','jayshree','1b82c817e99c76c9e4a6f0c6cbf909932493d7d7','admin'),('AD1003','prashant','09aa524fb1e1ba6416355a63919894a109767f81','admin'),('FT10000','shakshi','de71a275ed207d9c2083ebfa9af5dcdfa3ea2b88','faculty'),('FT10001','hemlata','9fc0eb1e2409ac968dd24a5de042a75f8858fd39','faculty'),('FT10002','pushparaj','7059e742d4eaf9dd0d68523f0a7a55202145966e','faculty'),('FT10003','ramesh','53edd6990376d7b5f512d2b5556613ca2567f04c','faculty'),('FT10004','shalini','029d95898629492320b1cfb0436343cd30b8ccb8','faculty'),('FT10005','rajendra','d5410081e43a90610b82a4d8d0f0ae3d24af4aa0','faculty'),('FT10006','tulsidaas','c1de21512a77f3018175b1d3aabd8921f6ac431e','faculty'),('id','uname','password','typeofuser'),('SA1000','prathamesh','e69df97395964dbf7444e83f25a96665543c8cc8','superadmin'),('ST10000','sairin','ca8653995b8f68f8e2bf45f84a50dd607c70b966','student'),('ST10001','naitik','ced0b0560c620233ad2495c2dd150b2ac7d6eccb','student'),('ST10002','dhiraj','45059401976799e150302321ae485dccd44bc431','student'),('ST10003','antra','fe8ef920d18b64861e2cd0ccee858af02532da0a','student'),('ST10004','priyanka','10286aae8a78fb7caf78636d52bcea0e2f9535bd','student'),('ST10005','charulata','895b6636192e24d924a6cca4749cecaf5d44e012','student'),('ST10006','mantasha','6c3aae084d67004332a262ce24bc66eef7466a12','student'),('ST10010','jayesh','f0d2580221200ed5a0a552890386f4d2431f765d','student'),('ST10011','aayush','16e3012aebb10bd15f076e9a63712e8d21bb5cf0','student'),('ST10012','namrata','ec52079585070c9e75666c3a0d54daf4ed38d096','student'),('ST10013','rashmi','a6fc10d2e6a9fda1db818df7208bcb40d82e2429','student'),('ST10014','abdul','3fb86591025780f719fcd21d6fd06a8330659670','student'),('ST10015','harshal','ab54d425fa8ac654e8cdf0307eebcc33ea46d08e','student'),('ST10016','mahesh','6a890e1065a1d4e8df9dcf1d9a2c9c740bbcf8aa','student'),('ST10017','komal','ddcaf8376eb8b84e79aefc166ba5b2973a1d72e8','student'),('ST10018','fatima','1ba1b5b562aef9cd264cace5b7bdd46a7c065c0a','student'),('ST10019','rehan','7b3ff990ff0359ecbf062fb0083fc13ce9185ea7','student'),('ST10020','ravindranath','f180e8e8c854018490cbae03100fc391fdb94283','student'),('ST10021','priya','7694b11562c650495284b33da917eea1d88b160f','student');
/*!40000 ALTER TABLE `login_details` ENABLE KEYS */;
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
