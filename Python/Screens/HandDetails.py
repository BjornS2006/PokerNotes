from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class HandDetailsScreen(Screen):
    #widgets uit de GUI definieren
    hPosLabel = ObjectProperty(None)
    preflopActionLabel = ObjectProperty(None)
    flopActionLabel = ObjectProperty(None)
    turnActionLabel = ObjectProperty(None)
    riverActionLabel = ObjectProperty(None)
    notesLabel = ObjectProperty(None)