from environment.floor import Floor
from playercharacter.playercharacter import Player
from kivy.uix.screenmanager import Screen


# the class which contains everything which will be displayed
# update method should include all relevent client side logic
# update method should also include animation calls etc.


class GameMainScreen(Screen):

    def __init__(self, **kwargs):
        super(GameMainScreen, self).__init__(**kwargs)

        self.FloorWidget = Floor()
        self.add_widget(self.FloorWidget)

        self.Player = Player()
        self.add_widget(self.Player)

    def update(self, *args):

        for kids in self.children:
            try:
                kids.update(self.children)
            except:
                pass
