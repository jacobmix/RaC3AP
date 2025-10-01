from BaseClasses import Item, ItemClassification

from .Types import ItemData, RaC3Item, weapon_type_to_name, WeaponType, EventData
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def create_itempool(world: "RaC3World") -> List[Item]:
    itempool: List[Item] = []
    options = world.options
    junk_dict = junk_items
    if not options.EnableWeaponLevelAsItem.value:
        junk_dict.update(junk_weapon_exp)

    for name in item_table.keys():
        item_type: ItemClassification = item_table.get(name).classification
        item_amount: int = item_table.get(name).count

        # Already placed items (Starting items and vanilla)
        if name in world.preplaced_items:
            if item_amount == 1:
                continue
            else:
                item_amount -= 1  # remove one from the pool as it has already been placed

        # WeaponLevelAsItem option
        if not options.EnableWeaponLevelAsItem.value:
            if name in progressive_weapons.keys():
                continue
        else:  # options.EnableWeaponLevelAsItem.value:
            if name in weapon_items.keys():
                continue

        # ExtraArmorUpgrade option
        if name == "Progressive Armor":
            item_amount += options.ExtraArmorUpgrade.value

        itempool += create_multiple_items(world, name, item_amount, item_type)

    victory = create_item(world, "Biobliterator Defeated!")
    world.multiworld.get_location("Command Center: Biobliterator Defeated!", world.player).place_locked_item(victory)
    itempool += create_junk_items(world, get_total_locations(world) - len(world.preplaced_items) - len(itempool) - 1,
                                  junk_dict)
    return itempool


