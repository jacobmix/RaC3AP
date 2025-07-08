CHECK_TYPE = {
    "bit": 0,
    "int": 1,
    "uint": 2,
    "byte": 3,
    "short": 4,
    "falseBit": 5,
    "long": 6,
    "nibble": 7,
}
COMPARE_TYPE = {
    "Match": 0,
    "GreaterThan": 1,
    "LessThan": 2,
}

ADDRESSES = {
  "SCPS-15084": {
    "Weapons": {
      "Shock Blaster":     {"unlockAddress": 0x00142CC7, "id": 39,  "ammoAddress": 0x0014288C, "lv1Ammo": 30, },
      "Nitro Launcher":    {"unlockAddress": 0x00142D17, "id": 119, "ammoAddress": 0x001429CC, "lv1Ammo": 8, },
      "N60 Storm":         {"unlockAddress": 0x00142CCF, "id": 47,  "ammoAddress": 0x001428AC, "lv1Ammo": 150, },
      "Plasma Whip":       {"unlockAddress": 0x00142D1F, "id": 127, "ammoAddress": 0x001429EC, "lv1Ammo": 25, },
      "Infector":          {"unlockAddress": 0x00142CD7, "id": 55,  "ammoAddress": 0x001428CC, "lv1Ammo": 15, },
      "SUCC Cannon":       {"unlockAddress": 0x00142D27, "id": 135, "ammoAddress": 0x00000000, "lv1Ammo": 0, },
      "Spitting Hydra":    {"unlockAddress": 0x00142CE7, "id": 71,  "ammoAddress": 0x0014290C, "lv1Ammo": 15, },
      "Agents of Doom":    {"unlockAddress": 0x00142CF7, "id": 87,  "ammoAddress": 0x0014294C, "lv1Ammo": 6, },
      "Flux Rifle":        {"unlockAddress": 0x00142D0F, "id": 111, "ammoAddress": 0x001429AC, "lv1Ammo": 10, },
      "Annihilator":       {"unlockAddress": 0x00142CDF, "id": 63,  "ammoAddress": 0x001428EC, "lv1Ammo": 20, },
      "Holo-Shield Glove": {"unlockAddress": 0x00142D07, "id": 103, "ammoAddress": 0x0014298C, "lv1Ammo": 8, },
      "Disk-Blade Gun":    {"unlockAddress": 0x00142CEF, "id": 79,  "ammoAddress": 0x0014292C, "lv1Ammo": 25, },
      "Rift Inducer":      {"unlockAddress": 0x00142CFF, "id": 95,  "ammoAddress": 0x0014296C, "lv1Ammo": 8, },
      "Qwack-O-Ray":       {"unlockAddress": 0x00142D2F, "id": 143, "ammoAddress": 0x00000000, "lv1Ammo": 0, },
      "RY3N0":             {"unlockAddress": 0x00142D37, "id": 151, "ammoAddress": 0x00142A4C, "lv1Ammo": 25, },
      "Mega-Turret Glove": {"unlockAddress": 0x00142CB5, "id": 21,  "ammoAddress": 0x00142844, "lv1Ammo": 10, },
      "Lava Gun":          {"unlockAddress": 0x00142CB1, "id": 17,  "ammoAddress": 0x00142834, "lv1Ammo": 150, },
      "Shield Charger":    {"unlockAddress": 0x00142CB6, "id": 22,  "ammoAddress": 0x00142848, "lv1Ammo": 3, },
      "Bouncer":           {"unlockAddress": 0x00142CB3, "id": 19,  "ammoAddress": 0x0014283C, "lv1Ammo": 10, },
      "Plasma Coil":       {"unlockAddress": 0x00142CB0, "id": 16,  "ammoAddress": 0x00142830, "lv1Ammo": 15, },
    },
    "Gadgets": {
      "Hacker" :         {"unlockAddress": 0x00142CB4, "id": 0,    },
      "Hypershot":       {"unlockAddress": 0x00142CAB, "id": 11,    },
      "Refractor":       {"unlockAddress": 0x00142CB2, "id": 18,    },
      "Tyhrra-Guise":    {"unlockAddress": 0x00142CBE, "id": 30,    },
      "Grav-Boots":      {"unlockAddress": 0x00142CAD, "id": 0,    },
      "Bolt Grabber V2": {"unlockAddress": 0x00142CA7, "id": 0,    },
      "Map-O-Matic":     {"unlockAddress": 0x00142CA5, "id": 0,    },
      "Nano Pak":        {"unlockAddress": 0x00142CC0, "id": 0,    },
      "Warp Pad":        {"unlockAddress": 0x00142CBF, "id": 31,    },
      "Gadgetron PDU":   {"unlockAddress": 0x00142CC3, "id": 35,    },
      "Charge-Boots":    {"unlockAddress": 0x00142CBD, "id": 0,    },
    },
    "VidComics": {
      "Qwark Vidcomic 1": {"unlockAddress": 0x001D554F },
      "Qwark Vidcomic 2": {"unlockAddress": 0x001D5551 },
      "Qwark Vidcomic 3": {"unlockAddress": 0x001D5552 },
      "Qwark Vidcomic 4": {"unlockAddress": 0x001D5550 },
      "Qwark Vidcomic 5": {"unlockAddress": 0x001D5553 },
    },
    "PlanetSlots": [
      0x00143050, 0x00143054, 0x00143058, 0x0014305C, 
      0x00143060, 0x00143064, 0x00143068, 0x0014306C ,
      0x00143070, 0x00143074, 0x00143078, 0x0014307C ,
      0x00143080, 0x00143084, 0x00143088, 0x0014308C ,
      0x00143090, 0x00143094, 0x00143098, 0x0014309C ,
    ],
    "PlanetValues": {
      "Veldin": 1,
      "Florana" : 2,
      "Starship Phoenix" : 3,
      "Marcadia" : 4,
      "Daxx" : 5,
      "Annihilation Nation" : 7,
      "Aquatos" : 8,
      "Tyhrranosis" : 9,
      "Zeldrin Starport" : 10,
      "Obani Gemini" : 11,
      "Rilgar" : 12,
      "Holostar Studios" : 13,
      "Koros" : 14,
      "Metropolis" : 16,
      "Zeldrin" : 17,
      "Aridia" : 18,
      "Qwarks Hideout" : 19,
      "Obani Draco" : 21,
      "Mylon" : 22,
      "Museum" : 24,
    },
    "QuickSelectSlots": [
      # Slot 1
      0x001D4C60, 0x001D4C64, 0x001D4C68, 0x001D4C6C,
      0x001D4C70, 0x001D4C74, 0x001D4C78, 0x001D4C7C,
      # Slot 2(With R1 button)
      0x001D4C80, 0x001D4C84, 0x001D4C88, 0x001D4C8C,
      0x001D4C90, 0x001D4C94, 0x001D4C98, 0x001D4C9C,
    ],
    "CurrentEquipped": 0x001D4C40,
    "LastUsed": [0x00142670, 0x00142674, 0x00142678],
    "ArmorVersion": 0x001426A0,
    "boltXPMultiplier": 0x001426BA,
    "Bolt": 0x00142660,
    "NanotechExp": 0x00142694,
    "CurrentPlanet": 0x001D545C,
    "EventFlags": {
      "FirstVisitingMyRoom": 0x001426E8,
    }
  }
}

