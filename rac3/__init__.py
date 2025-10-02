import logging
from typing import Any, Dict, Optional

from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import CollectionState, WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, SuffixIdentifier, Type

from .Items import (create_item, create_itempool, filter_item_names, gadget_items, item_table, post_planets,
                    progressive_armor, progressive_weapons, t_bolts, weapon_items)
from .Locations import get_level_locations, get_location_names, get_regions, get_total_locations, rac3_locations
from .Rac3Options import EnableWeaponLevelAsItem, GAME_TITLE_FULL, RaC3Options
from .Regions import create_regions
from .Rules import set_rules
from .Types import Multiplier, multiplier_to_name, RaC3Item, weapon_type_to_name, WeaponType

rac3_logger = logging.getLogger("RatchetAndClank3")
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
    preplaced_items: list[str] = []
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
        self.preplaced_items = []
        starting_weapons = Items.starting_weapons(self, self.options.StartingWeapons.value)
        starting_planets = ["Infobot: Florana", "Infobot: Starship Phoenix"]
        create_regions(self)
        self.get_location("Veldin: First Ranger").place_locked_item(self.create_item(starting_weapons[0]))
        self.get_location("Veldin: Second Ranger").place_locked_item(self.create_item(starting_weapons[1]))
        self.get_location("Veldin: Save Veldin").place_locked_item(self.create_item(starting_planets[0]))
        self.get_location("Florana: Defeat Qwark").place_locked_item(self.create_item(starting_planets[1]))
        self.preplaced_items.extend(starting_weapons)
        self.preplaced_items.extend(starting_planets)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "StartingWeapons": [self.preplaced_items[0], self.preplaced_items[1]],
                "BoltAndXPMultiplier": multiplier_to_name[Multiplier(self.options.BoltAndXPMultiplier)],
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

    # For Universal Tracker integration
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a regen in UT
        return slot_data

    # def post_fill(self) -> None:
    #    from Utils import visualize_regions
    #    visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.player_name}_world.puml",
    #                      regions_to_highlight=self.multiworld.get_all_state(False).reachable_regions[
    #                          self.player])
