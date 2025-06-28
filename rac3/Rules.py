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
             lambda state: state.has("Qwark Vidcomic 1", world.player)
             and state.has("Infobot: Annihilation Nation",world.player))

    #Getting to Aquatos
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aquatos", world.player),
             lambda state: state.has("Infobot: Aquatos", world.player)
             and state.has("Tyhrra-Guise", world.player))

    #Getting to Tyhrranosis
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Tyhrranosis", world.player),
             lambda state: state.has("Infobot: Tyhrranosis", world.player))

    #Getting to Daxx
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Daxx", world.player),
             lambda state: state.has("Infobot: Daxx", world.player))

    #Getting to Obani Gemini
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Obani Gemini", world.player),
             lambda state: state.has("Refractor", world.player)
             and state.has("Infobot: Obani Gemini", world.player)
             and state.has("Qwark Vidcomic 3", world.player))

    #Getting to Rilgar
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Rilgar", world.player),
             lambda state: state.has("Infobot: Rilgar", world.player))

    #Getting to Holostar Studios
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Holostar Studios", world.player),
             lambda state: state.has("Infobot: Holostar Studios", world.player)
             and state.has("Hacker", world.player)
             and state.has("Hypershot", world.player))

    #Getting to Obani Draco (lol)
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Obani Draco", world.player),
             lambda state: state.has("Infobot: Obani Draco", world.player)
             and state.has("Grav-Boots", world.player))

    #Getting to Zeldrin Starport
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Zeldrin Starport", world.player),
             lambda state: state.has("Infobot: Zeldrin Starport", world.player))

    #Getting to Metropolis
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Metropolis", world.player),
             lambda state: state.has("Infobot: Metropolis", world.player)
             and state.has("Qwark Vidcomic 4", world.player))

    #Getting to Zeldrin
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Zeldrin", world.player),
             lambda state: state.has("Infobot: Zeldrin", world.player)
             and state.has("Hypershot", world.player))

    #Getting to Aridia
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aridia", world.player),
             lambda state: state.has("Infobot: Aridia", world.player))

    #Getting to Qwark's Hideout
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Qwarks Hideout", world.player),
             lambda state: state.has("Infobot: Qwarks Hideout", world.player)
             and state.has("Warp Pad", world.player)
             and state.has("Hypershot", world.player))

    #Getting to Koros
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Koros", world.player),
             lambda state: state.has("Infobot: Koros", world.player))

    #Getting to Mylon
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Mylon", world.player),
             lambda state: state.has("Infobot: Mylon", world.player)
             and state.has("Hacker", world.player)
             and state.has("Tyhrra-Guise", world.player)
             and state.has("Hypershot", world.player)
             and state.has("Grav-Boots", world.player))


