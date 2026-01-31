重要的一些sql语句
<img width="1262" height="527" alt="image" src="https://github.com/user-attachments/assets/96380ce3-f379-44da-a8c8-3edd0d74a79f" />

1.select用法
SELECT column1, column2, ...(列的名字)
FROM table_name;（表的名字）

2.select distinct用法
SELECT DISTINCT column1, column2, ...
FROM table_name;
区别：和上面的区别在于只会列出不一样的
SELECT COUNT(DISTINCT Country) FROM Customers;
这个会列出不一样的数字

3.where用法
SELECT column1, column2, ...
FROM table_name
WHERE condition;

<img width="1719" height="724" alt="image" src="https://github.com/user-attachments/assets/635d3c46-0e6c-44b9-ac76-26b83b1540ec" />

4.
