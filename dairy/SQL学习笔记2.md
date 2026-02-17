## 1.SQL语句复习

### NOT NULL

* 创建表的时候声明

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255) NOT NULL,

&#x20;   Age int

);

* 后面进行改变

ALTER TABLE Persons

ALTER/MODIFY COLUMN Age int NOT NULL;

### UNIQUE

* 单独一列约束

CREATE TABLE Persons (

&#x20;   ID int NOT NULL UNIQUE,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int

);

* 多列约束

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int,

&#x20;   CONSTRAINT UC\_Person UNIQUE (ID,LastName)

);

* 改变约束

ALTER TABLE Persons

ADD UNIQUE (ID);

ALTER TABLE Persons

ADD CONSTRAINT UC\_Person UNIQUE (ID,LastName);

* 删除约束

ALTER TABLE Persons

DROP INDEX/CONSTRAINT UC\_Person;

### PRIMARY KEY

* mysql创建

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int,

&#x20;   PRIMARY KEY (ID)

);

* 其他的

CREATE TABLE Persons (

&#x20;   ID int NOT NULL PRIMARY KEY,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int

);

* 多列的约束添加

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int,

&#x20;   CONSTRAINT PK\_Person PRIMARY KEY (ID,LastName)

);

* 已经存在的表上进行约束的添加 单列/多列

ALTER TABLE Persons

ADD PRIMARY KEY (ID);

ALTER TABLE Persons

ADD CONSTRAINT PK\_Person PRIMARY KEY (ID,LastName);

* 丢弃约束

ALTER TABLE Persons

DROP PRIMARY/CONSTRAINT KEY;

### FOREIGN KEY

* MYSQL创建

CREATE TABLE Orders (

&#x20;   OrderID int NOT NULL,

&#x20;   OrderNumber int NOT NULL,

&#x20;   PersonID int,

&#x20;   PRIMARY KEY (OrderID),

&#x20;   FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)

);

* 其他创建

CREATE TABLE Orders (

&#x20;   OrderID int NOT NULL PRIMARY KEY,

&#x20;   OrderNumber int NOT NULL,

&#x20;   PersonID int FOREIGN KEY REFERENCES Persons(PersonID)

);

* 多列创建

CREATE TABLE Orders (

&#x20;   OrderID int NOT NULL,

&#x20;   OrderNumber int NOT NULL,

&#x20;   PersonID int,

&#x20;   PRIMARY KEY (OrderID),

&#x20;   CONSTRAINT FK\_PersonOrder FOREIGN KEY (PersonID)

&#x20;   REFERENCES Persons(PersonID)

);

* 已有添加

ALTER TABLE Orders

ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

ALTER TABLE Orders

ADD CONSTRAINT FK\_PersonOrder

FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

* 删除约束

ALTER TABLE Orders

DROP FOREIGN KEY/CONSTRAINT FK\_PersonOrder;

### CHECK约束

* 同上只需要将关键词改变，**注意括号**

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int,

&#x20;   City varchar(255),

&#x20;   CONSTRAINT CHK\_Person CHECK (Age>=18 AND City='Sandnes')

);

CREATE TABLE Persons (

&#x20;   ID int NOT NULL,

&#x20;   LastName varchar(255) NOT NULL,

&#x20;   FirstName varchar(255),

&#x20;   Age int CHECK (Age>=18)

);

### DEFAULT约束

* 创建时添加

CREATE TABLE Orders (

&#x20;   ID int NOT NULL,

&#x20;   OrderNumber int NOT NULL,

&#x20;   OrderDate date DEFAULT GETDATE()

);

* 单独添加

Mysql

ALTER TABLE Persons

ALTER City SET DEFAULT 'Sandnes';

SQL server

ALTER TABLE Persons

ADD CONSTRAINT df\_City

DEFAULT 'Sandnes' FOR City;

MS Access

ALTER TABLE Persons

ALTER COLUMN City SET DEFAULT 'Sandnes';

Orcle

ALTER TABLE Persons

MODIFY City DEFAULT 'Sandnes';

* 删除

Mysql

ALTER TABLE Persons

ALTER City DROP DEFAULT;

其他

ALTER TABLE Persons

ALTER COLUMN City DROP DEFAULT;

### UPDATE

UPDATE *table\_name*
SET *column1&#x20;*=*&#x20;value1*,*&#x20;column2&#x20;*=*&#x20;value2*, ...
WHERE *condition*;

## 2.命名规范

1. 原则：清晰、一致、具有描述性。

2. 表名：使用复数名词，清晰描述实体内容。例如：`users`, `orders`, `products`， 而非 `user`, `order_data`, `prod`。

3. 字段名：使用小写蛇形命名法（snake\_case），避免使用数据库关键字。例如：`user_id`, `created_at`, `email_address`， 而非 `UserId`, `created`, `emailAddress`。

4. 主键：建议使用 `id` 或 `表名_id`（如 `user_id`）。

5. 外键：应明确关联关系，通常格式为 `关联表名_id`。例如，在 `orders` 表中关联 `users` 表，外键字段应为 `user_id`。

6. 索引名：包含表名、字段名和类型。例如：`idx_users_email` (普通索引), `uk_users_username` (唯一索引), `pk_users` (主键索引)。

## 3.练习在之前的基础上对表进行分析

### 背景

现在在keep\_learning的数据集中，存在两个表分别是 users、workouts，其中两个表的结构分别是

users(id int, name char(255), gender char(10), join\_date date, age int)

workouts(id int, user\_id int, workout\_date date, duration\_minutes int, calories int)

每个表格中存在五条数据，利用所学知识进行表格的进一步完善。

增加两个表格，一个表格是训练类型表格初始列是编号，训练名称，每小时卡路里，参与训练的人数，

另外一个表格是训练与人员表格关联表，初始列是编号，训练类型编号，用户id，开始日期

### 分析并解决

users是父表，在workouts中user\_id作为外键来进行约束

两个表中的id都是各自表的主键

锻炼的时间必须要在用户加入时间之后

年龄的范围在18-60岁

性别只能是“male”or“female”

date错误进行更正

```sql
#先对缺失的表进行补充
#训练类型表格初始列是编号，训练名称，每小时卡路里，参与训练的人数，
#mysql登录指令
#mysql -h localhost -u root -p
CREATE TABLE train_types(
    id int PRIMARY KEY,
    train_name char(255),
    hour_calries int check(hour_calries > 0), 
    joined_pernum int check(joined_pernum >= 0) default 0 
);
#训练与人员表格关联表，初始列是编号，训练类型编号，用户id，开始日期
ALTER TABLE users
ADD PRIMARY KEY(id);
ALTER TABLE workouts
ADD PRIMARY KEY(id);
CREATE TABLE train_users(
    id int PRIMARY KEY,
    train_id int,
    user_id int,
    begin_date date,
    FOREIGN KEY(train_id) REFERENCES train_types(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

### 遇见问题：sqlite是轻量级的应用，无法对已经存在的表进行更改，重新下载MYSQL来完成

