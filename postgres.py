
'''
create table IF NOT EXISTS person(
personId serial primary key,
lastName varchar(50) not null,
firstName varchar(50) not null
);

create table IF NOT EXISTS address(
addressId serial primary key,
personId integer references person(personId),
city varchar(50) not null,
state varchar(50) not null
);

select
    p.firstName,
    p.lastName,
    a.city,
    a.state
from Person p
left join Address a ON p.personId = a.personId;   #обьяденил нужные колонки через лефт джойн (с null)



SELECT e.name, b.bonus
from Employee e
left join Bonus b on e.empId = b.empId
where b.bonus < 1000 or b.bonus  is null; #заселектил колонки с бонусом и нэймом из 2 тэйблов и вывел с условием


select salary as SecondHighestSalary
from(
select salary, DENSE_RANK() over (order by salary desc) as rank
from Employee
) ranked
where rank = 2
limit 1;# не прошло по null

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);# это норм можно дернуть как с максимума так и с минимума но по мне с минимума корректней тк это по любому 2 элемент а макс подходит просто под задачу

SELECT min(salary) AS SecondHighestSalary
FROM Employee
WHERE salary > (SELECT min(salary) FROM Employee);

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;# НА ДУБЛИКАТ ЕСЛИ НАДО КОЛВО ТО МОЖНО ДОБАВИТЬ COUNT(*) AS "count" ПОСЛЕ СЕЛЕКТА


select e.name as Employee
from Employee e
join Employee m on e.managerId = m.id
where e.salary > m.salary; отсортить если зп больше чем у менеджера


select c.name as Customers
from Customers c
left join Orders o on c.id = o.customerId
where o.customerId is null; просто найти у кого есть заказы по айдишкам

delete from Person
where id  not in(
select min(id) # подзапрос с мин айди для уникального email
from person
group by email
); удалить дубликаты


select w1.id
from Weather w1
join Weather w2 on w1.recordDate = w2.recordDate + INTERVAL '1 day'
where w1.temperature > w2.temperature; вывести температуру самую высокую с разницей в 1 день с прошлой

=========================================================================================================


SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id; # дернуть первое вхождение плэера

select name
from Customer
where referee_id !=2 or referee_id is null; чето типо рефералки

SELECT customer_number
FROM Orders
GROUP BY customer_number
order by count(*) desc
limit 1; макс колво заказов от кастомера и вывести его айди


select name, population,area
from World
where area >= 3000000 or  population > 25000000; условия


select class
from Courses
group by class
having count(*)>5; дернуть того чье колво больше пяти в классе


SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);сложно надо думать

select x,y,z,
    case
        when x + y > z and x + z > y and z + y > x then 'Yes'
        else 'No'
    end as triangle
from Triangle # чекнули треугольники
======================================================================

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM Scores
ORDER BY score DESC;



select distinct l1.num as ConsecutiveNums
from Logs l1
join Logs l2 on l1.id = l2.id-1 and l1.num =l2.num
join Logs l3 on l1.id = l3.id -2 and l1.num =l3.num



SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);подзапрос







