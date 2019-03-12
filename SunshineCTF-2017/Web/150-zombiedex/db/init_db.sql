create database CTFdb;
use CTFdb;
create table users(
    username varchar(50),
    password varchar(200)
);
insert into `users`(`username`,`password` ) values ("The_only_user_in_the_database","thisshouldhopefullybeimpossibletoguessbecauseitisreallylongandidontcare786649872163498716234987612394876129348");
create user chall identified by 'zoomc@-yiNm2+RK';
grant select on CTFdb.* to chall;
