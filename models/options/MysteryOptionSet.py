from models.options.option_utility import get_option_keyvalue_dict

class MysteryOptionSet():
    def __init__(self):
        self.mystery_random_choice = get_option_keyvalue_dict("RandomChoice")
        self.mystery_random_pick = False
        self.mystery_itemA = get_option_keyvalue_dict("ItemChoiceA")
        self.mystery_itemB = get_option_keyvalue_dict("ItemChoiceB")
        self.mystery_itemC = get_option_keyvalue_dict("ItemChoiceC")
        self.mystery_itemD = get_option_keyvalue_dict("ItemChoiceD")
        self.mystery_itemE = get_option_keyvalue_dict("ItemChoiceE")
        self.mystery_itemF = get_option_keyvalue_dict("ItemChoiceF")
        self.mystery_itemG = get_option_keyvalue_dict("ItemChoiceG")
