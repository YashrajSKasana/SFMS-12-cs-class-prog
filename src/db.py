import mysql.connector
import getpass as gp

class DB():
  def __init__(self, host, user, password, database):
    self.tables = ["main", "AdminCred"]
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.db = self.connect()
    self.cur = self.db.cursor()

  @staticmethod
  def ask_for(info):
    info_data = {}
    for q in info:
      info_data[q] = input(f"Enter {q}: ")
    return info_data

  def save(self):
    self.db.commit()
    print("Your changes have been saved :>")

  def connect(self):
    db = mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.database
   )
    print("Connection established successfully :>")
    return db

  def get_head(self,ti):
    table = self.tables[ti]
    self.cur.execute(f"SHOW COLUMNS FROM `{table}`")
    return [col[0] for col in cur.fetchall()]

  def get_record(self, ti, pk):
    table = self.tables[ti]
    rec_ID = input(f"Enter {pk}: ")
    query = f"SELECT * FROM {table} WHERE {pk} = %s"
    self.cur.execute(query, (rec_ID,))
    record = self.cur.fetchone()
    return record

  def add_record(self):
    head = self.get_head(0)

    print()
    head_parameters = self.ask_for(head)
    values = [head_parameters[h] for h in head]

    query = f"INSERT INTO `{table}` ({', '.join(head)}) VALUES ({', '.join(['%s']*len(head))})"
    self.cur.execute(query, values)
    print("Record added successfully :>")

  def display_record(self):
    rec = self.get_record(0,"AdmissionNo")
    if rec is None:
      print(f"There is no record with primary key '{rec_ID}' :<")
    else:
      head = self.get_head(0)
      for row, col in zip(head, rec):
        print(f"{row}: {col}")

  def del_record(self):
    table = self.tables[0]
    pk = "AdmissionNo"
    rec_ID = input(f"Enter {pk}: ")

    query = f"DELETE FROM `{table}` WHERE {pk} = %s"
    self.cur.execute(query, (rec_ID,))
    print("Record deleted successfully :>")


  def change_record(self):
    rec = self.get_record(0,"AdmissionNo")
    if rec is None:
      print("Record not found :<")
      return
    head = self.get_head(0)
    pk_index = head.index(pk)
    print("Leave field empty to keep old value.")

    update_cols = []
    update_vals = []

    for i, col in enumerate(head):
      if col == pk:
        continue

      val = input(f"{col} [{rec[i]}]: ")
      if val != "":
        update_cols.append(f"`{col}`=%s")
        update_vals.append(val)

    if not update_cols:
      print("No changes made :>")
      return

    query = f"UPDATE `{table}` SET {', '.join(update_cols)} WHERE `{pk}`=%s"
    self.cur.execute(query, update_vals + [rec_ID])
    print("Record updated successfully :>")

  def authorisation(self):
    table = self.tables[1]
    admin_name = input("Admin Name: ")
    passwd = gp.getpass()

    query = f"SELECT 1 FROM `{table}` WHERE Name=%s AND Passward=%s"
    self.cur.execute(query, (admin_name, passwd))
    return self.cur.fetchone() is not None
