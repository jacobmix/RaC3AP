from enum import  IntEnum
from typing import Optional, NamedTuple, Tuple, Dict, List
from math import ceil
import struct
from logging import Logger
from time import sleep, time

from .pcsx2_interface.pine import Pine
from .Rac3Addresses import LOCATIONS, CHECK_TYPE, COMPARE_TYPE, ADDRESSES
from . import Items, Locations
import random

class Dummy(IntEnum):
    test = 0

class GameInterface():
    """
    Base class for connecting with a pcsx2 game
    """

    pcsx2_interface: Pine = Pine()
    logger: Logger
    game_id_error: Optional[str] = None
    current_game: Optional[str] = None
    addresses: Dict = {}

    def __init__(self, logger) -> None:
        self.logger = logger

    def _read8(self, address: int):
        return self.pcsx2_interface.read_int8(address)

    def _read16(self, address: int):
        return self.pcsx2_interface.read_int16(address)

    def _read32(self, address: int):
        return self.pcsx2_interface.read_int32(address)

    def _read_bytes(self, address: int, n: int):
        return self.pcsx2_interface.read_bytes(address, n)

    def _read_float(self, address: int):
        return struct.unpack("f",self.pcsx2_interface.read_bytes(address, 4))[0]

    def _write8(self, address: int, value: int):
        self.pcsx2_interface.write_int8(address, value)

    def _write16(self, address: int, value: int):
        self.pcsx2_interface.write_int16(address, value)

    def _write32(self, address: int, value: int):
        self.pcsx2_interface.write_int32(address, value)

    def _write_bytes(self, address: int, value: bytes):
        self.pcsx2_interface.write_bytes(address, value)

    def connect_to_game(self):
        """
        Initializes the connection to PCSX2 and verifies it is connected to the
        right game
        """
        if not self.pcsx2_interface.is_connected():
            self.pcsx2_interface.connect()
            if not self.pcsx2_interface.is_connected():
                return
            self.logger.info("Connected to PCSX2 Emulator")
        try:
            game_id = self.pcsx2_interface.get_game_id()
            # The first read of the address will be null if the client is faster than the emulator
            self.current_game = None
            if game_id in ADDRESSES.keys():
                self.current_game = game_id
                self.addresses = ADDRESSES[game_id]
            if self.current_game is None and self.game_id_error != game_id and game_id != b'\x00\x00\x00\x00\x00\x00':
                self.logger.warning(
                    f"Connected to the wrong game ({game_id})")
                self.game_id_error = game_id
        except RuntimeError:
            pass
        except ConnectionError:
            pass

    def disconnect_from_game(self):
        self.pcsx2_interface.disconnect()
        self.current_game = None
        self.logger.info("Disconnected from PCSX2 Emulator")

    def get_connection_state(self) -> bool:
        try:
            connected = self.pcsx2_interface.is_connected()
            return connected and self.current_game is not None
        except RuntimeError:
            return False

