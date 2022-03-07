"""
This module is used to modify entrances / loading zones. Depending on chosen
settings it can set pre-determined paths or randomize them.
"""

def get_shorter_bowsercastle() -> list:
    """
    Returns a list of tuples representing modified entrances in Bowser's Castle
    to shorten it.
    """
    # Sets up the following connections:
    # kpa_50  (1)  <-> kpa_82  (0) (Hall to Guard Door 1 <-> Guard Door 2)
    # kpa_82  (1)  <-> kpa_32  (0) (Guard Door 2 <-> Lower Grand Hall)
    # kpa_51  (1)  <-> kpa_130 (0) (Hall to Water Puzzle <-> Bill Blaster Hall)
    # kpa_112 (1)  <-> kpa_61  (0) (Hidden Passage 1 <-> Battlement)
    # kpa_33  (2)  <-> kpa_102 (0) (Upper Grand Hall <-> Blue Fire Bridge)
    kpa_entrance_modifications = [
        (0xA3161A00, 0x161B00),
        (0xA3162701, 0x161101),
        (0xA3161600, 0x160D00),
        (0xA3161A02, 0x161B01),
        (0xA3163000, 0x162F00),
        (0xA3163101, 0x161201),
        (0xA3162700, 0x161600),
        (0xA3161B01, 0x162601),
        (0xA3161300, 0x162400),
        (0xA3161002, 0x160E02),
    ]

    return kpa_entrance_modifications
