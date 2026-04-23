from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class AddStakeScreen(Screen):
    #widgets uit de GUI definieren
    sbInput = ObjectProperty(None)
    bbInput = ObjectProperty(None)
    addStake = ObjectProperty(None)
    