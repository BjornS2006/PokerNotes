from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class CardPicker(Popup):
    on_card_selected = ObjectProperty(None)

    # Diamonds (Ruiten)
    diam_A = ObjectProperty(None)
    diam_K = ObjectProperty(None)
    diam_Q = ObjectProperty(None)
    diam_J = ObjectProperty(None)
    diam_T = ObjectProperty(None)
    diam_9 = ObjectProperty(None)
    diam_8 = ObjectProperty(None)
    diam_7 = ObjectProperty(None)
    diam_6 = ObjectProperty(None)
    diam_5 = ObjectProperty(None)
    diam_4 = ObjectProperty(None)
    diam_3 = ObjectProperty(None)
    diam_2 = ObjectProperty(None)

    # Spades (Schoppen)
    spad_A = ObjectProperty(None)
    spad_K = ObjectProperty(None)
    spad_Q = ObjectProperty(None)
    spad_J = ObjectProperty(None)
    spad_T = ObjectProperty(None)
    spad_9 = ObjectProperty(None)
    spad_8 = ObjectProperty(None)
    spad_7 = ObjectProperty(None)
    spad_6 = ObjectProperty(None)
    spad_5 = ObjectProperty(None)
    spad_4 = ObjectProperty(None)
    spad_3 = ObjectProperty(None)
    spad_2 = ObjectProperty(None)

    # Hearts (Harten)
    heart_A = ObjectProperty(None)
    heart_K = ObjectProperty(None)
    heart_Q = ObjectProperty(None)
    heart_J = ObjectProperty(None)
    heart_T = ObjectProperty(None)
    heart_9 = ObjectProperty(None)
    heart_8 = ObjectProperty(None)
    heart_7 = ObjectProperty(None)
    heart_6 = ObjectProperty(None)
    heart_5 = ObjectProperty(None)
    heart_4 = ObjectProperty(None)
    heart_3 = ObjectProperty(None)
    heart_2 = ObjectProperty(None)

    # Clubs (Klaveren)
    club_A = ObjectProperty(None)
    club_K = ObjectProperty(None)
    club_Q = ObjectProperty(None)
    club_J = ObjectProperty(None)
    club_T = ObjectProperty(None)
    club_9 = ObjectProperty(None)
    club_8 = ObjectProperty(None)
    club_7 = ObjectProperty(None)
    club_6 = ObjectProperty(None)
    club_5 = ObjectProperty(None)
    club_4 = ObjectProperty(None)
    club_3 = ObjectProperty(None)
    club_2 = ObjectProperty(None)

    # Close button
    close_btn = ObjectProperty(None)

    def select_card(self, card):
        if self.on_card_selected:
            self.on_card_selected(card)
        self.dismiss()