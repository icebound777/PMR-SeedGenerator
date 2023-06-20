from models.options.option_utility import get_option_default_value

class MysteryOptionSet():
    def __init__(self):
        self.mystery_random_choice = get_option_default_value("RandomChoice")
        self.mystery_random_pick = False
        self.mystery_itemA = get_option_default_value("ItemChoiceA")
        self.mystery_itemB = get_option_default_value("ItemChoiceB")
        self.mystery_itemC = get_option_default_value("ItemChoiceC")
        self.mystery_itemD = get_option_default_value("ItemChoiceD")
        self.mystery_itemE = get_option_default_value("ItemChoiceE")
        self.mystery_itemF = get_option_default_value("ItemChoiceF")
        self.mystery_itemG = get_option_default_value("ItemChoiceG")
