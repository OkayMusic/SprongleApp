import socket

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.clock import Clock

from game.gamemain import GameMainScreen
from loginscreen.loginscreen import LoginScreen


class SprongleApp(App):

    def build(self):
        self.State = SprongleStateController(transition=NoTransition())

        # check_state is very cheap, so the state is checked very frequently
        Clock.schedule_interval(self.State.check_state, 1. / 144.)
        Clock.schedule_interval(self.State.update, 1. / 144.)

        return self.State


class SprongleStateController(ScreenManager):

    def __init__(self, **kwargs):
        super(SprongleStateController, self).__init__(**kwargs)
        # initialize the app's state to be the loginscreen state
        self.Login = LoginScreen()
        self.Login.name = 'LoginScreen'
        self.add_widget(self.Login)

    def check_state(self, *args):
        if self.current == 'LoginScreen':
            if self.Login.logged_in == True:
                self.GameScreen = GameMainScreen()
                self.GameScreen.Player.PlayerName.text = \
                    self.Login.UserDetails.Username.text
                self.GameScreen.name = 'GameScreen'
                self.add_widget(self.GameScreen)

                self.current = 'GameScreen'

    def update(self, *args):
        if self.current == 'LoginScreen':
            pass
        elif self.current == 'GameScreen':
            self.GameScreen.update()


if __name__ == '__main__':
    SprongleApp().run()
    # s.run()
