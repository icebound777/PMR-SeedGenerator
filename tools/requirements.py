from simulate import Mario


def have_map(map_name):
    mario = Mario.instance
    return map_name in mario.maps

def have_entry(map_name, entrance_number):
    mario = Mario.instance
    if map_name not in mario.maps:
        return False
    return entrance_number in mario.maps[map_name]

def have_item(item_name):
    mario = Mario.instance
    return item_name in mario.items

def have_partner(partner_name):
    mario = Mario.instance
    return partner_name in mario.partner

def have_hammer(level):
    mario = Mario.instance
    return Mario.instance.hammer >= level

def have_boots(level):
    mario = Mario.instance
    return Mario.instance.boots >= level

def have_three_letters():
    mario = Mario.instance
    count = 0
    for item_name in mario.items:
        if item_name.startswith("Letter"):
            count += 1
    if count >= 3:
        return True
    return False


def KMR_04(index):
    return [
        have_map("KMR_03"),
    ][index]

def KMR_03(index):
    return [
        have_map("KMR_04"),
        have_map("KMR_05"),
    ][index]

def KMR_05(index):
    return [
        have_map("KMR_03"),
        have_map("KMR_02"),
    ][index]

def KMR_02(index):
    return [
        have_map("KMR_09"),
        have_map("KMR_00"),
        have_map("KMR_05"),
        have_map("TIK_01"),
    ]

def KMR_09(index):
    return [
        have_map("KMR_02"),
        have_map("KMR_06"),
    ][index]

def KMR_06(index):
    return [
        have_map("KMR_09"),
        have_map("KMR_07"),
    ][index]

def KMR_07(index):
    return [
        have_map("KMR_06"),
        have_map("KMR_12"),
    ][index]

def KMR_12(index):
    return [
        have_map("KMR_07"),
        have_map("KMR_11"),
    ][index]

def KMR_11(index):
    return [
        have_map("KMR_12"),
        have_map("KMR_10"),
    ][index]

def KMR_10(index):
    return [
        have_map("KMR_11"),
        have_map("MAC_00"),
    ][index]

def MAC_00(index):
    return [
        have_map("KMR_10"),
        have_map("MAC_01"),
        True,
        have_map("TIK_19"),
        have_map("KMR_20"),
        True,
    ][index]

def MAC_01(index):
    return [
        have_map("MAC_00"),
        have_map("NOK_11"),
        have_map("OSR_01"),
        have_map("MAC_02"),
    ][index]

def MAC_02(index):
    return [
        have_map("MAC_04"),
        have_map("MIM_10"),
        have_map("MAC_01"),
        have_map("MAC_03"),
        have_map("TIK_06"),
        have_map("TIK_15"),
    ][index]

def MAC_03(index):
    return [
        have_map("MAC_02"),
        have_map("IWA_10"),
        have_map("MGM_00"),
    ][index]

def MAC_04(index):
    return [
        have_map("MAC_02"),
        have_map("MAC_05"),
        have_map("OMO_03"),
    ][index]

def MAC_05(index):
    return [
        have_map("MAC_04"),
        have_map("JAN_00"),
    ][index]
    
def TIK_01(index):
    return [
        have_map("TIK_06") and have_hammer(1),
        have_map("TIK_03") and have_hammer(1),
        have_map("TIK_01"),
        have_map("TIK_01"),
        have_map("TIK_01"),
    ][index]





