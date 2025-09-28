from .Types import LocData, WeaponType
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def get_total_locations(world: "RaC3World") -> int:
    locations = [ l for l in world.multiworld.get_locations() if l.player == world.player ]
    return len(locations)

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}
    return names

def get_regions() -> list:
    regions = [data.region for _, data in location_table.items()]
    return regions

rac3_locations = {
    #----- Planet Veldin -----#
    "Veldin: Received Shock Cannon": LocData(50001000, "Veldin"),
    "Veldin: Received Nitro Launcher": LocData(50001001, "Veldin"),
    "Veldin: Infobot: Florana": LocData(50001003, "Veldin"),

    #----- Planet Florana -----#
    "Florana: Received Plasma Whip": LocData(50001004, "Florana"),
    "Florana: Received N60 Storm": LocData(50001005, "Florana"),
    "Florana: T-Bolt: Below Gadgetron Vendor": LocData(50001006, "Florana"),
    "Florana: T-Bolt: Path of Death": LocData(50001007, "Florana"),
    "Florana: Infobot: Starship Phoenix": LocData(50001008, "Florana"),
    "Florana: Stay Squaky Clean": LocData(50001610, "Florana"),

    #----- Starship Phoenix -----#
    "Phoenix: Received SUCC Cannon": LocData(50001009, "Starship Phoenix"),
    "Phoenix: Received Infector": LocData(50001010, "Starship Phoenix"),
    "Phoenix: T-Bolt: Last VR Deck Challenges": LocData(50001011, "Starship Phoenix"),
    "Phoenix: T-Bolt: Complete VR Training": LocData(50001012, "Starship Phoenix"),
    "Phoenix: Received Magna Plate Armor":LocData(50001013, "Starship Phoenix"),
    "Phoenix: Received Adamantine Armor": LocData(50001014, "Starship Phoenix"),
    "Phoenix: Received Aegis Mark V Armor": LocData(50001015, "Starship Phoenix"),
    "Phoenix: Received Infernox Armor": LocData(50001016, "Starship Phoenix"),
    "Phoenix: Received Hacker": LocData(50001017, "Starship Phoenix"),
    "Phoenix: Received Hypershot": LocData(50001018, "Starship Phoenix"),
    "Phoenix: Infobot: Marcadia": LocData(50001019, "Starship Phoenix"),
    "Phoenix: Infobot: Koros": LocData(50001020, "Starship Phoenix"),
    "Phoenix: Infobot: Annihilation Nation": LocData(50001021, "Starship Phoenix"),
    "Phoenix: Infobot: Aquatos": LocData(50001022, "Starship Phoenix"),
    "Phoenix: Infobot: Tyhrranosis": LocData(50001023, "Starship Phoenix"),
    "Phoenix: Infobot: Daxx": LocData(50001024, "Starship Phoenix"),
    "Phoenix: Infobot: Obani Gemini": LocData(50001025, "Starship Phoenix"),
    "Phoenix: Infobot: Zeldrin": LocData(50001026, "Starship Phoenix"),
    "Phoenix: Infobot: Qwarks Hideout": LocData(50001027, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 4": LocData(50001413, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 5": LocData(50001414, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 1 Clear": LocData(50001600, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 2 Clear": LocData(50001601, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 3 Clear": LocData(50001602, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 4 Clear": LocData(50001603, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 5 Clear": LocData(50001604, "Starship Phoenix"),
    "Phoenix: Turn Up The Heat!": LocData(50001611, "Starship Phoenix"),
    "Phoenix: Strive for Arcade Perfection": LocData(50001612, "Starship Phoenix"),
    "Phoenix: Beat Helga's Best Time": LocData(50001613, "Starship Phoenix"),
    "Phoenix: Monkeying Around": LocData(50001614, "Starship Phoenix"),
    "Phoenix: Pirate booty - set a new record for qwark": LocData(50001615, "Starship Phoenix"),
    "Phoenix: Deja Q All over Again - set a new record for qwark": LocData(50001616, "Starship Phoenix"),
    "Phoenix: Arriba Amoeba! - set a new record for qwark": LocData(50001617, "Starship Phoenix"),
    "Phoenix: Shadow of the robot - set a new record for qwark": LocData(50001618, "Starship Phoenix"),
    "Phoenix: The Shaming of the Q - set a new record for qwark": LocData(50001619, "Starship Phoenix"),

    #----- Planet Marcadia -----#
    "Marcadia: Received Spitting Hydra": LocData(50001030, "Marcadia Region 1"),
    "Marcadia: Received Refractor": LocData(50001031, "Marcadia Region 1"),
    "Marcadia: T-Bolt: After Pool of Water": LocData(50001032, "Marcadia Region 1"),
    "Marcadia: T-Bolt: Last Refractor Room": LocData(50001033, "Marcadia Region 2"),
    "Marcadia: T-Bolt: Ceiling just before Al": LocData(50001034, "Marcadia Region 2"),
    "Marcadia: Qwark Vidcomic 1": LocData(50001035, "Marcadia Region 2"),
    "Marcadia: Marcadia Mission 01": LocData(50001036, "Marcadia Region 1"),
    "Marcadia: Marcadia Mission 02": LocData(50001037, "Marcadia Region 1"),
    "Marcadia: Marcadia Mission 03": LocData(50001038, "Marcadia Region 1"),
    "Marcadia: Marcadia Mission 04": LocData(50001039, "Marcadia Region 1"),
    "Marcadia: Marcadia Mission 05": LocData(50001040, "Marcadia Region 1"),
    "Marcadia: Reflect on how to score": LocData(50001620, "Marcadia Region 2"),

    #----- Annihilation Nation -----#
    "Annihilation: Received Agents of Doom": LocData(50001140, "Annihilation Nation"),
    "Annihilation: Received Tyhrra-Guise": LocData(50001141, "Annihilation Nation"),
    "Annihilation: T-Bolt: Heat Street": LocData(50001142, "Annihilation Nation"),
    "Annihilation: T-Bolt: Maze of Blaze": LocData(50001143, "Annihilation Nation 2"),
    "Annihilation: Grand Prize Bout": LocData(50001144, "Annihilation Nation"),
    "Annihilation: The Terrible Two": LocData(50001145, "Annihilation Nation"),
    "Annihilation: Robot Rampage": LocData(50001146, "Annihilation Nation"),
    "Annihilation: Two Minute Warning": LocData(50001147, "Annihilation Nation"),
    "Annihilation: 90 Seconds of Carnage": LocData(50001148, "Annihilation Nation"),
    "Annihilation: Onslaught": LocData(50001149, "Annihilation Nation"),
    "Annihilation: Whip it Good": LocData(50001150, "Annihilation Nation"),
    "Annihilation: Hydra'n Seek": LocData(50001151, "Annihilation Nation"),
    "Annihilation: Championship Bout": LocData(50001152, "Annihilation Nation"),
    "Annihilation: Meet Courtney - Arena": LocData(50001153, "Annihilation Nation 2"),
    "Annihilation: Ninja Challenge": LocData(50001154, "Annihilation Nation 2"),
    "Annihilation: Counting Ducks": LocData(50001155, "Annihilation Nation 2"),
    "Annihilation: Cycling Weapons": LocData(50001156, "Annihilation Nation 2"),
    "Annihilation: One Hit Wonder": LocData(50001157, "Annihilation Nation 2"),
    "Annihilation: Time to SUCC": LocData(50001158, "Annihilation Nation 2"),
    "Annihilation: Naptime": LocData(50001159, "Annihilation Nation 2"),
    "Annihilation: More Cycling Weapons": LocData(50001160, "Annihilation Nation 2"),
    "Annihilation: Dodge the Twins": LocData(50001161, "Annihilation Nation 2"),
    "Annihilation: Chop Chop": LocData(50001162, "Annihilation Nation 2"),
    "Annihilation: Sleep Inducer": LocData(50001163, "Annihilation Nation 2"),
    "Annihilation: The Other White Meat": LocData(50001164, "Annihilation Nation 2"),
    "Annihilation: Championship Bout II": LocData(50001165, "Annihilation Nation 2"),
    "Annihilation: Qwarktastic Battle": LocData(50001166, "Annihilation Nation 2"),
    "Annihilation: Heat Street": LocData(50001167, "Annihilation Nation"),
    "Annihilation: Crispy Critter": LocData(50001168, "Annihilation Nation 2"),
    "Annihilation: Pyro Playground": LocData(50001169, "Annihilation Nation 2"),
    "Annihilation: Suicide Run": LocData(50001170, "Annihilation Nation 2"),
    "Annihilation: BBQ Boulevard": LocData(50001171, "Annihilation Nation 2"),
    "Annihilation: Maze of Blaze": LocData(50001172, "Annihilation Nation 2"),
    "Annihilation: Cremation Station": LocData(50001173, "Annihilation Nation 2"),
    "Annihilation: The Annihilator (Gauntlet)": LocData(50001174, "Annihilation Nation 2"),
    "Annihilation: Qwark Vidcomic 2": LocData(50001175, "Annihilation Nation"),
    "Annihilation: Qwark Vidcomic 3": LocData(50001176, "Annihilation Nation 2"),
    "Annihilation: Bash the bug": LocData(50001617, "Annihilation Nation 2"),
    "Annihilation: Be an eight time champ": LocData(50001618, "Annihilation Nation 2"),
    "Annihilation: Flee Flawlessly": LocData(50001619, "Annihilation Nation"),
    "Annihilation: Lights, camera action!": LocData(50001620, "Annihilation Nation"),

    #----- Planet Aquatos -----#
    "Aquatos: Received Flux Rifle": LocData(50001090, "Aquatos"),
    "Aquatos: T-Bolt: Under the Bridge": LocData(50001091, "Aquatos"),
    "Aquatos: T-Bolt: Underwater Bolt": LocData(50001092, "Aquatos"),
    "Aquatos: T-Bolt: Behind the Locked Gate": LocData(50001093, "Aquatos"),
    "Aquatos: T-Bolt: Top Left Bolt": LocData(50001094, "Aquatos"),
    "Aquatos: T-Bolt: Swinging Bolt": LocData(50001095, "Aquatos"),
    "Aquatos: 1 Sewer Crystal Traded": LocData(50001096, "Aquatos"),
    "Aquatos: 5 Sewer Crystals Traded": LocData(50001097, "Aquatos"),
    "Aquatos: 10 Sewer Crystals Traded": LocData(50001098, "Aquatos"),
    "Aquatos: 20 Sewer Crystals Traded": LocData(50001099, "Aquatos"),
    "Aquatos: Search for sunken treasure": LocData(50001621, "Aquatos"),
    "Aquatos: Hit the motherload": LocData(50001634, "Aquatos"),

    #----- Planet Tyhrranosis -----#
    "Tyhrranosis: Received Annihilator": LocData(50001300, "Tyhrranosis"),
    "Tyhrranosis: Received Holo-Shield Glove": LocData(50001301, "Tyhrranosis"),
    "Tyhrranosis: T-Bolt: South East Cannon": LocData(50001302, "Tyhrranosis"),
    "Tyhrranosis: T-Bolt: Underground Cave Bolt": LocData(50001303, "Tyhrranosis"),
    "Tyhrranosis: Destroy the Momma Tyhrranoid": LocData(50001605, "Tyhrranosis"),
    "Tyhrranosis: Kavu Island Mission 1": LocData(50001606, "Tyhrranosis Region 2"),
    "Tyhrranosis: Kavu Island Mission 2": LocData(50001607, "Tyhrranosis Region 2"),
    "Tyhrranosis: Kavu Island Mission 3": LocData(50001608, "Tyhrranosis Region 2"),
    "Tyhrranosis: Kavu Island Mission 4": LocData(50001609, "Tyhrranosis Region 2"),
    "Tyhrranosis: Be a Sharpshooter": LocData(50001622, "Tyhrranosis"),

    #----- Planet Daxx -----#
    "Daxx: T-Bolt: Right of the Taxi": LocData(50001320, "Daxx Region 2"),
    "Daxx: T-Bolt: Time Sensitive Door": LocData(50001321, "Daxx Region 2"),
    "Daxx: Received Charge Boots": LocData(50001322, "Daxx Region 1"),
    "Daxx: Post-Daxx": LocData(50001323, "Daxx Region 2"),
    "Daxx: Bugs to Birdie" : LocData(50001616, "Aridia"), # In the vanilla game you get the quack o ray on Aridia, but the skill point is done on Daxx

    #----- Obani Gemini -----#
    "Obani_Gemini: Received Disk Blade Gun": LocData(50001340, "Obani Gemini"),
    "Obani_Gemini: T-Bolt: Follow the Lava": LocData(50001341, "Obani Gemini"),
    "Obani_Gemini: T-Bolt: Between the Twin Towers": LocData(50001342, "Obani Gemini"),
    "Obani_Gemini: Infobot: Rilgar": LocData(50001343, "Obani Gemini"),
    "Obani_Gemini: Get to the belt": LocData(50001623, "Obani Gemini"),

    #----- Planet Rilgar -----#
    "Rilgar: Received Grav Boots": LocData(50001360, "Rilgar"),
    "Rilgar: Infobot: Holostar Studios": LocData(50001361, "Rilgar"),
    "Rilgar: Rilgar Mission 01": LocData(50001365, "Rilgar"),
    "Rilgar: Rilgar Mission 02": LocData(50001366, "Rilgar"),
    "Rilgar: Rilgar Mission 03": LocData(50001367, "Rilgar"),
    "Rilgar: Bash the party": LocData(50001624, "Rilgar"),

    # ----- Holostar Studios -----#
    "Holostar: Received Rift Inducer": LocData(50001390, "Holostar Studios"),
    "Holostar: T-Bolt: Atop the Chairs": LocData(50001391, "Holostar Studios"),
    "Holostar: T-Bolt: Lot 42's Grav Ramp": LocData(50001392, "Holostar Studios"),
    "Holostar: T-Bolt: Kamikaze Noids": LocData(50001393, "Holostar Studios"),
    "Holostar: Infobot: Obani Draco": LocData(50001394, "Holostar Studios"),
    "Holostar: Feeling Lucky": LocData(50001625, "Holostar Studios"),

    #----- Obani Draco (lol) -----#
    "Obani_Draco: Infobot: Zeldrin Starport": LocData(50001370, "Obani Draco"),

    #----- Zeldrin Starport -----#
    "Zeldrin_Starport: Received Bolt Grabber V2": LocData(50001410, "Zeldrin Starport Region 2"),
    "Zeldrin_Starport: T-Bolt: Inside the Second Ship": LocData(50001411, "Zeldrin Starport Region 2"),
    "Zeldrin_Starport: T-Bolt: Atop the Twin Shooters": LocData(50001412, "Zeldrin Starport Region 2"),


    #----- Planet Metropolis -----#
    "Metropolis: Received Map-O-Matic": LocData(50001430, "Metropolis Region 2"),
    "Metropolis: T-Bolt: Across the Gap": LocData(50001431, "Metropolis Region 1"),
    "Metropolis: T-Bolt: Right of the Balcony": LocData(50001432, "Metropolis Region 2"),
    "Metropolis: T-Bolt: Tall Tower (Hovership)": LocData(50001433, "Metropolis Region 2"),
    "Metropolis: Metal-Noids": LocData(50001434, "Metropolis Region 1"),
    "Metropolis: Metro Storm Mission 01": LocData(50001435, "Metropolis Region 2"),
    "Metropolis: Metro Storm Mission 02": LocData(50001436, "Metropolis Region 2"),
    "Metropolis: Metro Storm Mission 03": LocData(50001437, "Metropolis Region 2"),
    "Metropolis: Metro Storm Mission 04": LocData(50001438, "Metropolis Region 2"),
    "Metropolis: Metro Storm Mission 05": LocData(50001439, "Metropolis Region 2"),
    "Metropolis: 2002 was a good year in the city": LocData(50001627, "Metropolis Region 1"),

    #----- Planet Zeldrin -----#
    "Zeldrin: Received Nano-Pak": LocData(50001450, "Zeldrin"),
    "Zeldrin: T-Bolt: Turn Around": LocData(50001451, "Zeldrin"),
    "Zeldrin: Infobot: Aridia": LocData(50001452, "Zeldrin"),
    "Zeldrin: Suck it up!": LocData(50001628, "Zeldrin"),
    "Zeldrin: Aim High": LocData(50001629, "Zeldrin"),

    #----- Planet Aridia -----#
    "Aridia: Received Warp Pad": LocData(50001470, "Aridia"),
    "Aridia: Received Qwack-O-Ray": LocData(50001471, "Aridia"),
    "Aridia: T-Bolt: Under the Bridge (Assassionation)": LocData(50001472, "Aridia"),
    "Aridia: T-Bolt: Behind the Base (X12 Endgame)": LocData(50001473, "Aridia"),
    "Alidia: Alidia Mission 01": LocData(50001475, "Alidia"),
    "Alidia: Alidia Mission 02": LocData(50001476, "Alidia"),
    "Alidia: Alidia Mission 03": LocData(50001477, "Alidia"),
    "Alidia: Alidia Mission 04": LocData(50001478, "Alidia"),
    "Alidia: Alidia Mission 05": LocData(50001479, "Alidia"),
    "Aridia: Go for hang time": LocData(50001630, "Aridia"),
    "Aridia: Zap back at ya'": LocData(50001631, "Aridia"),

    #----- Qwark's Hideout -----#
    "Qwark's_Hideout: Received Gadgetron PDU": LocData(50001490, "Qwarks Hideout"),
    "Qwark's_Hideout: T-Bolt: Glide from the Ramp": LocData(50001491, "Qwarks Hideout"),
    "Qwark's_Hideout: Break the Dan": LocData(50001632, "Qwarks Hideout"),

    #----- Planet Koros -----#
    "Koros: T-Bolt: Behind the Metal Fence": LocData(50001493, "Koros"),
    "Koros: T-Bolt: Pair of Towers": LocData(50001494, "Koros"),
    "Koros: Infobot: Mylon": LocData(50001495, "Koros"),
    "Koros: You break it, you win it": LocData(50001626, "Koros"),

    #----- Planet Mylon -----#
    "Mylon: T-Bolt: Behind the Forcefield": LocData(50001496, "Mylon"),
    "Mylon: Dr. Nefarious Defeated!": LocData(50001497, "Mylon"),
    "Mylon: Biobliterator Defeated!": LocData(50001498, "Mylon"),
    "Mylon: Spread your germs": LocData(50001633, "Mylon")
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

    "Shield Charger: V2": LocData(50001568, "Shield Charger Upgrades"),
    "Shield Charger: V3": LocData(50001569, "Shield Charger Upgrades"),
    "Shield Charger: V4": LocData(50001570, "Shield Charger Upgrades"),
    "Shield Charger: V5": LocData(50001571, "Shield Charger Upgrades"),

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
    # **weapon_upgrades
}

#class EventData(NamedTuple):
#    name:       str
#    ap_code:    Optional[int] = None
#class LocData(NamedTuple):
#    ap_code: Optional[int]
#    region: Optional[str]
def get_level_locations(region):
    return map(lambda l: l[0], get_level_location_data(region))

def get_level_location_data(region):
    return filter(lambda l: l[1].region == (region), location_table.items())

