## 从问题开始思考如何搭建数据库

### Q1：假设我们要存储用户的"跑步记录"，我会设计几张表？每张表存什么？为什么这样分？

应该设计两张表，一张表来存储用户的静态信息，一张表来存储运动记录是每一次运动会不同的东西，通过外键约束将运动记录和用户信息连接起来。

### Q2:如果用户问"我上周跑了多少公里"，数据库需要哪些字段才能回答这个问题？

需要使用筛选跑步日期，并且统计跑步距离

### Q3:表名用 `user_workout_log` 好还是 `sessions` 好？从 LLM 理解的角度考虑。

使用user\_workout\_log,从LLM视角前者清晰表达了用户运动日志

### 总结：

从三个问题我们总结出我们设计的数据库表需要满足以下要求：

* 设计的数据库需要满足数据库第三范式：

  * **第一范式：每个字段不可再分**：比如时间段记录是不可取的，应该分为开始时间和结束时间

  * **第二范式：非主键字段完全依赖主键**：不应该在运动记录表中存储用户姓名，因为用户姓名完全依赖于用户ID不是运动记录表中的主键

  * **第三范式：非主键字段不依赖其他非主键字段**：不能存储BMI值，因为BMI值是使用身高和体重来计算的，应该动态获取，而不是存储

* 数据表或者是具体列的命名要符合LLM可以认知的，清晰表达，避免类型sessions等泛化性命名

## SQLite数据库搭建

### 使用draw.io来绘制数据库基本ER图

