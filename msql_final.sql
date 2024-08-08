use classicmodels;
#drop table if exists Student;
CREATE TABLE Student (
StdID INT(4) PRIMARY KEY, StdName VARCHAR(30) NOT NULL,
Sex VARCHAR(1), Percentage DECIMAL(5,2), SClass INT ,
Sec VARCHAR(1), Stream VARCHAR(10), DOB DATE );

INSERT INTO Student VALUES (1001, "AKSHRA AGARWAL","F",70.00,11,"A", "comp","1996/11/10");
insert into student (stdid, stdname, sex, percentage, sclass, sec, stream, dob) values
    (1002, 'ANJANI SHARMA', 'FEMALE', 75, 11, 'A', 'Commerce', '1996-09-18'),
    (1003, 'ANSHUL SAXENA', 'MALE', 78, 11, 'A', 'Commerce', '1996-11-19'),
    (1004, 'AISHWARYA SINGH', 'FEMALE', 79, 11, 'A', 'Commerce', '1996-11-01'),
    (1005, 'AKRITI SAXENA', 'FEMALE', 76, 11, 'A', 'Commerce', '1996-09-20'),
    (1006, 'KHUSHI AGARWAL', 'FEMALE', 77, 11, 'A', 'Commerce', '2003-09-14'),
    (1007, 'MAAHI AGARWAL', 'FEMALE', 74, 11, 'A', 'Science', '1997-04-21'),
    (1008, 'MITALI GUPTA', 'FEMALE', 78, 12, 'A', 'Science', '1997-11-26'),
    (1009, 'NIKUNJ AGARWAL', 'MALE', 58, 12, 'A', 'Science', '1997-07-12'),
    (1010, 'PARKHI', 'FEMALE', 59, 12, 'A', 'Commerce', '1997-12-20'),
    (1011, 'PRAKHAR TIWARI', 'MALE', 43, 12, 'A', 'Science', '1997-04-22'),
    (1012, 'RAGHAV GANGWAR', 'MALE', 58, 12, 'A', 'Commerce', '1997-12-21'),
    (1013, 'SAHIL SARASWAT', 'MALE', 57, 12, 'A', 'Commerce', '1997-08-13'),
    (1014, 'SWATI MISHRA', 'FEMALE', 98, 11, 'A', 'Science', '1996-08-13'),
    (1015, 'HARSH AGARWAL', 'MALE', 58, 11, 'B', 'Science', '2003-08-28'),
    (1016, 'HARSHIT KUMAR', 'MALE', 98, 11, 'B', 'Science', '2003-05-22'),
    (1017, 'JAHANVI KAPOOR', 'MALE', 65, 11, 'B', 'Science', '1997-01-10'),
    (1018, 'STUTI MISHRA', 'MALE', 66, 11, 'C', 'Commerce', '1996-01-10'),
    (1019, 'SURYANSH KUMAR AGARWAL', 'MALE', 85, 11, 'C', 'Commerce', '2007-08-22'),
    (1020, 'TANI RASTOGI', 'FEMALE', 75, 12, 'C', 'Commerce', '1998-01-15'),
    (1021, 'TANISHK GUPTA', 'MALE', 55, 12, 'C', 'Science', '1998-04-11'),
    (1022, 'TANMAY AGARWAL', 'MALE', 57, 11, 'C', 'Commerce', '1998-06-28'),
    (1023, 'YASH SAXENA', 'MALE', 79, 11, 'C', 'Science', '1998-03-13'),
    (1024, 'YESH DUBEY', 'MALE', 85, 12, 'C', 'Commerce', '1998-04-03');
    
alter table student 
modify Sex varchar(6);

select * from student;

select stdName, dob from student;

SELECT * FROM student WHERE percentage >= 80;

-- 4. To display student name, stream and percentage where percentage of student is more than 80 
SELECT StdName, Stream, Percentage WHERE percentage > 80;

-- 5. To display all records of science students whose percentage is more than 75 form student table. 
SELECT * FROM student WHERE stream = 'Science' AND percentage > 75;

DESCRIBE Student;

ALTER TABLE Student ADD TeacherID VARCHAR(20);
ALTER TABLE Student MODIFY TeacherID INT ; 

ALTER TABLE Student DROP TeacherID;

SELECT stdname, percentage - 5 FROM Student;

SELECT StdName AS 'Student Name',
DOB As 'Date of Birth' 
FROM Student;

-- 4. Display the name of all students whose stream is not Science
SELECT StdNameFROMstudent 
WHERE Stream <>'Science';

-- 5. Display all name and percentage where percentage is between 60 and 80
SELECT StdName, percentage 
FROM student 
WHERE percentage >=60 AND percentage<=80 ;
SELECT * FROM Student WHERE StdName LIKE 'G_' ; 
SELECT * FROM Student WHERE StdName='G';
SELECT * FROM Student WHERE StdName LIKE 'G%' ;

SELECT DISTINCT Stream FROM Student;
SELECT StdName, Sex, Stream FROM Student WHERE percentage BETWEEN 70 AND 80;

create table employeesTable(
empno INT,
ename varchar(20),
job varchar(10),
mgr Int,
hiredate date,
sal decimal(5,2),
comm decimal(10,2),
deptno INT);

ALTER TABLE employeestable RENAME COLUMN  empname TO ename;

INSERT INTO employeesTable (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(8369, 'SMITH', 'CLERK', 8902, '1990-12-18', 800.00, NULL, 20),
(8499, 'ANYA', 'SALESMAN', 8698, '1991-02-20', 160.00, 300.00, 30),
(8521, 'SETH', 'SALESMAN', 8698, '1991-02-22', 150.00, 500.00, 30),
(8566, 'MAHADEVAN', 'MANAGER', 8839, '1991-04-02', 2985.00, NULL, 20),
(8654, 'MOMIN', 'SALESMAN', 8696, '1991-09-28', 1250.00, 1400.00, 30),
(8698, 'BINA', 'MANAGER', 8839, '1991-05-01', 2850.00, NULL, 30),
(8887, 'SHIVANSH', 'MANAGER', 8839, '1991-06-09', 2450.00, NULL, 10),
(8888, 'SCOTT', 'ANALYST', 8566, '1992-12-09', 3000.00, NULL, 20),
(8839, 'AMIR', 'PRESIDENT', NULL, '1991-11-18', 5000.00, NULL, 10),
(8844, 'KULDEEP', 'SALESMAN', 8698, '1991-09-08', 1500.00, 0.00, 30);








 










