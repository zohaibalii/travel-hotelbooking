-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 07, 2021 at 01:40 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zb`
--

-- --------------------------------------------------------

--
-- Table structure for table `airportcity`
--

CREATE TABLE `airportcity` (
  `sno` int(11) NOT NULL,
  `airportname` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` int(11) NOT NULL,
  `flightname` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airportcity`
--

INSERT INTO `airportcity` (`sno`, `airportname`, `city`, `country`, `flightname`) VALUES
(23, 'JINNAH INTERNATIONAL 2', '18', 22, ''),
(24, 'Islamabad Airport', '20', 22, ''),
(25, 'Sukkur Airport', '22', 22, ''),
(26, 'qabul airport', '24', 23, ''),
(27, 'Borg El Arab Airport', '25', 34, '');

-- --------------------------------------------------------

--
-- Table structure for table `airportcountry`
--

CREATE TABLE `airportcountry` (
  `sno` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airportcountry`
--

INSERT INTO `airportcountry` (`sno`, `name`) VALUES
(3, 'pakistan');

-- --------------------------------------------------------

--
-- Table structure for table `auth`
--

CREATE TABLE `auth` (
  `sno` int(11) NOT NULL,
  `username` varchar(70) NOT NULL,
  `password` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth`
--

INSERT INTO `auth` (`sno`, `username`, `password`) VALUES
(1, 'pakistann', 'pakistann');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `idd` int(11) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`idd`, `city`, `country`) VALUES
(18, 'karachi', 22),
(19, 'New Yourk', 24),
(20, 'Islamabad', 22),
(21, 'Dubai', 28),
(22, 'Sukkur', 22),
(23, 'Abu Dhabi', 28),
(24, 'Kabul', 23),
(26, 'BORG EL ARAB', 37),
(28, 'Milan', 38);

-- --------------------------------------------------------

--
-- Table structure for table `contactform`
--

CREATE TABLE `contactform` (
  `sno` int(11) NOT NULL,
  `des` varchar(1000) NOT NULL,
  `contact` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contactform`
--

INSERT INTO `contactform` (`sno`, `des`, `contact`) VALUES
(15, 'A hotel is an establishment that provides paid lodging on a short-term basis. Facilities provided inside a hotel room may range from a modest-quality mattress in a small room to large suites with bigger, higher-quality beds, a dresser, a refrigerator and other kitchen facilities, upholstered chairs, a flat screen television, and en-suite bathrooms. Small, lower-priced hotels may offer only the most basic guest services and facilities.    ', '+923003848744');

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `sno` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `visareq` varchar(500) NOT NULL,
  `language` varchar(50) NOT NULL,
  `currency` varchar(50) NOT NULL,
  `area` varchar(200) NOT NULL,
  `cimage` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`sno`, `name`, `description`, `visareq`, `language`, `currency`, `area`, `cimage`) VALUES
