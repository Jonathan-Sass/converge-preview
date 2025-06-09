import pymysql.cursors
import logging
import traceback

class MySQLConnection:
    def __init__(self, db):
        self.db_name = db
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db=self.db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
        except pymysql.MySQLError as e:
            logging.error(f"Failed to connect to database: {self.db_name}, error: {str(e)}")
            raise

    def ensure_connection(self):
        """Ensures the connection is active, otherwise reconnects."""
        try:
            self.connection.ping(reconnect=True)
        except pymysql.MySQLError as e:
            logging.error(f"Connection lost, attempting to reconnect. Error: {str(e)}")
            self.connect()

    def query_db(self, query: str, data: dict = None, many: bool=False):
        self.ensure_connection()  # Check and reconnect if needed
        with self.connection.cursor() as cursor:
            try:
                if many and isinstance(data, list):
                    cursor.executemany(query, data)
                else:
                    if isinstance(data, list) and len(data) == 1:
                        data = data[0]
                    cursor.execute(query, data)

                print("Running Query:", query)
                
                if "insert" in query.lower():
                    self.connection.commit()
                    return cursor.lastrowid
                elif "select" in query.lower():
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except pymysql.err.InterfaceError as e:
                logging.error(f"InterfaceError encountered, possibly due to a dropped connection. Query: {query}, data: {data}, error: {str(e)}")
                logging.error("Stack Trace: " + traceback.format_exc())
                self.reconnect()
                return False
            except Exception as e:
                logging.error(f"Error executing query: {query}, data: {data}, error: {str(e)}")
                logging.error("Stack Trace: " + traceback.format_exc())
                return False
            finally:
                if self.connection and self.connection.open:
                    self.connection.close()

    def reconnect(self):
        logging.info("Reconnecting to the database.")
        self.connect()

def connectToMySQL(db):
    return MySQLConnection(db)






# import pymysql.cursors
# import logging
# import traceback

# class MySQLConnection:
#     def __init__(self, db):
#         connection = pymysql.connect(host = 'localhost', 
#                                     user = 'root', 
#                                     password = 'root', 
#                                     db = db, 
#                                     charset = 'utf8mb4', 
#                                     cursorclass = pymysql.cursors.DictCursor, 
#                                     autocommit = False)
#         self.connection = connection
#     def query_db(self, query:str, data:dict=None):
#         with self.connection.cursor() as cursor:
#             try:
#                 query = cursor.mogrify(query, data)
#                 print("Running Query:", query)
#                 cursor.execute(query)
#                 if query.lower().find("insert") >= 0:
#                     self.connection.commit()
#                     return cursor.lastrowid
#                 elif query.lower().find("select") >= 0:
#                     result = cursor.fetchall()
#                     return result
#                 else:
#                     self.connection.commit()
#             except pymysql.err.InterfaceError as e:
#                 logging.error(f"InterfaceError encountered, possibly due to a dropped connection. Query: {query}, data: {data}, error: {str(e)}")
#                 logging.error("Stack Trace: " + traceback.format_exc())
#                 # Attempt to reconnect or handle the error appropriately
#                 self.reconnect()
#                 return False
#             except Exception as e:
#                 # print("Something went wrong", e)
#                 logging.error(f"Error executing query: {query}, data: {data}, error: {str(e)}")
#                 logging.error("Stack Trace: " + traceback.format_exc())
#                 return False
#             finally:
#                 if self.connection and self.connection.open:
#                     self.connection.close()

#     def reconnect(self):
#         # Logic to reconnect to the database
#         self.connection.ping(reconnect=True)


# def connectToMySQL(db):
#     return MySQLConnection(db)