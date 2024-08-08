use classicmodels;

select * from worker;
-- Write a query to display all the first_name  in upper case
select upper(FIRST_NAME) 
from Worker;

-- Write a querty to display unique department from workers table
select distinct DEPARTMENT 
from Worker;

-- Write an SQL query to print the first three characters of FIRST_NAME from Worker table
select  substr(first_name,1,3) 
from Worker;

-- Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
SELECT POSITION('a' IN first_name) AS Position
FROM Worker
WHERE first_name = 'Amitabh';

-- Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length
select distinct length(department) Length, department 
from Worker;

-- Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending
select * from Worker 
order by FIRST_NAME Asc, DEPARTMENT Desc;

-- Write a query to get workers whose name are Vipul and Satish
 select * from Worker 
 where FIRST_NAME in ("Vipul","Satish");

-- Write an SQL query to print details of the Workers whose FIRST_NAME contains 'a'
 select * from Worker 
 where FIRST_NAME like "%a%";

-- Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets
 select * from Worker 
 where FIRST_NAME like "_____h";
 
-- Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000
select * from Worker 
where salary between 100000 and 500000;

-- Write an SQL query to print details of the Workers who have joined in Feb’2014
select * from Worker where YEAR(joining_date) = 2014 AND MONTH(joining_date) = 2;
select * from worker where joining_data like "2014-02-%";

-- Write an SQL query to fetch the count of employees working in the department ‘Admin’
select count(*) Employees 
from Worker 
group by department 
having department ="admin";

-- Write an SQL query to fetch the no. of workers for each department in the descending order
select * from worker;
select * from employees;
select * from title;

select count(worker_id),department from worker group by department;
-- Write a query to display workers who are managers
select w.first_name,w.last_name,t.worker_title from worker w join title t on w.worker_id = t.worker_ref_id where t.worker_title="Manager";
-- Write query to find duplicate rows title table
select worker_title as duplicate_rows,count(*) from title group by worker_title having count(*)>1;

-- Write a query to fetch departments along with the total salaries paid for each of them
select * from worker;
select department,sum(salary) from worker group by department;

-- Write a query to fetch the names of workers who earn the highest salary

select first_name,salary from worker where salary =
(select max(salary) from worker)

















