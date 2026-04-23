from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class BRAmount:
    #widgets uit de GUI definieren
    amountInput = ObjectProperty(None)
    closeButton = ObjectProperty(None)
    amount = 1