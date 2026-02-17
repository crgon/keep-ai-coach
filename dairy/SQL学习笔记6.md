## 重要知识点

### EXISTS

SELECT *column\_name(s)*
FROM *table\_name*
WHERE EXISTS
(SELECT *column\_name&#x20;*&#x46;ROM *table\_name* WHERE *condition*);

案例：

SELECT SupplierName

FROM Suppliers

WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=MTM5ZDJiMjZkZjY4YWVlNjFmZGRlZGMxMWMwNmQ0ZWZfbDQ2eks3Nlo0YTdPbk51Tnh2U0pGWFlZU3VDZzJ3dHdfVG9rZW46U0NVc2JjNHAzbzFwM214blRPc2NTeTZ2blRoXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### ANY/ALL

SELECT *column\_name(s)*
FROM *table\_name*
WHERE *column\_name operator* ANY
&#x20; (SELECT *column\_name*&#xA;*&#x20;&#x20;*&#x46;ROM *table\_name*&#xA;*&#x20;&#x20;*&#x57;HERE *condition*);

* 结果返回一个布尔值

* 如果任何子查询值满足条件，则返回 TRUE。

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=MTdiM2MxMTI4ZmY1NDJhOTMyZGU3YjY1ZDY4MjI1Y2NfODI5b1BWOG9qUWN0VFhraTBzNUx5YXE5blJPUkFHdVFfVG9rZW46SzJ1ZmI2YldGb2JGaXJ4OTlxUGN6WmlLbm9lXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

SELECT ALL *column\_name(s)*
FROM *table\_name*
WHERE *condition*;

SELECT *column\_name(s)*
FROM *table\_name*
WHERE *column\_name operator* ALL
&#x20; (SELECT *column\_name*&#xA;*&#x20;&#x20;*&#x46;ROM *table\_name*&#xA;*&#x20;&#x20;*&#x57;HERE *condition*);

* 结果返回一个布尔值

* 如果所有子查询值都满足条件，则返回 TRUE。

* 与 、 以及 语句一起使用`SELECTWHEREHAVING`

### SELECT INTO

将所有列复制到一个新表中

SELECT \*
INTO *newtable* \[IN *externaldb*]
FROM *oldtable*
WHERE *condition*;

以下SQL语句将多个表的数据复制到新表中：

SELECT Customers.CustomerName, Orders.OrderID

INTO CustomersOrderBackup2017

FROM Customers

LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

### INSERT

只将一个表中的部分列复制到另一个表:

INSERT INTO *table2&#x20;*(*column1*, *column2*, *column3*, ...)
SELECT *column1*, *column2*, *column3*, ...
FROM *table1*
WHERE *condition*;

### CASE

CASE

&#x20;   WHEN condition1 THEN result1

&#x20;   WHEN condition2 THEN result2

&#x20;   WHEN conditionN THEN resultN

&#x20;   ELSE result

END;

SELECT CustomerName, City, Country

FROM Customers

ORDER BY

(CASE

&#x20;   WHEN City IS NULL THEN Country

&#x20;   ELSE City

END);

### IFNULL、ISNULL、COALESCE和 NVL

SELECT ProductName, UnitPrice \* (UnitsInStock + IFNULL(UnitsOnOrder, 0))

FROM Products;

### 程序创建和运行

CREATE PROCEDURE SelectAllCustomers

AS

SELECT \* FROM Customers

GO;

EXEC SelectAllCustomers;

多个语句

CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)

AS

SELECT \* FROM Customers WHERE City = @City AND PostalCode = @PostalCode

GO;

EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';

### 注释

单行注释以 `--`开头。

多行注释以`/**/`

## LeetCodeSQL 重要50题重点习题（考点：聚合函数+排序分组 难度:简单-中等 完成进度：24/50）

