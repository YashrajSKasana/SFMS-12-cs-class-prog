class TerminalMenu:

  def __init__(self, options):
    self.options = options

  def show(self):
    for i,option in enumerate(self.options):
      print(f"({i}) {option}")
    print()
    index = input("» ")
    if index.isdigit() and int(index) in range(0,len(self.options)):
      return int(index)
    else:
      print("Invalid input please enter the the (number) in frount of sesired option.")
      input("Retry: ")
      return None

