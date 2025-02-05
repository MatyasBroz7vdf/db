import mysql.connector

def connect(_host, _port, _user, _password, _database):
  print("connect_function_activated")
  _mydb = mysql.connector.connect(
    host = _host,
    port = _port,
    user = _user,
    password = _password,
    database = _database
  )
  print(_mydb)
  return _mydb

def execute(sql, _mydb):
  print("execute_function_activated")
  cursor = _mydb.cursor(dictionary=True)
  cursor.execute(sql)

  if sql.strip().lower().startswith(("insert", "update", "delete", "alter", "set")):
        _mydb.commit()
        print("Data committed.")
  
  
  results = cursor.fetchall()
  return results

def clear(_mydb):
  print("clear_function_activated")
  execute("SET FOREIGN_KEY_CHECKS = 0;", _mydb)
  execute("DELETE FROM vendor;", _mydb)
  execute("DELETE FROM product;", _mydb)
  execute("ALTER TABLE product AUTO_INCREMENT = 1;", _mydb)
  execute("ALTER TABLE vendor AUTO_INCREMENT = 1;", _mydb)
  execute("SET FOREIGN_KEY_CHECKS = 1;", _mydb)




def close(_mydb):
  print("close_function_activated")
  _mydb.close()
  _mydb = None




