from typing import Dict
from BaseClasses import MultiWorld, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from .Items import item_table, create_itempool, create_item, weapon_items, progressive_weapons, gadget_items, post_planets, progressive_armor, t_bolts, filter_item_names
from .Locations import get_location_names, get_total_locations, rac3_locations, get_level_locations
from .Options import RaC3Options
from .Regions import create_regions
from .Types import WeaponType, weapon_type_to_name, RaC3Item, multiplier_to_name, Multiplier
from .Rules import set_rules

from typing import Dict, Optional, Mapping, Any
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess
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

    game = "Ratchet and Clank 3 Up your Arsenal"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()

    item_name_groups = {
        "Progression": set(filter_item_names(ItemClassification.progression)),
        "Useful": set(filter_item_names(ItemClassification.useful)),
        "Filter": set(filter_item_names(ItemClassification.filler)),
    }
    location_name_groups =  {
        "Veldin": set(get_level_locations("Veldin")),
        "Florana": set(get_level_locations("Florana")),
        "Phoenix": set(get_level_locations("Starship Phoenix")),
        "Marcadia1": set(get_level_locations("Marcadia Region 1")),
        "Marcadia2": set(get_level_locations("Marcadia Region 2")),
        "Annihilation": set(get_level_locations("Annihilation Nation")),
        "Aquatos": set(get_level_locations("Aquatos")),
        "Tyhrranosis": set(get_level_locations("Tyhrranosis")),
        "Daxx1": set(get_level_locations("Daxx Region 1")),
        "Daxx2": set(get_level_locations("Daxx Region 2")),
        "Obani Gemini": set(get_level_locations("Obani Gemini")),
        "Rilgar": set(get_level_locations("Rilgar")),
        "Holostar": set(get_level_locations("Holostar Studios")),
        "Obani Draco": set(get_level_locations("Obani Draco")),
        "Zeldrin Starport": set(get_level_locations("Zeldrin Starport Region 2")),
        "Metropolis1": set(get_level_locations("Metropolis Region 1")),
        "Metropolis2": set(get_level_locations("Metropolis Region 2")),
        "Zeldrin": set(get_level_locations("Zeldrin")),
        "Aridia": set(get_level_locations("Aridia")),
        "Qwarks Hideout": set(get_level_locations("Qwarks Hideout")),
        "Koros": set(get_level_locations("Koros")),
        "Mylon": set(get_level_locations("Mylon")),
    }
    options_dataclass = RaC3Options
    options = RaC3Options
    web = RaC3Web()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        starting_weapon = (weapon_type_to_name[WeaponType(self.options.StartingWeapon)])
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
                "BoltandXPMultiplier": multiplier_to_name[Multiplier(self.options.BoltandXPMultiplier)]
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