LOCATIONS = [
  {
    "Name": "Received Shock Cannon",
    "Id": 50001000,
    "Address": "0x00142CC7",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Nitro Launcher",
    "Id": 50001001,
    "Address": "0x00142D17",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Florana",
    "Id": 50001003,
    "Address": "0x001426E4",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Plasma Whip",
    "Id": 50001004,
    "Address": "0x00142D1F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received N60 Storm",
    "Id": 50001005,
    "Address": "0x00142CCF",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Below Gadgetron Vendor",
    "Id": 50001006,
    "Address": "0x001BBB29",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Path of Death",
    "Id": 50001007,
    "Address": "0x001BBB2A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Starship Phoenix",
    "Id": 50001008,
    "Address": "0x001426E6",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received SUCC Cannon",
    "Id": 50001009,
    "Address": "0x00142D27",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Infector",
    "Id": 50001010,
    "Address": "0x00142CD7",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: All VR Deck Challenges",
    "Id": 50001011,
    "Address": "0x001BBB30",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Complete VR Training",
    "Id": 50001012,
    "Address": "0x001BBB31",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Magna Plate Armor",
    "Id": 50001013,
    "Address": "0x001426A0",
    "CheckValue": "1",
    "CheckType": 3
  },
  {
    "Name": "Received Adamantine Armor",
    "Id": 50001014,
    "Address": "0x001426A0",
    "CheckValue": "2",
    "CheckType": 3
  },
  {
    "Name": "Received Aegis Mark V Armor",
    "Id": 50001015,
    "Address": "0x001426A0",
    "CheckValue": "3",
    "CheckType": 3
  },
  {
    "Name": "Received Infernox Armor",
    "Id": 50001016,
    "Address": "0x001426A0",
    "CheckValue": "4",
    "CheckType": 3
  },
  {
    "Name": "Received Hacker",
    "Id": 50001017,
    "Address": "0x00142CB4",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Hypershot",
    "Id": 50001018,
    "Address": "0x00142CAB",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Marcadia",
    "Id": 50001019,
    # "Address": "0x001426E9",
    # "CheckType": 0,
    # "AddressBit": 0
    "Address": "0x001D545C", # When first visiting to Starship Phoenix
    "CheckType": 3,
    "CheckValue": "3",
  },
  {
    "Name": "Infobot: Koros",
    "Id": 50001020,
    "Address": "0x001D553E",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Annihilation Nation",
    "Id": 50001021,
    "Address": "0x001426EB",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Aquatos",
    "Id": 50001022,
    # " Address": 0x001426F6, #  Correct Infobot address
    "Address": "0x0014276F", #  Same as Thyrra-Guise Getting event. This event behinds Phoenix Ship event.
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Tyhrranosis",
    "Id": 50001023,
    # "Address": "0x00142C1B",
    "Address": "0x0014275E", #  Same as 1 Sewer Crystal Traded
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Daxx",
    "Id": 50001024,
    #  "Address": "0x00142765",
    "Address": "0x00142765", #  Same as T-Bolt: VR training
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Obani Gemini",
    "Id": 50001025,
    "Address": "0x0014553B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Zeldrin",
    "Id": 50001026,
    #  "Address": "0x001D5541",
    "Address": "0x00142708", #  Same as defeat Giant Cronk
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Qwarks Hideout",
    "Id": 50001027,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 5 #  3E 00X0_0000
  },
  {
    "Name": "Qwark Vidcomic 4",
    "Id": 50001413,
    "Address": "0x001D5550",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwark Vidcomic 5",
    "Id": 50001414,
    "Address": "0x001D5553",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Metropolis",
    "Id": 50001415,
    "Address": "0x001D5550",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Spitting Hydra",
    "Id": 50001030,
    "Address": "0x00142CE7",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Refractor",
    "Id": 50001031,
    # "Address": "0x00142CB2", # item flag
    "Address": "0x00142C29", # Marcadia Mission event Flag
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: After Pool of Water",
    "Id": 50001032,
    "Address": "0x001BBB39",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Last Refractor Room",
    "Id": 50001033,
    "Address": "0x001BBB3A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Ceiling just before Al",
    "Id": 50001034,
    "Address": "0x001BBB3B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwark Vidcomic 1",
    "Id": 50001035,
    "Address": "0x001D554F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Agents of Doom",
    "Id": 50001140,
    "Address": "0x00142CF7",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Tyhrra-Guise",
    "Id": 50001141,
    "Address": "0x0014276F", #  Same as Grand Prize Bout(Thyrra-Guise Getting event)
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Heat Street",
    "Id": 50001142,
    "Address": "0x001BBB51",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Maze of Blaze",
    "Id": 50001143,
    "Address": "0x001BBB52",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Grand Prize Bout",
    "Id": 50001144,
    "Address": "0x0014276F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "The Terrible Two",
    "Id": 50001145,
    "Address": "0x00142772",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Robot Rampage",
    "Id": 50001146,
    "Address": "0x00142773",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Two Minute Warning",
    "Id": 50001147,
    "Address": "0x00142774",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "90 Seconds of Carnage",
    "Id": 50001148,
    "Address": "0x00142775",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Onslaught",
    "Id": 50001149,
    "Address": "0x00142776",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Whip It Good",
    "Id": 50001150,
    "Address": "0x00142777",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Hydra N' Seek",
    "Id": 50001151,
    "Address": "0x00142778",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Championship Bout",
    "Id": 50001152,
    "Address": "0x00142779",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Ninja Challenge",
    "Id": 50001154,
    "Address": "0x0014277D",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Counting Ducks",
    "Id": 50001155,
    "Address": "0x0014277E",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Cycling Weapons",
    "Id": 50001156,
    "Address": "0x0014277F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "One Hit Wonder",
    "Id": 50001157,
    "Address": "0x00142780",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Time to SUCC",
    "Id": 50001158,
    "Address": "0x00142781",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Naptime",
    "Id": 50001159,
    "Address": "0x00142782",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Meet Courtney - Arena",
    "Id": 50001153,
    "Address": "0x00142771",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "More Cycling Weapons",
    "Id": 50001160,
    "Address": "0x00142783",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Dodge the Twins",
    "Id": 50001161,
    "Address": "0x00142784",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Chop Chop",
    "Id": 50001162,
    "Address": "0x00142785",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Sleep Inducer",
    "Id": 50001163,
    "Address": "0x00142786",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "The Other White Meat",
    "Id": 50001164,
    "Address": "0x00142787",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Championship Bout II",
    "Id": 50001165,
    "Address": "0x00142788",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwarktastic Battle",
    "Id": 50001166,
    "Address": "0x00142789",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Heat Street",
    "Id": 50001167,
    "Address": "0x0014276E",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Crispy Critter",
    "Id": 50001168,
    "Address": "0x0014277A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Pyro Playground",
    "Id": 50001169,
    "Address": "0x0014277B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Suicide Run",
    "Id": 50001170,
    "Address": "0x0014277C",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "BBQ Boulevard", #  (Meet Courtney - Gauntlet) 
    "Id": 50001171,
    "Address": "0x00142770",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Maze of Blaze",
    "Id": 50001172,
    "Address": "0x0014278A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Cremation Station",
    "Id": 50001173,
    "Address": "0x0014278B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "The Annihilator (Gauntlet)",
    "Id": 50001174,
    "Address": "0x0014278C",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwark Vidcomic 2",
    "Id": 50001175,
    "Address": "0x001D5551",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwark Vidcomic 3",
    "Id": 50001176,
    "Address": "0x001D5552",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Flux Rifle",
    "Id": 50001090,
    "Address": "0x00142D0F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Under the Bridge",
    "Id": 50001091,
    "Address": "0x001BBB5A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Underwater Bolt",
    "Id": 50001092,
    "Address": "0x001BBB5B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Behind the Locked Gate",
    "Id": 50001093,
    "Address": "0x001BBB59",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Top Left Bolt",
    "Id": 50001094,
    "Address": "0x001BBBF9",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Swinging Bolt",
    "Id": 50001095,
    "Address": "0x001BBBFA",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "1 Sewer Crystal Traded",
    "Id": 50001096,
    "Address": "0x0014275E", #  JP: 1426DE,
    "CompareType": 1, #  Greater than
    "CheckType": 3, #  Byte type
    "CheckValue": "0"
  },
  {
    "Name": "5 Sewer Crystals Traded",
    "Id": 50001097,
    "Address": "0x0014275E", #  JP: 1426DE,
    "CheckType": 3, #  Byte type
    "CompareType": 1, #  Greater than
    "CheckValue": "4"
  },
  {
    "Name": "10 Sewer Crystals Traded",
    "Id": 50001098,
    "Address": "0x0014275E", #  JP: 1426DE,
    "CheckType": 3, #  Byte type
    "CompareType": 1, #  Greater than
    "CheckValue": "9" #  0x9
  },
  {
    "Name": "20 Sewer Crystals Traded",
    "Id": 50001099,
    "Address": "0x0014275E", #  JP: 1426DE,
    "CheckType": 3, #  Byte type
    "CompareType": 1, #  Greater than
    "CheckValue": "19" #  0x13
  },
  {
    "Name": "Received Annihilator",
    "Id": 50001300,
    "Address": "0x00142CDF",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Holo-Shield Glove",
    "Id": 50001301,
    "Address": "0x00142D07",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: South East Cannon",
    "Id": 50001302,
    "Address": "0x001BBB62",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Underground Cave Bolt",
    "Id": 50001303,
    "Address": "0x001BBB61",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Right of the Taxi",
    "Id": 50001320,
    "Address": "0x001BBB41",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Time-Sensitive Door",
    "Id": 50001321,
    "Address": "0x001BBB42",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Charge Boots",
    "Id": 50001322,
    "Address": "0x00142CBD",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Post-Daxx",
    "Id": 50001323,
    # "Address": "0x00143B39", #  ??
    "Address": "0x00142C2D", #  Daxx Courtney Room
    "CheckType": 0,
    "AddressBit": 6 #  0x60: 0XX0_0000
  },
  {
    "Name": "Received Disk Blade Gun",
    "Id": 50001340,
    "Address": "0x00142CEF",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Follow the Lava",
    "Id": 50001341,
    "Address": "0x001BBB72",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Between the Twin Towers",
    "Id": 50001342,
    "Address": "0x001BBB71",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Rilgar",
    "Id": 50001343,
    "Address": "0x00142BB2",
    "CheckType": 0,
    "AddressBit": 3 #  08: 0000_X000
  },
  {
    "Name": "Received Grav Boots",
    "Id": 50001360,
    #  "Address": "0x00142CAD",
    "Address": "0x00142C40",
    "CheckType": 0,
    "AddressBit": 3 #  0x08: 0000_X000
  },
  {
    "Name": "Infobot: Holostar Studios",
    "Id": 50001361,
    "Address": "0x00142705",
    #  "Address": "0x00142771", #  WA: Same as Meet Courtney - Arena
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Rift Inducer",
    "Id": 50001390,
    "Address": "0x00142CFF",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Atop the Chairs",
    "Id": 50001391,
    "Address": "0x001BBB82",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Lot 42's Grav Ramp",
    "Id": 50001392,
    "Address": "0x001BBB83",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Kamikaze Noids",
    "Id": 50001393,
    "Address": "0x001BBB81",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Obani Draco",
    "Id": 50001394,
    "Address": "0x00142713",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Zeldrin Starport",
    "Id": 50001370,
    "Address": "0x0014270D",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Bolt Grabber V2",
    "Id": 50001410,
    "Address": "0x00142CA7",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Inside the Second Ship",
    "Id": 50001411,
    "Address": "0x001BBB6A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Atop the Twin Shooters",
    "Id": 50001412,
    "Address": "0x001BBB69",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Map-O-Matic",
    "Id": 50001430,
    #  "Address": "0x00142CA5", #  item flag
    "Address": "0x00142C64", #  Metropolice Mission Clear
    "CheckType": 0,
    "AddressBit": 5 #  0x20 : 00X0_0000 
  },
  {
    "Name": "T-Bolt: Across the Gap",
    "Id": 50001431,
    "Address": "0x001BBB99",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Right of the Balcony",
    "Id": 50001432,
    "Address": "0x001BBB9A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Tall Tower (Hovership)",
    "Id": 50001433,
    "Address": "0x001BBBE9",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Metal-Noids",
    "Id": 50001434,
    "Address": "0x0014275C",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Nano-Pak",
    "Id": 50001450,
    "Address": "0x00142CC0",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Turn Around",
    "Id": 50001451,
    "Address": "0x001BBBA1",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Aridia",
    "Id": 50001452,
    "Address": "0x00142722", # Correct Address: 0x00142C52(4bit: 0x07->0x0f) (US), but Event is not happenned in some case.
    "CheckType": 0,
    "AddressBit": 1 # / 0x02: 0000_00X0
  },
  {
    "Name": "Received Warp Pad",
    "Id": 50001470,
    # "Address": "0x00142CBF", #  Item flag
    "Address": "0x00142C56", #  Clear Aridia
    "CheckType": 0,
    "AddressBit": 4 #  0x10: 000X_0000
  },
  {
    "Name": "Received Qwack-O-Ray",
    "Id": 50001471,
    "Address": "0x00142D2F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Under the Bridge (Assassination)",
    "Id": 50001472,
    "Address": "0x001BBBAA",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Behind the Base (X12 Endgame)",
    "Id": 50001473,
    "Address": "0x001BBBA9",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Received Gadgetron PDU",
    "Id": 50001490,
    "Address": "0x00142CC3",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Glide from the Ramp",
    "Id": 50001491,
    "Address": "0x001BBBB1",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Behind the Metal Fence",
    "Id": 50001493,
    "Address": "0x001BBB89",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: Pair of Towers",
    "Id": 50001494,
    "Address": "0x001BBB8A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Infobot: Mylon",
    "Id": 50001495,
    "Address": "0x00142C49",
    "CheckType": 0,
    "AddressBit": 3 #  04 -> 0C: 0000_X000
  },
  {
    "Name": "T-Bolt: Behind the Forcefield",
    "Id": 50001496,
    "Address": "0x001BBBC9",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Dr. Nefarious Defeated!",
    "Id": 50001497,
    "Address": "0x0014270F",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Biobliterator Defeated!",
    "Id": 50001498,
    "Address": "0x00142BB6",
    "CheckType": 0,
    "AddressBit": 6 #  40: 0X00_0000
  },
  {
    "Name": "T-Bolt: VidComic 1",
    "Id": 50001201,
    "Address": "0x001BBB32",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: VidComic 2",
    "Id": 50001202,
    "Address": "0x001BBB33",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: VidComic 3",
    "Id": 50001203,
    "Address": "0x001BBB34",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: VidComic 4",
    "Id": 50001204,
    "Address": "0x001BBB35",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "T-Bolt: VidComic 5",
    "Id": 50001205,
    "Address": "0x001BBB36",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Shock Blaster: V2",
    "Id": 50001500,
    "Address": "0x00142E7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "4800"
  },
  {
    "Name": "Shock Blaster: V3",
    "Id": 50001501,
    "Address": "0x00142E7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "12800"
  },
  {
    "Name": "Shock Blaster: V4",
    "Id": 50001502,
    "Address": "0x00142E7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "22400"
  },
  {
    "Name": "Shock Blaster: V5",
    "Id": 50001503,
    "Address": "0x00142E7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "32000"
  },
  {
    "Name": "Nitro Launcher: V2",
    "Id": 50001504,
    "Address": "0x00142FBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "6400"
  },
  {
    "Name": "Nitro Launcher: V3",
    "Id": 50001505,
    "Address": "0x00142FBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "16000"
  },
  {
    "Name": "Nitro Launcher: V4",
    "Id": 50001506,
    "Address": "0x00142FBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "35200"
  },
  {
    "Name": "Nitro Launcher: V5",
    "Id": 50001507,
    "Address": "0x00142FBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "83200"
  },
  {
    "Name": "N60 Storm: V2",
    "Id": 50001508,
    "Address": "0x00142E9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "6400"
  },
  {
    "Name": "N60 Storm: V3",
    "Id": 50001509,
    "Address": "0x00142E9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "16000"
  },
  {
    "Name": "N60 Storm: V4",
    "Id": 50001510,
    "Address": "0x00142E9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "48000"
  },
  {
    "Name": "N60 Storm: V5",
    "Id": 50001511,
    "Address": "0x00142E9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "57600"
  },
  {
    "Name": "Plasma Whip: V2",
    "Id": 50001512,
    "Address": "0x00142FDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "6400"
  },
  {
    "Name": "Plasma Whip: V3",
    "Id": 50001513,
    "Address": "0x00142FDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "25600"
  },
  {
    "Name": "Plasma Whip: V4",
    "Id": 50001514,
    "Address": "0x00142FDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "57600"
  },
  {
    "Name": "Plasma Whip: V5",
    "Id": 50001515,
    "Address": "0x00142FDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "105600"
  },
  {
    "Name": "Infector: V2",
    "Id": 50001516,
    "Address": "0x00142EBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "12800"
  },
  {
    "Name": "Infector: V3",
    "Id": 50001517,
    "Address": "0x00142EBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "25600"
  },
  {
    "Name": "Infector: V4",
    "Id": 50001518,
    "Address": "0x00142EBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "64000"
  },
  {
    "Name": "Infector: V5",
    "Id": 50001519,
    "Address": "0x00142EBC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "121600"
  },
  {
    "Name": "SUCC Cannon: V2",
    "Id": 50001520,
    "Address": "0x00142FFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "6400"
  },
  {
    "Name": "SUCC Cannon: V3",
    "Id": 50001521,
    "Address": "0x00142FFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "19200"
  },
  {
    "Name": "SUCC Cannon: V4",
    "Id": 50001522,
    "Address": "0x00142FFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "38400"
  },
  {
    "Name": "SUCC Cannon: V5",
    "Id": 50001523,
    "Address": "0x00142FFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "76800"
  },
  {
    "Name": "Spitting Hydra: V2",
    "Id": 50001524,
    "Address": "0x00142EFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "9600"
  },
  {
    "Name": "Spitting Hydra: V3",
    "Id": 50001525,
    "Address": "0x00142EFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "28800"
  },
  {
    "Name": "Spitting Hydra: V4",
    "Id": 50001526,
    "Address": "0x00142EFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "57600"
  },
  {
    "Name": "Spitting Hydra: V5",
    "Id": 50001527,
    "Address": "0x00142EFC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "96000"
  },
  {
    "Name": "Agents Of Doom: V2",
    "Id": 50001528,
    "Address": "0x00142F3C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "12800"
  },
  {
    "Name": "Agents Of Doom: V3",
    "Id": 50001529,
    "Address": "0x00142F3C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "32000"
  },
  {
    "Name": "Agents Of Doom: V4",
    "Id": 50001530,
    "Address": "0x00142F3C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "96000"
  },
  {
    "Name": "Agents Of Doom: V5",
    "Id": 50001531,
    "Address": "0x00142F3C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "192000"
  },
  {
    "Name": "Flux Rifle: V2",
    "Id": 50001532,
    "Address": "0x00142F9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "6400"
  },
  {
    "Name": "Flux Rifle: V3",
    "Id": 50001533,
    "Address": "0x00142F9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "19200"
  },
  {
    "Name": "Flux Rifle: V4",
    "Id": 50001534,
    "Address": "0x00142F9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "48000"
  },
  {
    "Name": "Flux Rifle: V5",
    "Id": 50001535,
    "Address": "0x00142F9C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "92800"
  },
  {
    "Name": "Annihilator: V2",
    "Id": 50001536,
    "Address": "0x00142EDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "25600"
  },
  {
    "Name": "Annihilator: V3",
    "Id": 50001537,
    "Address": "0x00142EDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "76800"
  },
  {
    "Name": "Annihilator: V4",
    "Id": 50001538,
    "Address": "0x00142EDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "204800"
  },
  {
    "Name": "Annihilator: V5",
    "Id": 50001539,
    "Address": "0x00142EDC",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "396800"
  },
  {
    "Name": "Holo-Shield Glove: V2",
    "Id": 50001540,
    "Address": "0x00142F7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "4800"
  },
  {
    "Name": "Holo-Shield Glove: V3",
    "Id": 50001541,
    "Address": "0x00142F7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "14400"
  },
  {
    "Name": "Holo-Shield Glove: V4",
    "Id": 50001542,
    "Address": "0x00142F7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "43200"
  },
  {
    "Name": "Holo-Shield Glove: V5",
    "Id": 50001543,
    "Address": "0x00142F7C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "86400"
  },
  {
    "Name": "Disk-Blade Gun: V2",
    "Id": 50001544,
    "Address": "0x00142F1C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "22400"
  },
  {
    "Name": "Disk-Blade Gun: V3",
    "Id": 50001545,
    "Address": "0x00142F1C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "67200"
  },
  {
    "Name": "Disk-Blade Gun: V4",
    "Id": 50001546,
    "Address": "0x00142F1C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "195200"
  },
  {
    "Name": "Disk-Blade Gun: V5",
    "Id": 50001547,
    "Address": "0x00142F1C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "387200"
  },
  {
    "Name": "Rift Inducer: V2",
    "Id": 50001548,
    "Address": "0x00142F5C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "25600"
  },
  {
    "Name": "Rift Inducer: V3",
    "Id": 50001549,
    "Address": "0x00142F5C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "76800"
  },
  {
    "Name": "Rift Inducer: V4",
    "Id": 50001550,
    "Address": "0x00142F5C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "204800"
  },
  {
    "Name": "Rift Inducer: V5",
    "Id": 50001551,
    "Address": "0x00142F5C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "396800"
  },
  {
    "Name": "Qwack-O-Ray: V2",
    "Id": 50001552,
    "Address": "0x0014301C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "32000"
  },
  {
    "Name": "Qwack-O-Ray: V3",
    "Id": 50001553,
    "Address": "0x0014301C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "96000"
  },
  {
    "Name": "Qwack-O-Ray: V4",
    "Id": 50001554,
    "Address": "0x0014301C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "256000"
  },
  {
    "Name": "Qwack-O-Ray: V5",
    "Id": 50001555,
    "Address": "0x0014301C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "512000"
  },
  {
    "Name": "RY3N0: V2",
    "Id": 50001556,
    "Address": "0x0014303C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "640000"
  },
  {
    "Name": "RY3N0: V3",
    "Id": 50001557,
    "Address": "0x0014303C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "1600000"
  },
  {
    "Name": "RY3N0: V4",
    "Id": 50001558,
    "Address": "0x0014303C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "2880000"
  },
  {
    "Name": "RY3N0: V5",
    "Id": 50001559,
    "Address": "0x0014303C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "4480000"
  },
  {
    "Name": "Mega-Turret Glove: V2",
    "Id": 50001560,
    "Address": "0x00142E34",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "12800"
  },
  {
    "Name": "Mega-Turret Glove: V3",
    "Id": 50001561,
    "Address": "0x00142E34",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "32000"
  },
  {
    "Name": "Mega-Turret Glove: V4",
    "Id": 50001562,
    "Address": "0x00142E34",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "64000"
  },
  {
    "Name": "Mega-Turret Glove: V5",
    "Id": 50001563,
    "Address": "0x00142E34",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "112000"
  },
  {
    "Name": "Lava Gun: V2",
    "Id": 50001564,
    "Address": "0x00142E24",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "19200"
  },
  {
    "Name": "Lava Gun: V3",
    "Id": 50001565,
    "Address": "0x00142E24",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "48000"
  },
  {
    "Name": "Lava Gun: V4",
    "Id": 50001566,
    "Address": "0x00142E24",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "86400"
  },
  {
    "Name": "Lava Gun: V5",
    "Id": 50001567,
    "Address": "0x00142E24",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "134400"
  },
  {
    "Name": "Shield Charger: V2",
    "Id": 50001568,
    "Address": "0x00142E38",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "70400"
  },
  {
    "Name": "Shield Charger: V3",
    "Id": 50001569,
    "Address": "0x00142E38",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "160000"
  },
  {
    "Name": "Shield Charger: V4",
    "Id": 50001570,
    "Address": "0x00142E38",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "307200"
  },
  {
    "Name": "Shield Charger: V5",
    "Id": 50001571,
    "Address": "0x00142E38",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "537600"
  },
  {
    "Name": "Bouncer: V2",
    "Id": 50001572,
    "Address": "0x00142E2C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "80000"
  },
  {
    "Name": "Bouncer: V3",
    "Id": 50001573,
    "Address": "0x00142E2C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "272000"
  },
  {
    "Name": "Bouncer: V4",
    "Id": 50001574,
    "Address": "0x00142E2C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "592000"
  },
  {
    "Name": "Bouncer: V5",
    "Id": 50001575,
    "Address": "0x00142E2C",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "976000"
  },
  {
    "Name": "Plasma Coil: V2",
    "Id": 50001576,
    "Address": "0x00142E20",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "256000"
  },
  {
    "Name": "Plasma Coil: V3",
    "Id": 50001577,
    "Address": "0x00142E20",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "576000"
  },
  {
    "Name": "Plasma Coil: V4",
    "Id": 50001578,
    "Address": "0x00142E20",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "960000"
  },
  {
    "Name": "Plasma Coil: V5",
    "Id": 50001579,
    "Address": "0x00142E20",
    "CompareType": 1,
    "CheckType": 1,
    "CheckValue": "1408000"
  },
  {
    "Name": "Marcadia Mission 01",
    "Id": 50001036,
    "Address": "0x00142738",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Marcadia Mission 02",
    "Id": 50001037,
    "Address": "0x00142739",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Marcadia Mission 03",
    "Id": 50001038,
    "Address": "0x0014273A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Marcadia Mission 04",
    "Id": 50001039,
    "Address": "0x0014273B",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Marcadia Mission 05",
    "Id": 50001040,
    "Address": "0x0014273C",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Rilgar Mission 01",
    "Id": 50001365,
    "Address": "0x0014273D",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Rilgar Mission 02",
    "Id": 50001366,
    "Address": "0x0014273E",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Rilgar Mission 03",
    "Id": 50001367,
    "Address": "0x00142C40", # As same as Grav-boots event
    "CheckType": 0,
    "AddressBit": 3
  },
  {
    "Name": "Metro Storm Mission 01",
    "Id": 50001435,
    "Address": "0x00142747",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Metro Storm Mission 02",
    "Id": 50001436,
    "Address": "0x00142748",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Metro Storm Mission 03",
    "Id": 50001437,
    "Address": "0x00142749",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Metro Storm Mission 04",
    "Id": 50001438,
    "Address": "0x0014274A",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Metro Storm Mission 05",
    "Id": 50001439,
    "Address": "0x0014274B", 
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Alidia Mission 01",
    "Id": 50001475,
    "Address": "0x00142742",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Alidia Mission 02",
    "Id": 50001476,
    "Address": "0x00142743",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Alidia Mission 03",
    "Id": 50001477,
    "Address": "0x00142744",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Alidia Mission 04",
    "Id": 50001478,
    "Address": "0x00142745",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Alidia Mission 05",
    "Id": 50001479,
    "Address": "0x00142746",
    "CheckType": 0,
    "AddressBit": 0
  },
  {
    "Name": "Qwark Vidcomic 1 Clear",
    "Id": 50001600,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 1
  },
  {
    "Name": "Qwark Vidcomic 2 Clear",
    "Id": 50001601,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 3
  },
  {
    "Name": "Qwark Vidcomic 3 Clear",
    "Id": 50001602,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 2
  },
  {
    "Name": "Qwark Vidcomic 4 Clear",
    "Id": 50001603,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 4
  },
  {
    "Name": "Qwark Vidcomic 5 Clear",
    "Id": 50001604,
    "Address": "0x00142734",
    "CheckType": 0,
    "AddressBit": 5
  },
]
