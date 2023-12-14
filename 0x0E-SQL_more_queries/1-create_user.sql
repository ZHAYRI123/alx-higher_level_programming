-- Creates the MySQL server user user_0d_1
CREATE USER IF NOT EISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . *TO user_0d_1@localhost;
