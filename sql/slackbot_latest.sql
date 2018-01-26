-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2017 at 09:04 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 5.6.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `slackbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(11) NOT NULL,
  `roomType` varchar(45) DEFAULT NULL,
  `check_in` varchar(20) DEFAULT NULL,
  `check_out` date DEFAULT NULL,
  `roomnumber` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `roomType`, `check_in`, `check_out`, `roomnumber`, `customer_id`) VALUES
(1, 'delux', '0000-00-00', '0000-00-00', NULL, NULL),
(2, 'suite', '2017-12-20', '2017-12-30', 1, 1),
(12, 'suite', '06/06/2018', NULL, 200, 47),
(20, 'suite', '2017-12-20', '2017-12-30', 1, 1),
(21, 'suite', '12/12/2019', NULL, 200, 49),
(22, 'suite', '12/13/2017', NULL, 200, 68);

-- --------------------------------------------------------

--
-- Table structure for table `currentuser`
--

CREATE TABLE `currentuser` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `currentuser`
--

INSERT INTO `currentuser` (`id`, `username`) VALUES
(1, 'shweta'),
(2, 'None'),
(3, 'kamesh'),
(4, 'rahul'),
(5, 'rahul.01'),
(6, 'sohit'),
(7, 'manisha'),
(8, 'sarita'),
(9, 'aditi'),
(10, 'jahnvi'),
(11, 'nishchay'),
(12, 'mina'),
(13, 'anirudh'),
(14, 'saloni'),
(15, 'madhur'),
(16, 'nikhila'),
(17, 'avni'),
(18, 'manushi'),
(19, 'raksha'),
(20, 'prerna'),
(21, 'amrita'),
(22, 'amrita01'),
(23, 'neha'),
(24, 'nikhil'),
(25, 'niharika'),
(26, 'salman'),
(27, 'monika'),
(28, 'nikita'),
(29, 'rajeev'),
(30, 'chirag'),
(31, 'mansi'),
(32, 'pranav'),
(33, 'shalini'),
(34, 'pranay'),
(35, 'sunil'),
(36, 'anuj'),
(37, 'niharika.01'),
(38, 'pujita'),
(39, 'foram'),
(40, 'raj'),
(41, 'shilpi'),
(42, 'tina'),
(43, 'tom'),
(44, 'rakesh'),
(45, 'mishika'),
(46, 'ruchita'),
(47, 'shyla'),
(48, 'priya'),
(49, 'rishi'),
(50, 'trisha'),
(51, 'raju'),
(52, 'avni09'),
(53, 'sanchit'),
(54, 'saloni.10'),
(55, 'saloni90'),
(56, 'nitin'),
(57, 'bhavna'),
(58, 'ron'),
(59, 'shikha'),
(60, 'lavi'),
(61, 'urvashi'),
(62, 'sri'),
(63, 'aki'),
(64, 'ravi'),
(65, 'reena'),
(66, 'krish'),
(67, 'mishi'),
(68, 'soni');

-- --------------------------------------------------------

--
-- Table structure for table `roomnumber`
--

CREATE TABLE `roomnumber` (
  `roomnumber` int(4) NOT NULL,
  `roomtype` varchar(10) NOT NULL,
  `isavailable` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `roomnumber`
--

INSERT INTO `roomnumber` (`roomnumber`, `roomtype`, `isavailable`) VALUES
(200, 'suite', 'Y'),
(201, 'suite', 'Y'),
(202, 'suite', 'Y'),
(203, 'suite', 'Y'),
(204, 'suite', 'Y'),
(205, 'suite', 'Y'),
(300, 'condo', 'Y'),
(301, 'condo', 'Y'),
(302, 'condo', 'Y'),
(303, 'condo', 'Y'),
(304, 'condo', 'Y'),
(305, 'condo', 'Y'),
(400, 'deluxe', 'Y'),
(401, 'deluxe', 'Y'),
(402, 'deluxe', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `roomtype`
--

CREATE TABLE `roomtype` (
  `idRoomType` int(11) NOT NULL,
  `Description` longtext,
  `NoOfRooms` int(11) DEFAULT NULL,
  `RentPerNight` int(11) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `roomtype`
--

INSERT INTO `roomtype` (`idRoomType`, `Description`, `NoOfRooms`, `RentPerNight`, `Type`) VALUES
(1, 'A functionally arranged living space with furnishings such as a writing desk and parlor style chairs, and a spacious bathroom provide a leisurely feel. Deluxe Rooms are available on the Penthouse floor as well.', 25, 100, 'deluxe'),
(2, 'The air conditioned living rooms are fitted with double sofa cum bed which allows a total occupany of 4 in the suite. All suites have balcony and a well- equipped open kitchenette. Ideal for couples, corporate guests and luxury travellers.', 50, 150, 'suite'),
(3, 'Each unit has a gas fireplace in the living room, fully equipped kitchen, dining seating, cable TV and high speed wireless internet. You will enjoy a private balcony with a gas BBQ grill and outdoor seating furniture. All of our condos also provide you with a bathroom for every bedroom.', 10, 2000, 'condo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `currentuser`
--
ALTER TABLE `currentuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roomtype`
--
ALTER TABLE `roomtype`
  ADD PRIMARY KEY (`idRoomType`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `currentuser`
--
ALTER TABLE `currentuser`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
