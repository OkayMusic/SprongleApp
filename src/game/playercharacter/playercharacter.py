from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.core.window import Window

from kivy.app import App

from kivy.graphics import Ellipse, Color, Rectangle


class Player(Widget):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(**kwargs)
        # size_hint must always be set or kivy gets angry
        self.size_hint = None, None

        self._is_collidable = True

        # if the keyboard closes None is called, '' is the keyboard's name
        self._keyboard = Window.request_keyboard(None, self, '')

        # define the shape of the widget
        self.x = 300
        self.y = 300
        self.width = 30
        self.height = 100

        # make the player's name appear above the player
        self.PlayerName = Label()
        self.PlayerName.pos = [self.x, self.height + self.y]
        self.PlayerName.width = self.width
        self.PlayerName.height = 30
        self.add_widget(self.PlayerName)

        # these attributes are changed when keyboard buttons are pressed
        self._up = 0
        self._right = 0
        # if enter is pressed, go into typing mode
        self._typing = False

        self._velocity = [0, 0]

        with self.canvas.before:
            Color(1., 1., 1.)

        with self.canvas:
            self.body = Rectangle()
            self.body.pos = self.pos
            self.body.size = self.size

        self._keyboard.bind(on_key_up=self.keyup_listener)
        self._keyboard.bind(on_key_down=self.keydown_listener)

    def update(self, widget_list, *args):
        print self.pos

        if self._up == 1 and self._velocity[1] <= 5:
            self._velocity[1] += 1
        elif self._up == -1 and self._velocity[1] >= -5:
            self._velocity[1] -= 1
        if self._right == 1 and self._velocity[0] <= 5:
            self._velocity[0] += 1
        elif self._right == -1 and self._velocity[0] >= -5:
            self._velocity[0] -= 1

        if self._up == 0 and self._velocity[1] > 0:
            self._velocity[1] -= 1
        elif self._up == 0 and self._velocity[1] < 0:
            self._velocity[1] += 1
        if self._right == 0 and self._velocity[0] > 0:
            self._velocity[0] -= 1
        elif self._right == 0 and self._velocity[0] < 0:
            self._velocity[0] += 1

        for widgets in widget_list:
            try:
                if widgets._is_collidable == True and widgets != self:
                    if self.collide_widget(widgets) == True:
                        if widgets.top - self.y < 5 and self._velocity[1] < 0:
                            self._velocity[1] = 0
            except:
                pass

        self.pos[0] += self._velocity[0]
        self.pos[1] += self._velocity[1]

        self.body.pos = self.pos
        self.PlayerName.pos = [self.x, self.height + self.y]

    def keydown_listener(self, *args):
        print 'keydown!', args
        [keyboard, (keycode, key), unicodeStuff, modifiers] = args
        if key == 'w' or key == 'up':
            self._up = 1
        if key == 's' or key == 'down':
            self._up = -1
        if key == 'd' or key == 'right':
            self._right = 1
        if key == 'a' or key == 'left':
            self._right = -1

    def keyup_listener(self, *args):
        print 'keyup!', args
        [keyboard, (keycode, key)] = args
        if key == 'w' or key == 'up':
            self._up = 0
        if key == 's' or key == 'down':
            self._up = 0
        if key == 'd' or key == 'right':
            self._right = 0
        if key == 'a' or key == 'left':
            self._right = 0
