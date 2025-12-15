from simple_term_menu import TerminalMenu
import os

class Interface:
  def __init__(self, db):
    self.db = db
    self.primary_menu_options = [
      "See your fee detals",
      "Admin options"
    ]
    self.admin_menu_options = [
      "Add new student",
      "Chnage detalis",
      "Save Changes"
    ]

    self.option_func = {
      "See your fee detals": self.db.display_record,
      "Admin options": self.admin_menu,
      "Add new student":self.db.add_record,
      "Chnage detalis":self.db.change_record,
      "Save Changes":self.db.save
    }
  @staticmethod
  def LOGO():
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
      status_bar=" Press Q or Esc to quit"
    )

    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      self.LOGO()
      index = primary_menu.show()

      if index is None:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.db.save()
        break

      option = self.primary_menu_options[index]
      func = self.option_func[option]
      func()
      input("Enter to go back: ")

  def admin_menu(self):
    is_auth = self.db.authorisation()
    if not is_auth:
      print("Authorisation faild :<")
      return
    admin_menu = TerminalMenu(
      self.admin_menu_options,
      status_bar=" Press Q or Esc to quit"
    )

    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      self.LOGO()
      index = admin_menu.show()

      if index is None:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.db.save()
        break

      option = self.admin_menu_options[index]
      func = self.option_func[option]
      func()
      input("Enter to go back: ")

