from BaseClasses import Region
from typing import TYPE_CHECKING
from .Types import RaC3Location
from .Locations import location_table

if TYPE_CHECKING:
    from . import RaC3World

def create_regions(world: "RaC3World"):

    #----- Introduction Sequence -----#
    menu = create_region(world, "Menu")
    veldin = create_region_and_connect(world, "Veldin", "Menu -> Veldin", menu)
    florana = create_region_and_connect(world, "Florana", "Veldin -> Florana", veldin)
    starship_phoenix = create_region_and_connect(world, "Starship Phoenix", "Florana -> Starship Phoenix", veldin)
    starship_phoenix.connect(florana, "Starship Phoenix -> Florana")

    #----- Regions within the game -----#
    marcadia = create_region(world, "Marcadia")
    annihilation_nation = create_region(world, "Annihilation Nation")
    aquatos = create_region(world, "Aquatos")
    tyhrranosis = create_region(world, "Tyhrranosis")
    daxx = create_region(world, "Daxx")
    obani_gemini = create_region(world, "Obani Gemini")
    rilgar = create_region(world, "Rilgar")
    obani_draco = create_region(world, "Obani Draco")
    holostar_studios = create_region(world, "Holostar Studios")
    zeldrin_starport = create_region(world, "Zeldrin Starport")
    metropolis = create_region(world, "Metropolis")
    zeldrin = create_region(world, "Zeldrin")
    aridia = create_region(world, "Aridia")
    quarks_hideout = create_region(world, "Quarks Hideout")
    koros = create_region(world, "Koros")
    mylon = create_region(world, "Mylon") #Victory Location

    #---- Connecting everything to Starship Phoenix -----#
    starship_phoenix.connect(marcadia, "Starship Phoenix -> Marcadia")
    starship_phoenix.connect(annihilation_nation, "Starship Phoenix -> Annihilation Nation")
    starship_phoenix.connect(aquatos, "Starship Phoenix -> Aquatos")
    starship_phoenix.connect(tyhrranosis, "Starship Phoenix -> Tyhrranosis")
    starship_phoenix.connect(daxx, "Starship Phoenix -> Daxx")
    starship_phoenix.connect(obani_gemini, "Starship Phoenix -> Obani Gemini")
    starship_phoenix.connect(rilgar, "Starship Phoenix -> Rilgar")
    starship_phoenix.connect(obani_draco, "Starship Phoenix -> Obani Draco")
    starship_phoenix.connect(holostar_studios, "Starship Phoenix -> Holostar Studios")
    starship_phoenix.connect(zeldrin_starport, "Starship Phoenix -> Zeldrin Starport")
    starship_phoenix.connect(metropolis, "Starship Phoenix -> Metropolis")
    starship_phoenix.connect(zeldrin, "Starship Phoenix -> Zeldrin")
    starship_phoenix.connect(aridia, "Starship Phoenix -> Aridia")
    starship_phoenix.connect(quarks_hideout, "Starship Phoenix -> Quarks Hideout")
    starship_phoenix.connect(koros, "Starship Phoenix -> Koros")
    starship_phoenix.connect(mylon, "Starship Phoenix -> Mylon")


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