(22, 'pakistan', 'Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the world\'s fifth-most populous country with a population exceeding 212.2 million. It has the world\'s second-largest Muslim population.', 'Entry, Exit and Visa Requirements · Obtain your visa at the Pakistani Embassy or a Consulate prior to initiating travel to Pakistan. ', 'Urdu', 'rupee', '307,374', ',egypt.jpg,egypt2.jpg'),
(23, 'Afganistan', 'Afghanistan, landlocked multiethnic country located in the heart of south-central Asia. Lying along important trade routes connecting southern and eastern Asia to Europe and the Middle East, Afghanistan has long been a prize sought by empire builders. Its capital and largest city is Kabul.', 'If you are an Afghanistan origin and your birthplace is listed as Afghanistan on your U.S. Passport, you are not required to obtain a visa or entry permit for personal visits. If you are traveling for a business contract and work purposes, you are required to obtain a visa. Please follow the instructions for U.S. nationals.', 'Afghani', 'Pkr', '647,230 km 2 ', ',170835226.jpg,afghanistan2.jpg'),
(26, 'Chaina', '0', '', '', '', '', 'chaina.jpg'),
(27, 'Indonesia', '0', '', '', '', '', 'indonesia.jpg'),
(28, 'UAe', ' Emirates of the United Arab Emirates إمارات دولة الإمارات العربية المتحدة Category: Federated state: Location: United Arab Emirates: Number: 7 Emirates: Populations: 72,000 (Umm Al Quwain) – 4,177,059 : Areas: 260 km 2 (100 sq mi) – 67,000 km 2 (26,000 sq mi) Government: Emirate government', 'Requirements for visa application. For all others nationals who are not granted visa-free or visa on arrival, UAE visas rules vary according to nationality, age and gender. For example, for Moroccans, Algerians, Libyans, Syrians, Mauritanians and Tunisians, the minimum age requirement to apply for a visa is 40.', 'Arabi', 'ryal', '83,600.00 km 2', ',170835226.jpg,afghanistan2.jpg,,170835226.jpg,afghanistan2.jpg'),
(29, 'Saudi Arbia', '0', '', '', '', '', 'saudi.jpg'),
(30, 'Qatar', '0', '', '', '', '', 'qatar.jpg'),
(32, 'Thailand', '0', '', '', '', '', 'thailand.jpg'),
(35, 'Turkey', 'Turkey, country that occupies a unique geographic position, lying partly in Asia and partly in Europe and serving as both a bridge and a barrier between them. The modern Turkish republic was founded in 1923 after the collapse of the Ottoman Empire, and its capital is Istanbul (formerly Constantinople).', 'Turkey Visa requirement for US, UK, and Canadian citizens. A passport that is valid for at least six months after the travel date is required. US citizens holding US passports must have visas to visit Turkey. Ordinary passport holders can get e-visas.', 'turkish', 'lira', '783,356 sq. km', ',1_14932_02.jpg,Best-Things-to-do-in-Istanbul-1163x775.jpg.optimal.jpg,istanbul-nigth-turkey-shutterstock_250783048.jpg'),
(36, 'England', 'England is bounded on the north by Scotland; on the west by the Irish Sea, Wales, and the Atlantic Ocean; on the south by the English Channel; and on the east by the North Sea. Relief. England’s topography is low in elevation but, except in the east, rarely flat. Much of it consists of rolling hillsides, with the highest elevations found in the north, northwest, and southwest.', 'UK visa application form. According to the UK visa type you are applying for, you may have to complete the form online at the website of the Visa4UK website, or ... Two photographs. These photos should be taken within the past six months and in color.', 'english', '£', '30,279 km2.', ',England-wallpaper-28.jpg,Rc28a90138ccba02f54242685a6f71655.jpg,Rd0ddc00e98d229c27fa44446e2b1b52a.jpg'),
(37, 'Egypt', 'Egyptian Arabic is the spoken language. Other dialects and minority languages are spoken regionally. ^ \"Among the peoples of the ancient Near East, only the Egyptians have stayed where they were and remained what they were, although they have changed their language once and their religion twice.', 'U.S. citizens must have a visa to enter Egypt. U.S. citizens can obtain a renewable single-entry 30-day tourist visa on arrival at Egyptian airports for a 25 USD fee. A multiple entry visa is also obtainable for 60 USD.', 'Egyptian', 'egyptian Pound', '1.01 million km²', ',egypt.jpg,egypt2.jpg'),
(38, 'Itlay', 'Italy officially the Italian Republic is a country consisting of a continental part, delimited by the Alps, a peninsula and several islands surrounding it. Italy is ...', 'The following list of documents are required for any short-term Italian Schengen visa application: Italian visa application form. ... Two identical photos. ... Valid passport. ... Copies of your previous visas (if applicable). Proof of accommodation. ... Proof of travel: ... Schengen travel visa insurance.', 'Itlian', 'Euro', '301,338 km²', ',20GorgeousSidetownsinItaly__HERO_shutterstock_688078159.jpg,best-places-in-italy.jpg,download (3).jpg');

-- --------------------------------------------------------

--
-- Table structure for table `extracharges`
--

