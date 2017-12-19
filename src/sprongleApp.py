import socket

from kivy.app import App
from loginscreen.loginscreen import LoginScreen

class SprongleApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    s = SprongleApp()
    s.run()
