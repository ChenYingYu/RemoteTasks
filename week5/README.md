# Task 1: Install MySQL server

# Task 2: Create database and table in your MySQL server

- Create a new database named website
  
  ```sql
  mysql> CREATE DATABASE website;
  ```
  
  ![Task2-1](./img/Task2-1.png)

- Create a new table named member, in the website database
  
  ```sql
  mysql> CREATE TABLE member (
      -> id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
      -> name VARCHAR(255) NOT NULL,
      -> email VARCHAR(255) NOT NULL,
      -> password VARCHAR(255) NOT NULL,
      -> follower_count INT UNSIGNED NOT NULL DEFAULT 0,
      -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
  ```
  
  ![Task2-2](./img/Task2-2.png)

# Task 3: SQL CRUD

- INSERT a new row to the member table where name, email and password must be set to test , test@test.com , and test . INSERT additional 4 rows with arbitrary data.
  
  ```sql
  mysql> INSERT INTO member(name, email, password)
      -> VALUES('test','test@test.com', 'test');
  ```
  
  ![Task3-1](./img/Task3-1.png)

- SELECT all rows from the member table.
  
  ```sql
  mysql> SELECT * FROM member;
  ```
  
  ![Task3-2](./img/Task3-2.png)

- SELECT all rows from the member table, in descending order of time.
  
  ```sql
  mysql> SELECT * FROM member ORDER BY time DESC;
  ```
  
  ![Task3-3](./img/Task3-3.png)

- SELECT total 3 rows, second to fourth, from the member table, in descending order

of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.

```sql
mysql> SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```

![Task3-4](./img/Task3-4.png)

- SELECT rows where email equals to test@test.com .
  
  ```sql
  mysql> SELECT * FROM member WHERE email='test@test.com';
  ```
  
  ![Task3-5](./img/Task3-5.png)

- SELECT rows where name includes the <u>es</u> keyword.
  
  ```sql
  mysql> SELECT * FROM member WHERE name LIKE '%es%';
  ```
  
  ![Task3-6](./img/Task3-6.png)

- SELECT rows where email equals to test@test.com and password equals to test .
  
  ```sql
  mysql> SELECT * FROM member 
      -> WHERE email='test@test.com'
      -> AND password='test';
  ```
  
  ![Task3-7](./img/Task3-7.png)

- UPDATE data in name column to test2 where email equals to test@test.com .
  
  ```sql
  mysql> UPDATE member
      -> SET name='test2'
      -> WHERE email='test@test.com';
  ```
  
  ![Task3-8](./img/Task3-8.png)

# Task 4: SQL Aggregation Functions

# Task 5: SQL JOIN