class Rac3Interface(GameInterface):
    ########################################
    # Mandatory functions                  #
    ########################################

    # Called at once when client started
    def Init(self):
        self.InitVariables()
        self.removeAllWeapons()
        self.removeAllGadgets()
        self.removeAllPlanets()

    # Called in periodically
    def Update(self):
        # Memory checkiing
        self.GadgetCycler()
        self.PlanetCycler()
        self.WeaponCycler()
        self.ArmorCycler()
        self.VerifyQuickSelectAndLastUsed()
        addr = ADDRESSES[self.current_game]["boltXPMultiplier"]
        addr = self.AddressConvert(addr)
        self._write8(addr, self.boltandXPMultiplierValue)


    def get_victory_code(self):
        victory_name = "Mylon: Biobliterator Defeated!" # This must can be changed by option
        return Locations.location_table[victory_name].ap_code

    def proc_option(self, slot_data):
        self.logger.info(f"{slot_data}")
        self.startingWeapon = slot_data["options"]["StartingWeapon"]
        self.boltandXPMultiplier = slot_data["options"]["BoltandXPMultiplier"]

    def item_received(self, item_code, processed_items_count = 0):
        # self.logger.info(f"{item_code}")
        if list(Items.weapon_items.values())[0].ap_code <= item_code and \
            item_code <= list(Items.weapon_items.values())[-1].ap_code:
            self.ReceivedWeapon(item_code)
        elif list(Items.progressive_weapons.values())[0].ap_code <= item_code and \
            item_code <= list(Items.progressive_weapons.values())[-1].ap_code:
            self.ReceivedWeaponProgressive(item_code)
        elif list(Items.gadget_items.values())[0].ap_code <= item_code and \
            item_code <= list(Items.gadget_items.values())[-1].ap_code:
            self.ReceivedGadget(item_code)
        elif list(Items.post_planets.values())[0].ap_code <= item_code and \
            item_code <= list(Items.post_planets.values())[-1].ap_code:
            self.ReceivedPlanet(item_code)
        elif list(Items.qwark_vidcomics.values())[0].ap_code <= item_code and \
            item_code <= list(Items.qwark_vidcomics.values())[-1].ap_code:
            self.ReceivedVidComic(item_code)
        elif list(Items.progressive_armor.values())[0].ap_code <= item_code and \
            item_code <= list(Items.progressive_armor.values())[-1].ap_code:
            self.ReceivedArmor(item_code)
        elif processed_items_count >= 0: # To avoid duplicated items sending when reconnection, First attempt is skipped.
            self.ReceivedOthers(item_code)


    def is_location_checked(self, ap_code):
        target_location = {}
        # search target location
        for location in LOCATIONS:
            if location["Id"] == ap_code:
                target_location = location
                break

        # Check location flag
        _value = 0
        addr = target_location["Address"]
        addr = self.AddressConvert(addr)
        if target_location["CheckType"] == CHECK_TYPE["bit"] or \
            target_location["CheckType"] == CHECK_TYPE["falseBit"]:
            _value = self._read8(addr)
            _value = (_value >> target_location["AddressBit"]) & 0x01
        elif target_location["CheckType"] == CHECK_TYPE["byte"]:
            _value = self._read8(addr)
        elif target_location["CheckType"] == CHECK_TYPE["short"]:
            _value = self._read16(addr)
        else:
            _value = self._read32(addr)

        _compare_value = 0
        if target_location["CheckType"] == CHECK_TYPE["bit"]:
            _compare_value = 0x01
        elif target_location["CheckType"] == CHECK_TYPE["falseBit"]:
            _compare_value = 0x00
        else:
            _compare_value = int(target_location["CheckValue"], 0)

        _compare_type = COMPARE_TYPE["Match"]
        if 'CompareType' in target_location:
            _compare_type = target_location["CompareType"]

        if _compare_type == COMPARE_TYPE["Match"]:
            return (_value == _compare_value)
        elif _compare_type == COMPARE_TYPE["GreaterThan"]:
            return (_value > _compare_value)
        elif _compare_type == COMPARE_TYPE["LessThan"]:
            return (_value < _compare_value)

    ###################################
    # Game dedicated functions        #
    ###################################

    def __init__(self, logger):
        super().__init__(logger)  # GameInterfaceの初期化
    
    def InitVariables(self):
        # Unlock state variables/ArmorUpgrade variable
        self.UnlockWeapons = {name: {"status": 0, "unlockDelay": 0} for name in ADDRESSES[self.current_game]["Weapons"].keys()}
        self.UnlockGadgets = {name: {"status": 0, "unlockDelay": 0}  for name in ADDRESSES[self.current_game]["Gadgets"].keys()}
        self.UnlockVidComics = {name: {"status": 0, "unlockDelay": 0}  for name in ADDRESSES[self.current_game]["VidComics"].keys()}
        self.UnlockPlanets = {name: {"status": 0, "unlockDelay": 0}  for name in ADDRESSES[self.current_game]["PlanetValues"].keys()}
        self.UnlockArmor = {"status": 0, "unlockDelay": 0}
        
        # Proc options
        ### Starting Weapon
        for name, weapon_data in self.UnlockWeapons.items():
            if name == self.startingWeapon:
                self.UnlockWeapons[name]["status"] = 1
                # Initial ammo
                if ADDRESSES[self.current_game]["Weapons"][name]["lv1Ammo"] != 0:
                    ammo = ADDRESSES[self.current_game]["Weapons"][name]["lv1Ammo"] 
                    addr = ADDRESSES[self.current_game]["Weapons"][name]["ammoAddress"]
                    addr = self.AddressConvert(addr)
                    self._write32(addr, ammo)
        # self.logger.info(f"self.UnlockWeapons.items(): {self.UnlockWeapons.items()}")
        ### Bolt and XPMultiplier
        val = int(self.boltandXPMultiplier[1:])
        self.boltandXPMultiplierValue = val - 1 # 0 = x1, 1 = x2, 3 = x4 ...

    # Address conversion from str to int(with US to JP)
    def AddressConvert(self, address):
        _addr = address
        if isinstance(address, str):
            _addr = int(address, 0)
        if 0x001BBB00 <= _addr and _addr <= 0x001BBBFF: # T-Bolt
            _addr += 0x9298
        elif 0x001D554F <= _addr and _addr <= 0x001D55543: # VidComic
            _addr += 0x9300
        elif 0x00100000 <= _addr and _addr <= 0x00100050: # DummyEXP
            _addr += 0
        elif 0x001D4C00 <= _addr and _addr <= 0x001D4CFF : # Equipped garamecha
            _addr += 0x92C0
        else:
            _addr -= 0x80
        return _addr

    # initialization
    def removeAllWeapons(self):
        for dict_data in ADDRESSES[self.current_game]["Weapons"].values():
            addr = dict_data["unlockAddress"]
            addr = self.AddressConvert(addr)
            self._write8(addr, 0)
    def removeAllGadgets(self):
        for dict_data in ADDRESSES[self.current_game]["Gadgets"].values():
            addr = dict_data["unlockAddress"]
            addr = self.AddressConvert(addr)
            self._write8(addr, 0)
        for dict_data in ADDRESSES[self.current_game]["VidComics"].values():
            addr = dict_data["unlockAddress"]
            addr = self.AddressConvert(addr)
            self._write8(addr, 0)
    def removeAllPlanets(self):
        for addr in ADDRESSES[self.current_game]["PlanetSlots"]:
            addr = self.AddressConvert(addr)
            self._write32(addr, 0)
        # Defailt Unlocked plantes
        self.UnlockPlanets["Veldin"]["status"] = 1
        self.UnlockPlanets["Florana"]["status"] = 1
        self.UnlockPlanets["Starship Phoenix"]["status"] = 1
        self.UnlockPlanets["Museum"]["status"] = 1

    # interval update function: Check unlock/lock status of items
    def WeaponCycler(self):
        for name, dict_data in self.UnlockWeapons.items():
            unlock_status = dict_data["status"]
            addr = ADDRESSES[self.current_game]["Weapons"][name]["unlockAddress"]
            addr = self.AddressConvert(addr)

            # self.logger.info(f"[WeaponCycler] {name}: status={unlock_status}, delay={self.UnlockWeapons[name]['unlockDelay']}, addr={hex(addr)}")
            if unlock_status == 0:
                self.UnlockWeapons[name]["unlockDelay"] += 1
                if dict_data["unlockDelay"] > 1:
                    self._write8(addr, 0)
                    self.UnlockWeapons[name]["unlockDelay"] = 0
            else:
                self._write8(addr, 1)

        addr = ADDRESSES[self.current_game]["CurrentEquipped"]
        addr = self.AddressConvert(addr)
        currentEquipped = self._read8(addr)
        for weapon_name, weapon_data in ADDRESSES[self.current_game]["Weapons"].items():
            if currentEquipped == weapon_data["id"] and self.UnlockWeapons[weapon_name]["status"] == 0:  # Not unlocked, but set case
                self._write8(addr, 9) # 9 is omnirench

    def GadgetCycler(self):
        for name, dict_data in self.UnlockGadgets.items():
            unlock_status = dict_data["status"]
            addr = ADDRESSES[self.current_game]["Gadgets"][name]["unlockAddress"]
            addr = self.AddressConvert(addr)

            if unlock_status == 0:
                self.UnlockGadgets[name]["unlockDelay"] += 1
                if dict_data["unlockDelay"] > 1:
                    val = self._read8(addr)
                    self._write8(addr,  (val & 0xfe) )
                    self.UnlockGadgets[name]["unlockDelay"] = 0
            else:
                # Get Gadget in event
                if name in ["Hacker", "Hypershot", "Tyhrra-Guise", "Grav-Boots", "Map-O-Matic", "Warp Pad"]: 
                    self._write8(addr, 2) # 0x2=0b0010
                # Get Gadget in field
                else:
                    self._write8(addr, 1) # 0x1

        for name, dict_data in self.UnlockVidComics.items():
            unlock_status = dict_data["status"]
            addr = ADDRESSES[self.current_game]["VidComics"][name]["unlockAddress"]
            addr = self.AddressConvert(addr)
            
            unlockDelayCount = 1
            if name == "Qwark Vidcomic 2":
                unlockDelayCount = 30 # WA for Annihilation Station Proceeding

            if unlock_status == 0:
                self.UnlockVidComics[name]["unlockDelay"] += 1
                if dict_data["unlockDelay"] > unlockDelayCount:
                    self._write8(addr, 0)
                    self.UnlockVidComics[name]["unlockDelay"] = 0
            else:
                self._write8(addr, 1)

    def PlanetCycler(self):
        for idx, name in enumerate(self.UnlockPlanets.keys()):
            addr = ADDRESSES[self.current_game]["PlanetSlots"][idx]
            addr = self.AddressConvert(addr)
            if self.UnlockPlanets[name]["status"] == 1:
                self._write8(addr, ADDRESSES[self.current_game]["PlanetValues"][name])
            else:
                self._write8(addr, 0)
            
            # For avoiding Deadlock, Hotostar is locked until Hacker and HyperShot is unlocked,
            if name == "Holostar Studios":
                if (self.UnlockGadgets["Hacker"]["status"] == 0 or self.UnlockGadgets["Hypershot"]["status"] == 0):
                    self._write8(addr, 0)    
                

    def ArmorCycler(self):
        addr = ADDRESSES[self.current_game]["ArmorVersion"]
        addr = self.AddressConvert(addr)
        currentArmorValue = self._read8(addr)

        if currentArmorValue !=  self.UnlockArmor["status"]:
            self.UnlockArmor["unlockDelay"] += 1
            if self.UnlockArmor["unlockDelay"] > 1:
                self._write8(addr, self.UnlockArmor["status"])
                self.UnlockArmor["unlockDelay"] = 0

    def VerifyQuickSelectAndLastUsed(self):
        _slots = ADDRESSES[self.current_game]["QuickSelectSlots"] + ADDRESSES[self.current_game]["LastUsed"]
        for addr in _slots:
            addr = self.AddressConvert(addr)
            slot_val = self._read8(addr)
            for weapon_name, weapon_data in ADDRESSES[self.current_game]["Weapons"].items():
                if slot_val == weapon_data["id"] and self.UnlockWeapons[weapon_name]["status"] == 0:  # Not unlocked, but set case
                    self._write8(addr, 0)
                    continue
            for gadget_name, gadget_data in ADDRESSES[self.current_game]["Gadgets"].items():
                if slot_val == gadget_data["id"] and self.UnlockGadgets[gadget_name]["status"] == 0: # Not unlocked, but set case
                    self._write8(addr, 0)
                    continue

    def ReceivedWeapon(self, ap_code):
        for name, item_data in Items.weapon_items.items():
            if item_data.ap_code == ap_code:
                self.UnlockWeapons[name]["status"] = 1

    def ReceivedWeaponProgressive(self, ap_code): # Not implemented as of now
        pass

    def ReceivedGadget(self, ap_code):
        for name, item_data in Items.gadget_items.items():
            if item_data.ap_code == ap_code:
                self.UnlockGadgets[name]["status"] = 1

    def ReceivedPlanet(self, ap_code):
        for name, item_data in Items.post_planets.items():
            if item_data.ap_code == ap_code:
                name = name.replace("Infobot: ","")
                self.UnlockPlanets[name]["status"] = 1

    def ReceivedVidComic(self, ap_code):
        for name, item_data in Items.qwark_vidcomics.items():
            if item_data.ap_code == ap_code:
                self.UnlockVidComics[name]["status"] = 1

    def ReceivedArmor(self, ap_code):
        self.UnlockArmor["status"] += 1
        if self.UnlockArmor["status"] > 4:
            self.UnlockArmor["status"] = 4

    def ReceivedOthers(self, ap_code):
        # Get Titanium Bolt
        if ap_code == Items.t_bolts["Titanium Bolt"].ap_code:
            pass # Nothing to do

        if ap_code == Items.junk_items["Bolts"].ap_code: # Random get bolts
            addr = ADDRESSES[self.current_game]["Bolt"]
            addr = self.AddressConvert(addr)
            bolt = self._read32(addr)
            self._write32(addr, bolt + 1000 * random.randint(1, 100))

        # Little buggy, but it works in general.
        # ToDo Fix this function
        if ap_code == Items.junk_items["Weapon EXP"].ap_code: # Random Weapon Upgrade
            unlocked_weapon_names = [name for name, data in self.UnlockWeapons.items() if data["status"] == 1]
            # Avoid LevelMax weapon
            for weapon_name in unlocked_weapon_names:
                target_weapon_data = [data for data in LOCATIONS if f"{weapon_name}: V" in data["Name"]]
                # self.logger.info(f"target_weapon_data[{len(target_weapon_data)}]: {target_weapon_data}")
                if len(target_weapon_data) > 0:
                    exp_list = [data["CheckValue"] for data in target_weapon_data] # Exp for v2~v5
                    addr = target_weapon_data[0]["Address"]
                    addr = self.AddressConvert(addr)
                    current_exp = self._read32(addr)
                    if current_exp >= int(exp_list[-1], 0):
                        unlocked_weapon_names.remove(weapon_name)

            if len(unlocked_weapon_names) > 0:
                weapon_num = random.randint(0, len(unlocked_weapon_names)-1)
                weapon_name = unlocked_weapon_names[weapon_num]
                target_weapon_data = [data for data in LOCATIONS if f"{weapon_name}: V" in data["Name"]]
                exp_list = [data["CheckValue"] for data in target_weapon_data] # Exp for v2~v5
                addr = target_weapon_data[0]["Address"]
                addr = self.AddressConvert(addr)
                current_exp = self._read32(addr)
                for target_exp in exp_list:    
                    if current_exp < int(target_exp, 0):
                        self._write32(addr, int(target_exp, 0))
                        break
