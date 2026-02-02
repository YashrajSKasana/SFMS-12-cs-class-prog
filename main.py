import os.path as path
import json
from src.interface.interface import Interface
from src.db import DB
from  datetime import datetime as dt
CONNECTION_INFO_FILE = r"./info_files/connection.json"
EXCEPTIONS_LOG_DIR = r"./info_files/logs/"
def get_connetion_cred():
  with open(CONNECTION_INFO_FILE) as f:
    crad = json.load(f)
    return crad

def log_exception(exception):
  exception = str(exception)
  time = dt.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
  file_name = rf"{EXCEPTIONS_LOG_DIR}{time}.txt"
  with open(file_name, 'w') as f:
    f.write(exception)

def new_connection():
  crad = {}
  crad['host'] = input("Enter Host: ")
  crad['user'] = input("Entr Usre: ")
  crad['password'] = input("Enter password: ")
  crad['database'] = input("Enter Database: ")

  with open(CONNECTION_INFO_FILE, 'w') as f:
    json.dump(crad, f)

def main():
  if not path.exists(CONNECTION_INFO_FILE):
    new_connection()

  connection_cred = get_connetion_cred()
  db = DB(**connection_cred)
  ui = Interface(db)
  ui.run()

if __name__ == "__main__":
  while True:
    try:
      main()
    except Exception as e:
      log_exception(e)
      print("an exception occured please try again :<")
      input("Retry: ")
      continue
    break
