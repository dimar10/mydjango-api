
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