def create_multiple_items(world: "RaC3World", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [RaC3Item(name, item_type, data.ap_code, world.player)]

    return itemlist


def create_item(world: "RaC3World", name: str) -> Item:
    data = item_table[name]
    return RaC3Item(name, data.classification, data.ap_code, world.player)


def create_junk_items(world: "RaC3World", count: int, junk_dict: Dict[str, object]) -> List[Item]:
    junk_pool: List[Item] = []
    # For now, all junk has equal weights
    for i in range(count):
        junk_pool.append(world.create_item(world.random.choices(list(junk_dict.keys()), k=1)[0]))
    return junk_pool


weapon_items = {
    "Shock Blaster": ItemData(50001400, ItemClassification.progression, 1),
    "Nitro Launcher": ItemData(50001401, ItemClassification.progression, 1),
    "N60 Storm": ItemData(50001402, ItemClassification.progression, 1),
    "Plasma Whip": ItemData(50001403, ItemClassification.progression, 1),
    "Infector": ItemData(50001404, ItemClassification.progression, 1),
    "Suck Cannon": ItemData(50001405, ItemClassification.progression, 1),
    "Spitting Hydra": ItemData(50001406, ItemClassification.progression, 1),
    "Agents of Doom": ItemData(50001407, ItemClassification.progression, 1),
    "Flux Rifle": ItemData(50001408, ItemClassification.progression, 1),
    "Annihilator": ItemData(50001409, ItemClassification.progression, 1),
    "Holo-Shield Glove": ItemData(50001410, ItemClassification.progression, 1),
    "Disk-Blade Gun": ItemData(50001411, ItemClassification.progression, 1),
    "Rift Inducer": ItemData(50001412, ItemClassification.progression, 1),
    "Qwack-O-Ray": ItemData(50001413, ItemClassification.progression, 1),
    "RY3N0": ItemData(50001414, ItemClassification.progression, 1),
    "Mini-Turret Glove": ItemData(50001415, ItemClassification.progression, 1),
    "Lava Gun": ItemData(50001416, ItemClassification.progression, 1),
    "Shield Charger": ItemData(50001417, ItemClassification.progression, 1),
    "Bouncer": ItemData(50001418, ItemClassification.progression, 1),
    "Plasma Coil": ItemData(50001419, ItemClassification.progression, 1)
}

progressive_weapons = {
    "Progressive Shock Blaster": ItemData(50001420, ItemClassification.progression, 5),
    "Progressive Nitro Launcher": ItemData(50001421, ItemClassification.progression, 5),
    "Progressive N60 Storm": ItemData(50001422, ItemClassification.progression, 5),
    "Progressive Plasma Whip": ItemData(50001423, ItemClassification.progression, 5),
    "Progressive Infector": ItemData(50001424, ItemClassification.progression, 5),
    "Progressive Suck Cannon": ItemData(50001425, ItemClassification.progression, 5),
    "Progressive Spitting Hydra": ItemData(50001426, ItemClassification.progression, 5),
    "Progressive Agents of Doom": ItemData(50001427, ItemClassification.progression, 5),
    "Progressive Flux Rifle": ItemData(50001428, ItemClassification.progression, 5),
    "Progressive Annihilator": ItemData(50001429, ItemClassification.progression, 5),
    "Progressive Holo-Shield Glove": ItemData(50001430, ItemClassification.progression, 5),
    "Progressive Disk-Blade Gun": ItemData(50001431, ItemClassification.progression, 5),
    "Progressive Rift Inducer": ItemData(50001432, ItemClassification.progression, 5),
    "Progressive Qwack-O-Ray": ItemData(50001433, ItemClassification.progression, 5),
    "Progressive RY3N0": ItemData(50001434, ItemClassification.progression, 5),
    "Progressive Mini-Turret Glove": ItemData(50001435, ItemClassification.progression, 5),
    "Progressive Lava Gun": ItemData(50001436, ItemClassification.progression, 5),
    "Progressive Shield Charger": ItemData(50001437, ItemClassification.progression, 5),
    "Progressive Bouncer": ItemData(50001438, ItemClassification.progression, 5),
    "Progressive Plasma Coil": ItemData(50001439, ItemClassification.progression, 5)
}
gadget_items = {
    "Hacker": ItemData(50001440, ItemClassification.progression, 1),
    "Hypershot": ItemData(50001441, ItemClassification.progression, 1),
    "Refractor": ItemData(50001442, ItemClassification.progression, 1),
    "Tyhrra-Guise": ItemData(50001443, ItemClassification.progression, 1),
    "Gravity-Boots": ItemData(50001444, ItemClassification.progression, 1),
    "Bolt Grabber V2": ItemData(50001445, ItemClassification.useful, 1),
    "Map-O-Matic": ItemData(50001446, ItemClassification.useful, 1),
    "Nano Pak": ItemData(50001447, ItemClassification.useful, 1),
    "Warp Pad": ItemData(50001448, ItemClassification.progression, 1),
    "Gadgetron PDA": ItemData(50001449, ItemClassification.useful, 1),
    "Charge-Boots": ItemData(50001450, ItemClassification.progression, 1),
    "Hyperstrike Smash": ItemData(50001451, ItemClassification.progression, 1)
}

post_planets = {
    "Infobot: Florana": ItemData(50001468, ItemClassification.progression, 1),
    "Infobot: Starship Phoenix": ItemData(50001469, ItemClassification.progression, 1),
    "Infobot: Marcadia": ItemData(50001452, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 1
    "Infobot: Annihilation Nation": ItemData(50001453, ItemClassification.progression, 1),
    # Post Starship Phoenix Visit 2 + Qwark Vidcomic 1
    "Infobot: Aquatos": ItemData(50001454, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 3
    "Infobot: Tyhrranosis": ItemData(50001455, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 4
    "Infobot: Daxx": ItemData(50001456, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 5
    "Infobot: Obani Gemini": ItemData(50001457, ItemClassification.progression, 1),  # Post Daxx
    "Infobot: Blackwater City": ItemData(50001458, ItemClassification.progression, 1),  # Post Obani Gemini
    "Infobot: Holostar Studios": ItemData(50001459, ItemClassification.progression, 1),
    # Post Blackwater City + Annihilation Nation Challenges
    "Infobot: Obani Draco": ItemData(50001460, ItemClassification.progression, 1),  # Post Holostar Studios
    "Infobot: Zeldrin Starport": ItemData(50001461, ItemClassification.progression, 1),  # Post Obani Draco
    "Infobot: Metropolis": ItemData(50001462, ItemClassification.progression, 1),
    # Post Zeldrin Starport + Qwark Vidcomic 4
    "Infobot: Crash Site": ItemData(50001463, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 7
    "Infobot: Aridia": ItemData(50001464, ItemClassification.progression, 1),  # Post Crash Site
    "Infobot: Qwarks Hideout": ItemData(50001465, ItemClassification.progression, 1),
    # Post Starship Phoenix Visit 8 + Qwark Vidcomic 5
    "Infobot: Koros": ItemData(50001466, ItemClassification.progression, 1),  # Post Starship Phoenix Visit 9
    "Infobot: Command Center": ItemData(50001467, ItemClassification.progression, 1),  # Post-Koros
}
progressive_vidcomics = {
    "Progressive Vidcomic": ItemData(50001475, ItemClassification.progression, 5),
}

progressive_armor = {
    "Progressive Armor": ItemData(50001480, ItemClassification.useful, 4),
}

t_bolts = {
    "Titanium Bolt": ItemData(50001490, ItemClassification.filler, 0)
}

junk_weapon_exp = {
    "Weapon EXP": ItemData(50001492, ItemClassification.filler, 0)
}

junk_items = {
    "Bolts": ItemData(50001491, ItemClassification.filler, 0),
    "Inferno Mode": ItemData(50001493, ItemClassification.filler, 0),
    "Jackpot Mode": ItemData(50001494, ItemClassification.filler, 0)
}

victory_item = {
    "Dr. Nefarious Defeated!": ItemData(50001500, ItemClassification.progression, 0),
    "Biobliterator Defeated!": ItemData(50001501, ItemClassification.progression, 0)
}

item_table = {
    **weapon_items,
    **progressive_weapons,
    **gadget_items,
    **post_planets,
    **progressive_vidcomics,
    **progressive_armor,
    **t_bolts,
    **junk_items,
    **junk_weapon_exp,
    **victory_item
}

# class ItemData(NamedTuple):
#    ap_code: Optional[int]
#    classification: ItemClassification
#    count: Optional[int] = 1

default_starting_weapons = {name: 1 for name in weapon_items.keys()}


def filter_items(classification):
    return filter(lambda l: l[1].classification == (classification), item_table.items())


def filter_item_names(classification):
    return map(lambda entry: entry[0], filter_items(classification))


def starting_weapons(world, weapon_dict: dict[str, int]) -> list[str]:
    weapon_list: list[str] = []
    for name in weapon_dict:
        count = weapon_dict[name]
        if count == 0:
            continue
        if world.options.EnableWeaponLevelAsItem.value:
            for i in range(count):
                weapon_list.append(f"Progressive {name}")
        else:
            weapon_list.append(name)
    world.random.shuffle(weapon_list)
    return [weapon_list[0], weapon_list[1]]
