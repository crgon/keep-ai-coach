## 一、重要的一些sql语句

![](images/day1-image.png)

### 1.select用法

SELECT column1, column2, ...(列的名字)

FROM table\_name;（表的名字）

### 2.select distinct用法

SELECT DISTINCT column1, column2, ...

FROM table\_name;

区别：和上面的区别在于只会列出不一样的

SELECT COUNT(DISTINCT Country) FROM Customers;

这个会列出不一样的数字

### 3.where用法

SELECT column1, column2, ...

FROM table\_name

WHERE condition;

SELECT \* FROM Products

WHERE Price BETWEEN 50 AND 60;

SELECT \* FROM Customers

WHERE City LIKE 's%';

(这个是以s作为开头)

SELECT \* FROM Customers

WHERE City IN ('Paris','London');

![](images/day1-image-1.png)

### 4.order by

SELECT *column1*,*&#x20;column2, ...*
FROM *table\_name*
ORDER BY *column1, column2, ...&#x20;*&#x41;SC|DESC;

Desc 是默认降序，ASC 是默认升序

### 5.create/drop—创建新的数据库

CREATE DATABASE testDB;  运行SHOW DATABASES;&#x20;

DROP DATABASE testDB;&#x20;

### 6.backup—备份数据库

BACKUP DATABASE *databasename*
TO DISK = '*filepath*'
(WITH DIFFERENTIAL);

后面是可选选项，是说自上次有变化的才更新

### 7.create—创造新表

CREATE TABLE Persons (

&#x20;   PersonID int,

&#x20;   LastName varchar(255),

&#x20;   FirstName varchar(255),

&#x20;   Address varchar(255),

&#x20;   City varchar(255)

);

挑选从已经存在的表格列中创造新表

CREATE TABLE *new\_table\_name* AS
&#x20;   SELECT *column1, column2,...*
&#x20;   FROM *existing\_table\_name*
&#x20;   WHERE ....;

### 8.drop/truncat—删除表格/表格数据

DROP TABLE Shippers;TRUNCATE TABLE *table\_name*;

### 9.更改表格的一些属性

ALTER TABLE *table\_name*
ADD *column\_name datatype*;

ALTER TABLE *table\_name*
DROP COLUMN *column\_name*;

ALTER TABLE *table\_name*
RENAME COLUMN *old\_name* to *new\_name*;

ALTER TABLE *table\_name*
ALTER/MODIFY COLUMN *column\_name datatype*;

增加列/删除列/重命名列名/修改列表属性

### 10. 添加约束

CREATE TABLE table\_name (

&#x20;   column1 datatype constraint,

&#x20;   column2 datatype constraint,

&#x20;   column3 datatype constraint,

&#x20;   ....

);

### 11.insert

INSERT INTO *table\_name* (*column1*,*&#x20;column2*,*&#x20;column3*, ...)
VALUES (*value1*,*&#x20;value2*,*&#x20;value3*, ...);

不写列就是给所有列添加

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)

VALUES

('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),

('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),

('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');

这个添加多行

![](images/day1-image-2.png)

## 二、安装轻量级SQL

### 1.安装SQLite

在https://www.sqlite.org/download.html官方网站上下载tools和dull，解压缩至一个独立的文件夹

### 2.配置环境变量

在配置环境变量中，把上面目录添加进环境变量

### 3.使用命令行验证是否成功安装

![](images/day1-image-3.png)

### 4.安装可视化工具

直接在官网下载https://www.sqlitestudio.pl/

## 三、检验题目

1. 在`keep_learning`数据库中创建两张表：

   * `users`表：包含id, name, age, gender, join\_date

   * `workouts`表：包含id, user\_id, workout\_date, duration\_minutes, calories\_burned

```sql
create table users (
    id int,
    name char(255),
    gender char(10),
    join_date date
);
create table workouts (
    id int,
    user_id int,
    workout_date date,
    duration_minutes int,
    calories int
 );
alter table users add age int;
#.schema user;这个是在cmd上看表格的列名
#.
```

* 向每张表插入至少5条模拟数据（数据要合理，比如年龄在18-50之间）

```sql
insert into users
(id, name, gender, join_data, age)
values
(1, 'xueliang', 'male', 2024-1-2, 23);
insert into users values (2, 'jiaxin', 'female', 2025, 25);
insert into users values (3, 'yexuan', 'female', 2025, 24);
insert into users values (4, 'wenqi', 'female', 2023, 23);
insert into users values (5, 'wenqin', 'male', 2024, 24);
insert into workouts values (1, 2, 2025, 50, 137),
(2, 4, 2024, 60, 189),
(3, 1, 2023, 48, 159),
(4, 2, 2022, 23, 78),
(5, 5, 2024, 55, 189);
```

![](images/day1-image-5.png)

![](images/day1-image-4.png)

