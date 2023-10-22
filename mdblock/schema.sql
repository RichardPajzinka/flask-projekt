drop table if exists articles;
create table articles (
	if integer primary key autoincrement,
	title text not null,
	content text not null
);