pyodbc-cli
==========

Very simple ODBC client shell. 

Dependencies are:
- prettytable 
- cmd
- pyodbc

Example: 

``` 
~/DEV/pyodbc-cli$ python cli.py "DSN=database; user=admin; password=12345"

(Cmd) SELECT 1 AS Number, 'abcde' AS String;

+--------+--------+
| Number | String |
+--------+--------+
|   1    | abcde  |
+--------+--------+

(Cmd) 
```

Main motivation to do this tiny odbc client is that unixodbc's isql sucks. It couldn't even parse a SQL script with comments and multiline SQL queries. Since pyodbc takes care of that, this script can handle common SQL scripts with comments and multiline queries. Just use it like this: 

```
cat script.sql | python cli.py "DSN=database; user=admin; password=12345"
```
