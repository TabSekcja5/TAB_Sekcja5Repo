from LoginPanel import LoginPanel
from Application import Application

class Main:
    def __init__(self):
        self.logged = False
        self.login_panel = LoginPanel(self)
        self.login_panel.mainloop()
    
    def create_main_panel(self):
        self.login_panel.destroy()
        app = Application()        
        app.mainloop()              


if __name__ == "__main__":
    main_app = Main()
