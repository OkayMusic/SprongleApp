from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.focus import FocusBehavior


class FocusTextInput(TextInput, FocusBehavior):
    pass

class UserDetailsGrid(GridLayout):
    def __init__(self, **kwargs):
        super(UserDetailsGrid, self).__init__(**kwargs)
        self.cols = 2

        self.UsernameLabel = Label(text='Username:')
        self.add_widget(self.UsernameLabel)
        self.Username = FocusTextInput(multiline=False, write_tab=False)
        self.add_widget(self.Username)

        self.PasswordLabel = Label(text='Password')
        self.add_widget(self.PasswordLabel)
        self.Password = FocusTextInput(password=True, multiline=False,
                                       write_tab=False)
        self.add_widget(self.Password)

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        self.UserDetails = UserDetailsGrid()
        self.UserDetails.size_hint = [1.5, 1.5]
        self.add_widget(self.UserDetails)
        self.UserDetails.Password.bind(on_text_validate=self.on_login)
        self.UserDetails.Username.bind(on_text_validate=self.on_login)

        self.LoginButton = Button(text='Login')
        self.add_widget(self.LoginButton)
        self.LoginButton.bind(on_press=self.on_login)

        self.AccountCreationButton = Button(text='Create account')
        self.add_widget(self.AccountCreationButton)
        self.AccountCreationButton.bind(on_press=self.on_create_account)

    def on_login(self, *args):
        print self.UserDetails.Username.text, self.UserDetails.Password.text
        self.login_success()

    def on_create_account(self, *args):
        self.remove_widget(self.LoginButton)
        self.remove_widget(self.AccountCreationButton)

        self.UserDetails.PasswordLabel.text = \
        '''Enter your password:\nMake it secure!'''

        self.ReEnterPasswordLabel = Label(text='Please re-enter your password:')
        self.UserDetails.add_widget(self.ReEnterPasswordLabel)

        self.ReEnterPassword = FocusTextInput(password=True, multiline=False,
                                              write_tab=False)
        self.UserDetails.add_widget(self.ReEnterPassword)

        self.CreateAccountButton = Button(text='Create account')
        self.add_widget(self.CreateAccountButton)

    def login_success(self):
        for child in self.children:
            self.remove_widget(child)
        return SprongleGame()
