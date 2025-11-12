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

# Task 4: SQL Aggregation Functions

# Task 5: SQL JOIN
