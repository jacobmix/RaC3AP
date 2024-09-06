from .Types import LocData, WeaponType
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def get_total_locations(world: "RaC3World") -> int:
    total = 0
    for name in location_table:
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}
    return names


rac3_locations = {

    #----- Planet Veldin -----#
    "Received Shock Cannon": LocData(50001000, "Veldin"),
    "Received Nitro Launcher": LocData(50001001, "Veldin"),
    "Infobot: Florana": LocData(50001003, "Veldin"),

    #----- Planet Florana -----#
    "Received Plasma Whip": LocData(50001004, "Florana"),
    "Received N60 Storm": LocData(50001005, "Florana"),
    "T-Bolt: Below Gadgetron Vendor": LocData(50001006, "Florana"),
    "T-Bolt: Path of Death": LocData(50001007, "Florana"),
    "Infobot: Starship Phoenix": LocData(50001008, "Florana"),

    #----- Starship Phoenix -----#
    "Received SUCC Cannon": LocData(50001009, "Starship Phoenix"),
    "Received Infector": LocData(50001010, "Starship Phoenix"),
    "T-Bolt: All VR Deck Challenges": LocData(50001011, "Starship Phoenix"),
    "T-Bolt: Complete VR Training": LocData(50001012, "Starship Phoenix"),
    "Received Magna Plate Armor":LocData(50001013, "Starship Phoenix"),
    "Received Adamantine Armor": LocData(50001014, "Starship Phoenix"),
    "Received Aegis Mark V Armor": LocData(50001015, "Starship Phoenix"),
    "Received Infernox Armor": LocData(50001016, "Starship Phoenix"),
    "Received Hacker": LocData(50001017, "Starship Phoenix"),
    "Received Hypershot": LocData(50001018, "Starship Phoenix"),
    "Infobot: Marcadia": LocData(50001019, "Starship Phoenix"),
    "Infobot: Koros": LocData(50001020, "Starship Phoenix"),
    "Infobot: Annihilation Nation": LocData(50001021, "Starship Phoenix"),
    "Infobot: Aquatos": LocData(50001022, "Starship Phoenix"),

    #----- Planet Marcadia -----#
    "Received Spitting Hydra": LocData(50001030, "Marcadia"),
    "Received Refractor": LocData(50001031, "Marcadia"),
    "T-Bolt: After Pool of Water": LocData(50001032, "Marcadia"),
    "T-Bolt: Last Refractor Room": LocData(50001033, "Marcadia"),
    "T-Bolt: Ceiling just before Al": LocData(50001034, "Marcadia"),
    "Qwark Vidcomic 1": LocData(50001035, "Marcadia"),

    #----- Annihilation Nation -----#
    "Received Agents of Doom": LocData(50001040, "Annihilation Nation"),
    "Received Tyhrra-Guise": LocData(50001041, "Annihilation Nation"),
    "T-Bolt: Heat Street": LocData(50001042, "Annihilation Nation"),
    "T-Bolt: Maze of Blaze": LocData(50001043, "Annihilation Nation"),
    "Grand Prize Bout": LocData(50001044, "Annihilation Nation"),
    "The Terrible Two": LocData(50001045, "Annihilation Nation"),
    "Robot Rampage": LocData(50001046, "Annihilation Nation"),
    "Two Minute Warning": LocData(50001047, "Annihilation Nation"),
    "90 Seconds of Carnage": LocData(50001048, "Annihilation Nation"),
    "Onslaught": LocData(50001049, "Annihilation Nation"),
    "Whip it Good": LocData(50001050, "Annihilation Nation"),
    "Hydra'n Seek": LocData(50001051, "Annihilation Nation"),
    "Championship Bout": LocData(50001052, "Annihilation Nation"),
    "Meet Courtney - Arena": LocData(50001053, "Annihilation Nation"),
    "Ninja Challenge": LocData(50001054, "Annihilation Nation"),
    "Counting Ducks": LocData(50001055, "Annihilation Nation"),
    "Cycling Weapons": LocData(50001056, "Annihilation Nation"),
    "One Hit Wonder": LocData(50001057, "Annihilation Nation"),
    "Time to Suck": LocData(50001058, "Annihilation Nation"),
    "Naptime": LocData(50001059, "Annihilation Nation"),
    "More Cycling Weapons": LocData(50001060, "Annihilation Nation"),
    "Dodge the Twins": LocData(50001061, "Annihilation Nation"),
    "Chop Chop": LocData(50001062, "Annihilation Nation"),
    "Sleep Inducer": LocData(50001063, "Annihilation Nation"),
    "The Other White Meat": LocData(50001064, "Annihilation Nation"),
    "Championship Bout II": LocData(50001065, "Annihilation Nation"),
    "Qwarktastic Battle": LocData(50001066, "Annihilation Nation"),

    #----- Planet Aquatos -----#
    "Received Flux Rifle": LocData(50001090, "Aquatos"),
    "T-Bolt: Under the Bridge": LocData(50001091, "Aquatos"),
    "T-Bolt: Underwater Bolt": LocData(50001092, "Aquatos"),
    "T-Bolt: Behind the Locked Gate": LocData(50001093, "Aquatos"),
    "T-Bolt: Top Left Bolt": LocData(50001094, "Aquatos"),
    "T-Bolt: Swinging Bolt": LocData(50001095, "Aquatos"),
    "1 Sewer Crystal Traded": LocData(50001096, "Aquatos"),
    "5 Sewer Crystals Traded": LocData(50001097, "Aquatos"),
    "10 Sewer Crystals Traded": LocData(50001098, "Aquatos"),
    "20 Sewer Crystals Traded": LocData(50001099, "Aquatos"),
    "Post-Aquatos": LocData(50001100, "Aquatos"),

    #----- Planet Tyhrranosis -----#
    "Received Annihilator": LocData(50001300, "Tyhrranosis"),
    "Received Holo-Shield Glove": LocData(50001301, "Tyhrranosis"),
    "T-Bolt: South East Cannon": LocData(50001302, "Tyhrranosis"),
    "T-Bolt: Underground Cave Bolt": LocData(50001303, "Tyhrranosis"),
    "Post-Tyhrranosis": LocData(50001304, "Tyhrranosis"),

    #----- Planet Daxx -----#
    "T-Bolt: Right of the Taxi": LocData(50001320, "Daxx"),
    "T-Bolt: Time Sensitive Door": LocData(50001321, "Daxx"),
    "Received Charge Boots": LocData(50001322, "Daxx"),
    "Post-Daxx 1": LocData(50001323, "Daxx"),
    "Post-Daxx 2": LocData(50001324, "Daxx"),

    #----- Obani Gemini -----#
    "Received Disk Blade Gun": LocData(50001340, "Obani Gemini"),
    "T-Bolt: Follow the Lava": LocData(50001341, "Obani Gemini"),
    "T-Bolt: Between the Twin Towers": LocData(50001342, "Obani Gemini"),
    "Post-Obani Gemini": LocData(50001343, "Obani Gemini"),

    #----- Planet Rilgar -----#
    "Received Grav Boots": LocData(50001360, "Rilgar"),
    "Post-Rilgar": LocData(50001361, "Rilgar"),

    #----- Obani Draco (lol) -----#
    "Post-Obani Draco": LocData(50001370, "Obani Draco"),

    #----- Holostar Studios -----#
    "Received Rift Inducer": LocData(50001390, "Holostar Studios"),
    "T-Bolt: Atop the Chairs": LocData(50001391, "Holostar Studios"),
    "T-Bolt: Lot 42's Grav Ramp": LocData(50001392, "Holostar Studios"),
    "T-Bolt: Kamikaze Noids": LocData(50001393, "Holostar Studios"),
    "Post-Holostar Studios": LocData(50001394, "Holostar Studios"),

    #----- Zeldrin Starport -----#
    "Received Bolt Grabber V2": LocData(50001410, "Zeldrin Starport"),
    "T-Bolt: Inside the Second Ship": LocData(50001411, "Zeldrin Starport"),
    "T-Bolt: Atop the Twin Shooters": LocData(50001412, "Zeldrin Starport"),
    "Post-Zeldrin Starport": LocData(50001413, "Zeldrin Starport"),

    #----- Planet Metropolis -----#
    "Received Map-O-Matic": LocData(50001430, "Metropolis"),
    "T-Bolt: Across the Gap": LocData(50001431, "Metropolis"),
    "T-Bolt: Right of the Balcony": LocData(50001432, "Metropolis"),
    "T-Bolt: Tall Tower (Hovership)": LocData(50001433, "Metropolis"),
    "Metal-Noids": LocData(50001434, "Metropolis"),
    "Post-Metropolis": LocData(50001435, "Metropolis"),

    #----- Planet Zeldrin -----#
    "Received Nano-Pak": LocData(50001450, "Zeldrin"),
    "T-Bolt: Turn Around": LocData(50001451, "Zeldrin"),
    "Post-Zeldrin": LocData(50001452, "Zeldrin"),

    #----- Planet Aridia -----#
    "Received Warp Pad": LocData(50001470, "Aridia"),
    "Received Qwack-O-Ray": LocData(50001471, "Aridia"),
    "T-Bolt: Under the Bridge (Assassionation)": LocData(50001472, "Aridia"),
    "T-Bolt: Behind the Base (X12 Endgame)": LocData(50001473, "Aridia"),
    "Post-Aridia": LocData(50001474, "Aridia"),

    #----- Qwark's Hideout -----#
    "Received Gadgetron PDU": LocData(50001490, "Qwarks Hideout"),
    "T-Bolt: Glide from the Ramp": LocData(50001491, "Qwarks Hideout"),
    "Post-Qwarks Hideout": LocData(50001492, "Qwarks Hideout"),

    #----- Planet Koros -----#
    "T-Bolt: Behind the Metal Fence": LocData(50001493, "Koros"),
    "T-Bolt: Pair of Towers": LocData(50001494, "Koros"),
    "Post-Koros": LocData(50001495, "Koros"),

    #----- Planet Mylon -----#
    "T-Bolt: Behind the Forcefield": LocData(50001496, "Mylon"),
    "Dr. Nefarious Defeated!": LocData(50001497, "Mylon")
}

