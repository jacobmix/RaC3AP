from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, DefaultOnToggle


def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in rac3_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class StartingWeapon(Choice):
    """
    Determines which weapon you will be starting with in the game
    """
    display_name = "Starting Weapon"
    option_shock_cannon = 1
    option_nitro_launcher = 2
    option_n60_storm = 3
    option_infector = 5
    option_suck_cannon = 6
    option_spitting_hydra = 7
    option_agents_of_doom = 8
    option_flux_rifle = 9
    option_annihilator = 10
    option_holo_shield_glove = 11
    option_disk_blade_gun = 12
    option_rift_inducer = 13
    option_qwack_o_ray = 14
    option_ry3n0 = 15
    option_mega_turret_glove = 16
    option_lava_gun = 17
    option_tesla_barrier = 18
    option_bouncer = 19
    option_plasma_coil = 20
    default = 1

@dataclass
class RaC3Options(PerGameCommonOptions):
    StartingWeapon:            StartingWeapon

rac3_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartingWeapon]
}

slot_data_options: List[str] = {
    "StartingWeapon"
}