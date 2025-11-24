-- MySQL dump 10.13  Distrib 8.4.7, for macos15 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.4.7

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test@test.com','test',0,'2025-11-12 20:16:50'),(2,'wise','wise@test.com','wise',10,'2025-11-12 20:18:07'),(3,'belle','belle@test.com','belle',20,'2025-11-12 20:18:57'),(4,'lucy','lucy@test.com','lucy',0,'2025-11-12 20:19:40'),(5,'nicole','nicole@test.com','nicole',0,'2025-11-12 20:21:10'),(6,'dd','d','d',0,'2025-11-20 21:04:34'),(7,'lex','lex','lex',0,'2025-11-24 21:06:02');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int unsigned NOT NULL,
  `content` text NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'The automobile layout consists of a front-engine design, with transaxle-type transmissions mounted at the rear of the engine and four wheel drive',1,'2025-11-13 00:15:02'),(2,2,'The automobile layout consists of a front-engine design, with transaxle-type transmissions mounted at the rear of the engine and four wheel drive',9618,'2025-11-13 00:16:37'),(3,3,'Carbonite web goalkeeper gloves are ergonomically designed to give easy fit',6401,'2025-11-13 00:17:00'),(4,4,'The slim & simple Maple Gaming Keyboard from Dev Byte comes with a sleek body and 7- Color RGB LED Back-lighting for smart functionality',1,'2025-11-13 00:17:20'),(5,5,'Andy shoes are designed to keeping in mind durability as well as trends, the most stylish range of shoes & sandals',2,'2025-11-13 00:17:36'),(6,1,'The Football Is Good For Training And Recreational Purposes',490,'2025-11-13 00:19:26'),(7,2,'New ABC 13 9370, 13.3, 5th Gen CoreA5-8250U, 8GB RAM, 256GB SSD, power UHD Graphics, OS 10 Home, OS Office A & J 2016',76,'2025-11-13 00:19:45'),(8,3,'Andy shoes are designed to keeping in mind durability as well as trends, the most stylish range of shoes & sandals',83,'2025-11-13 00:20:07'),(9,4,'The Football Is Good For Training And Recreational Purposes',4785,'2025-11-13 00:20:24'),(10,5,'The automobile layout consists of a front-engine design, with transaxle-type transmissions mounted at the rear of the engine and four wheel drive',4,'2025-11-13 00:20:40'),(15,6,'fffff',0,'2025-11-21 22:03:36'),(16,6,'fffff',0,'2025-11-24 06:02:54');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `query_logs`
--

DROP TABLE IF EXISTS `query_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `query_logs` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `target_id` int unsigned DEFAULT NULL,
  `searcher_id` int unsigned DEFAULT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `searcher_id` (`searcher_id`),
  KEY `idx_target_time` (`target_id`,`time` DESC),
  CONSTRAINT `query_logs_ibfk_1` FOREIGN KEY (`target_id`) REFERENCES `member` (`id`),
  CONSTRAINT `query_logs_ibfk_2` FOREIGN KEY (`searcher_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `query_logs`
--

LOCK TABLES `query_logs` WRITE;
/*!40000 ALTER TABLE `query_logs` DISABLE KEYS */;
INSERT INTO `query_logs` VALUES (1,3,6,'2025-11-24 20:21:09'),(2,4,6,'2025-11-24 20:21:15'),(3,4,6,'2025-11-24 20:54:38'),(4,6,6,'2025-11-24 20:54:43'),(5,3,6,'2025-11-24 21:05:02'),(6,4,6,'2025-11-24 21:05:04'),(7,5,6,'2025-11-24 21:05:08'),(8,3,6,'2025-11-24 21:05:19'),(9,6,7,'2025-11-24 21:06:15'),(10,5,7,'2025-11-24 21:06:17'),(11,6,7,'2025-11-24 21:19:43');
/*!40000 ALTER TABLE `query_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-24 21:49:00
