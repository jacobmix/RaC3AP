from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, DefaultOnToggle, ItemDict, StartInventoryPool

from .Items import default_starting_weapons

# Common variable
GAME_TITLE = "Rac3"
GAME_TITLE_FULL = "Ratchet & Clank 3"


def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in rac3_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list


class StartingWeapons(ItemDict):
    """
    Determines which weapons you will be starting the game with, provide a count of the weapons you want to be picked
    between, 2 are selected to be placed on Veldin.
    """
    display_name = "Starting Weapons"
    min = 0
    max = 5
    default = default_starting_weapons
    valid_keys = default_starting_weapons.keys()


class BoltAndXPMultiplier(Choice):
    """
    Determines what your bolts and xp will be multiplied by, recommended to go with x6 if you hate grinding,
    x10 if you're looking to do a sync
    """
    display_name = "BoltAndXPMultiplier"
    option_x1 = 1
    option_x2 = 2
    option_x4 = 3
    option_x6 = 4
    option_x8 = 5
    option_x10 = 6
    default = 1


class EnableWeaponLevelAsItem(Choice):
    """
    Determines weapon level is unlocked items or not.
    """
    display_name = "EnableWeaponLevelAsItem"
    option_disable = 0
    option_enable = 1
    default = 0


class ExtraArmorUpgrade(Choice):
    """
    Determines Which extra number of ArmorUpgrade items contains in itempool. 1~2 is recommended.
    """
    display_name = "ExtraArmorUpgrade"
    option_no_extra = 0
    option_extra_1 = 1
    option_extra_2 = 2
    option_extra_3 = 3
    option_extra_4 = 4
    default = 0


@dataclass
class RaC3Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    starting_weapons: StartingWeapons
    bolt_and_xp_multiplier: BoltAndXPMultiplier
    enable_weapon_level_as_item: EnableWeaponLevelAsItem
    extra_armor_upgrade: ExtraArmorUpgrade


rac3_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartInventoryPool, StartingWeapons, BoltAndXPMultiplier, EnableWeaponLevelAsItem,
                        ExtraArmorUpgrade]
}

slot_data_options: list[str] = [
    "StartInventoryFromPool"
    "BoltAndXPMultiplier",
    "StartingWeapons",
    "EnableWeaponLevelAsItem",
    "ExtraArmorUpgrade",
]
