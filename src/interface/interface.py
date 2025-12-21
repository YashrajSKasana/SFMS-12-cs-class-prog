from .menu import TerminalMenu
import os

class Interface:

  add_student = lambda self: self.db.add_record(0)
  rm_student = lambda self: self.db.del_record(0, "AdmissionNo")
  chang_student_details = lambda self: self.db.change_record(0, "AdmissionNo")
  add_admin = lambda self: self.db.add_record(1)
  rm_admin = lambda self: self.db.del_record(1, "Name")

  def __init__(self, db):
    self.db = db
    self.primary_menu_options = [
      "Quit",
      "See Your Fee Detalis",
      "Get Recipt",
      "Admin Options"
    ]
    self.admin_menu_options = [
      "Quit",
      "Add New Student",
      "Chnage Student Detalis",
      "Remove Student Detalis",
      "Add Admin",
      "Remove Admin",
      "Save Changes"
    ]
    self.option_func = {
      "see your fee detalis": self.student_detalis,
      "admin options": self.admin_menu,
      "get recipt":self.db.make_recipt,
      "add new student":self.add_student,
      "chnage student detalis":self.chang_student_details,
      "remove student detalis":self.rm_student,
      "add admin":self.add_admin,
      "remove admin":self.rm_admin,
      "save changes":self.db.save
    }

  @staticmethod
  def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = """
    +--------------------------------------------------------+
    |                                                        |
    |                                                        |
    |    █████████  ██████   ██████ ███████████  █████████   |
    |   ███░░░░░███░░██████ ██████ ░░███░░░░░░█ ███░░░░░███  |
    |  ░███    ░░░  ░███░█████░███  ░███   █ ░ ░███    ░░░   |
    |  ░░█████████  ░███░░███ ░███  ░███████   ░░█████████   |
    |   ░░░░░░░░███ ░███ ░░░  ░███  ░███░░░█    ░░░░░░░░███  |
    |   ███    ░███ ░███      ░███  ░███  ░     ███    ░███  |
    |  ░░█████████  █████     █████ █████      ░░█████████   |
    |   ░░░░░░░░░  ░░░░░     ░░░░░ ░░░░░        ░░░░░░░░░    |
    |                                                        |
    |                                                        |
    +--------------------------------------------------------+
    """

    print(logo)
    print()
    print()

  def run(self):
    primary_menu = TerminalMenu(
      self.primary_menu_options,
    )

    while True:
      self.LOGO()

      index = primary_menu.show()
      if index is None:
        continue
      elif index == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.db.save()
        break

      self.LOGO()

      option = self.primary_menu_options[index]
      func = self.option_func[option.lower()]
      func()
      input("Enter to go back: ")

  def admin_menu(self):
    is_auth = self.db.authorisation()
    if not is_auth:
      print("Authorisation faild :<")
      return
    admin_menu = TerminalMenu(
      self.admin_menu_options,
    )

    while True:
      self.LOGO()

      index = admin_menu.show()
      if index is None:
        continue
      elif index == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.db.save()
        break

      self.LOGO()

      option = self.admin_menu_options[index]
      func = self.option_func[option.lower()]
      func()
      input("Enter to go back: ")

  def student_detalis(self):
    rec = self.db.get_record(0,"AdmissionNo")
    if rec is None:
      print(f"There is no record with given Admission No :<")
    else:
      head = self.db.get_head(0)
      for row, col in zip(head, rec):
        print(f"{row}: {col}")


