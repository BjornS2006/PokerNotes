from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

class CardPicker(Popup):
    on_card_selected = ObjectProperty(None)

def select_card(self, card):
    if self.on_card_selected:
        self.on_card_selected(card)
    self.dismiss()