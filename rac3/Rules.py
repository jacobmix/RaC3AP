from worlds.generic.Rules import add_rule, set_rule
from .Types import weapon_type_to_shortened_name
from typing import TYPE_CHECKING
from .Locations import rac3_locations
from .Items import gadget_items

if TYPE_CHECKING:
    from . import RaC3World


def set_rules_planets(world):
    # Getting to Marcadia
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Marcadia", world.player),
             lambda state: state.has("Infobot: Marcadia", world.player)
                           and state.has("Refractor", world.player))

    # Getting to Annihilation Nation:
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Annihilation Nation", world.player),
             lambda state: state.has("Progressive Vidcomic", world.player, 1)
                           and state.has("Infobot: Annihilation Nation", world.player))

    # Getting to Aquatos
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aquatos", world.player),
             lambda state: state.has("Infobot: Aquatos", world.player)
                           and state.has("Tyhrra-Guise", world.player))

    # Getting to Tyhrranosis
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Tyhrranosis", world.player),
             lambda state: state.has("Infobot: Tyhrranosis", world.player))

    # Getting to Daxx
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Daxx", world.player),
             lambda state: state.has("Infobot: Daxx", world.player))

    # Getting to Obani Gemini
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Obani Gemini", world.player),
             lambda state: state.has("Infobot: Obani Gemini", world.player)
                           and state.has("Refractor", world.player))

    # Getting to Blackwater City
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Blackwater City", world.player),
             lambda state: state.has("Infobot: Blackwater City", world.player))

    # Getting to Holostar Studios
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Holostar Studios", world.player),
             lambda state: state.has("Infobot: Holostar Studios", world.player)
                           and state.has("Hacker", world.player)
                           and state.has("Hypershot", world.player))

    # Getting to Obani Draco (lol)
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Obani Draco", world.player),
             lambda state: state.has("Infobot: Obani Draco", world.player)
                           and state.has("Gravity-Boots", world.player))

    # Getting to Zeldrin Starport
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Zeldrin Starport", world.player),
             lambda state: state.has("Infobot: Zeldrin Starport", world.player))

    # Getting to Metropolis
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Metropolis", world.player),
             lambda state: state.has("Infobot: Metropolis", world.player)
                           and state.has("Progressive Vidcomic", world.player, 4))

    # Getting to Crash Site
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Crash Site", world.player),
             lambda state: state.has("Infobot: Crash Site", world.player)
                           and state.has("Hypershot", world.player))

    # Getting to Aridia
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aridia", world.player),
             lambda state: state.has("Infobot: Aridia", world.player))

    # Getting to Qwark's Hideout
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Qwarks Hideout", world.player),
             lambda state: state.has("Infobot: Qwarks Hideout", world.player)
                           and state.has("Warp Pad", world.player)
                           and state.has("Hypershot", world.player))

    # Getting to Koros
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Koros", world.player),
             lambda state: state.has("Infobot: Koros", world.player))

    # Getting to Command Center
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Command Center", world.player),
             lambda state: state.has("Infobot: Command Center", world.player)
                           and state.has("Hacker", world.player)
                           and state.has("Tyhrra-Guise", world.player)
                           and state.has("Hypershot", world.player)
                           and state.has("Gravity-Boots", world.player))


