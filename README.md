Pyodbc-CLI
==========

Very simple ODBC client shell. 

Dependencies are:
- prettytable 
- cmd
- pyodbc

Example: 

``` 
~/DEV/pyodbc-cli$ python cli.py "DSN=vertica"

(Cmd) SELECT 1 AS Number, 'abcde' AS String;

+--------+--------+
| Number | String |
+--------+--------+
|   1    | abcde  |
+--------+--------+

(Cmd) 
```
