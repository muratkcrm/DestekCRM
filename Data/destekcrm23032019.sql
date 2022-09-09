-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: destekcrm
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add site',7,'add_site'),(26,'Can change site',7,'change_site'),(27,'Can delete site',7,'delete_site'),(28,'Can view site',7,'view_site'),(29,'Can add satis duyurular',8,'add_satisduyurular'),(30,'Can change satis duyurular',8,'change_satisduyurular'),(31,'Can delete satis duyurular',8,'delete_satisduyurular'),(32,'Can view satis duyurular',8,'view_satisduyurular'),(33,'Can add satis gorusmesi',9,'add_satisgorusmesi'),(34,'Can change satis gorusmesi',9,'change_satisgorusmesi'),(35,'Can delete satis gorusmesi',9,'delete_satisgorusmesi'),(36,'Can view satis gorusmesi',9,'view_satisgorusmesi'),(37,'Can add satis kurumlar',10,'add_satiskurumlar'),(38,'Can change satis kurumlar',10,'change_satiskurumlar'),(39,'Can delete satis kurumlar',10,'delete_satiskurumlar'),(40,'Can view satis kurumlar',10,'view_satiskurumlar'),(41,'Can add satis sozlesmeler',11,'add_satissozlesmeler'),(42,'Can change satis sozlesmeler',11,'change_satissozlesmeler'),(43,'Can delete satis sozlesmeler',11,'delete_satissozlesmeler'),(44,'Can view satis sozlesmeler',11,'view_satissozlesmeler'),(45,'Can add satis sozlesme takip',12,'add_satissozlesmetakip'),(46,'Can change satis sozlesme takip',12,'change_satissozlesmetakip'),(47,'Can delete satis sozlesme takip',12,'delete_satissozlesmetakip'),(48,'Can view satis sozlesme takip',12,'view_satissozlesmetakip'),(49,'Can add satis uygulama',13,'add_satisuygulama'),(50,'Can change satis uygulama',13,'change_satisuygulama'),(51,'Can delete satis uygulama',13,'delete_satisuygulama'),(52,'Can view satis uygulama',13,'view_satisuygulama'),(53,'Can add st ssatis notlar',14,'add_stssatisnotlar'),(54,'Can change st ssatis notlar',14,'change_stssatisnotlar'),(55,'Can delete st ssatis notlar',14,'delete_stssatisnotlar'),(56,'Can view st ssatis notlar',14,'view_stssatisnotlar'),(57,'Can add destek talebi kayit',15,'add_destektalebikayit'),(58,'Can change destek talebi kayit',15,'change_destektalebikayit'),(59,'Can delete destek talebi kayit',15,'delete_destektalebikayit'),(60,'Can view destek talebi kayit',15,'view_destektalebikayit'),(61,'Can add destek talebi notlar',16,'add_destektalebinotlar'),(62,'Can change destek talebi notlar',16,'change_destektalebinotlar'),(63,'Can delete destek talebi notlar',16,'delete_destektalebinotlar'),(64,'Can view destek talebi notlar',16,'view_destektalebinotlar'),(65,'Can add destek talebi turu',17,'add_destektalebituru'),(66,'Can change destek talebi turu',17,'change_destektalebituru'),(67,'Can delete destek talebi turu',17,'delete_destektalebituru'),(68,'Can view destek talebi turu',17,'view_destektalebituru'),(69,'Can add duyurular',18,'add_duyurular'),(70,'Can change duyurular',18,'change_duyurular'),(71,'Can delete duyurular',18,'delete_duyurular'),(72,'Can view duyurular',18,'view_duyurular'),(73,'Can add kategori',19,'add_kategori'),(74,'Can change kategori',19,'change_kategori'),(75,'Can delete kategori',19,'delete_kategori'),(76,'Can view kategori',19,'view_kategori'),(77,'Can add kisi',20,'add_kisi'),(78,'Can change kisi',20,'change_kisi'),(79,'Can delete kisi',20,'delete_kisi'),(80,'Can view kisi',20,'view_kisi'),(81,'Can add kurum birimi',21,'add_kurumbirimi'),(82,'Can change kurum birimi',21,'change_kurumbirimi'),(83,'Can delete kurum birimi',21,'delete_kurumbirimi'),(84,'Can view kurum birimi',21,'view_kurumbirimi'),(85,'Can add kurumlar',22,'add_kurumlar'),(86,'Can change kurumlar',22,'change_kurumlar'),(87,'Can delete kurumlar',22,'delete_kurumlar'),(88,'Can view kurumlar',22,'view_kurumlar'),(89,'Can add uygulama',23,'add_uygulama'),(90,'Can change uygulama',23,'change_uygulama'),(91,'Can delete uygulama',23,'delete_uygulama'),(92,'Can view uygulama',23,'view_uygulama'),(93,'Can add onm cari kayit',24,'add_onmcarikayit'),(94,'Can change onm cari kayit',24,'change_onmcarikayit'),(95,'Can delete onm cari kayit',24,'delete_onmcarikayit'),(96,'Can view onm cari kayit',24,'view_onmcarikayit'),(97,'Can add onm duyurular',25,'add_onmduyurular'),(98,'Can change onm duyurular',25,'change_onmduyurular'),(99,'Can delete onm duyurular',25,'delete_onmduyurular'),(100,'Can view onm duyurular',25,'view_onmduyurular'),(101,'Can add onm hesap',26,'add_onmhesap'),(102,'Can change onm hesap',26,'change_onmhesap'),(103,'Can delete onm hesap',26,'delete_onmhesap'),(104,'Can view onm hesap',26,'view_onmhesap'),(105,'Can add onm hesap kasa tutar',27,'add_onmhesapkasatutar'),(106,'Can change onm hesap kasa tutar',27,'change_onmhesapkasatutar'),(107,'Can delete onm hesap kasa tutar',27,'delete_onmhesapkasatutar'),(108,'Can view onm hesap kasa tutar',27,'view_onmhesapkasatutar'),(109,'Can add onm hesap plani',28,'add_onmhesapplani'),(110,'Can change onm hesap plani',28,'change_onmhesapplani'),(111,'Can delete onm hesap plani',28,'delete_onmhesapplani'),(112,'Can view onm hesap plani',28,'view_onmhesapplani'),(113,'Can add onm hesap plani detay',29,'add_onmhesapplanidetay'),(114,'Can change onm hesap plani detay',29,'change_onmhesapplanidetay'),(115,'Can delete onm hesap plani detay',29,'delete_onmhesapplanidetay'),(116,'Can view onm hesap plani detay',29,'view_onmhesapplanidetay'),(117,'Can add onm kasa banka',30,'add_onmkasabanka'),(118,'Can change onm kasa banka',30,'change_onmkasabanka'),(119,'Can delete onm kasa banka',30,'delete_onmkasabanka'),(120,'Can view onm kasa banka',30,'view_onmkasabanka'),(121,'Can add onm personel',31,'add_onmpersonel'),(122,'Can change onm personel',31,'change_onmpersonel'),(123,'Can delete onm personel',31,'delete_onmpersonel'),(124,'Can view onm personel',31,'view_onmpersonel'),(125,'Can add onm stok kart',32,'add_onmstokkart'),(126,'Can change onm stok kart',32,'change_onmstokkart'),(127,'Can delete onm stok kart',32,'delete_onmstokkart'),(128,'Can view onm stok kart',32,'view_onmstokkart'),(129,'Can add onm stok liste',33,'add_onmstokliste'),(130,'Can change onm stok liste',33,'change_onmstokliste'),(131,'Can delete onm stok liste',33,'delete_onmstokliste'),(132,'Can view onm stok liste',33,'view_onmstokliste'),(133,'Can add gelen belge',34,'add_gelenbelge'),(134,'Can change gelen belge',34,'change_gelenbelge'),(135,'Can delete gelen belge',34,'delete_gelenbelge'),(136,'Can view gelen belge',34,'view_gelenbelge'),(137,'Can add not defteri kayit',35,'add_notdefterikayit'),(138,'Can change not defteri kayit',35,'change_notdefterikayit'),(139,'Can delete not defteri kayit',35,'delete_notdefterikayit'),(140,'Can view not defteri kayit',35,'view_notdefterikayit'),(141,'Can add not defteri notlar',36,'add_notdefterinotlar'),(142,'Can change not defteri notlar',36,'change_notdefterinotlar'),(143,'Can delete not defteri notlar',36,'delete_notdefterinotlar'),(144,'Can view not defteri notlar',36,'view_notdefterinotlar'),(145,'Can add not duyurular',37,'add_notduyurular'),(146,'Can change not duyurular',37,'change_notduyurular'),(147,'Can delete not duyurular',37,'delete_notduyurular'),(148,'Can view not duyurular',37,'view_notduyurular');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$kIZVjVYQqrNY$kCSFeP8lqAd8uNn0M5Zn+rILz08EgjvVmwdEfRjSFYU=','2019-03-29 14:37:44.392387',1,'murat','murat','karakas','karakasmur@gmail.com',1,1,'2019-03-25 17:50:04.339935'),(2,'pbkdf2_sha256$120000$qvKbSaXfogWZ$oLq+hJbbUHNMGrY8yvLMZP/qHdL/UjzTgo36nqoUzDA=','2019-03-26 13:12:13.084030',1,'murat1','murat','karakas','karakasmur@hotmail.com',1,1,'2019-03-26 13:08:34.262214');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(34,'EvrakTakip','gelenbelge'),(35,'NotDefteri','notdefterikayit'),(36,'NotDefteri','notdefterinotlar'),(37,'NotDefteri','notduyurular'),(24,'OnMuhasebe','onmcarikayit'),(25,'OnMuhasebe','onmduyurular'),(26,'OnMuhasebe','onmhesap'),(27,'OnMuhasebe','onmhesapkasatutar'),(28,'OnMuhasebe','onmhesapplani'),(29,'OnMuhasebe','onmhesapplanidetay'),(30,'OnMuhasebe','onmkasabanka'),(31,'OnMuhasebe','onmpersonel'),(32,'OnMuhasebe','onmstokkart'),(33,'OnMuhasebe','onmstokliste'),(8,'Satis','satisduyurular'),(9,'Satis','satisgorusmesi'),(10,'Satis','satiskurumlar'),(11,'Satis','satissozlesmeler'),(12,'Satis','satissozlesmetakip'),(13,'Satis','satisuygulama'),(14,'Satis','stssatisnotlar'),(6,'sessions','session'),(7,'sites','site'),(15,'TalepYonetimi','destektalebikayit'),(16,'TalepYonetimi','destektalebinotlar'),(17,'TalepYonetimi','destektalebituru'),(18,'TalepYonetimi','duyurular'),(19,'TalepYonetimi','kategori'),(20,'TalepYonetimi','kisi'),(21,'TalepYonetimi','kurumbirimi'),(22,'TalepYonetimi','kurumlar'),(23,'TalepYonetimi','uygulama');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-25 17:49:01.861955'),(2,'auth','0001_initial','2019-03-25 17:49:03.748317'),(3,'EvrakTakip','0001_initial','2019-03-25 17:49:03.986572'),(4,'OnMuhasebe','0001_initial','2019-03-25 17:49:07.188846'),(5,'NotDefteri','0001_initial','2019-03-25 17:49:08.298041'),(6,'Satis','0001_initial','2019-03-25 17:49:10.687117'),(7,'TalepYonetimi','0001_initial','2019-03-25 17:49:14.767752'),(8,'admin','0001_initial','2019-03-25 17:49:15.168738'),(9,'admin','0002_logentry_remove_auto_add','2019-03-25 17:49:15.199975'),(10,'admin','0003_logentry_add_action_flag_choices','2019-03-25 17:49:15.237730'),(11,'contenttypes','0002_remove_content_type_name','2019-03-25 17:49:15.600977'),(12,'auth','0002_alter_permission_name_max_length','2019-03-25 17:49:15.754600'),(13,'auth','0003_alter_user_email_max_length','2019-03-25 17:49:15.886093'),(14,'auth','0004_alter_user_username_opts','2019-03-25 17:49:15.917335'),(15,'auth','0005_alter_user_last_login_null','2019-03-25 17:49:16.155597'),(16,'auth','0006_require_contenttypes_0002','2019-03-25 17:49:16.155597'),(17,'auth','0007_alter_validators_add_error_messages','2019-03-25 17:49:16.202447'),(18,'auth','0008_alter_user_username_max_length','2019-03-25 17:49:16.434179'),(19,'auth','0009_alter_user_last_name_max_length','2019-03-25 17:49:16.929912'),(20,'sessions','0001_initial','2019-03-25 17:49:17.041619'),(21,'sites','0001_initial','2019-03-25 17:49:17.107227'),(22,'sites','0002_alter_domain_unique','2019-03-25 17:49:17.159108');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2x40pbp9g5f28i6ytss3sycrg0iakjf5','MzExYzM0MTBiZDZlMTM3YjI4ZTk0N2Y1Y2JkNGMyNDI1YjYzNTc0Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MzA2ODgxYmZmNzFiZGU0ZDYwNGU4YzcwMmZiYmFiNDk1NjU5ZjViIn0=','2019-04-12 14:37:50.921618'),('3tukgqtmqy8e6j2nipp2crv8uo66vbfu','MGY0Y2EwZmQzZGZmY2MxYTQ0MTAxOTczODU4MmMxOTBmMjJmYTc1Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MzA2ODgxYmZmNzFiZGU0ZDYwNGU4YzcwMmZiYmFiNDk1NjU5ZjViIiwiRGVzdGVrVGFsZWJpc2F5aXNpQWt0aWZzIjowLCJEZXN0ZWtUYWxlYmlzYXlpc2lQYXNpZnMiOjAsIkRlc3Rla1RhbGViaXNheWlzaXMiOjAsIktpc2lTYXlpc2kiOjAsIlV5Z3VsYW1hU2F5aXNpIjowLCJLdXJ1bVNheWlzaXMiOjAsIkJpcmltU2F5aXNpcyI6MCwia3VydW1sYXJHdW5jZWxsZUlEIjoxfQ==','2019-04-09 13:16:47.799897');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evraktakip_gelenbelge`
--

DROP TABLE IF EXISTS `evraktakip_gelenbelge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `evraktakip_gelenbelge` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `GlnBelgeNosu` varchar(50) NOT NULL,
  `GLNBelgeKayitTarihi` datetime(6) DEFAULT NULL,
  `GLNBelgeKurum` varchar(50) NOT NULL,
  `GLNBelgeKurumSayisi` varchar(50) NOT NULL,
  `GLNBelgeUretimTarihi` datetime(6) DEFAULT NULL,
  `GLNBelgeKonu` varchar(50) NOT NULL,
  `GLNBelgeAciklama` longtext NOT NULL,
  `GLNBelgeEk` varchar(50) NOT NULL,
  `GLNBelgeDosya` varchar(100) DEFAULT NULL,
  `GLNBelgeAktif` tinyint(1) NOT NULL,
  `GLNBelgeUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `EvrakTakip_gelenbelge_GLNBelgeUser_id_4978fb5b_fk_auth_user_id` (`GLNBelgeUser_id`),
  CONSTRAINT `EvrakTakip_gelenbelge_GLNBelgeUser_id_4978fb5b_fk_auth_user_id` FOREIGN KEY (`GLNBelgeUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evraktakip_gelenbelge`
--

LOCK TABLES `evraktakip_gelenbelge` WRITE;
/*!40000 ALTER TABLE `evraktakip_gelenbelge` DISABLE KEYS */;
/*!40000 ALTER TABLE `evraktakip_gelenbelge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notdefteri_notdefterikayit`
--

DROP TABLE IF EXISTS `notdefteri_notdefterikayit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `notdefteri_notdefterikayit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NotBaslik` varchar(250) DEFAULT NULL,
  `NotStokOlcuBirimi` varchar(50) NOT NULL,
  `NotStokMiktar` double DEFAULT NULL,
  `NotStokAlisFiyati` double DEFAULT NULL,
  `NotNakiyeMasraf` double DEFAULT NULL,
  `NotDigerMasraf` double DEFAULT NULL,
  `NotToplam` double DEFAULT NULL,
  `NotOran` double DEFAULT NULL,
  `NotMamul` double DEFAULT NULL,
  `NotAdres` varchar(250) DEFAULT NULL,
  `NotIl` varchar(50) DEFAULT NULL,
  `NotIlce` varchar(50) DEFAULT NULL,
  `NotEmail` varchar(254) DEFAULT NULL,
  `NotYetkili` varchar(150) DEFAULT NULL,
  `NotTelefon` varchar(50) DEFAULT NULL,
  `NotAciklama` varchar(2000) DEFAULT NULL,
  `NotDosya` varchar(100) DEFAULT NULL,
  `NotAktif` tinyint(1) NOT NULL,
  `NotDurumu` varchar(50) NOT NULL,
  `NotSonTarihi` datetime(6) DEFAULT NULL,
  `NotCreate` datetime(6) DEFAULT NULL,
  `NotUser_id` int(11) DEFAULT NULL,
  `StokAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `NotDefteri_notdefterikayit_NotUser_id_b3c60531_fk_auth_user_id` (`NotUser_id`),
  KEY `NotDefteri_notdefter_StokAdi_id_536a7a87_fk_OnMuhaseb` (`StokAdi_id`),
  CONSTRAINT `NotDefteri_notdefter_StokAdi_id_536a7a87_fk_OnMuhaseb` FOREIGN KEY (`StokAdi_id`) REFERENCES `onmuhasebe_onmstokkart` (`id`),
  CONSTRAINT `NotDefteri_notdefterikayit_NotUser_id_b3c60531_fk_auth_user_id` FOREIGN KEY (`NotUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notdefteri_notdefterikayit`
--

LOCK TABLES `notdefteri_notdefterikayit` WRITE;
/*!40000 ALTER TABLE `notdefteri_notdefterikayit` DISABLE KEYS */;
/*!40000 ALTER TABLE `notdefteri_notdefterikayit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notdefteri_notdefterinotlar`
--

DROP TABLE IF EXISTS `notdefteri_notdefterinotlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `notdefteri_notdefterinotlar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NotDefteriNotlarKonu` varchar(50) NOT NULL,
  `NotDefteriMetin` longtext,
  `NotDefteriOlusturmaTarihi` datetime(6) DEFAULT NULL,
  `NotDefteriNotDosya` varchar(100) DEFAULT NULL,
  `NotDefteriNotAktif` tinyint(1) NOT NULL,
  `NotDefteriKayit_id` int(11) DEFAULT NULL,
  `NotDefteriNotUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `NotDefteri_notdefter_NotDefteriKayit_id_f5075c50_fk_NotDefter` (`NotDefteriKayit_id`),
  KEY `NotDefteri_notdefter_NotDefteriNotUser_id_5994ed9e_fk_auth_user` (`NotDefteriNotUser_id`),
  CONSTRAINT `NotDefteri_notdefter_NotDefteriKayit_id_f5075c50_fk_NotDefter` FOREIGN KEY (`NotDefteriKayit_id`) REFERENCES `notdefteri_notdefterikayit` (`id`),
  CONSTRAINT `NotDefteri_notdefter_NotDefteriNotUser_id_5994ed9e_fk_auth_user` FOREIGN KEY (`NotDefteriNotUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notdefteri_notdefterinotlar`
--

LOCK TABLES `notdefteri_notdefterinotlar` WRITE;
/*!40000 ALTER TABLE `notdefteri_notdefterinotlar` DISABLE KEYS */;
/*!40000 ALTER TABLE `notdefteri_notdefterinotlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notdefteri_notduyurular`
--

DROP TABLE IF EXISTS `notdefteri_notduyurular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `notdefteri_notduyurular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NotDuyuruTarihi` datetime(6) NOT NULL,
  `NotDuyuruBaslik` varchar(250) NOT NULL,
  `NotDuyuruAciklama` longtext,
  `NotDuyuruAktif` tinyint(1) NOT NULL,
  `NotDuyuruUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `NotDefteri_notduyuru_NotDuyuruUser_id_851922b2_fk_auth_user` (`NotDuyuruUser_id`),
  CONSTRAINT `NotDefteri_notduyuru_NotDuyuruUser_id_851922b2_fk_auth_user` FOREIGN KEY (`NotDuyuruUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notdefteri_notduyurular`
--

LOCK TABLES `notdefteri_notduyurular` WRITE;
/*!40000 ALTER TABLE `notdefteri_notduyurular` DISABLE KEYS */;
/*!40000 ALTER TABLE `notdefteri_notduyurular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmcarikayit`
--

DROP TABLE IF EXISTS `onmuhasebe_onmcarikayit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmcarikayit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `CariKodu` varchar(50) DEFAULT NULL,
  `CariUnvani` varchar(50) DEFAULT NULL,
  `CariAdi` varchar(50) NOT NULL,
  `CariSoyadi` varchar(50) NOT NULL,
  `CariDurumu` varchar(50) NOT NULL,
  `CariAdres` varchar(50) NOT NULL,
  `CariUlke` varchar(50) DEFAULT NULL,
  `CariIl` varchar(50) DEFAULT NULL,
  `CariIlce` varchar(50) DEFAULT NULL,
  `CariTelefon1` varchar(50) NOT NULL,
  `CariCepTelefon` varchar(50) NOT NULL,
  `CariFaks` varchar(50) NOT NULL,
  `CariEmail` varchar(100) NOT NULL,
  `CariVergiDairesi` varchar(50) NOT NULL,
  `CariVergiNosu` varchar(50) NOT NULL,
  `CariKimlikNosu` varchar(50) NOT NULL,
  `CariKayitTarihi` datetime(6) DEFAULT NULL,
  `CariSonHareketTarihi` datetime(6) DEFAULT NULL,
  `CariAktif` tinyint(1) NOT NULL,
  `HesapAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmcarika_HesapAdi_id_be37b5b7_fk_OnMuhaseb` (`HesapAdi_id`),
  CONSTRAINT `OnMuhasebe_onmcarika_HesapAdi_id_be37b5b7_fk_OnMuhaseb` FOREIGN KEY (`HesapAdi_id`) REFERENCES `onmuhasebe_onmhesapplani` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmcarikayit`
--

LOCK TABLES `onmuhasebe_onmcarikayit` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmcarikayit` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmcarikayit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmduyurular`
--

DROP TABLE IF EXISTS `onmuhasebe_onmduyurular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmduyurular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DuyuruTarihi` datetime(6) NOT NULL,
  `DuyuruBaslik` varchar(250) DEFAULT NULL,
  `DuyuruAciklama` longtext,
  `DuyuruAktif` tinyint(1) NOT NULL,
  `DuyuruUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmduyurular_DuyuruUser_id_9870e69f_fk_auth_user_id` (`DuyuruUser_id`),
  CONSTRAINT `OnMuhasebe_onmduyurular_DuyuruUser_id_9870e69f_fk_auth_user_id` FOREIGN KEY (`DuyuruUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmduyurular`
--

LOCK TABLES `onmuhasebe_onmduyurular` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmduyurular` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmduyurular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmhesap`
--

DROP TABLE IF EXISTS `onmuhasebe_onmhesap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmhesap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ONModemeTarihi` datetime(6) NOT NULL,
  `ONModemeTuru` varchar(50) NOT NULL,
  `ONMKayitTarihi` datetime(6) DEFAULT NULL,
  `StokOlcuBirimi` varchar(50) NOT NULL,
  `ONMHesapAciklama` varchar(250) NOT NULL,
  `ONMMiktar` double DEFAULT NULL,
  `ONMFiyat` double DEFAULT NULL,
  `ONMParaBirimi` varchar(50) NOT NULL,
  `ONMDurumu` varchar(50) NOT NULL,
  `ONMhesapTutar` double DEFAULT NULL,
  `ONMHesapAktif` tinyint(1) NOT NULL,
  `CariAdi_id` int(11) NOT NULL,
  `KasaBankaAdi_id` int(11) NOT NULL,
  `StokAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmhesap_CariAdi_id_69e9f6e0_fk_OnMuhaseb` (`CariAdi_id`),
  KEY `OnMuhasebe_onmhesap_KasaBankaAdi_id_a2ed28cf_fk_OnMuhaseb` (`KasaBankaAdi_id`),
  KEY `OnMuhasebe_onmhesap_StokAdi_id_d88289e7_fk_OnMuhaseb` (`StokAdi_id`),
  CONSTRAINT `OnMuhasebe_onmhesap_CariAdi_id_69e9f6e0_fk_OnMuhaseb` FOREIGN KEY (`CariAdi_id`) REFERENCES `onmuhasebe_onmcarikayit` (`id`),
  CONSTRAINT `OnMuhasebe_onmhesap_KasaBankaAdi_id_a2ed28cf_fk_OnMuhaseb` FOREIGN KEY (`KasaBankaAdi_id`) REFERENCES `onmuhasebe_onmkasabanka` (`id`),
  CONSTRAINT `OnMuhasebe_onmhesap_StokAdi_id_d88289e7_fk_OnMuhaseb` FOREIGN KEY (`StokAdi_id`) REFERENCES `onmuhasebe_onmstokkart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmhesap`
--

LOCK TABLES `onmuhasebe_onmhesap` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmhesap` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmhesap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmhesapkasatutar`
--

DROP TABLE IF EXISTS `onmuhasebe_onmhesapkasatutar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmhesapkasatutar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ONMHesapTarih` datetime(6) DEFAULT NULL,
  `ONMHesapAktarmaSonuBasi` double DEFAULT NULL,
  `ONMHesapSonTarih` datetime(6) DEFAULT NULL,
  `ONMHesapAktarma` double DEFAULT NULL,
  `ONMParaBirimi` varchar(50) NOT NULL,
  `HesapAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmhesapk_HesapAdi_id_fdef15e2_fk_OnMuhaseb` (`HesapAdi_id`),
  CONSTRAINT `OnMuhasebe_onmhesapk_HesapAdi_id_fdef15e2_fk_OnMuhaseb` FOREIGN KEY (`HesapAdi_id`) REFERENCES `onmuhasebe_onmhesapplani` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmhesapkasatutar`
