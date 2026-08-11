
select * from Cinema
where id % 2 != 0
and description not in ('boring')
order by rating desc

''' Есть таблица employees с колонками id, name, department, salary.
Задание: Для каждого сотрудника выведите его имя, отдел, зарплату и ранг зарплаты внутри отдела (1 — самая высокая).'''

select
    name,
    department,
    salary,
    rank() over (partition by department order by salary desc) as salary_rank
from employees;

'''Таблица sales с колонками date, amount.
Задание: Для каждого дня выведите сумму продаж и разницу с предыдущим днём.'''
select
    date,
    amount,
    amount - lag(amount) over (order by date) as diff_from_prev
from sales;

''' Таблица orders с колонками order_date, revenue.
Задание: Для каждой даты выведите выручку и среднюю выручку за текущий и 6 предыдущих дней.'''

select
    order_date,
    revenue,
    avg(revenue) over (
        order by order_date
        rows between 6 preceding and current row
        ) as rolling_avg_7d
from orders;

'''Таблица products с колонками category, product_name, sales.
Задание: Для каждого товара выведите его продажи и долю от общих продаж категории в процентах.'''

select
    category,
    product_name,
    sales,
    round(
        100.0 * sales /sum(sales) over (partition by category),
        2
    ) as pct_of_category
FROM products;

'''Таблица students с колонками class, student_name, score.
Задание: Выведите только тех учеников, у кого оценка входит в топ-2 в их классе.'''
WITH ranked AS (
    SELECT
        class,
        student_name,
        score,
        DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC) as rnk
    FROM students
)
SELECT class, student_name, score
FROM ranked
WHERE rnk <= 2;
'''Таблица clicks с колонками user_id, click_time. Сессия — последовательность кликов одного пользователя с интервалом не более 30 минут.
Задание: Назначьте каждому клику номер сессии.'''

WITH gaps AS (
    SELECT
        user_id,
        click_time,
        click_time - LAG(click_time) OVER (PARTITION BY user_id ORDER BY click_time) as gap
    FROM clicks
),
sessions AS (
    SELECT
        user_id,
        click_time,
        SUM(CASE WHEN gap > INTERVAL '30 minutes' THEN 1 ELSE 0 END)
            OVER (PARTITION BY user_id ORDER BY click_time) as session_num
    FROM gaps
)
SELECT * FROM sessions;
'''Таблица salaries с колонкой amount.
Задание: Найдите медианную зарплату.'''
WITH ordered AS (
    SELECT
        amount,
        ROW_NUMBER() OVER (ORDER BY amount) as rn,
        COUNT(*) OVER () as total
    FROM salaries
)
SELECT AVG(amount) as median
FROM ordered
WHERE rn IN (FLOOR((total + 1) / 2.0), CEIL((total + 1) / 2.0));
'''Таблица stock_prices с колонками ticker, date, price.
Задание: Для каждого тикера выведите первую и последнюю цену в датасете.'''
SELECT DISTINCT
    ticker,
    FIRST_VALUE(price) OVER (PARTITION BY ticker ORDER BY date) as first_price,
    LAST_VALUE(price) OVER (
        PARTITION BY ticker
        ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as last_price
FROM stock_prices;


