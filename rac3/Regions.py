from BaseClasses import Region
from typing import TYPE_CHECKING
from .Types import RaC3Location
from .Locations import location_table

if TYPE_CHECKING:
    from . import RaC3World


def create_regions(world: "RaC3World"):
    # ----- Introduction Sequence -----#
    menu = create_region(world, "Menu")
    veldin = create_region_and_connect(world, "Veldin", "Menu -> Veldin", menu)
    florana = create_region_and_connect(world, "Florana", "Veldin -> Florana", veldin)
    starship_phoenix = create_region_and_connect(world, "Starship Phoenix", "Florana -> Starship Phoenix", florana)
    starship_phoenix.connect(florana, "Starship Phoenix -> Florana")

    # ----- Regions within the game -----#
    marcadia_first_half = create_region(world, "Marcadia Region 1")
    annihilation_nation = create_region(world, "Annihilation Nation")
    aquatos = create_region(world, "Aquatos")
    tyhrranosis = create_region(world, "Tyhrranosis")
    daxx_first_half = create_region(world, "Daxx Region 1")
    obani_gemini = create_region(world, "Obani Gemini")
    blackwater_city = create_region(world, "Blackwater City")
    obani_draco = create_region(world, "Obani Draco")
    holostar_studios = create_region(world, "Holostar Studios")
    zeldrin_starport_first_half = create_region(world, "Zeldrin Starport Region 1")
    metropolis_first_half = create_region(world, "Metropolis Region 1")
    crash_site = create_region(world, "Crash Site")
    aridia = create_region(world, "Aridia")
    qwarks_hideout = create_region(world, "Qwarks Hideout")
    koros = create_region(world, "Koros")
    command_center = create_region(world, "Command Center")  # Victory Location

    # ----- Connecting everything to Starship Phoenix -----#
    starship_phoenix.connect(marcadia_first_half, "Starship Phoenix -> Marcadia")
    starship_phoenix.connect(annihilation_nation, "Starship Phoenix -> Annihilation Nation")
    starship_phoenix.connect(aquatos, "Starship Phoenix -> Aquatos")
    starship_phoenix.connect(tyhrranosis, "Starship Phoenix -> Tyhrranosis")
    starship_phoenix.connect(daxx_first_half, "Starship Phoenix -> Daxx")
    starship_phoenix.connect(obani_gemini, "Starship Phoenix -> Obani Gemini")
    starship_phoenix.connect(blackwater_city, "Starship Phoenix -> Blackwater City")
    starship_phoenix.connect(obani_draco, "Starship Phoenix -> Obani Draco")
    starship_phoenix.connect(holostar_studios, "Starship Phoenix -> Holostar Studios")
    starship_phoenix.connect(zeldrin_starport_first_half, "Starship Phoenix -> Zeldrin Starport")
    starship_phoenix.connect(metropolis_first_half, "Starship Phoenix -> Metropolis")
    starship_phoenix.connect(crash_site, "Starship Phoenix -> Crash Site")
    starship_phoenix.connect(aridia, "Starship Phoenix -> Aridia")
    starship_phoenix.connect(qwarks_hideout, "Starship Phoenix -> Qwarks Hideout")
    starship_phoenix.connect(koros, "Starship Phoenix -> Koros")
    starship_phoenix.connect(command_center, "Starship Phoenix -> Command Center")

    # ----- Split planet connections for gadget reasons -----#

    # Marcadia later part requires Grav Boots for titan bolts
    marcadia_second_half = create_region(world, "Marcadia Region 2")
    marcadia_first_half.connect(marcadia_second_half,
                                rule=lambda state: state.has("Refractor", world.player)
                                                   and state.has("Gravity-Boots", world.player)),

    # Annihilation mission is shown after Daxx Region2
    annihilation_nation_second_half = create_region(world, "Annihilation Nation 2")
    annihilation_nation.connect(annihilation_nation_second_half,
                                rule=lambda state: state.can_reach("Daxx Region 2", player=world.player)),

    tyhrranosis_second_half = create_region(world, "Tyhrranosis Region 2")
    tyhrranosis.connect(tyhrranosis_second_half,
                        rule=lambda state: state.can_reach("Tyhrranosis", player=world.player)),

    # You can get the charge boots without hacker or hypershot
    daxx_second_half = create_region(world, "Daxx Region 2")
    daxx_first_half.connect(daxx_second_half,
                            rule=lambda state: state.has("Hypershot", world.player)
                                               and state.has("Hacker", world.player)),

    # You can do the Qwark half of Zeldrin Starport with no other requirements
    zeldrin_starport_second_half = create_region(world, "Zeldrin Starport Region 2")
    zeldrin_starport_first_half.connect(zeldrin_starport_second_half,
                                        rule=lambda state: state.has("Hypershot", world.player)),

    # You can get Metal-Noids in metropolis with no other requirements
    metropolis_second_half = create_region(world, "Metropolis Region 2")
    metropolis_first_half.connect(metropolis_second_half,
                                  rule=lambda state: state.has("Gravity-Boots", world.player)
                                                     and state.has("Refractor", world.player)),

    # ----- Dummy regions for weapon upgrade organization -----#

    shock_blaster_upgrades = create_region(world, "Shock Blaster Upgrades")
    menu.connect(shock_blaster_upgrades, rule=lambda state: state.has("Shock Blaster", world.player)),

    nitro_launcher_upgrades = create_region(world, "Nitro Launcher Upgrades")
    menu.connect(nitro_launcher_upgrades, rule=lambda state: state.has("Nitro Launcher", world.player)),

    n60_storm_upgrades = create_region(world, "N60 Storm Upgrades")
    menu.connect(n60_storm_upgrades, rule=lambda state: state.has("N60 Storm", world.player)),

    plasma_whip_upgrades = create_region(world, "Plasma Whip Upgrades")
    menu.connect(plasma_whip_upgrades, rule=lambda state: state.has("Plasma Whip", world.player)),

    infector_upgrades = create_region(world, "Infector Upgrades")
    menu.connect(infector_upgrades, rule=lambda state: state.has("Infector", world.player)),

    suck_cannon_upgrades = create_region(world, "Suck Cannon Upgrades")
    menu.connect(suck_cannon_upgrades, rule=lambda state: state.has("SUCC Cannon", world.player)),

    spitting_hydra_upgrades = create_region(world, "Spitting Hydra Upgrades")
    menu.connect(spitting_hydra_upgrades, rule=lambda state: state.has("Spitting Hydra", world.player)),

    agents_of_doom_upgrades = create_region(world, "Agents of Doom Upgrades")
    menu.connect(agents_of_doom_upgrades, rule=lambda state: state.has("Agents of Doom", world.player)),

    flux_rifle_upgrades = create_region(world, "Flux Rifle Upgrades")
    menu.connect(flux_rifle_upgrades, rule=lambda state: state.has("Flux Rifle", world.player)),

    annihilator_upgrades = create_region(world, "Annihilator Upgrades")
    menu.connect(annihilator_upgrades, rule=lambda state: state.has("Annihilator", world.player)),

    holo_shield_glove_upgrades = create_region(world, "Holo-Shield Glove Upgrades")
    menu.connect(holo_shield_glove_upgrades, rule=lambda state: state.has("Holo-Shield Glove", world.player)),

    disk_blade_gun_upgrades = create_region(world, "Disk-Blade Gun Upgrades")
    menu.connect(disk_blade_gun_upgrades, rule=lambda state: state.has("Disk-Blade Gun", world.player)),

    rift_inducer_upgrades = create_region(world, "Rift Inducer Upgrades")
    menu.connect(rift_inducer_upgrades, rule=lambda state: state.has("Rift Inducer", world.player)),

    qwack_o_ray_upgrades = create_region(world, "Qwack-O-Ray Upgrades")
    menu.connect(qwack_o_ray_upgrades, rule=lambda state: state.has("Qwack-O-Ray", world.player)),

    RY3N0_upgrades = create_region(world, "RY3N0 Upgrades")
    menu.connect(RY3N0_upgrades, rule=lambda state: state.has("RY3N0", world.player)),

    mega_turret_glove_upgrades = create_region(world, "Mini-Turret Glove Upgrades")
    menu.connect(mega_turret_glove_upgrades, rule=lambda state: state.has("Mini-Turret Glove", world.player)),

    lava_gun_upgrades = create_region(world, "Lava Gun Upgrades")
    menu.connect(lava_gun_upgrades, rule=lambda state: state.has("Lava Gun", world.player)),

    tesla_barrier_upgrades = create_region(world, "Shield Charger Upgrades")
    menu.connect(tesla_barrier_upgrades, rule=lambda state: state.has("Shield Charger", world.player)),

    bouncer_upgrades = create_region(world, "Bouncer Upgrades")
    menu.connect(bouncer_upgrades, rule=lambda state: state.has("Bouncer", world.player)),

    plasma_coil_upgrades = create_region(world, "Plasma Coil Upgrades")
    menu.connect(plasma_coil_upgrades, rule=lambda state: state.has("Plasma Coil", world.player))


def create_region(world: "RaC3World", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    for (key, data) in location_table.items():
        if data.region == name:
            location = RaC3Location(world.player, key, data.ap_code, reg)
            reg.locations.append(location)

    world.multiworld.regions.append(reg)
    return reg


def create_region_and_connect(world: "RaC3World",
                              name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg
