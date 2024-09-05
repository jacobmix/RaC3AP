from typing import Dict
from BaseClasses import MultiWorld, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from .Items import item_table, create_itempool, create_item, weapon_items, progressive_weapons, gadget_items, post_planets, progressive_armor, t_bolts
from .Locations import get_location_names, get_total_locations
from .Options import RaC3Options
from .Regions import create_regions
from .Types import WeaponType, weapon_type_to_name, RaC3Item
from .Rules import set_rules

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
                "StartingEpisode": weapon_type_to_name[WeaponType(self.options.StartingWeapon)],
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