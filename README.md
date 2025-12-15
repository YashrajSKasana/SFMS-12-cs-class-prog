
Simple Fee Management System

This is a simple CLI-based Simple Fee Management System built using Python and MySQL. The project uses Poetry for dependency management and virtual environments.

Requirements
Python 3.12
MySQL 8.0 or higher
Poetry

Install Poetry
If Poetry is not installed, run:

python -m pip install poetry

Check installation:

poetry --version

Setup and Run the Project

1. Clone the repository

git clone https://github.com/YashrajSKasana/SFMS-12-cs-class-prog.git
cd SFMS-12-cs-class-prog

2. Install dependencies using Poetry

poetry install

3. Activate the virtual environment

poetry env activate

4. Run the project

python main.py

Database Setup

1. Login to MySQL

mysql -u root -p

2. Create and select database

CREATE DATABASE school_db;
USE school_db;

Create Tables
AdminCred table

CREATE TABLE AdminCred (
Name VARCHAR(50) NOT NULL,
Password VARCHAR(255) NOT NULL,
PRIMARY KEY (AdminName)
);

Insert mock admin data

INSERT INTO AdminCred VALUES ('admin', 'admin123');

Main table (student records)

CREATE TABLE main (
AdmissionNo INT NOT NULL,
StudentName VARCHAR(100) NOT NULL,
Class VARCHAR(20) NOT NULL,
Section VARCHAR(10),
ParentName VARCHAR(100),
ParentPhone VARCHAR(15),
ParentEmail VARCHAR(100),
PaidFee DECIMAL(10,2) DEFAULT 0.00,
DueFee DECIMAL(10,2) DEFAULT 0.00,
Address TEXT,
PRIMARY KEY (AdmissionNo)
);

Insert mock student data (20 records)

INSERT INTO main (
AdmissionNo, StudentName, Class, Section,
ParentName, ParentPhone, ParentEmail,
PaidFee, DueFee, Address
) VALUES
(101, 'Aarav Sharma', '10', 'A', 'Rakesh Sharma', '9876543210', '[rakesh.sharma@gmail.com](mailto:rakesh.sharma@gmail.com)', 20000.00, 5000.00, 'Delhi'),
(102, 'Ananya Verma', '10', 'A', 'Sanjay Verma', '9876543211', '[sanjay.verma@gmail.com](mailto:sanjay.verma@gmail.com)', 25000.00, 0.00, 'Delhi'),
(103, 'Rohan Gupta', '9', 'B', 'Manoj Gupta', '9876543212', '[manoj.gupta@gmail.com](mailto:manoj.gupta@gmail.com)', 15000.00, 10000.00, 'Noida'),
(104, 'Priya Singh', '9', 'B', 'Amit Singh', '9876543213', '[amit.singh@gmail.com](mailto:amit.singh@gmail.com)', 18000.00, 7000.00, 'Ghaziabad'),
(105, 'Kunal Mehta', '8', 'A', 'Rajesh Mehta', '9876543214', '[rajesh.mehta@gmail.com](mailto:rajesh.mehta@gmail.com)', 22000.00, 3000.00, 'Faridabad'),
(106, 'Sneha Patel', '8', 'A', 'Nilesh Patel', '9876543215', '[nilesh.patel@gmail.com](mailto:nilesh.patel@gmail.com)', 25000.00, 0.00, 'Ahmedabad'),
(107, 'Aditya Jain', '10', 'C', 'Suresh Jain', '9876543216', '[suresh.jain@gmail.com](mailto:suresh.jain@gmail.com)', 12000.00, 13000.00, 'Jaipur'),
(108, 'Neha Kapoor', '9', 'A', 'Vikas Kapoor', '9876543217', '[vikas.kapoor@gmail.com](mailto:vikas.kapoor@gmail.com)', 20000.00, 5000.00, 'Chandigarh'),
(109, 'Arjun Malhotra', '8', 'B', 'Karan Malhotra', '9876543218', '[karan.malhotra@gmail.com](mailto:karan.malhotra@gmail.com)', 17000.00, 8000.00, 'Delhi'),
(110, 'Pooja Nair', '10', 'B', 'Sunil Nair', '9876543219', '[sunil.nair@gmail.com](mailto:sunil.nair@gmail.com)', 26000.00, 0.00, 'Kochi'),
(111, 'Vivek Yadav', '9', 'C', 'Pradeep Yadav', '9876543220', '[pradeep.yadav@gmail.com](mailto:pradeep.yadav@gmail.com)', 14000.00, 11000.00, 'Lucknow'),
(112, 'Isha Khanna', '8', 'C', 'Rohit Khanna', '9876543221', '[rohit.khanna@gmail.com](mailto:rohit.khanna@gmail.com)', 23000.00, 2000.00, 'Amritsar'),
(113, 'Mohit Bansal', '10', 'A', 'Deepak Bansal', '9876543222', '[deepak.bansal@gmail.com](mailto:deepak.bansal@gmail.com)', 25000.00, 0.00, 'Panipat'),
(114, 'Kavya Joshi', '9', 'A', 'Anil Joshi', '9876543223', '[anil.joshi@gmail.com](mailto:anil.joshi@gmail.com)', 19000.00, 6000.00, 'Udaipur'),
(115, 'Siddharth Roy', '8', 'B', 'Subhash Roy', '9876543224', '[subhash.roy@gmail.com](mailto:subhash.roy@gmail.com)', 16000.00, 9000.00, 'Kolkata'),
(116, 'Ritika Das', '10', 'C', 'Alok Das', '9876543225', '[alok.das@gmail.com](mailto:alok.das@gmail.com)', 21000.00, 4000.00, 'Kolkata'),
(117, 'Nikhil Choudhary', '9', 'B', 'Mahesh Choudhary', '9876543226', '[mahesh.ch@gmail.com](mailto:mahesh.ch@gmail.com)', 18000.00, 7000.00, 'Ajmer'),
(118, 'Simran Kaur', '8', 'A', 'Harpreet Singh', '9876543227', '[harpreet.singh@gmail.com](mailto:harpreet.singh@gmail.com)', 24000.00, 1000.00, 'Ludhiana'),
(119, 'Aman Ali', '10', 'B', 'Salim Ali', '9876543228', '[salim.ali@gmail.com](mailto:salim.ali@gmail.com)', 13000.00, 12000.00, 'Bhopal'),
(120, 'Tanvi Kulkarni', '9', 'C', 'Milind Kulkarni', '9876543229', '[milind.k@gmail.com](mailto:milind.k@gmail.com)', 20000.00, 5000.00, 'Pune');

Verify setup

SELECT * FROM main;
SELECT * FROM AdminCred;

Note
you only need to enter database details only ones then program will store and reuse them.
