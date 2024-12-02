import mysql.connector
from mysql.connector import Error


CREATE DATABASE  IF NOT EXISTS `bts` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bts`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bts
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `bug`
--

DROP TABLE IF EXISTS `bug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bug` (
  `bugId` int NOT NULL AUTO_INCREMENT,
  `bugPostingDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `custLoginId` varchar(10) NOT NULL,
  `bugStatus` varchar(20) DEFAULT 'New Bug',
  `productName` varchar(45) NOT NULL,
  `bugDesc` text NOT NULL,
  `expertAssignedDate` datetime DEFAULT NULL,
  `expertLoginId` varchar(10) DEFAULT NULL,
  `bugSolvedDate` datetime DEFAULT NULL,
  `solution` text,
  PRIMARY KEY (`bugId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bug`
--

LOCK TABLES `bug` WRITE;
/*!40000 ALTER TABLE `bug` DISABLE KEYS */;
INSERT INTO `bug` VALUES (1,'2023-07-06 00:16:28','cu2001','Solved','Laptop','Screen is flickring','2023-07-11 00:11:17','cu2001','2023-07-11 00:11:45','Pls visit nearest service center'),(2,'2023-07-06 00:20:01','cu2001','Solved','Mobile','keyboard is not working','2023-07-08 05:30:57','ex3002','2023-07-08 05:35:01','Pls visit nearest service center'),(3,'2023-07-06 16:46:31','cu2001','New Bug','lptop','sbjahd',NULL,NULL,NULL,NULL),(4,'2023-07-10 23:54:58','cu2001','New Bug','Mobile','Phone is hanging',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `bug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `custLoginId` varchar(10) NOT NULL,
  `custPassword` varchar(20) DEFAULT NULL,
  `custName` varchar(45) DEFAULT NULL,
  `custAge` int DEFAULT NULL,
  `custPhone` varchar(10) DEFAULT NULL,
  `custEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`custLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('cu1017','aditigupta','Aditi',17,'7765855559','aditi12@gmail.com'),('cu2001','pass1234','priya',21,'11111','priya@demo.com'),('cu2002','password','anjali',22,'5454544','priya@demo.com'),('cu2322','sim123','Simran',19,'12221211','sim123@gm.com'),('diya11','diya123','Diya',21,'99988899','diy@gmail.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `empLoginId` varchar(10) NOT NULL,
  `empPassword` varchar(20) DEFAULT NULL,
  `empType` varchar(20) DEFAULT NULL,
  `empName` varchar(45) DEFAULT NULL,
  `empPhone` varchar(10) DEFAULT NULL,
  `empEmail` varchar(45) DEFAULT NULL,
  `empStatus` varchar(20) DEFAULT 'ACTIVE',
  PRIMARY KEY (`empLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('ad1001','password','admin','Priti Singh','9998887776','help@admin.com','ACTIVE'),('ad1002','123456','Admin','Riya','333344455','riya@123','ACTIVE'),('ad1003','1234@','admin','Riya','4545454543','riyagup@12','ACTIVE'),('ex3001','pass123','expert','DemoUser','444444444','expert@admin.com','ACTIVE'),('ex3002','pass1234','expert','Aditi','444499992','aditi71@admin.com','ACTIVE');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-15 21:52:41