--

LOCK TABLES `onmuhasebe_onmhesapkasatutar` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapkasatutar` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapkasatutar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmhesapplani`
--

DROP TABLE IF EXISTS `onmuhasebe_onmhesapplani`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmhesapplani` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `HesapKodu` varchar(50) DEFAULT NULL,
  `HesapUstKodu` varchar(50) DEFAULT NULL,
  `HesapAdi` varchar(250) DEFAULT NULL,
  `HesapOzelligi` varchar(50) NOT NULL,
  `HesapAcilisTarihi` datetime(6) DEFAULT NULL,
  `HesapSonHareketTarihi` datetime(6) DEFAULT NULL,
  `HesapBilanco` varchar(50) NOT NULL,
  `HesapTuru` varchar(50) NOT NULL,
  `HesapDurumu` varchar(50) NOT NULL,
  `HesapIslem` varchar(50) NOT NULL,
  `HesapDosya` varchar(100) DEFAULT NULL,
  `HesapAciklama` varchar(250) NOT NULL,
  `HesapAktif` tinyint(1) NOT NULL,
  `HesapdetayId` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmhesapplani`
--

LOCK TABLES `onmuhasebe_onmhesapplani` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapplani` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapplani` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmhesapplanidetay`
--

DROP TABLE IF EXISTS `onmuhasebe_onmhesapplanidetay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmhesapplanidetay` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Hesapplan_Id` varchar(50) DEFAULT NULL,
  `DetayHesapKodu` varchar(50) DEFAULT NULL,
  `DetayHesapUstKodu` varchar(50) DEFAULT NULL,
  `DetayHesapAdi` varchar(250) DEFAULT NULL,
  `DetayHesapOzelligi` varchar(50) NOT NULL,
  `DetayHesapSonHareketTarihi` datetime(6) DEFAULT NULL,
  `DetayHesapTuru` varchar(50) NOT NULL,
  `DetayHesapDurumu` varchar(50) NOT NULL,
  `DetayHesapAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmhesapplanidetay`
