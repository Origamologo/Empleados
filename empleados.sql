-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: empleados
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Table structure for table `EducationFields`
--

DROP TABLE IF EXISTS `EducationFields`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EducationFields` (
  `EducationField` varchar(255) NOT NULL,
  PRIMARY KEY (`EducationField`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EducationFields`
--

LOCK TABLES `EducationFields` WRITE;
/*!40000 ALTER TABLE `EducationFields` DISABLE KEYS */;
/*!40000 ALTER TABLE `EducationFields` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees`
--

DROP TABLE IF EXISTS `Employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees` (
  `EmployeeID` int NOT NULL,
  `Age` int DEFAULT NULL,
  `Attrition` varchar(3) DEFAULT NULL,
  `BusinessTravel` varchar(255) DEFAULT NULL,
  `DistanceFromHome` int DEFAULT NULL,
  `Education` int DEFAULT NULL,
  `EnvironmentSatisfaction` int DEFAULT NULL,
  `Gender` varchar(1) DEFAULT NULL,
  `JobInvolvement` int DEFAULT NULL,
  `JobLevel` int DEFAULT NULL,
  `JobRole` varchar(255) DEFAULT NULL,
  `JobSatisfaction` int DEFAULT NULL,
  `MaritalStatus` varchar(255) DEFAULT NULL,
  `MonthlyIncome` float DEFAULT NULL,
  `MonthlyRate` int DEFAULT NULL,
  `NumCompaniesWorked` int DEFAULT NULL,
  `OverTime` varchar(3) DEFAULT NULL,
  `PercentSalaryHike` int DEFAULT NULL,
  `PerformanceRating` float DEFAULT NULL,
  `RelationshipSatisfaction` int DEFAULT NULL,
  `StockOptionLevel` int DEFAULT NULL,
  `TotalWorkingYears` float DEFAULT NULL,
  `TrainingTimesLastYear` int DEFAULT NULL,
  `WorkLifeBalance` float DEFAULT NULL,
  `YearsAtCompany` int DEFAULT NULL,
  `YearsSinceLastPromotion` int DEFAULT NULL,
  `YearsWithCurrManager` int DEFAULT NULL,
  `DateOfBirth` int DEFAULT NULL,
  `RemoteWork` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  KEY `JobRole` (`JobRole`),
  CONSTRAINT `Employees_ibfk_1` FOREIGN KEY (`JobRole`) REFERENCES `JobRoles` (`JobRole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `Employees` WRITE;
/*!40000 ALTER TABLE `Employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `Employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JobRoles`
--

DROP TABLE IF EXISTS `JobRoles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JobRoles` (
  `JobRole` varchar(255) NOT NULL,
  `EducationField` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`JobRole`),
  KEY `EducationField` (`EducationField`),
  CONSTRAINT `JobRoles_ibfk_1` FOREIGN KEY (`EducationField`) REFERENCES `EducationFields` (`EducationField`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JobRoles`
--

LOCK TABLES `JobRoles` WRITE;
/*!40000 ALTER TABLE `JobRoles` DISABLE KEYS */;
/*!40000 ALTER TABLE `JobRoles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-22  8:42:10
