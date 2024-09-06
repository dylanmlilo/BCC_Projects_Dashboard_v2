-- MySQL dump 10.13  Distrib 9.0.0, for Win64 (x86_64)
--
-- Host: localhost    Database: bcc_water_data
-- ------------------------------------------------------
-- Server version	9.0.0

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
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity` varchar(255) NOT NULL,
  `output_id` int NOT NULL,
  `responsible_person_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `output_id` (`output_id`),
  KEY `responsible_person_id` (`responsible_person_id`),
  CONSTRAINT `activities_ibfk_1` FOREIGN KEY (`output_id`) REFERENCES `output` (`id`),
  CONSTRAINT `activities_ibfk_2` FOREIGN KEY (`responsible_person_id`) REFERENCES `responsiblepeople` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (1,'Producing a Topographical/ Base Map (80)',1,1),(2,'Conducting Reconnaissance survey (20)',1,2),(3,'Institutionalizing GIS Policy (4)',2,3),(4,'Training staff members (5)',3,4),(5,'Developing web-based application (3)',4,5),(6,'Providing accurate and up- to-date Geo- databases (3)',5,6),(7,'Providing three (3) decision making tools (4)',6,7);
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_type`
--

DROP TABLE IF EXISTS `contract_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_type`
--

LOCK TABLES `contract_type` WRITE;
/*!40000 ALTER TABLE `contract_type` DISABLE KEYS */;
INSERT INTO `contract_type` VALUES (1,'Servicing'),(2,'Services'),(3,'Goods'),(4,'Works');
/*!40000 ALTER TABLE `contract_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dam_data`
--

DROP TABLE IF EXISTS `dam_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dam_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dam_id` int NOT NULL,
  `date` date NOT NULL,
  `dam_reading` decimal(10,2) NOT NULL,
  `dam_percentage` decimal(5,2) NOT NULL,
  `dam_volume` decimal(15,2) NOT NULL,
  `daily_inflow` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dam_id` (`dam_id`),
  CONSTRAINT `dam_data_ibfk_1` FOREIGN KEY (`dam_id`) REFERENCES `dams` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dam_data`
--

LOCK TABLES `dam_data` WRITE;
/*!40000 ALTER TABLE `dam_data` DISABLE KEYS */;
INSERT INTO `dam_data` VALUES (1,1,'2024-03-04',87.18,28.58,23543522.34,100.00),(2,2,'2024-03-04',90.21,50.23,21833794.23,100.00),(3,3,'2024-03-04',89.23,40.34,19782341.54,0.00),(4,4,'2024-03-04',78.34,43.23,18235463.34,100.00),(5,5,'2024-03-04',90.20,41.30,17235243.76,0.00),(6,6,'2024-03-04',88.24,38.67,23847343.21,0.00),(7,1,'2024-03-05',90.23,40.12,26354846.34,0.00),(8,2,'2024-03-05',88.74,45.33,21837463.45,0.00),(9,3,'2024-03-05',80.34,51.45,19263745.33,0.00),(10,4,'2024-03-05',84.22,47.12,18236273.46,0.00),(11,5,'2024-03-05',90.12,46.22,21264538.55,0.00),(12,6,'2024-03-05',89.78,48.25,22546354.33,0.00),(13,1,'2024-03-06',78.22,38.25,21276362.23,0.00),(14,2,'2024-03-06',90.22,45.33,23424232.24,0.00),(15,3,'2024-03-06',87.35,47.22,21323232.45,129.00),(16,4,'2024-03-06',88.34,50.12,23442323.32,100.00),(17,5,'2024-03-06',90.12,49.01,21232323.32,250.00),(18,6,'2024-03-06',86.33,30.00,23423232.34,105.00),(19,1,'2024-03-07',89.32,49.55,21343242.00,0.00),(20,2,'2024-03-07',87.35,58.00,25455553.00,0.00),(21,3,'2024-03-07',87.45,37.33,23232323.00,100.00),(22,4,'2024-03-07',89.34,45.34,22364543.87,50.00),(23,5,'2024-03-07',90.00,50.32,22364543.87,0.00),(24,6,'2024-03-07',89.00,49.32,22338490.87,0.00),(25,4,'2024-03-08',87.00,45.00,23435435.00,400.00),(26,3,'2024-03-10',88.44,45.34,232424324.23,325.00),(27,1,'2024-03-11',87.33,39.05,2334424324.45,0.00),(28,1,'2024-03-15',90.00,45.00,232344334.00,121122.00);
/*!40000 ALTER TABLE `dam_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dams`
--

DROP TABLE IF EXISTS `dams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dam_name` varchar(255) NOT NULL,
  `dam_description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dams`
--

LOCK TABLES `dams` WRITE;
/*!40000 ALTER TABLE `dams` DISABLE KEYS */;
INSERT INTO `dams` VALUES (1,'Inyankuni Dam','Nestled in Insiza District, Zimbabwe, Inyankuni Dam serves as a crucial water source for Bulawayo. Constructed in 1965 on the Inyankuni River, it boasts a maximum capacity of 44 million cubic meters (m³).  This dam has become a vital part of Bulawayo\'s water security since the mid-20th century, supplementing the supplies from Upper Ncema and Umzingwane Dams.  However, water restrictions are likely to be implemented if the dam level falls below 30% capacity. Inyankuni Dam also attracts birdwatchers due to the diverse birdlife found around the dam.'),(2,'Insiza Mayfair Dam','Holding the title of the largest dam supplying water to Bulawayo, Insiza Mayfair Dam boasts a capacity of 109 million cubic meters (m³). Completed in 1933, it\'s the oldest operational dam in the city\'s water system.  Insiza Mayfair Dam played a critical role in Bulawayo\'s development during the early 20th century by providing a reliable water source for its growing population. Water rationing might be necessary if the dam level falls below 40% capacity. The dam\'s scenic location, surrounded by picturesque hills, adds to its significance.'),(3,'Mtshabezi Dam','Located on the Mtshabezi River, Mtshabezi Dam is a multi-purpose dam serving various needs.  This dam, with a capacity of 35.5 million cubic meters (m³), provides water for irrigation, domestic use, and hydropower generation.  Constructed in 1972, Mtshabezi Dam significantly influenced the development of the agricultural sector in the region. The dam\'s hydroelectric power station contributes to the national grid. Water restrictions for irrigation and reduced power generation might occur if the level falls below 25% capacity. The dam also offers recreational opportunities like fishing and boating (during high water levels).'),(4,'uMzingwane Dam','While no longer the primary source, uMzingwane Dam, also known as the Bulawayo Dam, still contributes to the city\'s water supply with a capacity of 12.1 million cubic meters (m³). Built-in 1903, uMzingwane Dam stands as a historical landmark showcasing early water management techniques in Zimbabwe. Water restrictions for Bulawayo are highly likely if the level falls below 15% capacity. The dam and its surroundings are a protected wildlife sanctuary, offering a haven for diverse plant and animal species.'),(5,'Lower Ncema Dam','Although smaller with a capacity of 4.8 million cubic meters (m³), Lower Ncema Dam plays a supporting role in supplying water for Bulawayo and surrounding communities. Constructed in the 1950s, this dam\'s role became crucial as the population grew. Water shortages are likely if the level reaches the critical point of 10% capacity. Lower Ncema Dam also serves as a vital stopover point for migratory birds, attracting birdwatchers to the area.'),(6,'Upper Ncema Dam','Built in 1924 with a capacity of 23.8 million cubic meters (m³), Upper Ncema Dam was one of the first major water sources for Bulawayo.  This dam significantly contributed to Bulawayo\'s early development by supplying water for domestic and industrial uses. Water restrictions for Bulawayo are likely to be implemented if the level dips below 20% capacity.  The dam\'s surroundings, with rolling hills and grasslands, provide opportunities for nature enthusiasts.');
/*!40000 ALTER TABLE `dams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `output`
--

