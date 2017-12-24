from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.uix.widget import Widget

from kivy.app import App


class Floor(Widget):

    def __init__(self, **kwargs):
        super(Floor, self).__init__(**kwargs)
        self.size_hint = None, None
        self._is_collidable = True
        self.root = App.get_running_app().root

        self.width = self.root.width
        self.height = 30

        with self.canvas:
            Color(0, 1., 0.01)
            GroundRec = Rectangle()
            GroundRec.pos = (0, 0)
            GroundRec.size = [self.width, self.height]
