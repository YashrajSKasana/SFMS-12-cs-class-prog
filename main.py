import os.path as path
import json
from interface.interface import Interface
from db.db import DB
CONNECTION_INFO_FILE = r"./info_files/connection.json"
def get_connetion_cred():
  with open(CONNECTION_INFO_FILE) as f:
    crad = json.load(f)
    return crad
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
  main()
