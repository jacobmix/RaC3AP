from typing import Dict, TYPE_CHECKING

from .Types import EventData, LocData

if TYPE_CHECKING:
    from . import RaC3World


def get_total_locations(world: "RaC3World") -> int:
    locations = [l for l in world.multiworld.get_locations() if l.player == world.player]
    return len(locations)


def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}
    return names


def get_regions() -> list:
    regions = [data.region for _, data in location_table.items()]
    return regions


rac3_locations = {
    # ----- Planet Veldin -----#
    "Veldin: First Ranger": LocData(50010000, "Veldin"),
    "Veldin: Second Ranger": LocData(50010001, "Veldin"),
    "Veldin: Save Veldin": LocData(50010002, "Veldin"),

    # ----- Planet Florana -----#
    "Florana: Received Plasma Whip": LocData(50020000, "Florana"),
    "Florana: Received N60 Storm": LocData(50020001, "Florana"),
    "Florana: T-Bolt: Below Gadgetron Vendor": LocData(50020002, "Florana"),
    "Florana: T-Bolt: Path of Death": LocData(50020003, "Florana"),
    "Florana: Defeat Qwark": LocData(50020004, "Florana"),
    "Florana: Skill Point: Stay Squeaky Clean": LocData(50020005, "Florana"),

    # ----- Starship Phoenix -----#
    "Phoenix: Received Suck Cannon": LocData(50030000, "Starship Phoenix"),
    "Phoenix: Received Infector": LocData(50030001, "Starship Phoenix"),
    "Phoenix: Received Magna Plate Armor": LocData(50030002, "Starship Phoenix"),
    "Phoenix: Received Adamantine Armor": LocData(50030003, "Starship Phoenix"),
    "Phoenix: Received Aegis Mark V Armor": LocData(50030004, "Starship Phoenix"),
    "Phoenix: Received Infernox Armor": LocData(50030005, "Starship Phoenix"),
    "Phoenix: Marcadia Invaded": LocData(50030006, "Starship Phoenix"),
    "Phoenix: Infobot: Koros": LocData(50030007, "Starship Phoenix"),  # Phoenix Assault post Qwark's Hideout
    "Phoenix: Infobot: Annihilation Nation": LocData(50030008, "Starship Phoenix"),  # Vidcomic 1
    "Phoenix: Infobot: Aquatos": LocData(50030009, "Starship Phoenix"),  # Annihilation Nation Grand Prize Bout
    "Phoenix: Infobot: Tyhrranosis": LocData(50030010, "Starship Phoenix"),  # Aquatos Base
    "Phoenix: Infobot: Daxx": LocData(50030011, "Starship Phoenix"),  # Tyhrranosis Noid Queen
    "Phoenix: Infobot: Metropolis": LocData(50030012, "Starship Phoenix"),  # Vidcomic 4
    "Phoenix: Infobot: Crash Site": LocData(50030013, "Starship Phoenix"),  # Metropolis Clunk Fight
    "Phoenix: Infobot: Qwarks Hideout": LocData(50030014, "Starship Phoenix"),  # Vidcomic 5
    "Phoenix: T-Bolt: VR Gadget Training": LocData(50030015, "Starship Phoenix"),
    "Phoenix: Received Hacker": LocData(50030016, "Starship Phoenix"),
    "Phoenix: Received Hypershot": LocData(50030017, "Starship Phoenix"),
    "Phoenix: VR: VR Gadget Training": LocData(50030018, "Starship Phoenix"),
    "Phoenix: VR: Warm Up": LocData(50030019, "Starship Phoenix"),
    "Phoenix: VR: Don't Look Down": LocData(50030020, "Starship Phoenix"),
    "Phoenix: VR: Speed Round": LocData(50030021, "Starship Phoenix"),
    "Phoenix: VR: Hot Stepper": LocData(50030022, "Starship Phoenix"),
    "Phoenix: VR: 90 Second Slayer": LocData(50030023, "Starship Phoenix"),
    "Phoenix: VR: The Shocker": LocData(50030024, "Starship Phoenix"),
    "Phoenix: VR: Wrench Beatdown": LocData(50030025, "Starship Phoenix"),
    "Phoenix: VR: Nerves of Titanium": LocData(50030026, "Starship Phoenix"),
    "Phoenix: T-Bolt: Nerves of Titanium": LocData(50030027, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 4": LocData(50030028, "Starship Phoenix"),  # Zeldrin Starport
    "Phoenix: Qwark Vidcomic 5": LocData(50030029, "Starship Phoenix"),  # Crash Site
    "Phoenix: Skill Point: Turn Up The Heat!": LocData(50030030, "Starship Phoenix"),
    "Phoenix: Skill Point: Strive for Arcade Perfection": LocData(50030031, "Starship Phoenix"),
    "Phoenix: Skill Point: Beat Helga's Best Time": LocData(50030032, "Starship Phoenix"),
    "Phoenix: Skill Point: Monkeying Around": LocData(50030033, "Starship Phoenix"),
    # Vidcomics
    "Phoenix: Qwark Vidcomic 1 Clear": LocData(50310000, "Starship Phoenix"),
    "Phoenix: T-Bolt: Vidcomic 1 100%": LocData(50310001, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 2 Clear": LocData(50330000, "Starship Phoenix"),
    "Phoenix: T-Bolt: Vidcomic 2 100%": LocData(50330001, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 3 Clear": LocData(50340000, "Starship Phoenix"),
    "Phoenix: T-Bolt: Vidcomic 3 100%": LocData(50340001, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 4 Clear": LocData(50320000, "Starship Phoenix"),
    "Phoenix: T-Bolt: Vidcomic 4 100%": LocData(50320001, "Starship Phoenix"),
    "Phoenix: Qwark Vidcomic 5 Clear": LocData(50350000, "Starship Phoenix"),
    "Phoenix: T-Bolt: Vidcomic 5 100%": LocData(50350001, "Starship Phoenix"),
    "Phoenix: Skill Point: Pirate booty - set a new record for qwark": LocData(50310003, "Starship Phoenix"),
    "Phoenix: Skill Point: Deja Q All over Again - set a new record for qwark": LocData(50330003, "Starship Phoenix"),
    "Phoenix: Skill Point: Arriba Amoeba! - set a new record for qwark": LocData(50340003, "Starship Phoenix"),
    "Phoenix: Skill Point: Shadow of the robot - set a new record for qwark": LocData(50320003, "Starship Phoenix"),
    "Phoenix: Skill Point: The Shaming of the Q - set a new record for qwark": LocData(50350003, "Starship Phoenix"),

    # ----- Planet Marcadia -----#
    "Marcadia: Received Spitting Hydra": LocData(50040000, "Marcadia Region 1"),
    "Marcadia: Received Refractor": LocData(50040001, "Marcadia Region 1"),
    "Marcadia: T-Bolt: After Pool of Water": LocData(50040002, "Marcadia Region 1"),
    "Marcadia: T-Bolt: Last Refractor Room": LocData(50040003, "Marcadia Region 2"),
    "Marcadia: T-Bolt: Ceiling just before Al": LocData(50040004, "Marcadia Region 2"),
    "Marcadia: Qwark Vidcomic 1": LocData(50040005, "Marcadia Region 2"),
    "Marcadia: Operation IRON SHIELD: Secure the Area": LocData(50040006, "Marcadia Region 1"),
    "Marcadia: Operation IRON SHIELD: Air Assault": LocData(50040007, "Marcadia Region 1"),
    "Marcadia: Operation IRON SHIELD: Turret Command": LocData(50040008, "Marcadia Region 1"),
    "Marcadia: Operation IRON SHIELD: Under the Gun": LocData(50040009, "Marcadia Region 1"),
    "Marcadia: Operation IRON SHIELD: Hit n' Run": LocData(50040010, "Marcadia Region 1"),
    "Marcadia: Skill Point: Reflect on how to score": LocData(50040011, "Marcadia Region 2"),

    # ----- Annihilation Nation -----#
    "Annihilation: Received Agents of Doom": LocData(50070000, "Annihilation Nation"),
    "Annihilation: Received Tyhrra-Guise": LocData(50070001, "Annihilation Nation"),
    "Annihilation: T-Bolt: Heat Street": LocData(50070002, "Annihilation Nation"),
    "Annihilation: T-Bolt: Maze of Blaze": LocData(50070003, "Annihilation Nation 2"),
    "Annihilation: Grand Prize Bout": LocData(50070004, "Annihilation Nation"),
    "Annihilation: The Terrible Two": LocData(50070005, "Annihilation Nation"),
    "Annihilation: Robot Rampage": LocData(50070006, "Annihilation Nation"),
    "Annihilation: Two Minute Warning": LocData(50070007, "Annihilation Nation"),
    "Annihilation: 90 Seconds of Carnage": LocData(50070008, "Annihilation Nation"),
    "Annihilation: Onslaught": LocData(50070009, "Annihilation Nation"),
    "Annihilation: Whip it Good": LocData(50070010, "Annihilation Nation"),
    "Annihilation: Hydra'n Seek": LocData(50070011, "Annihilation Nation"),
    "Annihilation: Championship Bout": LocData(50070012, "Annihilation Nation"),
    "Annihilation: Meet Courtney - Arena": LocData(50070013, "Annihilation Nation 2"),
    "Annihilation: Ninja Challenge": LocData(50070014, "Annihilation Nation 2"),
    "Annihilation: Counting Ducks": LocData(50070015, "Annihilation Nation 2"),
    "Annihilation: Cycling Weapons": LocData(50070016, "Annihilation Nation 2"),
    "Annihilation: One Hit Wonder": LocData(50070017, "Annihilation Nation 2"),
    "Annihilation: Time to Suck": LocData(50070018, "Annihilation Nation 2"),
    "Annihilation: Naptime": LocData(50070019, "Annihilation Nation 2"),
    "Annihilation: More Cycling Weapons": LocData(50070020, "Annihilation Nation 2"),
    "Annihilation: Dodge the Twins": LocData(50070021, "Annihilation Nation 2"),
    "Annihilation: Chop Chop": LocData(50070022, "Annihilation Nation 2"),
    "Annihilation: Sleep Inducer": LocData(50070023, "Annihilation Nation 2"),
    "Annihilation: The Other White Meat": LocData(50070024, "Annihilation Nation 2"),
    "Annihilation: Championship Bout II": LocData(50070025, "Annihilation Nation 2"),
    "Annihilation: Qwarktastic Battle": LocData(50070026, "Annihilation Nation 2"),
    "Annihilation: Heat Street": LocData(50070027, "Annihilation Nation"),
    "Annihilation: Crispy Critter": LocData(50070028, "Annihilation Nation 2"),
    "Annihilation: Pyro Playground": LocData(50070029, "Annihilation Nation 2"),
    "Annihilation: Suicide Run": LocData(50070030, "Annihilation Nation 2"),
    "Annihilation: BBQ Boulevard": LocData(50070031, "Annihilation Nation 2"),
    "Annihilation: Maze of Blaze": LocData(50070032, "Annihilation Nation 2"),
    "Annihilation: Cremation Station": LocData(50070033, "Annihilation Nation 2"),
    "Annihilation: The Annihilator (Gauntlet)": LocData(50070034, "Annihilation Nation 2"),
    "Annihilation: Qwark Vidcomic 2": LocData(50070035, "Annihilation Nation"),
    "Annihilation: Qwark Vidcomic 3": LocData(50070036, "Annihilation Nation 2"),
    "Annihilation: Skill Point: Bash the bug": LocData(50070037, "Annihilation Nation 2"),
    "Annihilation: Skill Point: Be an eight time champ": LocData(50070038, "Annihilation Nation 2"),
    "Annihilation: Skill Point: Flee Flawlessly": LocData(50070039, "Annihilation Nation"),
    "Annihilation: Skill Point: Lights, camera action!": LocData(50070040, "Annihilation Nation"),

    # ----- Planet Aquatos -----#
    "Aquatos: Received Flux Rifle": LocData(50080000, "Aquatos"),
    "Aquatos: T-Bolt: Under the Bridge": LocData(50080001, "Aquatos"),
    "Aquatos: T-Bolt: Underwater Bolt": LocData(50080002, "Aquatos"),
    "Aquatos: T-Bolt: Behind the Locked Gate": LocData(50080003, "Aquatos"),
    "Aquatos: Skill Point: Search for sunken treasure": LocData(50080004, "Aquatos"),
    "Aquatos: Received Mini-Turret Glove": LocData(50080005, "Aquatos"),
    "Aquatos: Received Lava Gun": LocData(50080006, "Aquatos"),
    "Aquatos: Received Shield Charger": LocData(50080007, "Aquatos"),  # Command Center
    "Aquatos: Received Bouncer": LocData(50080008, "Aquatos"),  # Qwarks Hideout
    "Aquatos: Received Plasma Coil": LocData(50080009, "Aquatos"),  # Koros
    # Base
    # Sewers
    "Aquatos: T-Bolt: Top Left Bolt": LocData(50280000, "Aquatos"),
    "Aquatos: T-Bolt: Swinging Bolt": LocData(50280001, "Aquatos"),
    "Aquatos: 1 Sewer Crystal Traded": LocData(50280002, "Aquatos"),
    "Aquatos: 5 Sewer Crystals Traded": LocData(50280003, "Aquatos"),
    "Aquatos: 10 Sewer Crystals Traded": LocData(50280004, "Aquatos"),
    "Aquatos: 20 Sewer Crystals Traded": LocData(50280005, "Aquatos"),
    "Aquatos: Skill Point: Hit the motherload": LocData(50280006, "Aquatos"),

    # ----- Planet Tyhrranosis -----#
    "Tyhrranosis: Received Annihilator": LocData(50090000, "Tyhrranosis"),
    "Tyhrranosis: Received Holo-Shield Glove": LocData(50090001, "Tyhrranosis"),
    "Tyhrranosis: T-Bolt: South East Cannon": LocData(50090002, "Tyhrranosis"),
    "Tyhrranosis: T-Bolt: Underground Cave Bolt": LocData(50090003, "Tyhrranosis"),
    "Tyhrranosis: Destroy the Momma Tyhrranoid": LocData(50090004, "Tyhrranosis"),
    "Tyhrranosis: Skill Point: Be a Sharpshooter": LocData(50090005, "Tyhrranosis"),
    # Missions
    "Tyhrranosis: Operation ISLAND STRIKE: Assault on Kavu Island": LocData(50290000, "Tyhrranosis Region 2"),
    "Tyhrranosis: Operation ISLAND STRIKE: Dogfight over Kavu Island": LocData(50290001, "Tyhrranosis Region 2"),
    "Tyhrranosis: Operation ISLAND STRIKE: Operation Thunderbolt": LocData(50290002, "Tyhrranosis Region 2"),
    "Tyhrranosis: Operation ISLAND STRIKE: The Final Battle": LocData(50290003, "Tyhrranosis Region 2"),

    # ----- Planet Daxx -----#
    "Daxx: Infiltrate Weapons Facility": LocData(50050000, "Daxx"),
    "Daxx: T-Bolt: Right of the Taxi": LocData(50050001, "Daxx"),
    "Daxx: T-Bolt: Time Sensitive Door": LocData(50050002, "Daxx"),
    "Daxx: Received Charge Boots": LocData(50050003, "Daxx"),
    "Daxx: Post-Daxx": LocData(50050004, "Daxx"),
    "Daxx: Skill Point: Bugs to Birdie": LocData(50050005, "Daxx"),
    # In the vanilla game you get the quack-o-ray on Aridia, but the skill point is done on Daxx

    # ----- Obani Gemini -----#
    "Obani_Gemini: Received Disk-Blade Gun": LocData(50110000, "Obani Gemini"),
    "Obani_Gemini: T-Bolt: Follow the Lava": LocData(50110001, "Obani Gemini"),
    "Obani_Gemini: T-Bolt: Between the Twin Towers": LocData(50110002, "Obani Gemini"),
    "Obani_Gemini: Infobot: Blackwater City": LocData(50110003, "Obani Gemini"),
    "Obani_Gemini: Skill Point: Get to the belt": LocData(50110004, "Obani Gemini"),

    # ----- Planet Blackwater City -----#
    "Blackwater City: Received Gravity Boots": LocData(50120000, "Blackwater City"),
    "Blackwater City: Infobot: Holostar Studios": LocData(50120001, "Blackwater City"),
    # Annihilation Nation 2 Courtney
    "Blackwater City: Operation BLACK TIDE: The Battle of Blackwater City": LocData(50120002, "Blackwater City"),
    "Blackwater City: Operation BLACK TIDE: The Bridge": LocData(50120003, "Blackwater City"),
    "Blackwater City: Operation BLACK TIDE: Counterattack": LocData(50120004, "Blackwater City"),
    "Blackwater City: Skill Point: Bash the party": LocData(50120005, "Blackwater City"),

    # ----- Holostar Studios -----#
    "Holostar: Received Rift Inducer": LocData(50130000, "Holostar Studios"),
    "Holostar: T-Bolt: Atop the Chairs": LocData(50130001, "Holostar Studios"),
    "Holostar: T-Bolt: Lot 42's Gravity Ramp": LocData(50130002, "Holostar Studios"),
    "Holostar: T-Bolt: Kamikaze Noids": LocData(50130003, "Holostar Studios"),
    "Holostar: Infobot: Obani Draco": LocData(50130004, "Holostar Studios"),  # Blackwater City and Holostar completed
    "Holostar: Skill Point: Feeling Lucky": LocData(50130005, "Holostar Studios"),

    # ----- Obani Draco (lol) -----#
    "Obani_Draco: Infobot: Zeldrin Starport": LocData(50210000, "Obani Draco"),

    # ----- Zeldrin Starport -----#
    "Zeldrin Starport: Received Bolt Grabber V2": LocData(50100000, "Zeldrin Starport"),
    "Zeldrin Starport: T-Bolt: Inside the Second Ship": LocData(50100001, "Zeldrin Starport"),
    "Zeldrin Starport: T-Bolt: Atop the Twin Shooters": LocData(50100002, "Zeldrin Starport"),

    # ----- Planet Metropolis -----#
    "Metropolis: T-Bolt: Across the Gap": LocData(50160000, "Metropolis Region 1"),
    "Metropolis: Skill Point: 2002 was a good year in the city": LocData(50160001, "Metropolis Region 1"),
    # Skrunch Trophy
    "Metropolis: Metal-Noids": LocData(50160002, "Metropolis Region 1"),
    "Metropolis: T-Bolt: Right of the Balcony": LocData(50160003, "Metropolis Region 1"),
    # Clunk Fight
    # Missions
    "Metropolis: T-Bolt: Tall Tower (Hovership)": LocData(50260000, "Metropolis Region 2"),
    "Metropolis: Operation URBAN STORM: Countdown": LocData(50260001, "Metropolis Region 2"),
    "Metropolis: Operation URBAN STORM: Urban Combat": LocData(50260002, "Metropolis Region 2"),
    "Metropolis: Operation URBAN STORM: Tower Attack": LocData(50260003, "Metropolis Region 2"),
    "Metropolis: Operation URBAN STORM: Air Superiority": LocData(50260004, "Metropolis Region 2"),
    "Metropolis: Operation URBAN STORM: Turret Command": LocData(50260005, "Metropolis Region 2"),
    "Metropolis: Received Map-O-Matic": LocData(50260006, "Metropolis Region 2"),

    # ----- Planet Crash Site -----#
    "Crash Site: T-Bolt: Turn Around": LocData(50170000, "Crash Site"),
    # Nefarious Trophy
    "Crash Site: Received Nano-Pak": LocData(50170001, "Crash Site"),
    "Crash Site: Escape Pod": LocData(50170002, "Crash Site"),
    "Crash Site: Infobot: Aridia": LocData(50170003, "Crash Site"),
    "Crash Site: Skill Point: Suck it up!": LocData(50170004, "Crash Site"),
    "Crash Site: Skill Point: Aim High": LocData(50170005, "Crash Site"),

    # ----- Planet Aridia -----#
    "Aridia: Received Warp Pad": LocData(50180000, "Aridia"),
    "Aridia: Received Qwack-O-Ray": LocData(50180001, "Aridia"),
    "Aridia: T-Bolt: Under the Bridge (Assassination)": LocData(50180002, "Aridia"),
    "Aridia: T-Bolt: Behind the Base (X12 Endgame)": LocData(50180003, "Aridia"),
    "Aridia: Operation DEATH VALLEY: The Tunnels of Outpost X12": LocData(50180004, "Aridia"),
    "Aridia: Operation DEATH VALLEY: Ambush in Red Rock Valley": LocData(50180005, "Aridia"),
    "Aridia: Operation DEATH VALLEY: Assassination": LocData(50180006, "Aridia"),
    "Aridia: Operation DEATH VALLEY: Reclaim the Valley": LocData(50180007, "Aridia"),
    "Aridia: Operation DEATH VALLEY: X12 Endgame": LocData(50180008, "Aridia"),
    "Aridia: Skill Point: Go for hang time": LocData(50180009, "Aridia"),
    "Aridia: Skill Point: Zap back at ya'": LocData(50180010, "Aridia"),

    # ----- Qwark's Hideout -----#
    "Qwarks Hideout: Received Gadgetron PDA": LocData(50190000, "Qwarks Hideout"),
    "Qwarks Hideout: T-Bolt: Glide from the Ramp": LocData(50190001, "Qwarks Hideout"),
    "Qwarks Hideout: Skill Point: Break the Dan": LocData(50190002, "Qwarks Hideout"),
    # Qwark Trophy
    # Phoenix Assault Trigger

    # ----- Planet Koros -----#
    # Courtney Gears Trophy
    "Koros: T-Bolt: Behind the Metal Fence": LocData(50140000, "Koros"),
    "Koros: T-Bolt: Pair of Towers": LocData(50140001, "Koros"),
    "Koros: Infobot: Command Center": LocData(50140002, "Koros"),
    "Koros: Skill Point: You break it, you win it": LocData(50140003, "Koros"),

    # ----- Planet Command Center -----#
    "Command Center: T-Bolt: Behind the Forcefield": LocData(50220000, "Command Center"),
    # Lawrence Trophy
    "Command Center: Skill Point: Spread Your Germs": LocData(50220001, "Command Center"),
    "Command Center: Dr. Nefarious Defeated!": LocData(50200000, "Command Center"),
    "Command Center: Biobliterator Defeated!": LocData(50200001, "Command Center")
}

weapon_upgrades = {

    "Shock Blaster: V2": LocData(50150000, "Shock Blaster Upgrades"),
    "Shock Blaster: V3": LocData(50150001, "Shock Blaster Upgrades"),
    "Shock Blaster: V4": LocData(50150002, "Shock Blaster Upgrades"),
    "Shock Blaster: V5": LocData(50150003, "Shock Blaster Upgrades"),

    "Nitro Launcher: V2": LocData(50150004, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V3": LocData(50150005, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V4": LocData(50150006, "Nitro Launcher Upgrades"),
    "Nitro Launcher: V5": LocData(50150007, "Nitro Launcher Upgrades"),

    "N60 Storm: V2": LocData(50150008, "N60 Storm Upgrades"),
    "N60 Storm: V3": LocData(50150009, "N60 Storm Upgrades"),
    "N60 Storm: V4": LocData(50150010, "N60 Storm Upgrades"),
    "N60 Storm: V5": LocData(50150011, "N60 Storm Upgrades"),

    "Plasma Whip: V2": LocData(50150012, "Plasma Whip Upgrades"),
    "Plasma Whip: V3": LocData(50150013, "Plasma Whip Upgrades"),
    "Plasma Whip: V4": LocData(50150014, "Plasma Whip Upgrades"),
    "Plasma Whip: V5": LocData(50150015, "Plasma Whip Upgrades"),

    "Infector: V2": LocData(50150016, "Infector Upgrades"),
    "Infector: V3": LocData(50150017, "Infector Upgrades"),
    "Infector: V4": LocData(50150018, "Infector Upgrades"),
    "Infector: V5": LocData(50150019, "Infector Upgrades"),

    "Suck Cannon: V2": LocData(50150020, "Suck Cannon Upgrades"),
    "Suck Cannon: V3": LocData(50150021, "Suck Cannon Upgrades"),
    "Suck Cannon: V4": LocData(50150022, "Suck Cannon Upgrades"),
    "Suck Cannon: V5": LocData(50150023, "Suck Cannon Upgrades"),

    "Spitting Hydra: V2": LocData(50150024, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V3": LocData(50150025, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V4": LocData(50150026, "Spitting Hydra Upgrades"),
    "Spitting Hydra: V5": LocData(50150027, "Spitting Hydra Upgrades"),

    "Agents of Doom: V2": LocData(50150028, "Agents of Doom Upgrades"),
    "Agents of Doom: V3": LocData(50150029, "Agents of Doom Upgrades"),
    "Agents of Doom: V4": LocData(50150030, "Agents of Doom Upgrades"),
    "Agents of Doom: V5": LocData(50150031, "Agents of Doom Upgrades"),

    "Flux Rifle: V2": LocData(50150032, "Flux Rifle Upgrades"),
    "Flux Rifle: V3": LocData(50150033, "Flux Rifle Upgrades"),
    "Flux Rifle: V4": LocData(50150034, "Flux Rifle Upgrades"),
    "Flux Rifle: V5": LocData(50150035, "Flux Rifle Upgrades"),

    "Annihilator: V2": LocData(50150036, "Annihilator Upgrades"),
    "Annihilator: V3": LocData(50150037, "Annihilator Upgrades"),
    "Annihilator: V4": LocData(50150038, "Annihilator Upgrades"),
    "Annihilator: V5": LocData(50150039, "Annihilator Upgrades"),

    "Holo-Shield Glove: V2": LocData(50150040, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V3": LocData(50150041, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V4": LocData(50150042, "Holo-Shield Glove Upgrades"),
    "Holo-Shield Glove: V5": LocData(50150043, "Holo-Shield Glove Upgrades"),

    "Disk-Blade Gun: V2": LocData(50150044, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V3": LocData(50150045, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V4": LocData(50150046, "Disk-Blade Gun Upgrades"),
    "Disk-Blade Gun: V5": LocData(50150047, "Disk-Blade Gun Upgrades"),

    "Rift Inducer: V2": LocData(50150048, "Rift Inducer Upgrades"),
    "Rift Inducer: V3": LocData(50150049, "Rift Inducer Upgrades"),
    "Rift Inducer: V4": LocData(50150050, "Rift Inducer Upgrades"),
    "Rift Inducer: V5": LocData(50150051, "Rift Inducer Upgrades"),

    "Qwack-O-Ray: V2": LocData(50150052, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V3": LocData(50150053, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V4": LocData(50150054, "Qwack-O-Ray Upgrades"),
    "Qwack-O-Ray: V5": LocData(50150055, "Qwack-O-Ray Upgrades"),

    "RY3N0: V2": LocData(50150056, "RY3N0 Upgrades"),
    "RY3N0: V3": LocData(50150057, "RY3N0 Upgrades"),
    "RY3N0: V4": LocData(50150058, "RY3N0 Upgrades"),
    "RY3N0: V5": LocData(50150059, "RY3N0 Upgrades"),

    "Mini-Turret Glove: V2": LocData(50150060, "Mini-Turret Glove Upgrades"),
    "Mini-Turret Glove: V3": LocData(50150061, "Mini-Turret Glove Upgrades"),
    "Mini-Turret Glove: V4": LocData(50150062, "Mini-Turret Glove Upgrades"),
    "Mini-Turret Glove: V5": LocData(50150063, "Mini-Turret Glove Upgrades"),

    "Lava Gun: V2": LocData(50150064, "Lava Gun Upgrades"),
    "Lava Gun: V3": LocData(50150065, "Lava Gun Upgrades"),
    "Lava Gun: V4": LocData(50150066, "Lava Gun Upgrades"),
    "Lava Gun: V5": LocData(50150067, "Lava Gun Upgrades"),

    "Shield Charger: V2": LocData(50150068, "Shield Charger Upgrades"),
    "Shield Charger: V3": LocData(50150069, "Shield Charger Upgrades"),
    "Shield Charger: V4": LocData(50150070, "Shield Charger Upgrades"),
    "Shield Charger: V5": LocData(50150071, "Shield Charger Upgrades"),

    "Bouncer: V2": LocData(50150072, "Bouncer Upgrades"),
    "Bouncer: V3": LocData(50150073, "Bouncer Upgrades"),
    "Bouncer: V4": LocData(50150074, "Bouncer Upgrades"),
    "Bouncer: V5": LocData(50150075, "Bouncer Upgrades"),

    "Plasma Coil: V2": LocData(50150076, "Plasma Coil Upgrades"),
    "Plasma Coil: V3": LocData(50150077, "Plasma Coil Upgrades"),
    "Plasma Coil: V4": LocData(50150078, "Plasma Coil Upgrades"),
    "Plasma Coil: V5": LocData(50150079, "Plasma Coil Upgrades"),

}

nanotech_milestones = {
    "Nanotech Milestone: 11": LocData(50250011, "Veldin"),
}

rac3_events = {  # Events have no ap_code
    "Cleared Veldin": EventData(None, "Veldin"),
    "Cleared Florana": EventData(None, "Florana"),
    "Cleared Marcadia": EventData(None, "Marcadia Region 2"),
    "Cleared Annihilation Nation 1": EventData(None, "Annihilation Nation"),
    "Cleared Annihilation Nation 2": EventData(None, "Annihilation Nation 2"),
    "Cleared Aquatos": EventData(None, "Aquatos"),
    "Cleared Tyhrranosis": EventData(None, "Tyhrranosis"),
    "Cleared Daxx": EventData(None, "Daxx"),
}

location_table: dict[str, LocData] = {
    **rac3_locations,
    **nanotech_milestones
    # **weapon_upgrades
}

location_groups: dict[str, set[str]] = {
    "Veldin": set(loc for loc in location_table.keys() if location_table[loc].region == "Veldin"),
    "Florana": set(loc for loc in location_table.keys() if location_table[loc].region == "Florana"),
    "Starship Phoenix": set(loc for loc in location_table.keys() if location_table[loc].region == "Starship Phoenix"),
    "Marcadia": set(loc for loc in location_table.keys() if
                    location_table[loc].region == "Marcadia Region 1"
                    or location_table[loc].region == "Marcadia Region 2"),
    "Annihilation Nation": set(loc for loc in location_table.keys() if
                               location_table[loc].region == "Annihilation Nation"
                               or location_table[loc].region == "Annihilation Nation 2"),
    "Aquatos": set(loc for loc in location_table.keys() if location_table[loc].region == "Aquatos"),
    "Tyhrranosis": set(loc for loc in location_table.keys() if
                       location_table[loc].region == "Tyhrranosis"
                       or location_table[loc].region == "Tyhrranosis Region 2"),
    "Daxx": set(loc for loc in location_table.keys() if location_table[loc].region == "Daxx"),
    "Obani Gemini": set(loc for loc in location_table.keys() if location_table[loc].region == "Obani Gemini"),
    "Blackwater City": set(loc for loc in location_table.keys() if location_table[loc].region == "Blackwater City"),
    "Holostar Studios": set(loc for loc in location_table.keys() if location_table[loc].region == "Holostar Studios"),
    "Obani Draco": set(loc for loc in location_table.keys() if location_table[loc].region == "Obani Draco"),
    "Zeldrin Starport": set(loc for loc in location_table.keys() if location_table[loc].region == "Zeldrin Starport"),
    "Metropolis": set(loc for loc in location_table.keys() if
                      location_table[loc].region == "Metropolis Region 1"
                      or location_table[loc].region == "Metropolis Region 2"),
    "Crash Site": set(loc for loc in location_table.keys() if location_table[loc].region == "Crash Site"),
    "Aridia": set(loc for loc in location_table.keys() if location_table[loc].region == "Aridia"),
    "Qwarks Hideout": set(loc for loc in location_table.keys() if location_table[loc].region == "Qwarks Hideout"),
    "Koros": set(loc for loc in location_table.keys() if location_table[loc].region == "Koros"),
    "Command Center": set(loc for loc in location_table.keys() if location_table[loc].region == "Command Center"),
}


# class EventData(NamedTuple):
#    name:       str
#    ap_code:    Optional[int] = None
# class LocData(NamedTuple):
#    ap_code: Optional[int]
#    region: Optional[str]
def get_level_locations(region):
    return map(lambda l: l[0], get_level_location_data(region))


def get_level_location_data(region):
    return filter(lambda l: l[1].region == region, location_table.items())
