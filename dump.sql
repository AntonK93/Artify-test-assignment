-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for artify
CREATE DATABASE IF NOT EXISTS `artify` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `artify`;

-- Dumping structure for table artify.sectors
CREATE TABLE IF NOT EXISTS `sectors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `parent_sector` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_sector` (`parent_sector`),
  CONSTRAINT `sectors_ibfk_1` FOREIGN KEY (`parent_sector`) REFERENCES `sectors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=latin1;

-- Dumping data for table artify.sectors: ~33 rows (approximately)
DELETE FROM `sectors`;
/*!40000 ALTER TABLE `sectors` DISABLE KEYS */;
INSERT INTO `sectors` (`id`, `name`, `parent_sector`) VALUES
	(1, 'Manufacturing', NULL),
	(2, 'Construction materials', 1),
	(3, 'Electronics and Optics', 1),
	(4, 'Food and Beverage', 1),
	(5, 'Bakery & confectionery products', 4),
	(6, 'Beverages', 4),
	(7, 'Fish & fish products', 4),
	(8, 'Meat & meat products', 4),
	(9, 'Milk & dairy products', 4),
	(10, 'Other', 4),
	(11, 'Sweets & snack food', 4),
	(12, 'Furniture', 1),
	(13, 'Bathroom/sauna', 12),
	(14, 'Bedroom', 12),
	(15, 'Children’s room', 12),
	(16, 'Kitchen', 12),
	(17, 'Living room', 12),
	(18, 'Office', 12),
	(19, 'Other', 12),
	(20, 'Outdoor', 12),
	(21, 'Project furn', 12),
	(22, 'Machinery', 1),
	(23, 'Machinery components', 22),
	(24, 'Machinery equipment/tools', 22),
	(25, 'Manufacture of machinery', 22),
	(26, 'Maritime', 22),
	(27, 'Aluminium and steel workboats', 26),
	(28, 'Boat/Yacht building', 26),
	(29, 'Ship repair and conversion', 26),
	(30, 'Metal structures', 22),
	(31, 'Other', 22),
	(32, 'Repair and maintenance service', 22),
	(33, 'Metalworking', 1),
	(34, 'Construction of metal structures', 33),
	(35, 'Houses and buildings', 33),
	(36, 'Metal products', 33),
	(37, 'Metal works', 33),
	(38, 'CNC-machining', 37),
	(39, 'Forgings, Fasteners', 37),
	(40, 'Gas, Plasma, Laser cutting', 37),
	(41, 'MIG, TIG, Aluminum welding', 37),
	(42, 'Plastic and Rubber', 1),
	(43, 'Packaging', 42),
	(44, 'Plastic goods', 42),
	(45, 'Plastic processing technology', 42),
	(46, 'Blowing', 45),
	(47, 'Moulding', 45),
	(48, 'Plastics welding and processing', 45),
	(49, 'Plastic profiles', 42),
	(50, 'Printing', 1),
	(51, 'Advertising', 50),
	(52, 'Book/Periodicals printing', 50),
	(53, 'Labelling and packaging printing', 50),
	(54, 'Textile and Clothing', 1),
	(55, 'Clothing', 54),
	(56, 'Textile', 54),
	(57, 'Wood', 1),
	(58, 'Other', 57),
	(59, 'Wooden building materials', 57),
	(60, 'Wooden houses', 57),
	(61, 'Other', NULL),
	(62, 'Creative industries', 61),
	(63, 'Energy technology', 61),
	(64, 'Environment', 61),
	(65, 'Service', NULL),
	(66, 'Business services', 65),
	(67, 'Engineering', 65),
	(68, 'Information Technology and Telecommunications', 65),
	(69, 'Data processing, Web portals, E-marketing', 68),
	(70, 'Programming, Consultancy', 68),
	(71, 'Software, Hardware', 68),
	(72, 'Telecommunications', 68),
	(73, 'Tourism', 65),
	(74, 'Translation services', 65),
	(75, 'Transport and Logistics', 65),
	(76, 'Air', 75),
	(77, 'Rail', 75),
	(78, 'Road', 75),
	(79, 'Water', 75);
/*!40000 ALTER TABLE `sectors` ENABLE KEYS */;

-- Dumping structure for table artify.user-info-selected-sectors-pivot
CREATE TABLE IF NOT EXISTS `user-info-selected-sectors-pivot` (
  `user_info_entry` int(11) NOT NULL,
  `sector_entry` int(11) NOT NULL,
  PRIMARY KEY (`user_info_entry`,`sector_entry`),
  KEY `user-info-entry` (`user_info_entry`) USING BTREE,
  KEY `sector-entry` (`sector_entry`) USING BTREE,
  CONSTRAINT `user-info-selected-sectors-pivot_ibfk_1` FOREIGN KEY (`user_info_entry`) REFERENCES `users-info` (`id`),
  CONSTRAINT `user-info-selected-sectors-pivot_ibfk_2` FOREIGN KEY (`sector_entry`) REFERENCES `sectors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table artify.user-info-selected-sectors-pivot: ~0 rows (approximately)
DELETE FROM `user-info-selected-sectors-pivot`;
/*!40000 ALTER TABLE `user-info-selected-sectors-pivot` DISABLE KEYS */;
/*!40000 ALTER TABLE `user-info-selected-sectors-pivot` ENABLE KEYS */;

-- Dumping structure for table artify.users-info
CREATE TABLE IF NOT EXISTS `users-info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(125) NOT NULL,
  `terms_agreed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Dumping data for table artify.users-info: ~0 rows (approximately)
DELETE FROM `users-info`;
/*!40000 ALTER TABLE `users-info` DISABLE KEYS */;
/*!40000 ALTER TABLE `users-info` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