![](https://jcnzdtxpvvg8.feishu.cn/space/api/box/stream/download/asynccode/?code=YmFhYTQ5YTgyN2M4N2QxZDgwZDczODhlYzcyZDNlM2RfWDlKUDl5cWp0UTBBWXFuQWFjYTVJUUw1MnllVVdTRjNfVG9rZW46Q1FJR2J1OFg4bzVMb3p4dEdRWWNwNWM4bndkXzE3NzEzMzYxNDg6MTc3MTMzOTc0OF9WNA)

### 写出SQLite建表语句

**需要注意的地方：**

* 注意SQLite的数据类型：`INTEGER`、`REAL`、`TEXT`、`BLOB`、`NULL`

* 注意SQLite的时间存储：

  * `TEXT`（ISO 8601 格式：`"2024-01-09 15:25:26"`）

  * `INTEGER`（Unix 时间戳：`1704799526`）

* 对于时间约束的方式（这里使用第一个）

  ```sql
  -- ✅ 方法 1：简单模式匹配（推荐新手）
  birthday TEXT CHECK(birthday GLOB '????-??-??')

  -- ✅ 方法 2：长度检查
  birthday TEXT CHECK(length(birthday) = 10)

  -- ✅ 方法 3：正则表达式（SQLite 3.8.3+）
  birthday TEXT CHECK(birthday REGEXP '^\d{4}-\d{2}-\d{2}$')
  ```

```sql
-- ========== FitMind 数据库建表语句 ==========

-- 用户表
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender INTEGER NOT NULL CHECK(gender IN (0, 1)),
    birthday TEXT CHECK(birthday GLOB '????-??-??'),
    register_time TEXT CHECK(register_time GLOB '????-??-?? ??:??:??') DEFAULT (datetime('now', 'localtime')),
    weight REAL CHECK(weight between 0.00 and 200.00),
    height REAL CHECK(height between 0.00 and 3.00),
    sport_rank INTEGER CHECK(sport_rank in(1,2,3,4,5)),
    fitness_goal INTEGER CHECK(fitness_goal in(1,2,3))
);

-- 运动记录表
CREATE TABLE workout_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    sport_type  INTEGER CHECK(sport_type in(1,2,3,4,5)),
    begin_time TEXT CHECK(begin_time GLOB '????-??-?? ??:??:??'),
    end_time TEXT CHECK(end_time GLOB '????-??-?? ??:??:??'),
    distance REAL CHECK(distance>=0),
    feeling INTEGER CHECK(feeling in(1,2,3,4,5)),
    calories REAL,
    heart_rate_max INTEGER,
    heart_rate_min INTEGER,
    notes TEXT DEFAULT '',
    weather TEXT DEFAULT 'unknown',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CHECK(begin_time < end_time)
);
```

### 为LLM写“数据字典”

**需要注意地方：**

* 注意使用LLM可以理解的方式进行命名

* 注意枚举值需要特意说明

```plain&#x20;text
# users 表 | 字段名 | 类型 | 说明 | 示例 |
 |--------|------|------|------| 
| id | INTEGER | 用户唯一标识 | 1001 | 
| name | TEXT | 用户姓名 | "张三" | 
| gender | INTEGER |  用户性别(1为男性,0为女性) | 1  | 
| birthday | TEXT |  出生年月 | "2017-01-09"  | 
| register_time | TEXT |  注册时间 | "2017-01-09 12:05:32"  | 
| weight | float |  体重单位为kg | 58.36  | 
| height | float |  身高单位m | 1.63  | 
| sport_rank | INTERGER |  运动等级(1-5) |  1  |
| fitness_goal | INTERGER |  训练目标(1-3) |  1  |
## workout_sessions 表 | 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------| 
| id | INTERGER | 记录唯一标识 | 10000001 | 
| user_id | INTERGER |  用户标识 | 1001  | 
| sport_type | INTERGER |  运动类型 | 1  | 
| begin_time | TEXT |  开始时间 | "2017-01-09 15:25:26"  | 
| end_time | TEXT |  结束时间 | "2017-01-09 15:59:59"  | 
| distance | float |  运动距离(km) | 1.25  | 
| feeling | INTERGER |  感受 | 1 | 
| calories | float |  消耗卡路里(kcal) | 163.58  | 
| heart_rate_max | INTERGER |  最高心率 | 165  | 
| heart_rate_min | INTERGER |  最低心率 | 86 |
| notes | TEXT |  用户备注 | '今天膝盖有点疼' |
| weather | TEXT |  天气 | 'sunday' |
### 枚举值说明
gender(性别)
0: 女性
1: 男性
sports_type(运动类型)
1: 跑步 (Running)
2: 骑行 (Cycling)
3: 游泳 (Swimming)
4: 力量训练 (Strength Training)
feeling(运动感受)
1: 非常轻松 (Very Easy)
2: 轻松 (Easy)
3: 适中 (Moderate)
4: 费力 (Hard)
5: 非常费力 (Very Hard)
sport_rank(运动等级)
1: 新手 (Beginner)
2: 初级 (Novice)
3: 中级 (Intermediate)
4: 高级 (Advanced)
5: 专家 (Expert)
fitness_goal(训练目标) 
1:减脂
2:增肌
3: 耐力提升
```

## 测试数据的插入

### **案例数据（部分数据，完整数据见github）**

```sql
INSERT INTO users (name, gender, birthday, register_time, weight, height, sport_rank, fitness_goal) VALUES
('张伟', 1, '1990-03-15', '2023-01-10 09:30:00', 75.5, 1.78, 3, 1),
('李强', 1, '1988-07-22', '2023-02-05 14:20:00', 82.3, 1.82, 4, 2),
('王磊', 1, '1992-11-08', '2023-03-12 10:15:00', 70.0, 1.75, 2, 3),
('刘洋', 1, '1985-05-30', '2023-04-18 16:45:00', 88.5, 1.85, 5, 2),
('陈浩', 1, '1995-09-12', '2023-05-22 11:30:00', 68.2, 1.72, 2, 1),
('杨军', 1, '1991-02-28', '2023-06-08 13:50:00', 79.8, 1.80, 4, 3)；

INSERT INTO workout_sessions (user_id, sport_type, begin_time, end_time, distance, feeling, calories, heart_rate_max, heart_rate_min, notes, weather) VALUES
(1, 1, '2024-01-15 06:30:00', '2024-01-15 07:15:00', 5.2, 3, 312, 165, 88, '早晨跑步状态不错', 'sunny'),
(2, 2, '2024-01-15 07:00:00', '2024-01-15 08:20:00', 15.8, 4, 480, 155, 90, '', 'sunny'),
(3, 1, '2024-01-15 18:30:00', '2024-01-15 19:00:00', 3.5, 2, 210, 145, 85, '', 'cloudy'),
(16, 1, '2024-01-15 06:45:00', '2024-01-15 07:20:00', 4.0, 2, 240, 152, 82, '感觉轻松', 'sunny'),
(17, 3, '2024-01-15 19:00:00', '2024-01-15 19:45:00', 1.2, 3, 380, 140, 75, '', 'sunny'),
(4, 4, '2024-01-15 17:00:00', '2024-01-15 18:00:00', 0.0, 4, 320, 125, 70, '力量训练日', 'sunny'),
(18, 2, '2024-01-15 08:00:00', '2024-01-15 09:30:00', 18.5, 3, 550, 148, 88, '', 'sunny'),
(5, 1, '2024-01-15 19:30:00', '2024-01-15 20:15:00', 6.0, 4, 360, 172, 92, '', 'cloudy')；
```

### 测试题

#### 1.查询"张伟"（user\_id=1）最近一周（2024-02-05 到 2024-02-12）的跑步总距离

```sql
SELECT SUM(distance) AS total_distance
FROM workout_sessions
WHERE user_id = (SELECT id FROM users WHERE name = '张伟')
  AND sport_type = 1
  AND date(begin_time) >= date('2024-01-22', '-7 days')
  AND date(begin_time) >= date('2024-01-22', '-1 days');
```

#### 2.查询所有用户在 2024-02-10（周六）的运动记录，按消耗卡路里从高到低排序

```sql
SELECT * FROM workout_sessions
WHERE strftime('%Y-%m-%d', begin_time)='2024-02-10' 
ORDER BY calories DESC;
```

#### 3.查询哪个用户的运动记录最多，以及有多少条记录（已经知道答案是 user\_id=1/2/3 并列第一，各8条）

```sql
SELECT user_id, COUNT(*) AS workout_numbers
FROM workout_sessions
GROUP BY user_id
HAVING COUNT(*) = (
    SELECT MAX(cnt) FROM (
        SELECT COUNT(*) AS cnt 
        FROM workout_sessions 
        GROUP BY user_id
    )
)
ORDER BY user_id;
```

#### 4.每个用户最喜欢的运动

知识补充：窗口函数

````sql
-- 给每个用户的运动记录编号（按次数排序）
SELECT 
    user_id,
    sport_type,
    COUNT(*) as count,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) as rank
FROM workout_sessions
GROUP BY user_id, sport_type;
```

**输出示例**：
```
user_id | sport_type | count | rank
--------|------------|-------|-----
1       | 1          | 5     | 1    ← 第1名
1       | 2          | 2     | 2
1       | 3          | 1     | 3
2       | 1          | 6     | 1    ← 第1名
2       | 4          | 1     | 2
````

完整代码

```sql
SELECT user_id, sport_type, count
FROM (
    SELECT 
        user_id,
        sport_type,
        COUNT(*) as count,
        -- TODO: 添加窗口函数，按用户分组，按count降序排序
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) as rank
    FROM workout_sessions
    GROUP BY user_id, sport_type
)
WHERE rank = 1
ORDER BY user_id;
```