### 1.620有趣的电影

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NjkyNDQ4NWM5YTlkODQ4NzkzODY5ZjBmY2I5OGZjZWJfMHRadjE1UURTQmExU05NVVVET1JseFRTaUp5aXZBcmlfVG9rZW46QVFjbmI5dDZub0pxTG94TDB6RGNrZ3FvblNkXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 2.1251平均售价

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=MzdmNjhlMDdjNDM2NmQwZGNiMDQyNmFjOWMyMjZmNDlfUzMyYjJpbEl4YlpNZkx0U05IdWFmMmVTMDFBUkN4dENfVG9rZW46Tm5pTWJnQnVzb251d1h4bThndGNHZ3RzbmdiXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NDI4MDk4ZWFjOGJmOWRmZjliYmQzNzY1ZGM4OTMxNTlfQnU2VGphbGRFNmVyZWlKOUxRRjBKNnhTRm1LcW53amtfVG9rZW46QzlpbWJBU1ljbzh4Uk94VnRkcWNHSDg4bnFlXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 3. 1075I项目员工I

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OWZkNDZlMzk2MmEyYjA0YWY2ZmFlYjhjZDMyMDVjOTlfZFFWaU5VOVY5aEduQ3NEMkgzdmN2UEJwTmhxbkU5WFlfVG9rZW46UHdqQ2JFaUZ0b2hhdGx4Qk5mOWNpZkF5bmhmXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 4.1633各赛事的用户注册率

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NDVlOTZhNTYzZDJhOTYzNTVkMjJlYjAwY2RiYTE5OTJfOTlWS2d2QllJd0M0WDdlN3VBUFVLTkRERnNVY2F1NFlfVG9rZW46QVNCRWJWZlBub3E4bUZ4amtwcGN5eEpXblZjXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 5. 1211查询结果的质量和占比

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YjhmODM3MmVlMmE4ODMxYjVlMWY3YTE2MGQ0YzJkNThfbXY5N3poQkZBcWppU3V2TVlyRVlEM3hTSEszRzRmZTZfVG9rZW46WExrNmJFUUxkb2pQNzZ4TkJvU2NWQjY0blBnXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

#### 补充知识点：在count中实现某种特定的情况下实现，案例如下：count(case when rating<3 THEN 1 END)

### 6.1193每月交易 I

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NzU5NTg2MjcxZGMwYmQzM2NiYzUwYTMwZjNjMTMwMDdfd0ZuOWZ4VUxUclNoNlVRd1A3Ymx1MWdlcnN4UDRQbWRfVG9rZW46WVBJUGJ5eEhab0dMaU94a01YTGNwTmNrbnVmXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 7.1173即时食物配送(重点掌握)

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=MmNmYzk0MWMxNzZiYjljMjU5NzcwMjhkMGRjNWZiZDZfaWllV3Y1QTFQbHMyY0xWbW1mMmxOZ0kxOWZpQkhlUnhfVG9rZW46SUFXVmJiaWRhb1d6enV4N2RLNmNDTDk3bmJlXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 8.550游戏玩法分析 IV

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=N2MzYjM1Zjc1Y2M2YWUyMTM1NzI3NDI4NmM5MGZlZGZfQ3F3Um5CWllubkxHanozOU9DcW1PbDFDQjh4ekc4MGdfVG9rZW46WnhObGJPcmlLb3h1WEZ4akZidGNYU0RtbkplXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 9.1141查询近20天活跃用户数

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NDk2NmZjYjI5NGJkZTg2N2QyNThmYzY2ZjdlOGZkNjFfQlRiSTVGajMxOGh2TTNEVTBpVWF3WFZqbmxKSk16ZW9fVG9rZW46U3RJM2JuTXh6b2pablh4aWFSS2NwVm11blpiXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)

### 10.2356每位教师所教授的科目种类数量

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=ODY5ODg0N2Y2YWI4NjkzMzk0ZjViNThmMzhkZTQwMTJfY3JtOEpmWWsyWmdPRDd1M3VBd0NYbngyZDFINDdVUWtfVG9rZW46SU5La2IyVGdsbzc1dXN4ZUJQOWNYemFpbkhvXzE3NzEzMzQ4NTE6MTc3MTMzODQ1MV9WNA)
