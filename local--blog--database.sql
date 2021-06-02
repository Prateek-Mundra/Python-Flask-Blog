-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 02, 2021 at 05:48 PM
-- Server version: 8.0.25-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `local--blog--database`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_number`, `message`, `date`) VALUES
(1, 'Prateek Mundra', 'prateekmundra123@gmail.com', '123456789', 'This is my first sample message for testing.', '2021-05-24 17:43:48'),
(3, 'Prateek_MundraCV', '1579780412316@edgenetworks.in', '9876543212', 'First message from website', '2021-05-24 17:58:53'),
(4, 'Rohan Das', '1579780412316@edgenetworks.in', '9876543212', 'You are building a great website.', '2021-05-27 10:47:09'),
(9, 'MS Dhoni', 'dhoni@gmail.com', '9960261693', 'Sample message for testing', '2021-05-29 23:57:14'),
(10, 'MS Dhoni', 'dhoni@gmail.com', '9960261693', 'Sample message for testing', '2021-05-30 00:03:12'),
(11, 'Tappu', 'tappu@gmail.com', '9999445584', 'Hi this is tappy', '2021-05-30 00:05:12'),
(12, 'Tappu', 'tappu@gmail.com', '9999445584', 'Hi this is tappy', '2021-05-30 00:09:12'),
(13, 'Prateek_MundraCV', 'Anusha.Peter@ust-global.com', '9876543212', 'This is a test message', '2021-05-30 00:14:48'),
(14, '', '', '', '', '2021-06-02 14:40:03'),
(15, '', '', '', '', '2021-06-02 14:41:53');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `tagline` text NOT NULL,
  `author` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `tagline`, `author`, `img_file`, `date`) VALUES
(1, 'This is my first post title', 'first-post', 'This is my first blog. I\'m really excited to make this using flask microframework.', 'Why is my tagline empty', 'kante123', 'about-bg.jpg', '2021-06-02 12:33:18'),
(2, 'From Kante to Mendy, heroes all: Reactions to Chelsea’s Champions League triumph', 'chelsea', 'Four months after being sacked by Paris Saint-Germain, Chelsea manager Thomas Tuchel lifted the Champions League as he got the better of Pep Guardiola once more to keep Manchester City waiting for European glory.\r\n\r\nA 1-0 victory in Porto rounded off a rollercoaster year for the German, who was handed the chance to revive Chelsea’s fortunes less than a month after losing his job in Paris', 'Chelsea have become the first team in history to win all three major European club competitions twice.', 'Prateek Mundra', 'cl.jpg', '2021-06-01 00:48:12'),
(3, 'This is website post', 'new slug', 'new content from this website, this is gonna be exciting', 'new tagline', 'prateek_mundra', 'sample.jpg', '2021-05-31 23:10:10'),
(6, 'sdfsf', '', '', '', 'mundra bhai', '', '2021-06-02 12:41:04'),
(7, 'n golo kante golo kante', 'kantebhai', '', 'Greatest Footballer', 'kante paji', '', '2021-06-02 16:19:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
