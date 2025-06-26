from worlds.generic.Rules import add_rule, set_rule
from .Types import weapon_type_to_shortened_name
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def set_rules(world: "RaC3World"):

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
             and state.has("Hacker", world.player))

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


    #world.multiworld.completion_condition[world.player] = lambda state: state.has("Dr. Nefarious Defeated!", world.player)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Biobliterator Defeated!", world.player)