weapon_upgrades = {

    "Shock Blaster: V2": LocData(50001500, "Shock Blaster Upgrades"),
    "Shock Blaster: V3": LocData(50001501, "Shock Blaster Upgrades"),
    "Shock Blaster: V4": LocData(50001502, "Shock Blaster Upgrades"),
    "Shock Blaster: V5": LocData(50001503, "Shock Blaster Upgrades"),

    "Nitro Launcher: V2": LocData(50001504, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V3": LocData(50001505, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V4": LocData(50001506, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V5": LocData(50001507, "Nitro Launcher Upgrades"),

    "N60 Storm: V2": LocData(50001508, "N60 Storm Upgrades"),
    "N60 Storm: V3": LocData(50001509, "N60 Storm Upgrades"),
    "N60 Storm: V4": LocData(50001510, "N60 Storm Upgrades"),
    "N60 Storm: V5": LocData(50001511, "N60 Storm Upgrades"),

    "Plasma Whip: V2": LocData(50001512, "Plasma Whip Upgrades"),
    "Plasma Whip: V3": LocData(50001513, "Plasma Whip Upgrades"),
    "Plasma Whip: V4": LocData(50001514, "Plasma Whip Upgrades"),
    "Plasma Whip: V5": LocData(50001515, "Plasma Whip Upgrades"),

    "Infector: V2": LocData(50001516, "Infector Upgrades"),
    "Infector: V3": LocData(50001517, "Infector Upgrades"),
    "Infector: V4": LocData(50001518, "Infector Upgrades"),
    "Infector: V5": LocData(50001519, "Infector Upgrades"),

    "Suck Cannon: V2": LocData(50001520, "Suck Cannon Upgrades"),
    "Suck Cannon: V3": LocData(50001521, "Suck Cannon Upgrades"),
    "Suck Cannon: V4": LocData(50001522, "Suck Cannon Upgrades"),
    "Suck Cannon: V5": LocData(50001523, "Suck Cannon Upgrades"),

    "Spitting Hydra: V2": LocData(50001524, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V3": LocData(50001525, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V4": LocData(50001526, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V5": LocData(50001527, "Spitting Hydra Upgrades"),

    "Agents of Doom: V2": LocData(50001528, "Agents of Doom Upgrades"),
    "Agents of Doom: V3": LocData(50001529, "Agents of Doom Upgrades"),
    "Agents of Doom: V4": LocData(50001530, "Agents of Doom Upgrades"),
    "Agents of Doom: V5": LocData(50001531, "Agents of Doom Upgrades"),

    "Flux Rifle: V2": LocData(50001532, "Flux Rifle Upgrades"),
    "Flux Rifle: V3": LocData(50001533, "Flux Rifle Upgrades"),
    "Flux Rifle: V4": LocData(50001534, "Flux Rifle Upgrades"),
    "Flux Rifle: V5": LocData(50001535, "Flux Rifle Upgrades"),

    "Annihilator: V2": LocData(50001536, "Annihilator Upgrades"),
    "Annihilator: V3": LocData(50001537, "Annihilator Upgrades"),
    "Annihilator: V4": LocData(50001538, "Annihilator Upgrades"),
    "Annihilator: V5": LocData(50001539, "Annihilator Upgrades"),

    "Holo-Shield Glove: V2": LocData(50001540, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V3": LocData(50001541, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V4": LocData(50001542, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V5": LocData(50001543, "Holo-Shield Glove Upgrades"),

    "Disk-Blade Gun: V2": LocData(50001544, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V3": LocData(50001545, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V4": LocData(50001546, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V5": LocData(50001547, "Disk-Blade Gun Upgrades"),

    "Rift Inducer: V2": LocData(50001548, "Rift Inducer Upgrades"),
    "Rift Inducer: V3": LocData(50001549, "Rift Inducer Upgrades"),
    "Rift Inducer: V4": LocData(50001550, "Rift Inducer Upgrades"),
    "Rift Inducer: V5": LocData(50001551, "Rift Inducer Upgrades"),

    "Qwack-O-Ray: V2": LocData(50001552, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V3": LocData(50001553, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V4": LocData(50001554, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V5": LocData(50001555, "Qwack-O-Ray Upgrades"),

    "RY3N0: V2": LocData(50001556, "RY3N0 Upgrades"),
    "RY3N0: V3": LocData(50001557, "RY3N0 Upgrades"),
    "RY3N0: V4": LocData(50001558, "RY3N0 Upgrades"),
    "RY3N0: V5": LocData(50001559, "RY3N0 Upgrades"),

    "Mega-Turret Glove: V2": LocData(50001560, "Mega-Turret Glove Upgrades"),
    "Mega-Turret Glove: V3": LocData(50001561, "Mega-Turret Glove Upgrades"),
    "Mega-Turret Glove: V4": LocData(50001562, "Mega-Turret Glove Upgrades"),
    "Mega-Turret Glove: V5": LocData(50001563, "Mega-Turret Glove Upgrades"),

    "Lava Gun: V2": LocData(50001564, "Lava Gun Upgrades"),
    "Lava Gun: V3": LocData(50001565, "Lava Gun Upgrades"),
    "Lava Gun: V4": LocData(50001566, "Lava Gun Upgrades"),
    "Lava Gun: V5": LocData(50001567, "Lava Gun Upgrades"),

    "Tesla Barrier: V2": LocData(50001568, "Tesla Barrier Upgrades"),
    "Tesla Barrier: V3": LocData(50001569, "Tesla Barrier Upgrades"),
    "Tesla Barrier: V4": LocData(50001570, "Tesla Barrier Upgrades"),
    "Tesla Barrier: V5": LocData(50001571, "Tesla Barrier Upgrades"),

    "Bouncer: V2": LocData(50001572, "Bouncer Upgrades"),
    "Bouncer: V3": LocData(50001573, "Bouncer Upgrades"),
    "Bouncer: V4": LocData(50001574, "Bouncer Upgrades"),
    "Bouncer: V5": LocData(50001575, "Bouncer Upgrades"),

    "Plasma Coil: V2": LocData(50001576, "Plasma Coil Upgrades"),
    "Plasma Coil: V3": LocData(50001577, "Plasma Coil Upgrades"),
    "Plasma Coil: V4": LocData(50001578, "Plasma Coil Upgrades"),
    "Plasma Coil: V5": LocData(50001579, "Plasma Coil Upgrades"),

}

location_table = {
    **rac3_locations,
    **weapon_upgrades
}