--

LOCK TABLES `onmuhasebe_onmhesapplanidetay` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapplanidetay` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmhesapplanidetay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmkasabanka`
--

DROP TABLE IF EXISTS `onmuhasebe_onmkasabanka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmkasabanka` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ONMKasaBankaAdi` varchar(50) DEFAULT NULL,
  `ONModemeTuru` varchar(50) NOT NULL,
  `ONMKasaBankaAktif` tinyint(1) NOT NULL,
  `HesapAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmkasaba_HesapAdi_id_0abb30c0_fk_OnMuhaseb` (`HesapAdi_id`),
  CONSTRAINT `OnMuhasebe_onmkasaba_HesapAdi_id_0abb30c0_fk_OnMuhaseb` FOREIGN KEY (`HesapAdi_id`) REFERENCES `onmuhasebe_onmhesapplani` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmkasabanka`
--

LOCK TABLES `onmuhasebe_onmkasabanka` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmkasabanka` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmkasabanka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmpersonel`
--

DROP TABLE IF EXISTS `onmuhasebe_onmpersonel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmpersonel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pAdiSoyadi` varchar(150) NOT NULL,
  `pEmail` varchar(20) NOT NULL,
  `pYasi` smallint(5) unsigned NOT NULL,
  `pTelefon` smallint(5) unsigned NOT NULL,
  `HesapAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmperson_HesapAdi_id_88f6cc6b_fk_OnMuhaseb` (`HesapAdi_id`),
  CONSTRAINT `OnMuhasebe_onmperson_HesapAdi_id_88f6cc6b_fk_OnMuhaseb` FOREIGN KEY (`HesapAdi_id`) REFERENCES `onmuhasebe_onmhesapplani` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmpersonel`
--

LOCK TABLES `onmuhasebe_onmpersonel` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmpersonel` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmpersonel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmstokkart`
--

DROP TABLE IF EXISTS `onmuhasebe_onmstokkart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmstokkart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `StokKodu` varchar(50) DEFAULT NULL,
  `StokAdi` varchar(50) DEFAULT NULL,
  `StokTuru` varchar(50) NOT NULL,
  `StokMiktari` double DEFAULT NULL,
  `StokOlcuBirimi` varchar(50) DEFAULT NULL,
  `StokAlisFiyati` double DEFAULT NULL,
  `StokSatisFiyati` double DEFAULT NULL,
  `StokIndirimMiktari` double DEFAULT NULL,
  `StokFireMiktari` double DEFAULT NULL,
  `StokIslemKullanici` varchar(50) NOT NULL,
  `StokAciklama` varchar(50) DEFAULT NULL,
  `StokKayitTarihi` datetime(6) DEFAULT NULL,
  `StokSonHareketTarihi` datetime(6) DEFAULT NULL,
  `StokAktif` tinyint(1) NOT NULL,
  `HesapAdi_id` int(11) DEFAULT NULL,
  `StokKullanici_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmstokka_HesapAdi_id_5d141929_fk_OnMuhaseb` (`HesapAdi_id`),
  KEY `OnMuhasebe_onmstokkart_StokKullanici_id_aa60d4c7_fk_auth_user_id` (`StokKullanici_id`),
  CONSTRAINT `OnMuhasebe_onmstokka_HesapAdi_id_5d141929_fk_OnMuhaseb` FOREIGN KEY (`HesapAdi_id`) REFERENCES `onmuhasebe_onmhesapplani` (`id`),
  CONSTRAINT `OnMuhasebe_onmstokkart_StokKullanici_id_aa60d4c7_fk_auth_user_id` FOREIGN KEY (`StokKullanici_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmstokkart`
--

LOCK TABLES `onmuhasebe_onmstokkart` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmstokkart` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmstokkart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onmuhasebe_onmstokliste`
--

DROP TABLE IF EXISTS `onmuhasebe_onmstokliste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `onmuhasebe_onmstokliste` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `StokKodu` varchar(50) DEFAULT NULL,
  `StokMiktari` double DEFAULT NULL,
  `StokToplam` double DEFAULT NULL,
  `StokOlcuBirimi` varchar(50) DEFAULT NULL,
  `StokKayitTarihi` datetime(6) DEFAULT NULL,
  `StokSonHareketTarihi` datetime(6) DEFAULT NULL,
  `StokAktif` tinyint(1) NOT NULL,
  `StokAdi_id` int(11) DEFAULT NULL,
  `StokKullanici_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `OnMuhasebe_onmstokli_StokAdi_id_24ca092e_fk_OnMuhaseb` (`StokAdi_id`),
  KEY `OnMuhasebe_onmstokli_StokKullanici_id_bf13293a_fk_auth_user` (`StokKullanici_id`),
  CONSTRAINT `OnMuhasebe_onmstokli_StokAdi_id_24ca092e_fk_OnMuhaseb` FOREIGN KEY (`StokAdi_id`) REFERENCES `onmuhasebe_onmstokkart` (`id`),
  CONSTRAINT `OnMuhasebe_onmstokli_StokKullanici_id_bf13293a_fk_auth_user` FOREIGN KEY (`StokKullanici_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onmuhasebe_onmstokliste`
--

LOCK TABLES `onmuhasebe_onmstokliste` WRITE;
/*!40000 ALTER TABLE `onmuhasebe_onmstokliste` DISABLE KEYS */;
/*!40000 ALTER TABLE `onmuhasebe_onmstokliste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satisduyurular`
--

DROP TABLE IF EXISTS `satis_satisduyurular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satisduyurular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DuyuruTarihi` datetime(6) NOT NULL,
  `DuyuruBaslik` varchar(250) DEFAULT NULL,
  `DuyuruAciklama` longtext,
  `DuyuruAktif` tinyint(1) NOT NULL,
  `DuyuruUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Satis_satisduyurular_DuyuruUser_id_a68763e7_fk_auth_user_id` (`DuyuruUser_id`),
  CONSTRAINT `Satis_satisduyurular_DuyuruUser_id_a68763e7_fk_auth_user_id` FOREIGN KEY (`DuyuruUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satisduyurular`
--

LOCK TABLES `satis_satisduyurular` WRITE;
/*!40000 ALTER TABLE `satis_satisduyurular` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satisduyurular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satisgorusmesi`
--

DROP TABLE IF EXISTS `satis_satisgorusmesi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satisgorusmesi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `SatisKonu` varchar(50) NOT NULL,
  `SatisGorusulenKisi` varchar(50) NOT NULL,
  `SatisGorusulenKisiTelefon` varchar(20) DEFAULT NULL,
  `SatisGorusulenKisiMail` varchar(50) DEFAULT NULL,
  `SatisDurumu` varchar(50) NOT NULL,
  `SatisAciklama` longtext NOT NULL,
  `SatisDosya` varchar(100) DEFAULT NULL,
  `SatisBaslamaTarihi` datetime(6) DEFAULT NULL,
  `SatisKapanmaTarihi` datetime(6) DEFAULT NULL,
  `SatisAktif` tinyint(1) NOT NULL,
  `SatisKurum_id` int(11) DEFAULT NULL,
  `SatisUser_id` int(11) DEFAULT NULL,
  `SatisUygulama_id` int(11),
  PRIMARY KEY (`id`),
  KEY `Satis_satisgorusmesi_SatisKurum_id_ca3fa02a_fk_Satis_sat` (`SatisKurum_id`),
  KEY `Satis_satisgorusmesi_SatisUser_id_d6a3742e_fk_auth_user_id` (`SatisUser_id`),
  KEY `Satis_satisgorusmesi_SatisUygulama_id_d477829e_fk_Satis_sat` (`SatisUygulama_id`),
  CONSTRAINT `Satis_satisgorusmesi_SatisKurum_id_ca3fa02a_fk_Satis_sat` FOREIGN KEY (`SatisKurum_id`) REFERENCES `satis_satiskurumlar` (`id`),
  CONSTRAINT `Satis_satisgorusmesi_SatisUser_id_d6a3742e_fk_auth_user_id` FOREIGN KEY (`SatisUser_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `Satis_satisgorusmesi_SatisUygulama_id_d477829e_fk_Satis_sat` FOREIGN KEY (`SatisUygulama_id`) REFERENCES `satis_satisuygulama` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satisgorusmesi`
--

LOCK TABLES `satis_satisgorusmesi` WRITE;
/*!40000 ALTER TABLE `satis_satisgorusmesi` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satisgorusmesi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satiskurumlar`
--

DROP TABLE IF EXISTS `satis_satiskurumlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satiskurumlar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `KurumAdi` varchar(250) NOT NULL,
  `KurumAdres` varchar(250) DEFAULT NULL,
  `KurumIl` varchar(50) DEFAULT NULL,
  `KurumEmail` varchar(254) DEFAULT NULL,
  `KurumYetkili` varchar(150) DEFAULT NULL,
  `KurumTelefon` varchar(50) DEFAULT NULL,
  `KurumAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satiskurumlar`
--

LOCK TABLES `satis_satiskurumlar` WRITE;
/*!40000 ALTER TABLE `satis_satiskurumlar` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satiskurumlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satissozlesmeler`
--

DROP TABLE IF EXISTS `satis_satissozlesmeler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satissozlesmeler` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `SozlesmeBaslangicTarihi` date NOT NULL,
  `SozlesmeBitisTarihi` date NOT NULL,
  `SozlesmeKurum` varchar(250) DEFAULT NULL,
  `SozlesmeKonusu` longtext,
  `SozlesmeDurumu` varchar(50) NOT NULL,
  `SozlesmeAktif` tinyint(1) NOT NULL,
  `SozlesmeUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Satis_satissozlesmeler_SozlesmeUser_id_d49497f9_fk_auth_user_id` (`SozlesmeUser_id`),
  CONSTRAINT `Satis_satissozlesmeler_SozlesmeUser_id_d49497f9_fk_auth_user_id` FOREIGN KEY (`SozlesmeUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satissozlesmeler`
--

LOCK TABLES `satis_satissozlesmeler` WRITE;
/*!40000 ALTER TABLE `satis_satissozlesmeler` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satissozlesmeler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satissozlesmetakip`
--

DROP TABLE IF EXISTS `satis_satissozlesmetakip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satissozlesmetakip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `SatisSozlesmeBitisTarihi` date NOT NULL,
  `SatisSozlesmeKurum` varchar(250) DEFAULT NULL,
  `SatisSozlesmeKonusu` longtext,
  `SatisSozlesmeAktif` tinyint(1) NOT NULL,
  `SatisSozlesmeUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Satis_satissozlesmet_SatisSozlesmeUser_id_694a8f90_fk_auth_user` (`SatisSozlesmeUser_id`),
  CONSTRAINT `Satis_satissozlesmet_SatisSozlesmeUser_id_694a8f90_fk_auth_user` FOREIGN KEY (`SatisSozlesmeUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satissozlesmetakip`
--

LOCK TABLES `satis_satissozlesmetakip` WRITE;
/*!40000 ALTER TABLE `satis_satissozlesmetakip` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satissozlesmetakip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_satisuygulama`
--

DROP TABLE IF EXISTS `satis_satisuygulama`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_satisuygulama` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `UygulamaAdi` varchar(30) NOT NULL,
  `UygulamaAciklama` varchar(150) NOT NULL,
  `UygulamaAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_satisuygulama`
--

LOCK TABLES `satis_satisuygulama` WRITE;
/*!40000 ALTER TABLE `satis_satisuygulama` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_satisuygulama` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satis_stssatisnotlar`
--

DROP TABLE IF EXISTS `satis_stssatisnotlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `satis_stssatisnotlar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `satisNotlarKonu` varchar(50) DEFAULT NULL,
  `satisMetin` longtext,
  `satisOlusturmaTarihi` datetime(6) DEFAULT NULL,
  `satisNotDosya` varchar(100) DEFAULT NULL,
  `satisNotAktif` tinyint(1) NOT NULL,
  `satisGorusmesi_id` int(11) DEFAULT NULL,
  `satisNotUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Satis_stssatisnotlar_satisGorusmesi_id_a6e1fd79_fk_Satis_sat` (`satisGorusmesi_id`),
  KEY `Satis_stssatisnotlar_satisNotUser_id_21251bdd_fk_auth_user_id` (`satisNotUser_id`),
  CONSTRAINT `Satis_stssatisnotlar_satisGorusmesi_id_a6e1fd79_fk_Satis_sat` FOREIGN KEY (`satisGorusmesi_id`) REFERENCES `satis_satisgorusmesi` (`id`),
  CONSTRAINT `Satis_stssatisnotlar_satisNotUser_id_21251bdd_fk_auth_user_id` FOREIGN KEY (`satisNotUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satis_stssatisnotlar`
--

LOCK TABLES `satis_stssatisnotlar` WRITE;
/*!40000 ALTER TABLE `satis_stssatisnotlar` DISABLE KEYS */;
/*!40000 ALTER TABLE `satis_stssatisnotlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_destektalebikayit`
--

DROP TABLE IF EXISTS `talepyonetimi_destektalebikayit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_destektalebikayit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DestekTalebiKonu` varchar(100) NOT NULL,
  `DestekTalebiDurumu` varchar(50) NOT NULL,
  `DestekTalebiAciklama` longtext NOT NULL,
  `DestekTalebiDosya` varchar(100) DEFAULT NULL,
  `DestekTalebiBaslamaTarihi` datetime(6) DEFAULT NULL,
  `DestekTalebiKapanmaTarihi` datetime(6) DEFAULT NULL,
  `DestekTalebiAktif` tinyint(1) NOT NULL,
  `DestekTalebiBirim_id` int(11) NOT NULL,
  `DestekTalebiKisi_id` int(11) NOT NULL,
  `DestekTalebiKurum_id` int(11) DEFAULT NULL,
  `DestekTalebiTuruAdi_id` int(11),
  `DestekTalebiUser_id` int(11) DEFAULT NULL,
  `DestekTalebiUygulama_id` int(11),
  PRIMARY KEY (`id`),
  KEY `TalepYonetimi_destektalebikayit_DestekTalebiBirim_id_ce734ead` (`DestekTalebiBirim_id`),
  KEY `TalepYonetimi_destektalebikayit_DestekTalebiKisi_id_bc487aef` (`DestekTalebiKisi_id`),
  KEY `TalepYonetimi_destek_DestekTalebiKurum_id_6142481b_fk_TalepYone` (`DestekTalebiKurum_id`),
  KEY `TalepYonetimi_destek_DestekTalebiTuruAdi__8db47844_fk_TalepYone` (`DestekTalebiTuruAdi_id`),
  KEY `TalepYonetimi_destek_DestekTalebiUser_id_d3e0a771_fk_auth_user` (`DestekTalebiUser_id`),
  KEY `TalepYonetimi_destek_DestekTalebiUygulama_c1bfcb6f_fk_TalepYone` (`DestekTalebiUygulama_id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiBirim_id_ce734ead_fk_TalepYone` FOREIGN KEY (`DestekTalebiBirim_id`) REFERENCES `talepyonetimi_kurumbirimi` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiKisi_id_bc487aef_fk_TalepYone` FOREIGN KEY (`DestekTalebiKisi_id`) REFERENCES `talepyonetimi_kisi` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiKurum_id_6142481b_fk_TalepYone` FOREIGN KEY (`DestekTalebiKurum_id`) REFERENCES `talepyonetimi_kurumlar` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiTuruAdi__8db47844_fk_TalepYone` FOREIGN KEY (`DestekTalebiTuruAdi_id`) REFERENCES `talepyonetimi_destektalebituru` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiUser_id_d3e0a771_fk_auth_user` FOREIGN KEY (`DestekTalebiUser_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiUygulama_c1bfcb6f_fk_TalepYone` FOREIGN KEY (`DestekTalebiUygulama_id`) REFERENCES `talepyonetimi_uygulama` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_destektalebikayit`
--

LOCK TABLES `talepyonetimi_destektalebikayit` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_destektalebikayit` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_destektalebikayit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_destektalebinotlar`
--

DROP TABLE IF EXISTS `talepyonetimi_destektalebinotlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_destektalebinotlar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DestekTalebiNotlarKonu` varchar(50) NOT NULL,
  `Metin` longtext,
  `OlusturmaTarihi` datetime(6) DEFAULT NULL,
  `DestekTalebiNotDosya` varchar(100) DEFAULT NULL,
  `DestekTalebiNotAktif` tinyint(1) NOT NULL,
  `DestekTalebiKayit_id` int(11) DEFAULT NULL,
  `DestekTalebiNotUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TalepYonetimi_destek_DestekTalebiKayit_id_e662a20b_fk_TalepYone` (`DestekTalebiKayit_id`),
  KEY `TalepYonetimi_destek_DestekTalebiNotUser__56d6c91d_fk_auth_user` (`DestekTalebiNotUser_id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiKayit_id_e662a20b_fk_TalepYone` FOREIGN KEY (`DestekTalebiKayit_id`) REFERENCES `talepyonetimi_destektalebikayit` (`id`),
  CONSTRAINT `TalepYonetimi_destek_DestekTalebiNotUser__56d6c91d_fk_auth_user` FOREIGN KEY (`DestekTalebiNotUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_destektalebinotlar`
--

LOCK TABLES `talepyonetimi_destektalebinotlar` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_destektalebinotlar` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_destektalebinotlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_destektalebituru`
--

DROP TABLE IF EXISTS `talepyonetimi_destektalebituru`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_destektalebituru` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DestekTalebiAdi` varchar(30) NOT NULL,
  `DestekTalebiAciklama` varchar(150) NOT NULL,
  `DestekTalebiAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_destektalebituru`
--

LOCK TABLES `talepyonetimi_destektalebituru` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_destektalebituru` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_destektalebituru` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_duyurular`
--

DROP TABLE IF EXISTS `talepyonetimi_duyurular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_duyurular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DuyuruTarihi` datetime(6) NOT NULL,
  `DuyuruBaslik` varchar(250) NOT NULL,
  `DuyuruAciklama` longtext,
  `DuyuruAktif` tinyint(1) NOT NULL,
  `DuyuruUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TalepYonetimi_duyurular_DuyuruUser_id_58634e95_fk_auth_user_id` (`DuyuruUser_id`),
  CONSTRAINT `TalepYonetimi_duyurular_DuyuruUser_id_58634e95_fk_auth_user_id` FOREIGN KEY (`DuyuruUser_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_duyurular`
--

LOCK TABLES `talepyonetimi_duyurular` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_duyurular` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_duyurular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_kategori`
--

DROP TABLE IF EXISTS `talepyonetimi_kategori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_kategori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `KategoriAdi` varchar(50) NOT NULL,
  `KategoriAciklama` varchar(150) DEFAULT NULL,
  `KategoriAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_kategori`
--

LOCK TABLES `talepyonetimi_kategori` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_kategori` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_kategori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_kisi`
--

DROP TABLE IF EXISTS `talepyonetimi_kisi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_kisi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `KisiAdiSoyadi` varchar(250) NOT NULL,
  `KisiTelefon` varchar(50) DEFAULT NULL,
  `KisiEmail` varchar(254) DEFAULT NULL,
  `KisiAktif` tinyint(1) NOT NULL,
  `KisiBirimAdi_id` int(11) NOT NULL,
  `KisiUser_id` int(11) DEFAULT NULL,
  `KurumAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TalepYonetimi_kisi_KisiBirimAdi_id_301ac3f0` (`KisiBirimAdi_id`),
  KEY `TalepYonetimi_kisi_KisiUser_id_424f0d17_fk_auth_user_id` (`KisiUser_id`),
  KEY `TalepYonetimi_kisi_KurumAdi_id_8366cc67_fk_TalepYone` (`KurumAdi_id`),
  CONSTRAINT `TalepYonetimi_kisi_KisiBirimAdi_id_301ac3f0_fk_TalepYone` FOREIGN KEY (`KisiBirimAdi_id`) REFERENCES `talepyonetimi_kurumbirimi` (`id`),
  CONSTRAINT `TalepYonetimi_kisi_KisiUser_id_424f0d17_fk_auth_user_id` FOREIGN KEY (`KisiUser_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `TalepYonetimi_kisi_KurumAdi_id_8366cc67_fk_TalepYone` FOREIGN KEY (`KurumAdi_id`) REFERENCES `talepyonetimi_kurumlar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_kisi`
--

LOCK TABLES `talepyonetimi_kisi` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_kisi` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_kisi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_kurumbirimi`
--

DROP TABLE IF EXISTS `talepyonetimi_kurumbirimi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_kurumbirimi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `BirimAdi` varchar(250) NOT NULL,
  `BirimAdresi` varchar(250) DEFAULT NULL,
  `BirimEmail` varchar(254) DEFAULT NULL,
  `BirimYetkili` varchar(150) DEFAULT NULL,
  `BirimTelefon` varchar(50) DEFAULT NULL,
  `BirimAktif` tinyint(1) NOT NULL,
  `BirimCreate` datetime(6) DEFAULT NULL,
  `KurumAdi_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TalepYonetimi_kurumb_KurumAdi_id_a52ad940_fk_TalepYone` (`KurumAdi_id`),
  CONSTRAINT `TalepYonetimi_kurumb_KurumAdi_id_a52ad940_fk_TalepYone` FOREIGN KEY (`KurumAdi_id`) REFERENCES `talepyonetimi_kurumlar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_kurumbirimi`
--

LOCK TABLES `talepyonetimi_kurumbirimi` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_kurumbirimi` DISABLE KEYS */;
INSERT INTO `talepyonetimi_kurumbirimi` VALUES (1,'İL SAĞLIK MÜDÜRLÜĞÜ','ÇORUM',NULL,NULL,NULL,1,'2019-03-26 13:16:47.671726',1);
/*!40000 ALTER TABLE `talepyonetimi_kurumbirimi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_kurumlar`
--

DROP TABLE IF EXISTS `talepyonetimi_kurumlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_kurumlar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `KurumAdi` varchar(250) NOT NULL,
  `KurumAdres` varchar(250) DEFAULT NULL,
  `KurumIl` varchar(50) DEFAULT NULL,
  `KurumEmail` varchar(254) DEFAULT NULL,
  `KurumYetkili` varchar(150) DEFAULT NULL,
  `KurumTelefon` varchar(50) DEFAULT NULL,
  `KurumAktif` tinyint(1) NOT NULL,
  `KurumCreate` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_kurumlar`
--

LOCK TABLES `talepyonetimi_kurumlar` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_kurumlar` DISABLE KEYS */;
INSERT INTO `talepyonetimi_kurumlar` VALUES (1,'ÇORUM İL SAĞLIK MÜDÜRLÜĞÜ','ÇORUM','ÇORUM',NULL,NULL,NULL,1,'2019-03-26 13:15:36.981145');
/*!40000 ALTER TABLE `talepyonetimi_kurumlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talepyonetimi_uygulama`
--

DROP TABLE IF EXISTS `talepyonetimi_uygulama`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `talepyonetimi_uygulama` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `UygulamaAdi` varchar(30) NOT NULL,
  `UygulamaAciklama` varchar(150) NOT NULL,
  `UygulamaAktif` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talepyonetimi_uygulama`
--

LOCK TABLES `talepyonetimi_uygulama` WRITE;
/*!40000 ALTER TABLE `talepyonetimi_uygulama` DISABLE KEYS */;
/*!40000 ALTER TABLE `talepyonetimi_uygulama` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_talepyonetimi_kurumbirimi`
--

DROP TABLE IF EXISTS `v_talepyonetimi_kurumbirimi`;
/*!50001 DROP VIEW IF EXISTS `v_talepyonetimi_kurumbirimi`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_talepyonetimi_kurumbirimi` AS SELECT 
 1 AS `id`,
 1 AS `KurumAdi`,
 1 AS `BirimAdi`,
 1 AS `BirimAdresi`,
 1 AS `BirimEmail`,
 1 AS `BirimYetkili`,
 1 AS `BirimTelefon`,
 1 AS `BirimAktif`,
 1 AS `BirimCreate`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'destekcrm'
--

--
-- Dumping routines for database 'destekcrm'
--

--
-- Final view structure for view `v_talepyonetimi_kurumbirimi`
--

/*!50001 DROP VIEW IF EXISTS `v_talepyonetimi_kurumbirimi`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_talepyonetimi_kurumbirimi` AS select `a`.`id` AS `id`,`b`.`KurumAdi` AS `KurumAdi`,`a`.`BirimAdi` AS `BirimAdi`,`a`.`BirimAdresi` AS `BirimAdresi`,`a`.`BirimEmail` AS `BirimEmail`,`a`.`BirimYetkili` AS `BirimYetkili`,`a`.`BirimTelefon` AS `BirimTelefon`,`a`.`BirimAktif` AS `BirimAktif`,`a`.`BirimCreate` AS `BirimCreate` from (`talepyonetimi_kurumbirimi` `a` join `talepyonetimi_kurumlar` `b` on((`a`.`KurumAdi_id` = `b`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 14:43:58