CREATE TABLE `extracharges` (
  `sno` int(11) NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `hotel` int(11) NOT NULL,
  `transfer` int(11) NOT NULL,
  `visa` int(11) NOT NULL,
  `insurance` int(11) NOT NULL,
  `profit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `extracharges`
--

INSERT INTO `extracharges` (`sno`, `country`, `city`, `hotel`, `transfer`, `visa`, `insurance`, `profit`) VALUES
(17, 22, 18, 71, 20, 11, 6, 11),
(18, 34, 25, 72, 12, 20, 12, 33),
(19, 22, 18, 73, 22, 11, 11, 22),
(20, 22, 20, 74, 11, 21, 12, 22),
(21, 28, 21, 75, 20, 33, 22, 22),
(22, 37, 26, 76, 40, 20, 20, 10);

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `sno` int(11) NOT NULL,
  `flightdate` date DEFAULT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `departurecity` int(11) NOT NULL,
  `departure` datetime NOT NULL,
  `arrival` datetime NOT NULL,
  `duration` varchar(50) NOT NULL,
  `arrivalcity` int(11) NOT NULL,
  `airportname` int(11) NOT NULL,
  `flightname` int(11) NOT NULL,
  `flightnumber` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`sno`, `flightdate`, `country`, `city`, `departurecity`, `departure`, `arrival`, `duration`, `arrivalcity`, `airportname`, `flightname`, `flightnumber`, `price`) VALUES
(106, '2021-02-02', 22, 20, 20, '2021-02-02 00:00:00', '2021-02-02 00:00:00', '2 h', 18, 24, 3, 3, 2000),
(108, '2021-02-01', 22, 18, 18, '2021-02-01 00:00:00', '2021-02-07 00:00:00', '7 days', 20, 23, 5, 6, 200);

-- --------------------------------------------------------

--
-- Table structure for table `flight2`
--

CREATE TABLE `flight2` (
  `sno` int(11) NOT NULL,
  `date` date NOT NULL,
  `dcountry` int(11) NOT NULL,
  `dcity` int(11) NOT NULL,
  `acountry` int(11) NOT NULL,
  `acity` int(11) NOT NULL,
  `airport` int(11) NOT NULL,
  `flightname` int(11) NOT NULL,
  `flightnumber` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flight2`
--

INSERT INTO `flight2` (`sno`, `date`, `dcountry`, `dcity`, `acountry`, `acity`, `airport`, `flightname`, `flightnumber`, `price`) VALUES
(1, '2021-03-01', 22, 18, 28, 21, 0, 0, 0, 200),
(2, '2021-03-02', 28, 21, 22, 18, 0, 0, 0, 1000),
(9, '2021-03-01', 22, 18, 28, 21, 23, 5, 6, 130);

-- --------------------------------------------------------

--
-- Table structure for table `flightname`
--

CREATE TABLE `flightname` (
  `sno` int(11) NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `airport` int(11) NOT NULL,
  `flightname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flightname`
--

INSERT INTO `flightname` (`sno`, `country`, `city`, `airport`, `flightname`) VALUES
(1, 22, 18, 1, 'pia'),
(2, 22, 18, 1, 'qatar air line'),
(3, 22, 20, 24, 'Pia'),
(4, 22, 22, 25, 'Pia'),
(5, 22, 18, 23, 'Pia'),
(6, 23, 24, 26, 'kabul airline'),
(7, 34, 25, 27, 'Egyptair');

-- --------------------------------------------------------

--
-- Table structure for table `flightnum`
--

CREATE TABLE `flightnum` (
  `sno` int(11) NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `airportname` int(11) NOT NULL,
  `flightname` int(11) NOT NULL,
  `flightnumber` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flightnum`
--

INSERT INTO `flightnum` (`sno`, `country`, `city`, `airportname`, `flightname`, `flightnumber`) VALUES
(1, 22, 18, 1, 1, 'AK-47'),
(2, 22, 18, 1, 1, '1'),
(3, 22, 20, 24, 3, 'AK-50'),
(4, 22, 22, 25, 4, 'AK-49'),
(6, 22, 18, 23, 5, 'ak-51'),
(7, 22, 18, 23, 5, 'ak-100'),
(8, 23, 24, 26, 6, 'zb-19'),
(9, 34, 25, 27, 7, 'ak-01');

-- --------------------------------------------------------

--
-- Table structure for table `hotelll`
--

CREATE TABLE `hotelll` (
  `sno` int(11) NOT NULL,
  `hotelname` varchar(1000) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pakage`
--

CREATE TABLE `pakage` (
  `sno` int(11) NOT NULL,
  `date` date NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `airport` varchar(70) NOT NULL,
  `flightname` varchar(70) NOT NULL,
  `flightprice` int(11) NOT NULL,
  `flightnumber` varchar(70) NOT NULL,
  `hotelname` int(11) NOT NULL,
  `departuredate` int(11) NOT NULL,
  `bed` varchar(100) NOT NULL,
  `roomsprice` int(11) NOT NULL,
  `arrivalcity` int(11) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `extracharges` int(11) NOT NULL,
  `days` varchar(100) NOT NULL,
  `acountry` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pakage`
--

INSERT INTO `pakage` (`sno`, `date`, `country`, `city`, `airport`, `flightname`, `flightprice`, `flightnumber`, `hotelname`, `departuredate`, `bed`, `roomsprice`, `arrivalcity`, `image`, `extracharges`, `days`, `acountry`) VALUES
(69, '2021-03-07', 28, 21, 'arab airline', 'qatar air line', 130, '100', 73, 0, ' \r\n                              Double Beds', 40, 18, 'Rc28a90138ccba02f54242685a6f71655.jpg', 73, '7 Days/8 Nights', 22),
(72, '2021-05-04', 38, 28, 'xyz', 'xyz', 250, '01', 76, 0, ' \r\n                              Double Beds', 320, 26, 'R103021afa719b993022c603ab4c20e9e.jpg', 76, '7 Days/8 Nights', 37);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `sno` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `adress` varchar(40) NOT NULL,
  `hotelname` varchar(100) NOT NULL,
  `persons` int(11) NOT NULL,
  `startdate` varchar(50) NOT NULL,
  `enddate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`sno`, `name`, `lastname`, `mobile`, `country`, `city`, `adress`, `hotelname`, `persons`, `startdate`, `enddate`) VALUES
(8, 'zohaib', 'ali', '03003858987', 'pakistan', 'Sukkur', 'karachi ', 'ramdhaa', 5, '2021-02-07', '2021-02-07'),
(9, 'zohaib', 'ali', '03003858987', 'pakistan', 'karachi', 'karachi ', 'palace 2', 5, '2021-02-02', '2021-02-14');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `sno` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `star` float NOT NULL,
  `des` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `sno` int(11) NOT NULL,
  `date` date NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `hotelid` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `bed` varchar(100) NOT NULL,
  `bathroom` varchar(100) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`sno`, `date`, `country`, `city`, `hotelid`, `price`, `bed`, `bathroom`, `status`) VALUES
(97, '2021-02-01', 22, 18, 71, 33, 'Single Bed', '', ''),
(105, '2021-02-01', 22, 18, 73, 22, 'Single Bed', '', ''),
(106, '2021-02-02', 22, 18, 73, 22, 'Single Bed', '', ''),
(107, '2021-02-01', 22, 20, 74, 22, 'Single Bed', '', ''),
(108, '2021-03-01', 22, 18, 73, 40, 'Double Beds', '', ''),
(109, '2021-02-03', 22, 18, 73, 33, 'Single Bed', '', ''),
(110, '2021-02-04', 22, 18, 73, 44, 'Single Bed', '', ''),
(111, '2021-02-05', 22, 18, 73, 33, 'Single Bed', '', ''),
(112, '2021-02-06', 22, 18, 73, 33, 'Single Bed', '', ''),
(113, '2021-02-02', 22, 18, 73, 33, 'Single Bed', '', ''),
(114, '2021-02-07', 22, 18, 73, 33, 'Single Bed', '', ''),
(115, '2021-02-01', 22, 18, 73, 33, 'Triple Beds', '', ''),
(116, '2021-03-01', 28, 21, 75, 33, 'Single Bed', '', ''),
(117, '2021-03-02', 28, 21, 75, 43, 'Single Bed', '', ''),
(118, '2021-03-03', 28, 21, 75, 33, 'Single Bed', '', ''),
(119, '2021-03-04', 28, 21, 75, 33, 'Single Bed', '', ''),
(120, '2021-03-05', 28, 21, 75, 33, 'Single Bed', '', ''),
(121, '2021-03-06', 28, 21, 75, 33, 'Single Bed', '', ''),
(122, '2021-03-07', 28, 21, 75, 33, 'Single Bed', '', ''),
(123, '2021-05-01', 37, 26, 76, 40, 'Single Bed', '', ''),
(124, '2021-05-02', 37, 26, 76, 40, 'Single Bed', '', ''),
(125, '2021-05-03', 37, 26, 76, 40, 'Single Bed', '', ''),
(128, '2021-05-01', 37, 26, 76, 40, 'Double Beds', '', ''),
(129, '2021-05-02', 37, 26, 76, 40, 'Double Beds', '', ''),
(130, '2021-05-03', 37, 26, 76, 40, 'Double Beds', '', ''),
(131, '2021-05-04', 37, 26, 76, 40, 'Double Beds', '', ''),
(132, '2021-05-05', 37, 26, 76, 40, 'Double Beds', '', ''),
(133, '2021-05-06', 37, 26, 76, 40, 'Double Beds', '', ''),
(135, '2021-05-07', 37, 26, 76, 40, 'Double Beds', '', ''),
(136, '2021-05-08', 37, 26, 76, 40, 'Double Beds', '', ''),
(137, '2021-05-09', 37, 26, 76, 40, 'Double Beds', '', ''),
(139, '2021-05-10', 37, 26, 76, 40, 'Double Beds', '', ''),
(142, '2021-05-11', 37, 26, 76, 40, 'Double Beds', '', ''),
(143, '2021-05-12', 37, 26, 76, 40, 'Double Beds', '', ''),
(144, '2021-05-13', 37, 26, 76, 40, 'Double Beds', '', ''),
(145, '2021-05-14', 37, 26, 76, 40, 'Double Beds', '', ''),
(146, '2021-05-15', 37, 26, 76, 40, 'Double Beds', '', ''),
(147, '2021-05-16', 37, 26, 76, 40, 'Double Beds', '', ''),
(148, '2021-05-17', 37, 26, 76, 40, 'Double Beds', '', ''),
(149, '2021-05-18', 37, 26, 76, 40, 'Double Beds', '', ''),
(150, '2021-05-19', 37, 26, 76, 40, 'Double Beds', '', ''),
(151, '2021-05-20', 37, 26, 76, 40, 'Double Beds', '', ''),
(153, '2021-05-22', 37, 26, 76, 40, 'Double Beds', '', ''),
(154, '2021-05-23', 37, 26, 76, 40, 'Double Beds', '', ''),
(156, '2021-05-25', 37, 26, 76, 40, 'Double Beds', '', ''),
(157, '2021-05-24', 37, 26, 76, 40, 'Double Beds', '', ''),
(158, '2021-05-26', 37, 26, 76, 40, 'Double Beds', '', ''),
(159, '2021-05-27', 37, 26, 76, 40, 'Double Beds', '', ''),
(160, '2021-05-28', 37, 26, 76, 40, 'Double Beds', '', ''),
(161, '2021-05-29', 37, 26, 76, 40, 'Double Beds', '', ''),
(162, '2021-05-30', 37, 26, 76, 40, 'Double Beds', '', ''),
(163, '2021-05-31', 37, 26, 76, 40, 'Double Beds', '', ''),
(164, '2021-05-21', 37, 26, 76, 40, 'Double Beds', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `slider`
--

CREATE TABLE `slider` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `des` varchar(500) NOT NULL,
  `img` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `slider`
--

INSERT INTO `slider` (`id`, `title`, `des`, `img`) VALUES
(4, 'karachi', 'hello karachi', 'karachiii.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `snohotel`
--

CREATE TABLE `snohotel` (
  `sno` int(11) NOT NULL,
  `country` int(11) NOT NULL,
  `city` int(11) NOT NULL,
  `hotelname` varchar(100) NOT NULL,
  `image` varchar(200) NOT NULL,
  `des` varchar(2000) NOT NULL,
  `transferr` int(11) NOT NULL,
  `visaa` int(11) NOT NULL,
  `insurancee` int(11) NOT NULL,
  `profitt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `snohotel`
--

INSERT INTO `snohotel` (`sno`, `country`, `city`, `hotelname`, `image`, `des`, `transferr`, `visaa`, `insurancee`, `profitt`) VALUES
(73, 22, 18, 'Regent Plaza', ',FRENCH.jpg,Islamabad.jpg', 'The hotel has a grand facade, which leads into an elegantly decorated lobby presenting an eye catching blend of National and International decor. The multi lingual staff at the front desk ensures that all guests’ needs are met instantly. The hotel has 440 luxurious and well appointed guests’ rooms, which cater to all the needs of the business and holiday travelers. These rooms include Presidential Suites, Executive Suites and Business Suites beside Standard Rooms, Deluxe Rooms, Executive Rooms and Executive Deluxe Rooms.', 0, 0, 0, 0),
(74, 22, 18, 'Sareena', ',d0935fe60294e3eb8348b89471603d94.jpg,download (1).jpg,download (2).jpg,download.jpg,R103021afa719b993022c603ab4c20e9e.jpg', ' https://en.wikipedia.org/wiki/Serena_Hotels\r\nSerena Hotels is a hospitality company which operates up-scale hotels and resorts in East Africa, Southern Africa and South Asia.. Serena comprises a collection of 36 luxury resorts, safari lodges, and hotels, which are located in East Africa (Kenya, Tanzania, Rwanda, Uganda, and Mozambique) and Central and South Asia (Pakistan, Afghanistan, and Tajikistan). zohaib', 0, 0, 0, 0),
(75, 37, 26, 'Burj Al Arab', '', '', 0, 0, 0, 0),
(76, 37, 26, 'IBEROTEL BORG EL ARAB', ',d0935fe60294e3eb8348b89471603d94.jpg,download (1).jpg,download (2).jpg,download.jpg,R103021afa719b993022c603ab4c20e9e.jpg', 'Borg el-Arab (Arabic: برج العرب‎) is an industrial city in the governorate of Alexandria, Egypt. It is located about 45 kilometers south-west of Alexandria and some seven kilometers from the Mediterranean coast. North of Borg El Arab is the King Maryut resort and Lake Maryut. The city has an airport, Borg El Arab Airport, that serves nearly 250,000 passengers every year. Borg El Arab is widely considered an extension of the city of Alexandria.[1]\r\n\r\nOn 23 April 1973 Egyptian President Anwar Sadat met with Syrian president Hafez al-Assad at the presidential resort in Borg El Arab for two days of detailed discussions in preparation for the joint offensive on Israel which launched the Yom Kippur War. President Hosni Mubarak performed the formal inauguration of the city in November 1988.[2]', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tour`
--

CREATE TABLE `tour` (
  `sno` int(11) NOT NULL,
  `country` int(11) NOT NULL,
  `days` varchar(100) NOT NULL,
  `cities` varchar(1000) NOT NULL,
  `place` varchar(100) NOT NULL,
  `plimit` int(11) NOT NULL,
  `day1` varchar(2000) NOT NULL,
  `day2` varchar(2000) NOT NULL,
  `day3` varchar(2000) NOT NULL,
  `day4` varchar(2000) NOT NULL,
  `day5` varchar(2000) NOT NULL,
  `day6` varchar(2000) NOT NULL,
  `day7` varchar(2000) NOT NULL,
  `dpoint` varchar(500) NOT NULL,
  `dtime` datetime DEFAULT NULL,
  `returndetail` varchar(200) NOT NULL,
  `images` varchar(200) NOT NULL,
  `dcountry` int(11) NOT NULL,
  `dcity` int(11) NOT NULL,
  `acountry` int(11) NOT NULL,
  `acity` int(11) NOT NULL,
  `airportname` varchar(50) NOT NULL,
  `flightname` varchar(50) NOT NULL,
  `flightnumber` varchar(50) NOT NULL,
  `flightprice` int(11) NOT NULL,
  `packageprice` int(11) NOT NULL,
  `transfer` int(11) NOT NULL,
  `visa` int(11) NOT NULL,
  `insurance` int(11) NOT NULL,
  `profit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tour`
--

INSERT INTO `tour` (`sno`, `country`, `days`, `cities`, `place`, `plimit`, `day1`, `day2`, `day3`, `day4`, `day5`, `day6`, `day7`, `dpoint`, `dtime`, `returndetail`, `images`, `dcountry`, `dcity`, `acountry`, `acity`, `airportname`, `flightname`, `flightnumber`, `flightprice`, `packageprice`, `transfer`, `visa`, `insurance`, `profit`) VALUES
(8, 22, '7 days', 'karachi,islamabad', 'x,y,z', 50, ' Madrid - Cordoba - Sevilla\r\nDeparture from our bus terminal at 8:00 a.m. through La Mancha country to Cordoba. Sightseeing tour visiting its famous Mosque/Cathedral and Jewish Quarter. Then to Sevilla. Dinner and accommodations.', ' Sevilla\r\nHalf board in the hotel. Morning city tour visiting the Park of María Luisa, Plaza de España, outskirts of the great Cathedral and its giralda Tower, and the typical Barrio de Santa Cruz, former Jewish quarter. Afternoon at leisure.', ' Sevilla - Granada\r\nBreakfast. Departure to Granada. Sightseeing tour visiting the impressive Alhambra, a world heritage site, with its beautiful Nazari Palaces and the Generalife gardens. Dinner and accommodations. Optional visit to the caves of Sacromonte and attend a typical show of gipsy flamenco.', '  Granada - Valencia\r\nBreakfast. Departure via Guadix, Baza and Puerto Lumbreras towards the Mediterranean coast and Valencia. Accommodations.', ' Valencia - Barcelona\r\nBreakfast. Free time. At mid morning departure to Barcelona. Arrival and accommodations.', '  Barcelona\r\nBreakfast and accommodation. Morning city sightseeing tour visiting the Park of Montjuic with spectacular views, Olympic Ring, monument to Columbus and the old Gothic Quarter. Afternoon at leisure. Optional night tour through the wide avenues and lighted buildings and fountains.', ' Barcelona - Zaragoza - Madrid\r\nBreakfast. Departure through Lerida and Zaragoza Time free. Continuation to Madrid. Arrival and end of our services.\r\n\r\nNights: Sevilla 2. Granada 1. Valencia 1. Barcelona 2', ' Near Plaza España, next to the Debod Temple', '2021-03-08 08:51:00', ' The activity ends in Plaza de España, next to Gran Vía street', ',afghanistan2.jpg', 28, 21, 22, 18, 'uaria', 'arabairline', '321', 130, 200, 22, 33, 11, 22);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airportcity`
--
ALTER TABLE `airportcity`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `airportcountry`
--
ALTER TABLE `airportcountry`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `auth`
--
ALTER TABLE `auth`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`idd`);

--
-- Indexes for table `contactform`
--
ALTER TABLE `contactform`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `extracharges`
--
ALTER TABLE `extracharges`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `flight2`
--
ALTER TABLE `flight2`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `flightname`
--
ALTER TABLE `flightname`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `flightnum`
--
ALTER TABLE `flightnum`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `hotelll`
--
ALTER TABLE `hotelll`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `pakage`
--
ALTER TABLE `pakage`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `slider`
--
ALTER TABLE `slider`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `snohotel`
--
ALTER TABLE `snohotel`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `tour`
--
ALTER TABLE `tour`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `airportcity`
--
ALTER TABLE `airportcity`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `airportcountry`
--
ALTER TABLE `airportcountry`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth`
--
ALTER TABLE `auth`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `idd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `contactform`
--
ALTER TABLE `contactform`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `extracharges`
--
ALTER TABLE `extracharges`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `flight`
--
ALTER TABLE `flight`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT for table `flight2`
--
ALTER TABLE `flight2`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `flightname`
--
ALTER TABLE `flightname`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `flightnum`
--
ALTER TABLE `flightnum`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `hotelll`
--
ALTER TABLE `hotelll`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pakage`
--
ALTER TABLE `pakage`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=165;

--
-- AUTO_INCREMENT for table `slider`
--
ALTER TABLE `slider`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `snohotel`
--
ALTER TABLE `snohotel`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `tour`
--
ALTER TABLE `tour`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
