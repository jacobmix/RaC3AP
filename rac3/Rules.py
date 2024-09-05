from worlds.generic.Rules import add_rule, set_rule
from .Types import weapon_type_to_shortened_name
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def set_rules(world: "RaC3World"):
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Marcadia", world.player),
             lambda state: state.has("Post-Starship Phoenix 1", world.player))
    add_rule(world.multiworld.get_entrance("Starship Phoenix -> Annihilation Nation", world.player),
             lambda state: state.has("Post-Marcadia", world.player))


    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)