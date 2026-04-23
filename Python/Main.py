import os
from kivy.app import App
from kivy.lang import Builder
from hover.HoverWidgets import HoverButton
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen

Factory.register('HoverButton', cls=HoverButton)
# load screen KV files
Builder.load_file('GUIs/HomeScreen.kv')
Builder.load_file('GUIs/HandNoting.kv')
Builder.load_file('GUIs/PastHands.kv')
Builder.load_file('GUIs/NewStake.kv')
Builder.load_file('GUIs/HandDetails.kv')

# load popup KV files
Builder.load_file('GUIs/CardPicker.kv')
Builder.load_file('GUIs/BRAmount.kv')

# register Python popup/controller classes with the Factory so Factory.CardPicker() creates our class
from Python.Screens.CardPicker import CardPicker
Factory.register('CardPicker', cls=CardPicker)
Factory.register('BRAmount', cls=BRAmount)

class HomeScreen(Screen): pass
class HandNotingScreen(Screen): pass
class PastHandsScreen(Screen): pass
class AddStakeScreen(Screen): pass
class HandDetailsScreen(Screen): pass

class PokerNotesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(HandNotingScreen(name='hand_noting'))
        sm.add_widget(PastHandsScreen(name='past_hands'))
        sm.add_widget(HandDetailsScreen(name='hand_details'))
        sm.add_widget(AddStakeScreen(name='add_stake'))
        return sm

if __name__ == '__main__':
    PokerNotesApp().run()