DROP TABLE IF EXISTS `output`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `output` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `output`
--

LOCK TABLES `output` WRITE;
/*!40000 ALTER TABLE `output` DISABLE KEYS */;
INSERT INTO `output` VALUES (1,'Topographical Map Produced'),(2,'Institutionalized GIS Policy'),(3,'Trained staff members'),(4,'Web-based application developed'),(5,'Accurate and up-to-date Geo- databases provided'),(6,'Three (3) decision making tools provided'),(7,'BCC Projects Dashboard Developement');
/*!40000 ALTER TABLE `output` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_managers`
--

DROP TABLE IF EXISTS `project_managers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_managers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `section` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_managers`
--

LOCK TABLES `project_managers` WRITE;
/*!40000 ALTER TABLE `project_managers` DISABLE KEYS */;
INSERT INTO `project_managers` VALUES (1,'M Funi',NULL),(2,'D Gwetu',NULL),(3,'G Mabhena',NULL),(4,'E Moyo',NULL),(5,'A Moyo',NULL),(6,'F Nkawu',NULL),(7,'Tsopo Moyo',NULL),(8,'Nigel Moyo',NULL),(9,'N Moyo',NULL),(10,'E Sibeko',NULL),(11,'S T Zondo',NULL),(12,'M V N Zondo',NULL),(13,'E G Ngwenya',NULL),(14,'Ntokozo Ncube',NULL),(15,'B Sibanda',NULL),(16,'S Mleya',NULL),(17,'C Nkomo',NULL),(18,'C Moyo',NULL),(19,'C Nkomo/D Mlilo',NULL),(20,'V Ndabezwe',NULL),(21,'B Ndlovu',NULL),(22,'Nigel Ngwenya',NULL),(23,'Pauline Sibanda',NULL),(24,'Faith Nkonde',NULL),(25,'Nobleman  Zulu',NULL),(26,'Prosper Mateza',NULL);
/*!40000 ALTER TABLE `project_managers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_data`
--

DROP TABLE IF EXISTS `projects_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contract_number` varchar(50) NOT NULL,
  `contract_name` text,
  `contract_type_id` int DEFAULT NULL,
  `project_manager_id` int DEFAULT NULL,
  `section_id` int DEFAULT NULL,
  `contractor` text,
  `year` varchar(20) DEFAULT NULL,
  `date_contract_signed` date DEFAULT NULL,
  `date_contract_signed_by_bcc` date DEFAULT NULL,
  `early_start_date` date DEFAULT NULL,
  `contract_duration_weeks` decimal(10,2) DEFAULT NULL,
  `contract_duration_months` decimal(10,2) DEFAULT NULL,
  `early_finish_date` date DEFAULT NULL,
  `extension_of_time` date DEFAULT NULL,
  `project_status` varchar(50) DEFAULT NULL,
  `contract_value_including_ten_percent_contingency` decimal(20,2) DEFAULT NULL,
  `performance_guarantee_value` decimal(20,2) DEFAULT NULL,
  `performance_guarantee_expiry_date` date DEFAULT NULL,
  `advance_payment_value` decimal(20,2) DEFAULT NULL,
  `advance_payment_guarantee_expiry_date` date DEFAULT NULL,
  `total_certified_interim_payments_to_date` decimal(20,2) DEFAULT NULL,
  `financial_progress_percentage` decimal(10,2) DEFAULT NULL,
  `roads_progress` decimal(10,2) DEFAULT NULL,
  `water_progress` decimal(10,2) DEFAULT NULL,
  `sewer_progress` decimal(10,2) DEFAULT NULL,
  `storm_drainage_progress` decimal(10,2) DEFAULT NULL,
  `public_lighting_progress` decimal(10,2) DEFAULT NULL,
  `physical_progress_percentage` decimal(10,2) DEFAULT NULL,
  `tax_clearance_validation` varchar(50) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contract_type_id` (`contract_type_id`),
  KEY `project_manager_id` (`project_manager_id`),
  KEY `section_id` (`section_id`),
  CONSTRAINT `projects_data_ibfk_1` FOREIGN KEY (`contract_type_id`) REFERENCES `contract_type` (`id`),
  CONSTRAINT `projects_data_ibfk_2` FOREIGN KEY (`project_manager_id`) REFERENCES `project_managers` (`id`),
  CONSTRAINT `projects_data_ibfk_3` FOREIGN KEY (`section_id`) REFERENCES `section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_data`
--

LOCK TABLES `projects_data` WRITE;
/*!40000 ALTER TABLE `projects_data` DISABLE KEYS */;
INSERT INTO `projects_data` VALUES (1,'COB/ESD/C01/2022','Emganwini High Density Residential Stands (118) Lot 2: Servicing with Roads, Water and Sewer Reticulation Systems',1,4,1,'TCI International (Pvt) Ltd','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,100.00,100.00,100.00,100.00,100.00,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(2,'COB/ESD/D02/2021','Cowdray Park High Density Residential Stands (151) Lot 3: Servicing with Roads, Water and Sewer Reticulation Systems',1,3,1,'Aggregate Properties (Pvt) Ltd','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,100.00,100.00,100.00,100.00,100.00,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(3,'COB/ESD/B45/2022w','Cowdray Park Sewer Diversion',4,3,1,NULL,'2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(4,'COB/ESD/A33/2022','Entumbane Outfall Sewer Rehabilitationn',4,3,1,NULL,'2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(5,'COB/ESD/E01/2021','Umganin Phase IV Residential Stands (730) Lot 2: Servicing with Roads, Water and Sewer Reticulation Systems',1,19,1,'Heaven View Properties','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,0.00,5.00,57.00,48.00,0.00,0.00,23.69,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(6,'COB/ESD/E02/2021','Umganin Phase IV Residential Stands (272) Lot 3: Servicing with Roads, Water, and Sewer Reticulation Systems',1,5,1,'Veluntina Investments','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,0.00,7.00,20.00,18.00,0.00,0.00,25.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(7,'COB/ESD/E03/2021','Umganin Phase IV Residential Stands (473) Lot 4: Servicing with Roads, Water and Sewer Reticulation Systems',1,1,1,'Cabin Lock Construction','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,0.00,30.00,90.00,83.00,0.00,0.00,65.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(8,'COB/ESD/G03/2022','Pumula South 117 stands',1,1,1,'Bulawayo City Council ','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,100.00,100.00,100.00,100.00,100.00,100.00,NULL,'https://drive.google.com/drive/folders/1zTK3f-g21KasXoSUTg-Fqr62wq9N29VJ?usp=sharing'),(9,'COB/ESD/E62/2022','Norwood Tracks Phase 1 2045 Stands',1,3,1,'Masimba Construction and Murena Consortium','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,35.00,32.00,35.00,38.00,0.00,0.00,35.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(10,'COB/ESD/F03/2022','Luveve North 453 Stands',1,4,1,'Natwecraft Investments','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,NULL,16.50,57.00,47.30,0.00,0.00,38.90,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(11,'COB/ESD/V33/2022','Willsgrove Phase 2',1,1,1,'R M Consruction','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,90.00,NULL,NULL,NULL,NULL,NULL,90.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(12,'COB/ESD/G33/2022','Mahatshula East 650 Stands',1,1,1,'Enock Construction and Earth Moving Equipment','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,68.00,NULL,NULL,NULL,NULL,NULL,68.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(13,'COB/ESD/A33/2022','Delta Fairbridge',4,5,1,'None','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1DN08S4fhOBpmDaPyddleqMdtSnDs1Vya?usp=sharing'),(14,'COB/ESD/20E/2017','Servicing of 144 Low Density Stand in Woodville and 14 Medium Density Stands in Paddonhurst with Roads, Water & Sewerage Reticulation',1,5,1,'Asphalt Products (Pvt) Ltd','2018','2018-06-27','2018-07-10','2018-08-06',27.00,28.00,'2019-03-08',NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,39.00,NULL,NULL,NULL,NULL,NULL,39.00,NULL,'https://drive.google.com/drive/folders/1DN08S4fhOBpmDaPyddleqMdtSnDs1Vya?usp=sharing'),(15,'COB/ESD/C49C/2016','Magwegwe West 390 stands: Servicing with Roads, Water and Sewer Reticulation Systems',1,17,1,'Tzircalle Bros PL','2016',NULL,NULL,'2017-04-13',NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,60.00,NULL,NULL,NULL,NULL,NULL,60.00,NULL,'https://drive.google.com/drive/folders/1DN08S4fhOBpmDaPyddleqMdtSnDs1Vya?usp=sharing'),(16,'COB/ESD/C23/2021','Emganwini 155 Stands: Servicing with Roads, Water and Sewer Reticulation Systems',1,4,1,'Natwecraft','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,100.00,100.00,100.00,100.00,100.00,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(17,'COB/ESD/C41D/2022','Rehabilitation of Morningside Outfall Sewer',4,7,3,'Saltaway Enterprises (Pvt) Ltd','2022','2022-11-05','2022-12-05','2022-12-05',28.00,7.00,'2023-06-30',NULL,'In Progress',350252.29,NULL,NULL,NULL,NULL,102886.25,29.00,NULL,NULL,NULL,NULL,NULL,50.00,'VALID','https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(18,'COB/ESD/C44A/2018','Emhlangeni Phase 2 502 Stands',1,20,1,'Bulawayo City Council','2018',NULL,NULL,'2018-10-01',62.00,16.00,'2020-03-31',NULL,'In Progress',4200000.00,NULL,NULL,NULL,NULL,398000.00,35.00,30.00,65.00,11.00,0.00,0.00,28.80,NULL,'https://drive.google.com/drive/folders/15Z8j_QMBsdAA1KGE-5wkSRsv_xhALx_v?usp=drive_link'),(19,'COB/ESD/4D/2021','Rehabilitation of Colbro Outfall Sewer',4,7,3,'Saltaway Enterprises(Pvt)','2022','2022-01-03','2022-01-17','2022-01-17',20.00,5.00,'2022-06-17','2022-09-17','Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,NULL,NULL,NULL,NULL,NULL,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(20,'COB/ESD/C31B/2021','Clearing of Sewer Blockages from identified and prioritised sewer lines in the City of Bulawayo on an \"as and when required\" basis',4,7,3,'Saltaway Enterprises (Pvt) Ltd','2021','2022-03-28','2022-04-04','2022-02-26',16.00,4.00,'2022-06-25','2022-08-10','Completed',460000.00,NULL,NULL,NULL,NULL,458084.35,100.00,NULL,NULL,NULL,NULL,NULL,100.00,'VALID','https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(21,'WATERWORX//B/2021','Replacement of non-functional meters and service connections at Entumbane',4,6,4,'Bulawayo City Council','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,NULL,NULL,NULL,NULL,NULL,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(22,'WATER/FOR/LIFE/2022','Installation of water and sewer connection in Cowdray Park Hlalani Kuhle',4,6,4,'Bulawayo City Council','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,70.00,NULL,NULL,NULL,NULL,NULL,70.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(23,'COB/ESD/40A/2021','Supply and delivery of Water distribution materials',3,6,4,'Actual hardware (Pvt)Ltd','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Retendered',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(24,'COB/ESD/40D/2021','Supply and delivery of  Sewer distribution materials',3,1,4,'Acrifruits','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Retendered',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(25,'COB/ESD/40A/2022','Supply and delivery of  Water distribution materials',3,6,2,'Actual hardware (Pvt)Ltd','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Retendered',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(26,'COB/ESD/40D/2022','Supply and delivery of  Sewer distribution materials',3,1,3,'Spectrum Engineerin(Pvt) Ltd','2022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Retendered',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(27,'COB/ESD/48C/2023','Supply and Delivery of skip bins',NULL,13,5,'Green Earth Waste & Recycling Pvt Ltd','2023','2023-04-19','2023-04-19',NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(28,'COB/ESD/S23/2023','Insiza elevated (100m section)',4,15,1,NULL,'2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(29,'COB/ESD/S24/2023','Installation of Nyamandlovu Flow Meters',4,16,1,NULL,'2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(30,'COB/ESD/S27/2023','Criterion Bypass',4,5,1,NULL,'2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(31,'COB/ESD/S30/2021','DMA Chamber',4,20,1,'Bulawayo City Council','2021',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(32,'COB/ESD/B45/2019','Voullaire Estates',1,20,1,'Private developer','2019',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,15.00,NULL,NULL,NULL,NULL,NULL,15.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(33,'COB/ESD/T45/2023','Framework agreement made for Sewer Cleaning and maintanance of blockages from identified and prioritized areas',4,7,1,NULL,'2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(34,'COB/ESD/T46/2023','UMzingwane bypass',4,19,1,NULL,'2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(35,'COB/ESD/T47/2023','Cowdray Park Water Mains',4,20,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Yet to start',NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(36,'COB/ESD/NS01/2020','Nust accommodation',4,17,1,'Private developer','2020',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Completed',NULL,NULL,NULL,NULL,NULL,NULL,100.00,NULL,NULL,NULL,NULL,NULL,100.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(37,'COB/ESD/WF05/2015','Waterford',1,20,1,'Private developer','2015',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(38,'COB/ESD/WQ10/2023','Supply of water and wastewater chemicals as an on or required bases',2,18,2,'Various companies (AI Davies, Chemplex)','2023',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,20.00,NULL,NULL,NULL,NULL,NULL,24.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(39,'COB/ESD/DS1/2017','Deep Section',4,19,1,'Tzicarlle','2017',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Stopped',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(62,'201569/1','Supply, Intallation and commissioning of water pumps and accessories for Inyankuni pump station',3,21,5,'Water Tight','2024',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,65.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link'),(63,'201569/2','Supply and Installation of water pumps and accessories for Umzingwane Pump Station',3,21,5,'Water Tight','2024',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'In Progress',NULL,NULL,NULL,NULL,NULL,NULL,5.00,NULL,NULL,NULL,NULL,NULL,0.00,NULL,'https://drive.google.com/drive/folders/1Oc32n1-DIfuAPWFEYQ3tcR17C3XrBHn2?usp=drive_link');
/*!40000 ALTER TABLE `projects_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservoir_data`
--

DROP TABLE IF EXISTS `reservoir_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservoir_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reservoir_id` int NOT NULL,
  `date` date NOT NULL,
  `reservoir_level` float NOT NULL,
  `reservoir_percentage` float NOT NULL,
  `reservoir_volume` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reservoir_id` (`reservoir_id`),
  CONSTRAINT `reservoir_data_ibfk_1` FOREIGN KEY (`reservoir_id`) REFERENCES `reservoirs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservoir_data`
--

LOCK TABLES `reservoir_data` WRITE;
/*!40000 ALTER TABLE `reservoir_data` DISABLE KEYS */;
INSERT INTO `reservoir_data` VALUES (1,1,'2024-03-01',12.5,69.83,50040),(2,2,'2024-03-01',17,91.4,41129),(3,3,'2024-03-01',15.6,86.67,58500),(4,4,'2024-03-01',15,78.95,35526.3),(5,5,'2024-03-01',15.9,83.68,37657.9),(6,6,'2024-03-01',2.69,72,64560),(7,7,'2024-03-01',0.91,12.13,169867),(8,1,'2024-03-02',13.5,75.42,0),(9,2,'2024-03-02',16,86.02,38709.7),(10,3,'2024-03-02',11,61.11,41250),(11,4,'2024-03-02',17,89.47,40263.2),(12,5,'2024-03-02',17.5,92.11,41447.4),(13,6,'2024-03-02',2.38,63,57120),(14,7,'2024-03-02',0.91,12.13,169867),(15,1,'2024-03-03',12,67.04,0),(16,1,'2024-03-04',10.5,58.66,0),(17,1,'2024-03-05',13,72.63,0),(18,1,'2024-03-06',13.2,73.74,0),(19,1,'2024-03-07',12.8,71.51,0),(20,1,'2024-03-08',13,72.63,0),(21,1,'2024-03-09',13.5,75.42,0),(22,1,'2024-03-10',12,67.04,0),(23,1,'2024-03-11',13,72.63,0),(24,1,'2024-03-12',15,83.8,0),(25,1,'2024-03-13',13,72.63,0),(26,1,'2024-03-14',13,72.63,0),(27,1,'2024-03-15',13.5,75.42,0),(28,1,'2024-03-16',13,72.63,0),(29,1,'2024-03-17',12,67.04,0),(30,1,'2024-03-18',13,72.63,0),(31,1,'2024-03-19',13,72.63,0),(32,1,'2024-03-20',13,72.63,0),(33,1,'2024-03-21',12,67.04,0),(34,1,'2024-03-22',12,67.04,0),(35,1,'2024-03-23',10,55.87,0),(36,1,'2024-03-24',11,61.45,0),(37,1,'2024-03-25',13,72.63,0),(38,1,'2024-03-26',13,72.63,0),(39,1,'2024-03-27',14,78.21,0),(40,1,'2024-03-28',13,72.63,0),(41,1,'2024-03-29',10,55.87,0),(42,1,'2024-03-30',10.5,58.66,0),(43,1,'2024-03-31',14,78.21,0),(44,1,'2024-04-01',12,67.04,0),(45,2,'2024-03-03',16,86.02,0),(46,2,'2024-03-04',17,91.4,0),(47,2,'2024-03-05',17,91.4,0),(48,2,'2024-03-05',17,91.4,0),(49,2,'2024-03-06',17,91.4,0),(50,2,'2024-03-07',17,91.4,0),(51,2,'2024-03-08',16,86.02,0),(52,2,'2024-03-09',17,91.4,0),(53,2,'2024-03-10',17,91.4,0),(54,2,'2024-03-11',17,91.4,0),(55,2,'2024-03-12',17,91.4,0),(56,2,'2024-03-13',17,91.4,0),(57,2,'2024-03-14',16,86.02,0),(58,2,'2024-03-15',16.5,88.71,0),(59,2,'2024-03-16',15.5,83.33,0),(60,2,'2024-03-17',16.5,88.71,0),(61,2,'2024-03-18',16,86.02,0),(62,2,'2024-03-19',16.5,88.71,0),(63,2,'2024-03-20',15.5,83.33,0),(64,2,'2024-03-21',17,91.4,0),(65,2,'2024-03-22',16,86.02,0),(66,2,'2024-03-23',17,91.4,0),(67,2,'2024-03-24',15,80.65,0),(68,2,'2024-03-25',8,43.01,0),(69,2,'2024-03-26',15,80.65,0),(70,2,'2024-03-27',17,91.4,0),(71,2,'2024-03-28',15.5,83.33,0),(72,2,'2024-03-29',17,91.4,0),(73,2,'2024-03-30',17,91.4,0),(74,2,'2024-03-31',16,86.02,0),(75,2,'2024-04-01',16,86.02,0),(76,2,'2024-04-02',16,86.02,0),(77,3,'2024-03-03',11,61.11,0),(78,3,'2024-03-04',16,88.89,0),(79,3,'2024-03-05',17,94.44,0),(80,3,'2024-03-06',16.5,91.67,0),(81,3,'2024-03-07',15.8,87.78,0),(82,3,'2024-03-08',15.5,86.11,0),(83,3,'2024-03-09',16.3,90.56,0),(84,3,'2024-03-10',17.5,97.22,0),(85,3,'2024-03-11',18,100,0),(86,3,'2024-03-12',13,72.22,0),(87,3,'2024-03-13',13,72.22,0),(88,3,'2024-03-14',15.8,87.78,0),(89,3,'2024-03-15',16.2,90,0),(90,3,'2024-03-16',17,94.44,0),(91,3,'2024-03-17',18,100,0),(92,3,'2024-03-18',16,88.89,0),(93,3,'2024-03-19',15,83.33,0),(94,3,'2024-03-20',14,77.78,0),(95,3,'2024-03-21',16,88.89,0),(96,3,'2024-03-22',16.8,93.33,0),(97,3,'2024-03-23',17.2,95.56,0),(98,3,'2024-03-24',17,94.44,0),(99,3,'2024-03-25',18,100,0),(100,3,'2024-03-26',17,94.44,0),(101,3,'2024-03-27',18,100,0),(102,3,'2024-03-28',17,94.44,0),(103,3,'2024-03-29',17.4,96.67,0),(104,3,'2024-03-30',16,88.89,0),(105,3,'2024-03-31',16,88.89,0),(106,3,'2024-04-01',15,83.33,0),(107,3,'2024-04-02',14,77.78,0),(108,4,'2024-03-03',11.5,60.53,0),(109,4,'2024-03-04',14.5,76.32,0),(110,4,'2024-03-05',17,89.47,0),(111,4,'2024-03-06',18.5,97.37,0),(112,4,'2024-03-07',14,73.68,0),(113,4,'2024-03-08',15.5,81.58,0),(114,4,'2024-03-09',14.5,76.32,0),(115,4,'2024-03-10',15.8,83.16,0),(116,4,'2024-03-11',18,94.74,0),(117,4,'2024-03-12',17,89.47,0),(118,4,'2024-03-13',14.5,76.32,0),(119,4,'2024-03-14',14.8,77.89,0),(120,4,'2024-03-15',14,73.68,0),(121,4,'2024-03-16',12.8,67.37,0),(122,4,'2024-03-17',15,78.95,0),(123,4,'2024-03-18',16.8,88.42,0),(124,4,'2024-03-19',11.8,62.11,0),(125,4,'2024-03-20',15.3,80.53,0),(126,4,'2024-03-21',15.8,83.16,0),(127,4,'2024-03-22',16,84.21,0),(128,4,'2024-03-23',16.2,85.26,0),(129,4,'2024-03-24',13.3,70,0),(130,4,'2024-03-25',11.2,58.95,0),(131,4,'2024-03-26',10.2,53.68,0),(132,4,'2024-03-27',14.8,77.89,0),(133,4,'2024-03-28',10.2,53.68,0),(134,4,'2024-03-29',10,52.63,0),(135,4,'2024-03-30',10,52.63,0),(136,4,'2024-03-31',13,68.42,0),(137,4,'2024-04-01',5,26.32,0),(138,4,'2024-04-02',9,47.37,0);
/*!40000 ALTER TABLE `reservoir_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservoirs`
--

DROP TABLE IF EXISTS `reservoirs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservoirs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reservoir_name` varchar(255) NOT NULL,
  `critical_level` float NOT NULL,
  `max_level` float NOT NULL,
  `design_volume` float NOT NULL,
  `reservoir_description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservoirs`
--

LOCK TABLES `reservoirs` WRITE;
/*!40000 ALTER TABLE `reservoirs` DISABLE KEYS */;
INSERT INTO `reservoirs` VALUES (1,'Magwegwe',9,17.9,10800,'Constructed in 1952, Magwegwe Reservoir played a crucial role in the early development of the city\'s western suburbs. With a design volume of 108,000 cubic meters, it holds a critical level of 9 feet and a maximum capacity of 17.9 feet.  Fun fact: The original design documents for Magwegwe Reservoir are rumored to have been signed by a famous engineer while he was picnicking near the dam site! Today, it primarily supplies water to the growing industrial zone on the city\'s outskirts.'),(2,'Hillside',7,18.6,45000,'Hillside Reservoir, built in 1978, is known for its picturesque location and is a popular spot for birdwatching. Though smaller than its counterparts, with a design volume of 45,000 cubic meters, it provides a vital source of water for the surrounding residential neighborhoods. The reservoir maintains a critical level of 7 feet and a maximum capacity of 8.6 feet.'),(3,'Rifle Range',5,18,67500,'Rifle Range Reservoir, constructed in 1960, has an interesting history. It was originally built to support a nearby shooting range, but its purpose shifted to municipal water supply after the range closed in the 1980s.  Boasting a design volume of 67,500 cubic meters, it has a critical level of 5 feet and a maximum capacity of 18 feet. The reservoir supplies water to the central business district and several high-rise buildings.'),(4,'6J',12,19,45000,'The relatively new 6J Reservoir, completed in 1995, incorporates modern water management technologies.  This 45,000 cubic meter capacity reservoir plays a vital role in ensuring a consistent water supply during peak demand periods. It maintains a critical level of 12 feet and a maximum capacity of 19 feet.  Primarily, 6J Reservoir supplies water to the city\'s eastern suburbs.'),(5,'Tuli',6,19,45000,'Tuli Reservoir, constructed in 1939, is the oldest and largest reservoir in the city\'s network.  With a design volume of 45,000 cubic meters, it has a critical level of 6 feet and a maximum capacity of 19 feet.  Tuli Reservoir serves as a critical backup source during emergencies and supplies water to several outlying communities.'),(6,'Criterion Clear',1,3.75,90000,'Criterion Clear Reservoir, built in 1998, is known for its advanced water treatment facilities.  This 90,000 cubic meter capacity reservoir plays a vital role in supplying high-quality drinking water to the city\'s central areas. It maintains a critical level of 1 meter and a maximum capacity of 3.75 meters.'),(7,'Criterion Raw',1,7.5,140000,'Criterion Raw Reservoir, the largest reservoir in the system completed in 1997, provides raw water for further treatment at the Criterion Water Treatment Plant.  This massive reservoir boasts a design volume of 1,400,000 cubic meters and maintains a critical level of 1 meter and a maximum capacity of 7.5 meters.  It serves as the primary source of water for the entire city.');
/*!40000 ALTER TABLE `reservoirs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responsiblepeople`
--

DROP TABLE IF EXISTS `responsiblepeople`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `responsiblepeople` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `designation` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responsiblepeople`
--

LOCK TABLES `responsiblepeople` WRITE;
/*!40000 ALTER TABLE `responsiblepeople` DISABLE KEYS */;
INSERT INTO `responsiblepeople` VALUES (1,'MrS.MkandlaMr P. Ncube/ MrD.Khumalo/Mr N. Mpofu.','Principal Land Surveyor. Land Survey technicians.'),(2,'Mr D. Khumalo/ Mr P. Ncube/ Mr N. Mpofu &amp; Miss S.Ndhlovu.','Land Survey technicians &amp; Town Planning Officer.'),(3,'Sibusisiwe Sibanda','GIS Manager'),(4,'Bothwell Nhlalo Sibanda','GIS Analyst'),(5,'Roderick Siziba','GIS Analyst'),(6,'Sifelani Ngwenya','GIS Technician'),(7,'Tumisang Faith Ndlovu','GIS Technician'),(8,'Dylan Mlilo','Intern Projects');
/*!40000 ALTER TABLE `responsiblepeople` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `section` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES (1,'Projects'),(2,'Water'),(3,'Sanitation'),(4,'Strategic Planning'),(5,'Electromechanical');
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strategic_tasks`
--

DROP TABLE IF EXISTS `strategic_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strategic_tasks` (
  `task_id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(255) DEFAULT NULL,
  `priority` varchar(255) DEFAULT NULL,
  `deadline` varchar(255) DEFAULT NULL,
  `task` text,
  `description` text,
  `assigned_to` int NOT NULL,
  `deliverables` text,
  `percentage_done` decimal(10,2) DEFAULT NULL,
  `fixed_cost` decimal(10,2) DEFAULT NULL,
  `estimated_hours` decimal(10,2) DEFAULT NULL,
  `actual_hours` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`task_id`),
  KEY `assigned_to` (`assigned_to`),
  CONSTRAINT `strategic_tasks_ibfk_1` FOREIGN KEY (`assigned_to`) REFERENCES `project_managers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strategic_tasks`
--

LOCK TABLES `strategic_tasks` WRITE;
/*!40000 ALTER TABLE `strategic_tasks` DISABLE KEYS */;
INSERT INTO `strategic_tasks` VALUES (1,'Complete','High','02/16/2024','AFDB CAW funding','Proposal Writing',26,'Project Submitted, Passed the first round and waiting for the evaluation stage. ',100.00,NULL,NULL,NULL),(2,'Overdue','High','09/07/2024','AFDB Mitigation Proposal','Proposal Writing',26,NULL,NULL,NULL,NULL,NULL),(3,'In Progress','High','08/10/2024','SDG Challenge Proposal','Proposal Writing',22,NULL,NULL,NULL,NULL,NULL),(4,'In Progress','High','12/06/2024','Hopefountain Underground Water.',NULL,26,NULL,NULL,NULL,NULL,NULL),(5,'In Progress','High',NULL,'Climate, WPC-Cowdray Park, PRIFUND',NULL,24,NULL,NULL,NULL,NULL,NULL),(6,'In Progress','High','31/07/2024','Identification and replacement of non functional DMA meter and monitering.',NULL,22,'Non Functional DMA meters identified. Proposing replacement.',NULL,NULL,NULL,NULL),(7,'Not Started','High','31/07/2024','Tuli Resevoir sensor fixing','Functional Tuli Reservoir sensor',23,NULL,NULL,NULL,NULL,NULL),(8,'In Progress','Medium','Monthly','City Wide Monthly Water Balance(Billed Volume)',NULL,22,'On going, in conjunction with E. Siziba (Finance)',NULL,NULL,NULL,NULL),(9,'In Progress','Medium','Quarterly','DMA Water Balance',NULL,22,NULL,NULL,NULL,NULL,NULL),(10,'In Progress','High','14/06/2024','Climate Resilient Plan',NULL,24,NULL,NULL,NULL,NULL,NULL),(11,'In Progress','High','10/06/2024','Water Safety Plan',NULL,23,'Attending to comments',NULL,NULL,NULL,NULL),(12,'In Progress','High','21/06/2024','Non Revenue Water Strategy',NULL,26,'Attending to comments',NULL,NULL,NULL,NULL),(13,'In Progress','Medium','Regularly','Logging-DMAs, Dams, Supply points',NULL,22,'Umzingwane & Nyamandlovu Logged with assistance of GIZ flexims. DMA Logging continues.',NULL,NULL,NULL,NULL),(14,'In Progress','High','31/07/2024','Energy Policy',NULL,23,NULL,NULL,NULL,NULL,NULL),(15,'Complete','High','Yearly','Analysis of the expected sewer inflows versus the actual sewer  inflows In regard to the waste water recycling.','Analysis of the expected sewer inflows versus the actual sewer inflows In regard to the waste water recycling.',22,'Analysis showing potential sewer that is being spilled into the environment.',NULL,NULL,NULL,NULL),(16,'In Progress','Medium','30/11/2024','Developing a model to run the sewer treatment plant works using  STOAT software as per recommendation of the WWT  STI.',NULL,24,NULL,NULL,NULL,NULL,NULL),(17,'In Progress','Medium','30/11/2024','Developing  a hydrology model to analyse our water resources using the WEAP software.',NULL,25,NULL,NULL,NULL,NULL,NULL),(18,'Complete','Medium','Quarterly',' Inco-operated Carbon balance calculation to project amount of carbon we are producing from water treatment.',NULL,22,'Improved water balance showing the amount of Carbon the City is contributing in terms of emmissions.',NULL,NULL,NULL,NULL),(19,'In Progress','Medium','30/11/2024','Inco-operate above results into LEAP',NULL,26,NULL,NULL,NULL,NULL,NULL),(20,'Complete','High','08/02/2024','Drafting Departmental Program and Subprograms for WASH.',NULL,26,NULL,NULL,NULL,NULL,NULL),(21,'In Progress','Low','30/08/2024','En-roads Climate change',NULL,25,NULL,NULL,NULL,NULL,NULL),(22,'Not Started','Low','30/11/2024','Sewer Hydraulic Model',NULL,24,NULL,NULL,NULL,NULL,NULL),(23,'In Progress','Medium','30/06/2025','Clear Water Hydraulic Model','Calliberating existing / Setting up a new model',22,'Magwegwe Epanet Model, ',NULL,NULL,NULL,NULL),(24,'In Progress','High','30/11/2025','WOPS 2 Proposal and Implementation','Reticulation of Nkulumane, Nketa Boreholes and design of a reservoir',23,'Concept note and implementation plan developed.',NULL,NULL,NULL,NULL),(25,'In Progress','Medium','30/08/2024','NRW Dashboard',NULL,25,NULL,NULL,NULL,NULL,NULL),(26,'Complete','Medium','Yearly','Bulawayo water pipeline efficiency',NULL,22,'53% Efficiency (2023 Figure)',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `strategic_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `activity_id` int NOT NULL,
  `description` text NOT NULL,
  `percentage_of_activity` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,1,'Conducting data searches at Surveyor General’s &amp; deeds office. (10) -picking all existing utilities (10) and infrastructure both onsite and offsite (10), existing servitudes (10), physical attributes of the land (contours, watercourses &amp; terrain) (20).',NULL),(2,2,'Walking of the site with the Town Planner to get an appreciation (60) and establishing ground control points. (40)',NULL),(3,3,'Drafting the GIS policy (2)',NULL),(4,3,'Approving and adopt the GIS Policy (1)',NULL),(5,3,'Implementing the policy(1)',NULL),(6,4,'Identifying training needs and staff (1)',NULL),(7,4,'Training staff members (2)',NULL),(8,4,'Monitoring the trained staff members (2)',NULL),(9,5,'Identifying key areas for web- based application need (0.5)',NULL),(10,5,'Researching on the web-based application focus area (0.5)',NULL),(11,5,'Developing the web-based  Roderick Siziba GIS Analyst  application (1.5)',NULL),(12,5,'Training of staff members in using the web-based application (0.5)',NULL),(13,6,'Collecting relevant and up-to-date data from departments (0.5)',NULL),(14,6,'Cleaning data collected (0.5)',NULL),(15,6,'Creating Geo- databases (0.5)',NULL),(16,6,'Integrating departmental Geo- databases (0.5)',NULL),(17,6,'Housing integrated Geo- database into the server (0.5)',NULL),(18,6,'Allocating of credentials and user types (0.5)',NULL),(19,7,'Identifying decision making tools (1)',NULL),(20,7,'Selecting three decision making tools (1)',NULL),(21,7,'Customizing the selected decision- making tools to suit the users’ needs (2)',NULL);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Dylan','Mlilo','Sherry123#','dylanmlilo12@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-06 10:41:25
