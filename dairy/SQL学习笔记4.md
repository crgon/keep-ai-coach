## 聚合函数

### 1.MAX/MIN

SELECT MIN/MAX(*column\_name*)
FROM *table\_name*
WHERE *condition*;

分组且别名：

SELECT MIN(Price) AS SmallestPrice, CategoryID

FROM Products

GROUP BY CategoryID;

### 2.COUNT

求表格中的总行数

SELECT COUNT(\*)

FROM Products

忽视重复：

SELECT COUNT(DISTINCT Price)

FROM Products;

分组并且计数

SELECT COUNT(\*) AS \[Number of records], CategoryID

FROM Products

GROUP BY CategoryID;

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YWIyODVhYTBjMmE5MzU5Y2FkZDg0YzIyYjExZTM2MjNfZ0UzNFFEbFVoNUI5WEVxNFc2T3p5MzV5VlNpTmJkd21fVG9rZW46V3dKbGJWell3b3NXWU94OVJFTWNkalYwbkdlXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)

### 3.SUM

SELECT OrderID, SUM(Quantity) AS \[Total Quantity]

FROM OrderDetails

GROUP BY OrderID;

### 4.AVG

SELECT \* FROM Products

WHERE price > (SELECT AVG(price) FROM Products);

### 5.LIKE

* 百分号表示零、一或多个字符`%`

* 下划线符号代表一个字符`_`

SELECT \* FROM Customers

WHERE city LIKE 'L\_nd\_\_';

### 6.IN

OR的plus版本

SELECT \* FROM Customers

WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);

### 7.BETWEEN

重点日期

SELECT \* FROM Orders

WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

### 8.别名

mysql：

SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address

FROM Customers;

如果你希望别名包含一个或多个空格，比如“”， 用方括号或双引号包围你的别名。

SELECT ProductName AS \[My Great Products]

FROM Products;

表别名（特别是自链接）

SELECT \* FROM Customers AS Persons;

### 9.LENGTH

主要是字符串

SELECT LENGTH(column\_name) FROM table\_name;

## LeetCodeSQL 重要50题重点习题（考点：查询+连接 难度:简单 完成进度：9/50）

### 1.585大的国家

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzc4MDEwYjBmZWJmMzdlMDBlNWIwYjBkZGUwYWZmZTBfZ1BENlE0N3lYemtSVjk3c0ZVREZQZzUxUGhuY0o5OTNfVG9rZW46V0Z4TmJyelZqbzNnejd4aWo3WmNRZGlPbnpoXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)



### 2.1148文章浏览 I

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YTExYTg1ZDZmYjYxMTgyYmExNWM4MWEwYjJkYThkNTFfVUtFZk5mY1dSd2pNM2VQMFVibEFUQUlPbDRPVDQ0ZVhfVG9rZW46QkhNS2J2aXFzb0dpZDR4ZHJaQ2NZRTJxbnpkXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)

### 3. 1683无效的推文

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDZiOTczYjYwZWJhNzEyZTZmYTI5ZDVkZDQ1OTJlYjhfcGQ4ekZhc2paTXV2ZVU1ZllqTHRrR2FiQ1g2V21KSXlfVG9rZW46UGx4UmJ2WVMyb0tJWWx4WWVpeGNvTlFsblNmXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)

### 4.1581进店却未进行过交易的顾客

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OWM0NjJmNDBmODU3NjUzMWVmOTI0NzUwNGQ0MTU4MGFfVVd3UWZoZ1ZQeFRDQThrNmpVem5WNXRDR1lxYW12QzlfVG9rZW46S2NZeWJjZnBCb05RRlF4QXZDbmNYZFplbkZlXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)

#### 1.第一种方法直接使用分组以及聚合函数等来进行完成

#### 2.使用连接

在先将其左连接起来观察特征，然后再根据特征进行筛选

### 5. 197上升的温度

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OGU1YzgwNjA1ZDBkMTA4NDIyMWIwNTkyMmEzMjk4YWVfakhuMG5JZXNPTVlXNkVpQXk2VmJFazV5THJkWGt0eDRfVG9rZW46RXF6OGJkQXE2b0xvb3l4RzJ5cmN5Y1d3bjhkXzE3NzEzMzQ1NDI6MTc3MTMzODE0Ml9WNA)

补充知识点时间的更新

SELECT DATE\_ADD('2022-02-24', INTERVAL 1 DAY);

SELECT DATE\_SUB('2022-02-24', INTERVAL -1 DAY);

