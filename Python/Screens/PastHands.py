from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class PastHandsScreen(Screen):
    #widgets uit de GUI definieren
    datumInput = ObjectProperty(None)
    preflopInput = ObjectProperty(None)
    flopInput = ObjectProperty(None)
    turnInput = ObjectProperty(None)
    riverInput = ObjectProperty(None)
    results_container = ObjectProperty(None)
