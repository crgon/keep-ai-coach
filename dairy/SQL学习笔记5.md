## 重要知识点

### UNION

* 格式：

SELECT *column\_name(s)* FROM *table1*
UNION
SELECT *column\_name(s)* FROM *table2*;

* 要求：

  * 所有选择的列需要数量相同，对应的列需要具备相似的数据类型

  * 所有选项的列必须按照一样的顺序

* 加上where

SELECT City, Country FROM Customers

WHERE Country='Germany'

UNION

SELECT City, Country FROM Suppliers

WHERE Country='Germany'

ORDER BY City;

* list一个类型但是不同名字的

SELECT 'Customer' AS Type, ContactName, City, Country

FROM Customers

UNION

SELECT 'Supplier', ContactName, City, Country

FROM Suppliers;

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=OWE0ZTI4Njg0NjEyMzJiZmVmOWY1MjhhZWIwZGJhMGFfa0JobHl6M0FHek9kbmdPdUtlM292MVpXWTViWk91a1hfVG9rZW46QUdTd2J4RHA2b3k1N3V4M3o1M2NoZnpIbmJkXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

### UNION ALL

会有重复值

SELECT *column\_name(s)* FROM *table1*
UNION ALL
SELECT *column\_name(s)* FROM *table2*;

### GROUP BY

SELECT COUNT(CustomerID), Country

FROM Customers

GROUP BY Country

ORDER BY COUNT(CustomerID) DESC;

### HAVING

在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。

HAVING 子句可以让我们筛选分组后的各组数据。

SELECT column1, aggregate\_function(column2)

FROM table\_name

GROUP BY column1

HAVING condition(可以使用聚合函数);

## LeetCodeSQL 重要50题重点习题（考点：连接 难度:简单-中等 完成进度：14/50）

### 1.1661每台机器的进程平均运行时间

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=NGE2MDgyNThjY2E4OTI4NmEyOGJlN2NhYWNlNTBjZGRfSDhnTWlwQmtZRkwzSXd2WXhMSVB4Qmhya1gxU1FWeXhfVG9rZW46T0t1TGI0Rjhyb3VoeTl4QXM1MWNJSDNmbmVmXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

补充函数：ROUND(number, digits)

```sql
# Write your MySQL query statement below
#第一个想法：是否将这个表自链接，形成开始和结束和时间戳来
select a.machine_id, a.process_id, a.timestamp, b.machine_id, b.process_id, b.timestamp
from Activity a, Activity b
where a.process_id=b.process_id and a.activity_type='start' and 
b.activity_type='end' and a.machine_id=b.machine_id;
#使用分组来进行机器的总体平均
#本题答案
select a.machine_id, round(avg(b.timestamp-a.timestamp),3) as processing_time 
from Activity a, Activity b
where a.process_id=b.process_id and a.activity_type='start' and 
b.activity_type='end' and a.machine_id=b.machine_id
group by a.machine_id;
```

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=ODQ1MTVlODZjMGMxZTI5ZjBjN2NhMGQwY2E4NjJiODVfU0FVMnpiaXEwUW9UWVU1VGF6cmxRb0poa1lXbVJ1Sk5fVG9rZW46S0MzUGJsdW4xb2lHdXZ4TGlHY2NyTjl2bnFoXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

### 2.577员工奖金

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWRmN2ExYTIxN2QzOWJhODBhYjQ0OWQ5MDQyOWJiNjhfcXNiVk9QZGRKeXhYMHBZaVpzSXRmY0NiRHQxd01kb1BfVG9rZW46SG9VTWJSQjV1b2t5bVd4OWE4TWN2dHR4bjFiXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

```sql
#直接使用左连接来连接奖金
select Employee.name, Bonus.bonus
from Employee
left join Bonus on Employee.empId = Bonus.empId
where Bonus.bonus<1000 or Bonus.bonus is null;
```

### 3. 1280学生们参加各科测试的次数

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTQzMWM0MDE1ZjYzNTYwMDkzN2U3Y2I1NzhiYTVhY2FfV3ZWS2xPak9DOG55Wmk0YjY1djRSZnBVVU02U05nT3lfVG9rZW46RjdkQ2JiU2hKb3pmMUt4OWU1U2N2ZW1Dbm1oXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

补充知识：笛卡尔积或者交叉连接CROSS JOIN不需要条件

SELECT t1.emp\_id, t1.emp\_name, t1.hire\_date, t2.dept\_name

FROM employees AS t1 CROSS JOIN departments AS t2;

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YjcwMzlmMDMwYmVjYWNiYzIxYzIyN2FlNjdjNmUyZjlfRlVmRHJaRUVvc3Awb1lIMWppNzhFa2puQ3RkbFY5NjZfVG9rZW46VWRzWWJYSHptb3dJQ3F4WGpGR2NyRzFNblNoXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

IFNULL() 函数用于判断第一个表达式是否为 NULL，如果为 NULL 则返回第二个参数的值，如果不为 NULL 则返回第一个参数的值。

IFNULL() 函数语法格式为：

IFNULL(expression, alt\_value)

```sql
# Write your MySQL query statement below
SELECT 
    s.student_id, s.student_name, sub.subject_name, IFNULL(grouped.attended_exams, 0) AS attended_exams
FROM 
    Students s
CROSS JOIN 
    Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) grouped 
ON s.student_id = grouped.student_id AND sub.subject_name = grouped.subject_name
ORDER BY s.student_id, sub.subject_name;

```

### 4.570至少有5名直接下属的经理

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=MDYxNTU5YjZkZjdiMTM5MjZkYWZjNTJiMDIyZmQxZjhfeUxzSWFsYjlQeXRwNE0yd3NmZUdaM05aMVFySmoxdndfVG9rZW46VVY2R2I3ZlMyb1M0OXF4RTBLdmN4dmwzbnZnXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)

* 经典错误（在where中不能使用聚合函数，因为where是在聚合前进行过滤的，应该使用having来进行过滤）

```plain&#x20;text
# Write your MySQL query statement below
#分组来收集经理id
select managerID, count(managerID)
from Employee
where count(managerID) > 5
group by managerID;
```

* 正确答案，自链接

```plain&#x20;text
# Write your MySQL query statement below
#分组来收集经理id
select b.name
from Employee a, Employee b
where a.managerID=b.id
group by a.managerID
having count(a.managerID)>=5;
```

### 5. 1934确定率

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YTVkMTQ3NThkZmZhNDVjOGYyNGU0YjQyYTY3ZDUyNWVfY2VMelRSUDk2NURQbE1UclNHSEprQUc2ZmNLYlVsYlRfVG9rZW46VWdyVmJ4VVphbzl3dzZ4M2xhcmMxUlpDblljXzE3NzEzMzQ3NDI6MTc3MTMzODM0Ml9WNA)



```sql
# Write your MySQL query statement below
#其中AVG(b.action='confirmed')等价于SUM(IF(action = 'confirmed', 1, 0)) / COUNT(action)
SELECT a.user_id, ROUND(IFNULL(AVG(b.action='confirmed'), 0), 2) AS confirmation_rate
FROM Signups AS a
LEFT JOIN Confirmations AS b
ON a.user_id = b.user_id
GROUP BY a.user_id;
```



