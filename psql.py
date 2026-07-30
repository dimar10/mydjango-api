create table topics(
id serial primary key,
name varchar(100) not null,
category varchar(50)

);

create table posts(
id serial primary key,
title varchar(100),
topic_id integer references topics(id) on delete restrict
);


-- запрос
with
-- собираем анные о записи и считаем ссылки до удаления
pre_stats as (
	select
		t.id,
		t.name,
		count(p.id) as ref_count
	from topics t
	left join posts p on p.topic_id = t.id
	where t.id =: topic_id --id
		and t.category != 'system' -- огр на системку
	group by t.id, t.name
);
--удаляем зависимые записи
del_posts as (
	delete from posts
	where topic_id in (select id from pre_stats)
	returning topic_id
);
--удаляем саму тематику
del_topics as (
	delete from topics
	where id in (select id from pre_stats)
	returning id,name
)
--возврат результата
select
	t.name,
	s.ref_count
from del_topics t
join pre_stats s on s.id = t.id
/*
если ссылки есть они посчитаются в реф каунт
потом удалятся в делпост затем тематика
*/