def set_rules_hard_location(world):
    #----- Planet Veldin -----# # Nothing
    #----- Planet Florana -----# # Nothing

    #----- Starship Phoenix -----#
    # "Phoenix: Received SUCC Cannon": LocData(50001009, "Starship Phoenix"),
    # "Phoenix: Received Infector": LocData(50001010, "Starship Phoenix"),
    # "Phoenix: T-Bolt: Last VR Deck Challenges": LocData(50001011, "Starship Phoenix"),
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
    #"Phoenix: Infobot: Marcadia": LocData(50001019, "Starship Phoenix"),
    add_rule(world.get_location("Phoenix: Infobot: Koros"),
            lambda state: state.can_reach("Qwarks Hideout", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Annihilation Nation"),
            lambda state: state.has("Qwark Vidcomic 1", world.player))
    add_rule(world.get_location("Phoenix: Infobot: Aquatos"),
            lambda state: state.has("Tyhrra-Guise", world.player))
    add_rule(world.get_location("Phoenix: Infobot: Tyhrranosis"),
                lambda state: state.can_reach("Aquatos", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Daxx"),
                lambda state: state.can_reach("Tyhrranosis", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Obani Gemini"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    # "Phoenix: Infobot: Obani Gemini": LocData(50001025, "Starship Phoenix"),
    add_rule(world.get_location("Phoenix: Infobot: Zeldrin"),
                lambda state: state.can_reach("Metropolis Region 2", player=world.player))
    add_rule(world.get_location("Phoenix: Infobot: Qwarks Hideout"),
            lambda state: state.has("Qwark Vidcomic 1", world.player)
            and state.has("Qwark Vidcomic 2", world.player)
            and state.has("Qwark Vidcomic 3", world.player)
            and state.has("Qwark Vidcomic 4", world.player)
            and state.has("Qwark Vidcomic 5", world.player))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 4"),
                lambda state: state.can_reach("Zeldrin Starport Region 2", player=world.player))
    add_rule(world.get_location("Phoenix: Qwark Vidcomic 5"),
                lambda state: state.can_reach("Zeldrin", player=world.player))

    #----- Planet Marcadia -----#
    add_rule(world.get_location("Marcadia: T-Bolt: Last Refractor Room"),
                lambda state: state.has("Refractor", world.player)
                and state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Marcadia: T-Bolt: Ceiling just before Al"),
                lambda state: state.has("Refractor", world.player)
                and state.has("Grav-Boots", world.player))

    #----- Annihilation Nation -----#
    # First visit (when getting Tyhrra-Guise")
    # "Annihilation: Heat Street": LocData(50001067, "Annihilation Nation"),
    # "Annihilation: T-Bolt: Heat Street": LocData(50001042, "Annihilation Nation"),
    # "Annihilation: Grand Prize Bout": LocData(50001044, "Annihilation Nation"),
    # "Annihilation: Robot Rampage": LocData(50001046, "Annihilation Nation"),
    # "Annihilation: 90 Seconds of Carnage": LocData(50001048, "Annihilation Nation"),
    # "Annihilation: Onslaught": LocData(50001049, "Annihilation Nation"),
    # "Annihilation: Whip it Good": LocData(50001050, "Annihilation Nation"),
    # "Annihilation: Hydra'n Seek": LocData(50001051, "Annihilation Nation"),
    # "Annihilation: The Terrible Two": LocData(50001045, "Annihilation Nation"),
    # "Annihilation: Two Minute Warning": LocData(50001047, "Annihilation Nation"),
    # "Annihilation: Championship Bout": LocData(50001052, "Annihilation Nation"),
    # "Annihilation: Qwark Vidcomic 2": LocData(50001075, "Annihilation Nation"),
    
    # Second visit: Post-Dax
    # "Annihilation: BBQ Boulevard": LocData(50001071, "Annihilation Nation"),
    # "Annihilation: Meet Courtney - Arena": LocData(50001053, "Annihilation Nation"),
    # "Annihilation: Qwark Vidcomic 3": LocData(50001076, "Annihilation Nation"),
    
    # After Courtney
    add_rule(world.get_location("Annihilation: Ninja Challenge"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Counting Ducks"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Cycling Weapons"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: One Hit Wonder"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Time to SUCC"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Naptime"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: More Cycling Weapons"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Dodge the Twins"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Chop Chop"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Sleep Inducer"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: The Other White Meat"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Crispy Critter"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Pyro Playground"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Suicide Run"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: T-Bolt: Maze of Blaze"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Maze of Blaze"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))

    # Maybe difficult
    add_rule(world.get_location("Annihilation: Championship Bout II"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Qwarktastic Battle"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: Qwarktastic Battle"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))
    add_rule(world.get_location("Annihilation: The Annihilator (Gauntlet)"),
            lambda state:  state.has("Qwark Vidcomic 3", world.player))

    #----- Planet Aquatos -----#
    add_rule(world.get_location("Aquatos: T-Bolt: Top Left Bolt"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Aquatos: T-Bolt: Swinging Bolt"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Aquatos: T-Bolt: Behind the Locked Gate"),
                lambda state: state.has("Hacker", world.player))
    
    #----- Planet Tyhrranosis -----#
    add_rule(world.get_location("Tyhrranosis: T-Bolt: Underground Cave Bolt"),
                lambda state: state.has("Hypershot", world.player))
    
    #----- Planet Daxx -----#
    add_rule(world.get_location("Daxx: T-Bolt: Right of the Taxi"),
                lambda state: state.has("Hypershot", world.player))
    add_rule(world.get_location("Daxx: T-Bolt: Time Sensitive Door"), # これだけなぜか条件を満たせない。
                lambda state: state.has("Hypershot", world.player)
                and state.has("Charge-Boots", world.player)
                and state.has("Hacker", world.player))

    #----- Obani Gemini -----#
    add_rule(world.get_location("Obani_Gemini: T-Bolt: Follow the Lava"),
                lambda state: state.has("Hypershot", world.player))

    #----- Planet Rilgar -----# # Nothing
    
    # ----- Holostar Studios -----#
    add_rule(world.get_location("Holostar: T-Bolt: Atop the Chairs"),
                lambda state: state.has("Hacker", world.player))
    add_rule(world.get_location("Holostar: T-Bolt: Lot 42's Grav Ramp"),
                lambda state: state.has("Hacker", world.player)
                and state.has("Hypershot", world.player))
    add_rule(world.get_location("Holostar: T-Bolt: Kamikaze Noids"),
                lambda state: state.has("Hacker", world.player)
                and state.has("Hypershot", world.player))

    #----- Obani Draco (lol) -----# # Nothing
    
    #----- Zeldrin Starport -----#
    add_rule(world.get_location("Zeldrin_Starport: Received Bolt Grabber V2"),
                lambda state: state.has("Hypershot", world.player))
    add_rule(world.get_location("Zeldrin_Starport: T-Bolt: Atop the Twin Shooters"),
                lambda state: state.has("Hypershot", world.player))

    #----- Planet Metropolis -----#
    add_rule(world.get_location("Metropolis: T-Bolt: Across the Gap"),
                lambda state: state.has("Hypershot", world.player))
    add_rule(world.get_location("Metropolis: Received Map-O-Matic"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Metropolis: T-Bolt: Tall Tower (Hovership)"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))

    #----- Planet Zeldrin -----#
    add_rule(world.get_location("Zeldrin: T-Bolt: Turn Around"),
                lambda state: state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Zeldrin: Received Nano-Pak"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Zeldrin: Infobot: Aridia"),
                lambda state: state.has("Hypershot", world.player)
                and state.has("Grav-Boots", world.player))
    
    #----- Planet Aridia -----#
    add_rule(world.get_location("Aridia: T-Bolt: Under the Bridge (Assassionation)"),
                lambda state: state.has("Grav-Boots", world.player))
    add_rule(world.get_location("Aridia: T-Bolt: Behind the Base (X12 Endgame)"),
                lambda state: state.has("Grav-Boots", world.player))

    #----- Qwark's Hideout -----#
    add_rule(world.get_location("Qwark's_Hideout: T-Bolt: Glide from the Ramp"),
                lambda state: state.has("Grav-Boots", world.player))
    
    #----- Planet Koros -----# # Nothing
    #----- Planet Mylon -----# # Nothing

    pass

def set_rules(world: "RaC3World"):

    # Rules for planets connection
    set_rules_planets(world)
    
    # Rules for hard to get Location
    set_rules_hard_location(world)

    #world.multiworld.completion_condition[world.player] = lambda state: state.has("Dr. Nefarious Defeated!", world.player)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Biobliterator Defeated!", world.player)

