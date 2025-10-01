import logging
from typing import Dict
from BaseClasses import MultiWorld, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from .Items import (item_table, create_itempool, create_item, weapon_items, progressive_weapons, gadget_items,
                    post_planets, progressive_armor, t_bolts, filter_item_names)
from .Locations import get_location_names, get_total_locations, rac3_locations, get_level_locations, get_regions
from .Rac3Options import EnableWeaponLevelAsItem, RaC3Options, GAME_TITLE_FULL
from .Regions import create_regions
from .Types import WeaponType, weapon_type_to_name, RaC3Item, multiplier_to_name, Multiplier
from .Rules import set_rules

from typing import Dict, Optional, Mapping, Any
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess

rac3_logger = logging.getLogger("Ratchet & Clank 3")
rac3_logger.setLevel(logging.DEBUG)


def run_client(_url: Optional[str] = None):
    from .Rac3Client import launch_client
    launch_subprocess(launch_client, name="Rac3Client")


components.append(
    Component("Ratchet & Clank 3 Client", func=run_client, component_type=Type.CLIENT,
              file_identifier=SuffixIdentifier(".aprac3"))
)


class RaC3Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Ratchet and Clank 3: Up Your Arsenal for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Bread"]
    )]


class RaC3World(World):
    """
    Ratchet and Clank 3 is a third person action shooter.
    Blast your enemies with over the top weaponry and save the galaxy from total disaster.
    """

    game = GAME_TITLE_FULL
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    # Config for Universal Tracker
    ut_can_gen_without_yaml = False
    disable_ut = False

    location_name_groups = {}
    for region in get_regions():
        location_name_groups[region] = set(get_level_locations(region))

    options_dataclass = RaC3Options
    options = RaC3Options
    web = RaC3Web()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        rac3_logger.warning(
            "INCOMPLETE WORLD! Slot '%s' is using an unfinished alpha world that is not stable yet!",
            self.player_name)
        rac3_logger.warning("INCOMPLETE WORLD! Slot '%s' may require send_location/send_item for completion!",
                            self.player_name)
        starting_weapon = (weapon_type_to_name[WeaponType(self.options.StartingWeapon.value)])
        if self.options.EnableWeaponLevelAsItem.value == EnableWeaponLevelAsItem.option_enable:
            starting_weapon = f"Progressive {starting_weapon}"
        self.multiworld.push_precollected(self.create_item(starting_weapon))

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "StartingWeapon": weapon_type_to_name[WeaponType(self.options.StartingWeapon)],
                "BoltandXPMultiplier": multiplier_to_name[Multiplier(self.options.BoltandXPMultiplier)],
                "EnableWeaponLevelAsItem": self.options.EnableWeaponLevelAsItem.value,
                "ExtraArmorUpgrade": self.options.ExtraArmorUpgrade.value,
            },
            "Seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "Slot": self.multiworld.player_name[self.player],  # to connect to server
            "TotalLocations": get_total_locations(self)
        }

        return slot_data

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)

    # For Univesal Tracker integration
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data

    # def post_fill(self) -> None:
    #    from Utils import visualize_regions
    #    visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.player_name}_world.puml",
    #                      regions_to_highlight=self.multiworld.get_all_state(False).reachable_regions[
    #                          self.player])
