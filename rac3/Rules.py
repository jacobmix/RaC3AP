from worlds.generic.Rules import add_rule, set_rule
from .Types import weapon_type_to_shortened_name
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def set_rules(world: "RaC3World"):

    # Getting to Annihilation Nation:
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Annihilation Nation", world.player),
             lambda state: state.has("Qwark Vidcomic 1", world.player)
             and state.has("Infobot: Annihilation Nation",world.player))

    #Getting to Aquatos
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aquatos", world.player),
             lambda state: state.has("Infobot: Aquatos", world.player))

    #Getting to Tyhrranosis
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Tyhrranosis", world.player),
             lambda state: state.has("Infobot: Tyhrranosis", world.player)
             and state.has("Tyhrra-Guise", world.player))





    '''
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Marcadia", world.player),
            lambda state: state.has("Post-Starship Phoenix: Marcadia", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Annihilation Nation", world.player),
            lambda state: state.has("Post-Starship Phoenix: Annihilation Nation", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Aquatos", world.player),
            lambda state: state.has("Post-Starship Phoenix: Aquatos", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Tyhrranosis", world.player),
             lambda state: state.has("Post-Starship Phoenix: Tyhrranosis", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Daxx", world.player),
             lambda state: state.has("Post-Starship Phoenix: Daxx", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Metropolis", world.player),
             lambda state: state.has("Post-Starship Phoenix: Metropolis", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Koros", world.player),
             lambda state: state.has("Post-Starship Phoenix: Koros", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Qwarks Hideout", world.player),
             lambda state: state.has("Post-Starship Phoenix: Qwarks Hideout", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Obani Gemini", world.player),
             lambda state: state.has("Post-Daxx: Obani Gemini",world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Rilgar", world.player),
             lambda state: state.has("Post-Obani Gemini", world.player))
    '''

    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Mylon", world.player),
             lambda state: state.has("Post-Koros", world.player)
             and state.has("Hacker", world.player))

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Dr. Nefarious Defeated!", world.player)