def set_rules_hard_location(world):
    # ----- Planet Veldin -----# # Nothing
    # ----- Planet Florana -----# # Nothing

    # ----- Starship Phoenix -----#
    # "Phoenix: Received SUCC Cannon": LocData(50001009, "Starship Phoenix"),
    # "Phoenix: Received Infector": LocData(50001010, "Starship Phoenix"),
    add_rule(world.get_location("Phoenix: VR: The Shocker"),
             lambda state: state.has("Shock Blaster", world.player)
                           or state.has("Progressive Shock Blaster", world.player))
    add_rule(world.get_location("Phoenix: T-Bolt: Last VR Deck Challenges"),
             lambda state: state.has("Shock Blaster", world.player)
                           or state.has("Progressive Shock Blaster", world.player))
    add_rule(world.get_location("Phoenix: T-Bolt: Complete VR Training"),
             lambda state: state.can_reach("Tyhrranosis", player=world.player))
    add_rule(world.get_location("Phoenix: Received Adamantine Armor"),
             lambda state: state.can_reach("Tyhrranosis", player=world.player))
    add_rule(world.get_location("Phoenix: Received Aegis Mark V Armor"),
             lambda state: state.can_reach("Zeldrin Starport Region 2", player=world.player))
    add_rule(world.get_location("Phoenix: Received Infernox Armor"),
             lambda state: state.can_reach("Koros", player=world.player))
    add_rule(world.get_location("Phoenix: Received Hacker"),
             lambda state: state.can_reach("Tyhrranosis", player=world.player))
    add_rule(world.get_location("Phoenix: Received Hypershot"),
             lambda state: state.can_reach("Tyhrranosis", player=world.player))
    # "Phoenix: Infobot: Marcadia": LocData(50001019, "Starship Phoenix"),
    add_rule(world.get_location("Phoenix: Infobot: Annihilation Nation"),
             lambda state: state.has("Progressive Vidcomic", world.player, 1))
    add_rule(world.get_location("Phoenix: Infobot: Aquatos"),
             lambda state: state.has("Tyhrra-Guise", world.player)
                           and state.can_reach("Annihilation Nation", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Tyhrranosis"),
             lambda state: state.can_reach("Aquatos", player=world.player)
                           and state.can_reach("Aquatos", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Daxx"),
             lambda state: state.can_reach("Tyhrranosis", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Obani Gemini"),
             lambda state: state.can_reach("Holostar Studios", player=world.player)
                           and state.can_reach("Blackwater City", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Crash Site"),
             lambda state: state.can_reach("Metropolis Region 2", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Qwarks Hideout"),
             lambda state: state.has("Progressive Vidcomic", world.player, 5)
                           and state.can_reach("Crash Site", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Koros"),
             lambda state: state.can_reach("Qwarks Hideout", player=world.player))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 4"),
             lambda state: state.can_reach("Zeldrin Starport Region 2", player=world.player))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 5"),
             lambda state: state.can_reach("Crash Site", player=world.player))
    # Vidcomic clear locations
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 1 Clear"),
             lambda state: state.has("Progressive Vidcomic", world.player, 1))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 2 Clear"),
             lambda state: state.has("Progressive Vidcomic", world.player, 2))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 3 Clear"),
             lambda state: state.has("Progressive Vidcomic", world.player, 3))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 4 Clear"),
             lambda state: state.has("Progressive Vidcomic", world.player, 4))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 5 Clear"),
             lambda state: state.has("Progressive Vidcomic", world.player, 5))
    # Skillpoints
    add_rule(world.get_location("Phoenix: Strive for Arcade Perfection"),
             lambda state: state.has("Progressive Vidcomic", world.player, 5))

    add_rule(world.get_location("Phoenix: Pirate booty - set a new record for qwark"),
             lambda state: state.has("Progressive Vidcomic", world.player, 1))
    add_rule(world.get_location("Phoenix: Deja Q All over Again - set a new record for qwark"),
             lambda state: state.has("Progressive Vidcomic", world.player, 2)),
    add_rule(world.get_location("Phoenix: Arriba Amoeba! - set a new record for qwark"),
             lambda state: state.has("Progressive Vidcomic", world.player, 3)),
    add_rule(world.get_location("Phoenix: Shadow of the robot - set a new record for qwark"),
             lambda state: state.has("Progressive Vidcomic", world.player, 4)),
    add_rule(world.get_location("Phoenix: The Shaming of the Q - set a new record for qwark"),
             lambda state: state.has("Progressive Vidcomic", world.player, 5)),

    # ----- Planet Marcadia -----#
    # "Marcadia: Received Spitting Hydra": LocData(50001030, "Marcadia Region 1"),
    # "Marcadia: Received Refractor": LocData(50001031, "Marcadia Region 1"),
    # "Marcadia: T-Bolt: After Pool of Water": LocData(50001032, "Marcadia Region 1"),
    add_rule(world.get_location("Marcadia: T-Bolt: Last Refractor Room"),
             lambda state: state.has("Refractor", world.player)
                           and state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Marcadia: T-Bolt: Ceiling just before Al"),
             lambda state: state.has("Refractor", world.player)
                           and state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Marcadia: Qwark Vidcomic 1"),
             lambda state: state.has("Refractor", world.player))

    # ----- Annihilation Nation -----#
    # First visit (when getting Tyhrra-Guise")
    add_rule(world.get_location("Annihilation: Whip it Good"),
             lambda state: state.has("Plasma Whip", world.player)
                           or state.has("Progressive Plasma Whip", world.player))
    add_rule(world.get_location("Annihilation: Hydra'n Seek"),
             lambda state: state.has("Spitting Hydra", world.player)
                           or state.has("Progressive Spitting Hydra", world.player))

    # Second visit: Post-Dax(Meeting Courtney)
    add_rule(world.get_location("Annihilation: Time to SUCC"),
             lambda state: state.has("SUCC Cannon", world.player)
                           or state.has("Progressive SUCC Cannon", world.player))
    add_rule(world.get_location("Annihilation: Chop Chop"),
             lambda state: state.has("Disk-Blade Gun", world.player)
                           or state.has("Progressive Disk-Blade Gun", world.player))
    add_rule(world.get_location("Annihilation: Sleep Inducer"),
             lambda state: state.has("Rift Inducer", world.player)
                           or state.has("Progressive Rift Inducer", world.player))
    add_rule(world.get_location("Annihilation: The Other White Meat"),
             lambda state: state.has("Qwack-O-Ray", world.player)
                           or state.has("Progressive Qwack-O-Ray", world.player))

    # Maybe difficult and long(100 rounds ...), so it restrict after getting items for clear the game.
    add_rule(world.get_location("Annihilation: Qwarktastic Battle"),
             lambda state: state.has("Progressive Vidcomic", world.player, 5)
                           and state.has("Hacker", world.player)
                           and state.has("Tyhrra-Guise", world.player)
                           and state.has("Hypershot", world.player)
                           and state.has("Gravity-Boots", world.player)),

    # ----- Planet Aquatos -----#
    # "Aquatos: Received Flux Rifle": LocData(50001090, "Aquatos"),
    # "Aquatos: T-Bolt: Under the Bridge": LocData(50001091, "Aquatos"),
    # "Aquatos: T-Bolt: Underwater Bolt": LocData(50001092, "Aquatos"),
    add_rule(world.get_location("Aquatos: T-Bolt: Top Left Bolt"),
             lambda state: state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Aquatos: T-Bolt: Swinging Bolt"),
             lambda state: state.has("Hypershot", world.player)
                           and state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Aquatos: T-Bolt: Behind the Locked Gate"),
             lambda state: state.has("Hacker", world.player))
    # "Aquatos: 1 Sewer Crystal Traded": LocData(50001096, "Aquatos"),
    # "Aquatos: 5 Sewer Crystals Traded": LocData(50001097, "Aquatos"),
    # "Aquatos: 10 Sewer Crystals Traded": LocData(50001098, "Aquatos"),
    # "Aquatos: 20 Sewer Crystals Traded": LocData(50001099, "Aquatos"),

    # ----- Planet Tyhrranosis -----#
    # "Tyhrranosis: Received Annihilator": LocData(50001300, "Tyhrranosis"),
    # "Tyhrranosis: Received Holo-Shield Glove": LocData(50001301, "Tyhrranosis"),
    add_rule(world.get_location("Tyhrranosis: T-Bolt: Underground Cave Bolt"),
             lambda state: state.has("Hypershot", world.player))
    # "Tyhrranosis: T-Bolt: South East Cannon": LocData(50001302, "Tyhrranosis"),

    # ----- Planet Daxx -----#
    # "Daxx: Received Charge Boots": LocData(50001322, "Daxx Region 1"),
    add_rule(world.get_location("Daxx: T-Bolt: Right of the Taxi"),
             lambda state: state.has("Hypershot", world.player))
    add_rule(world.get_location("Daxx: T-Bolt: Time Sensitive Door"),
             lambda state: state.has("Hypershot", world.player)
                           and state.has("Charge-Boots", world.player)
                           and state.has("Hacker", world.player))
    add_rule(world.get_location("Daxx: Post-Daxx"),
             lambda state: state.has("Hypershot", world.player))
    add_rule(world.get_location("Daxx: Skill Point: Bugs to Birdie"),
             lambda state: state.has("Qwack-O-Ray", world.player)
                           or state.has("Progressive Qwack-O-Ray", world.player))

    # ----- Obani Gemini -----#
    add_rule(world.get_location("Obani_Gemini: T-Bolt: Follow the Lava"),
             lambda state: state.has("Hypershot", world.player))

    # ----- Planet Blackwater City -----# # Nothing

    # ----- Holostar Studios -----# # Nothing

    # ----- Obani Draco (lol) -----# # Nothing

    # ----- Zeldrin Starport -----# # Nothing

    # ----- Planet Metropolis -----#
    add_rule(world.get_location("Metropolis: T-Bolt: Across the Gap"),
             lambda state: state.has("Hypershot", world.player))

    # ----- Planet Crash Site -----#
    add_rule(world.get_location("Crash Site: T-Bolt: Turn Around"),
             lambda state: state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Crash Site: Received Nano-Pak"),
             lambda state: state.has("Gravity-Boots", world.player))

    # ----- Planet Aridia -----#
    add_rule(world.get_location("Aridia: T-Bolt: Under the Bridge (Assassionation)"),
             lambda state: state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Aridia: T-Bolt: Behind the Base (X12 Endgame)"),
             lambda state: state.has("Gravity-Boots", world.player))

    # ----- Qwark's Hideout -----#
    add_rule(world.get_location("Qwark's_Hideout: Received Gadgetron PDA"),
             lambda state: state.has("Gravity-Boots", world.player))
    add_rule(world.get_location("Qwark's_Hideout: T-Bolt: Glide from the Ramp"),
             lambda state: state.has("Gravity-Boots", world.player))

    # ----- Planet Koros -----#
    add_rule(world.multiworld.get_location("Koros: Skill Point: You break it, you win it", world.player),
             lambda state: state.has("Hyperstrike Smash", world.player))

    # ----- Planet Command Center -----#
    add_rule(world.multiworld.get_location("Command Center: Skill Point: Spread Your Germs", world.player),
             lambda state: state.has("Infector", world.player)
                           or state.has("Progressive Infector", world.player))


def set_rules(world: "RaC3World"):
    # Rules for planets connection
    set_rules_planets(world)

    # Rules for hard to get Location
    set_rules_hard_location(world)

    # world.multiworld.completion_condition[world.player] = lambda state: state.has("Dr. Nefarious Defeated!",
    # world.player)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Biobliterator Defeated!",
                                                                                  world.player)
