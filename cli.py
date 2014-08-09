# -*- coding: utf-8 -*-
#!/usr/bin/python
import readline
import cmd
import sys
import pyodbc
from prettytable import from_db_cursor

# global state
WAITING_EOC = 1

class ODBC_CLI(cmd.Cmd):
    def __init__(self, connection_string ):
        try:
            self.connection_string = connection_string
            self.connection = pyodbc.connect(connection_string)
        except Exception, e:
            print "Couldn't connect."
            print e
            exit(1)
        self.sql_command = ""
        cmd.Cmd.__init__(self)
        
    def do_greet(self, line):
        print "Hola"
        
    """These three functions ( quit, exit, EOF ) exit from the shell """
    def do_quit(self, line):
        return True    
    def do_exit(self, line):
        return True        
    def do_EOF(self, line):
        print "Adiós"
        return True
        
    def default(self, line):
        """The default loop sends the sql instruction to the odbc connection until it founds a line terminating in ';'.
            
        Use prettytable to display the result.
        """
    
        if line[-1] == ';':
            try:
                self.result = self.execute( self.sql_command + line )
                print from_db_cursor(self.result)
            except Exception, e:
                print e
                
            self.sql_command = ""

        else:
            self.sql_command = self.sql_command + "\n" + line
            self.status = WAITING_EOC
            
    def execute(self, sql_query):
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        return cursor

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("connection_string", help="ODBC connection string, could be \"DSN=datasourceName\", for example. ")
    args = parser.parse_args()
    ODBC_CLI(args.connection_string).cmdloop()