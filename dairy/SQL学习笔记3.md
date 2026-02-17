## 基础知识点

### 1.AND / OR 语句

SELECT *column1*,*&#x20;column2, ...*
FROM *table\_name*
WHERE *condition1* AND *condition2* AND *condition3 ...*;

或者两者进行结合

SELECT \* FROM Customers

WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');

将AND和OR相结合

### 2.NOT

SELECT *column1*,*&#x20;column2, ...*
FROM *table\_name*
WHERE NOT *condition*;

not可以接where后面的多种表现

### 3.（NOT）NULL

SELECT *column\_names*
FROM *table\_name*
WHERE *column\_name* IS NULL;

SELECT *column\_names*
FROM *table\_name*
WHERE *column\_name* IS NOT NULL;

### 4.DELETE

删除特定条件的记录

DELETE FROM *table\_name&#x20;*&#x57;HERE *condition*;

删除所有记录但是不删除表

DELETE FROM *table\_name*;

## 重要考点——JOIN

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2E0NTYwZmQwODI5MDJmYzNkYTUzMjM5NGZkNGY3YWRfOU11WGNlZWJ1MjFZVnBiNVVmdUd3cXV2V2pyWTRrbXRfVG9rZW46T3N5amJrT0pBbzFhNmJ4SGV1bmN1UHB5bkRjXzE3NzEzMzQzOTM6MTc3MTMzNzk5M19WNA)

### 1.（inner）join

两者

SELECT Products.ProductID, Products.ProductName, Categories.CategoryName

FROM Products

INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

三者

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName

FROM ((Orders

INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)

INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

### 2.LEFT JOIN/RIGHT JOIN

这两者是一样的，只是那个表完全，看之前的图片就可以知道区别

SELECT Customers.CustomerName, Orders.OrderID

FROM Customers（左）

LEFT JOIN Orders（右） ON Customers.CustomerID = Orders.CustomerID

ORDER BY Customers.CustomerName;

### 3. FULL OUTER JOIN

SELECT Customers.CustomerName, Orders.OrderID

FROM Customers

FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID

ORDER BY Customers.CustomerName;

### 4. 自链接self join

SELECT *column\_name(s)*
FROM *table1 T1, table1 T2*
WHERE *condition*;

T1， T2是同一个表的别名

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City

FROM Customers A, Customers B

WHERE A.CustomerID <> B.CustomerID

AND A.City = B.City

ORDER BY A.City;

## LeetCodeSQL 重要50题重点习题（考点：查询+连接 难度:简单）

### 1.1757可回收且低脂的产品

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YzJjMzNlYmEyZjNkMWI1MGVhNDBkNDJmNjJkYzY3YzdfcnJ5YkNUUVNWN3BMbHRaMGlxb3AwU1lwVVBMMURiT3ZfVG9rZW46VXF6ZGJOWk5xb0pmU2J4YlVJZmNVRVRubjhjXzE3NzEzMzQzOTM6MTc3MTMzNzk5M19WNA)

```sql
# Write your MySQL query statement below

SELECT product_id 
FROM Products
WHERE low_fats='Y' and recyclable='Y';
```

### 2.584寻找用户推荐人

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OTRlOTg4YzY5NmZjNzgzYTEzODJhNzIwMDliMDVkZTFfY2JKQmVtRnBuWTllbDltTlFEN0FtUGJiVnpkVkl0UUNfVG9rZW46QmcxVWIwYWVRbzRlQzR4cmRpZmMxeWNlbkczXzE3NzEzMzQzOTM6MTc3MTMzNzk5M19WNA)



```sql
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id<>2 OR referee_id IS NULL;
```

### 3. 1378使用唯一标识符来代替员工ID

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OWM1OGZlYWE4MWY2ZWI5MjI0YTFhZTNlNGI2MmM3NmRfVzVibGxVWGozcjVQNVp6RFg2SDZ1dWFNWWV0SUZWWlVfVG9rZW46TDNKcGJSZkdhbzd6STF4cmJmNWNiRWdhbm9kXzE3NzEzMzQzOTM6MTc3MTMzNzk5M19WNA)

```sql
# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI
RIGHT JOIN Employees
ON EmployeeUNI.id=Employees.id;
```

### 4.1068产品销售分析I

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NWMxZTg2MDI3ODE1ZmE5ZTExN2RjYmJlYmMyYzU4OTZfb2t3VFZwM2xUd2ZCNlEwYW9XTllnblRlQTFzTllGcFFfVG9rZW46SjBxRWIxN3d6b0FuY2x4dmRnNWNtVkxrbkxkXzE3NzEzMzQzOTM6MTc3MTMzNzk5M19WNA)

```sql
# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
FROM Product
RIGHT JOIN Sales 
ON Product.product_id=Sales.product_id;
```
