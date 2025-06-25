using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*
 * Bolt:
 * English  : 20 142660
 * Japanese : 20 1425E0
 * diff: -0x80
 * 
 * Quicksetting:
 * English  : 20 1D4C50
 * Japanese : 20 1E1A30
 * diff: CDE0
 * 
 * CurrentEquipment:
 * English  : 20 1D4C40
 * Japanese : 20 1DDF00
 * diff: 92C0
 *
 * Skillpoint
 * English  : 20 1D54B0 ~ CF ( B0 and CF is not used in game)
 * Japanese : 20 1DE7B0 ~ CF ( CE and CF is not used and B0 is used for 22th skip point)
 * diff: 9300
 *
 * Titanium bolt
 * English  : 20 1BBB29 ~ 40(0x28)byte ( Spreadsheet is 1BBB18, but location file is 1BBB29)
 * Japanese : 20 1C4DC1 ~ 40(0x28)byte
 * diff: 9298
 * 
 * Story Flag
 * English  : 20 1426E0 ~ xx(0xXX)byte
 * Japanese : 20 142660 ~ xx(0xXX)byte
 * diff: 0x80
 */
/*
 * Marcadia Mission 1426B8 - BA
 * 
 */
namespace RaC3AP
{
    public static class GlobalConfig
    {
        public const int AddressOffset = -0x80; // EN: 0x00, JP: -0x80
        public const int QuicksetOffset = 0xCDE0; // EN: 0x00, JP: 0xCDE0
        public const int CurrentEquipmentOffset = 0x92C0; // EN: 0x00, JP: 0x92C0
        public const int VidComicOffset = 0x9300; // EN: 0x00, JP: 0x9300
        public const int TitaniumOffset = 0x9298; // EN: 0x00, JP: 0x9300
        /*
        public const int AddressOffset = 0x0; // EN: 0x00, JP: -0x80
        public const int QuicksetOffset = 0x0; // EN: 0x00, JP: 0xCDE0
        public const int CurrentEquipmentOffset = 0x0; // EN: 0x00, JP: 0x92C0
        */

        public const int DefeatNefarious = 0x2027DC18 + GlobalConfig.AddressOffset;
    }

    public class WeaponUnlocks
    {
        //All weapon unlock addresses
        public const int unlockShockBlaster = 0x20142CC7 + GlobalConfig.AddressOffset;
        public const int unlockNitroLauncher = 0x20142D17 + GlobalConfig.AddressOffset;
        public const int unlockN60Storm = 0x20142CCF + GlobalConfig.AddressOffset;
        public const int unlockPlasmaWhip = 0x20142D1F + GlobalConfig.AddressOffset;
        public const int unlockInfector = 0x20142CD7 + GlobalConfig.AddressOffset;
        public const int unlockSuckCannon = 0x20142D27 + GlobalConfig.AddressOffset;
        public const int unlockSpittingHydra = 0x20142CE7 + GlobalConfig.AddressOffset;
        public const int unlockAgentsOfDoom = 0x20142CF7 + GlobalConfig.AddressOffset;
        public const int unlockFluxRifle = 0x20142D0F + GlobalConfig.AddressOffset;
        public const int unlockAnnihilator = 0x20142CDF + GlobalConfig.AddressOffset;
        public const int unlockHoloShieldGlove = 0x20142D07 + GlobalConfig.AddressOffset;
        public const int unlockDiskBladeGun = 0x20142CEF + GlobalConfig.AddressOffset;
        public const int unlockRiftInducer = 0x20142CFF + GlobalConfig.AddressOffset;
        public const int unlockQwackORay = 0x020142D2F + GlobalConfig.AddressOffset;
        public const int unlockRY3N0 = 0x20142D37 + GlobalConfig.AddressOffset;
        public const int unlockMegaTurretGlove = 0x20142CB5 + GlobalConfig.AddressOffset;
        public const int unlockLavaGun = 0x20142CB1 + GlobalConfig.AddressOffset;
        public const int unlockShieldCharger = 0x20142CB6 + GlobalConfig.AddressOffset;
        public const int unlockBouncer = 0x20142CB3 + GlobalConfig.AddressOffset;
        public const int unlockPlasmaCoil = 0x20142CB0 + GlobalConfig.AddressOffset;
    }

        public class Addresses
    {
        public const int ammoShockBlaster = 0x2014288C + GlobalConfig.AddressOffset;
        public const int ammoNitroLauncher = 0x201429CC + GlobalConfig.AddressOffset;
        public const int ammoN60Storm = 0x201428AC + GlobalConfig.AddressOffset;
        public const int ammoPlasmaWhip = 0x201429EC + GlobalConfig.AddressOffset;
        public const int ammoInfector = 0x201428CC + GlobalConfig.AddressOffset;
        public const int ammoSpittingHydra = 0x2014290C + GlobalConfig.AddressOffset;
        public const int ammoAgentsOfDoom = 0x2014294C + GlobalConfig.AddressOffset;
        public const int ammoFluxRifle = 0x201429AC + GlobalConfig.AddressOffset;
        public const int ammoAnnihilator = 0x201428EC + GlobalConfig.AddressOffset;
        public const int ammoHoloShieldGlove = 0x2014298C + GlobalConfig.AddressOffset;
        public const int ammoDiskBladeGun = 0x2014292C + GlobalConfig.AddressOffset;
        public const int ammoRiftInducer = 0x2014296C + GlobalConfig.AddressOffset;
        public const int ammoRY3N0 = 0x20142A4C + GlobalConfig.AddressOffset;
        public const int ammoMegaTurretGlove = 0x20142844 + GlobalConfig.AddressOffset;
        public const int ammoLavaGun = 0x20142834 + GlobalConfig.AddressOffset;
        public const int ammoShieldCharger = 0x20142848 + GlobalConfig.AddressOffset;
        public const int ammoBouncer = 0x2014283C + GlobalConfig.AddressOffset;
        public const int ammoPlasmaCoil = 0x20142830 + GlobalConfig.AddressOffset;


        public const int boltXPMultiplier = 0x201426BA + GlobalConfig.AddressOffset;
        public const int armorEquipped = 0x201426A0 + GlobalConfig.AddressOffset;
        public const int currentArmor = 0;
        public const int weaponDisplay = 0x201A5E08 + GlobalConfig.AddressOffset;
        public const int boltIncrementDisplay = 0x201E0440 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponOne = 0x20142670 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponTwo = 0x20142674 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponThree = 0x20142678 + GlobalConfig.AddressOffset;

        public const int junkAddr1 = 0x2027DC00 + GlobalConfig.AddressOffset;
        public const int junkAddr2 = 0x2027DC04 + GlobalConfig.AddressOffset;

        public const int currentlyEquippedWeapon = 0x201D4C40 + GlobalConfig.CurrentEquipmentOffset;
    }
    public class GadgetAddresses
    {

        public const int hyperShot = 0x20142CAB + GlobalConfig.AddressOffset;
        public const int refractor = 0x20142CB2 + GlobalConfig.AddressOffset;
        public const int tyhrraGuise = 0x20142CBE + GlobalConfig.AddressOffset;
        public const int warpPad = 0x20142CBF + GlobalConfig.AddressOffset;
        public const int pda = 0x20142CC3 + GlobalConfig.AddressOffset;
        public const int chargeBoots = 0x20142CBD + GlobalConfig.AddressOffset;
        public const int gravBoots = 0x20142CAD + GlobalConfig.AddressOffset;
        public const int hacker = 0x20142CB4 + GlobalConfig.AddressOffset;
        public const int boltGrabberV2 = 0x20142CA7 + GlobalConfig.AddressOffset;
        public const int mapOMatic = 0x20142CA5 + GlobalConfig.AddressOffset;
        public const int nanoPak = 0x20142CC0 + GlobalConfig.AddressOffset;

        public const int vidComic1 = 0x201D554F + GlobalConfig.VidComicOffset;
        public const int vidComic2 = 0x201D5551 + GlobalConfig.VidComicOffset;
        public const int vidComic3 = 0x201D5552 + GlobalConfig.VidComicOffset;
        public const int vidComic4 = 0x201D5550 + GlobalConfig.VidComicOffset;
        public const int vidComic5 = 0x201D5553 + GlobalConfig.VidComicOffset;
    }
    public class PlanetSlots
    {
        public const int slotOne = 0x20143050 + GlobalConfig.AddressOffset;
        public const int slotTwo = 0x20143054 + GlobalConfig.AddressOffset;
        public const int slotThree = 0x20143058 + GlobalConfig.AddressOffset;
        public const int slotFour = 0x2014305C + GlobalConfig.AddressOffset;
        public const int slotFive = 0x20143060 + GlobalConfig.AddressOffset;
        public const int slotSix = 0x20143064 + GlobalConfig.AddressOffset;
        public const int slotSeven = 0x20143068 + GlobalConfig.AddressOffset;
        public const int slotEight = 0x2014306C + GlobalConfig.AddressOffset;
        public const int slotNine = 0x20143070 + GlobalConfig.AddressOffset;
        public const int slotTen = 0x20143074 + GlobalConfig.AddressOffset;
        public const int slotEleven = 0x20143078 + GlobalConfig.AddressOffset;
        public const int slotTwelve = 0x2014307C + GlobalConfig.AddressOffset;
        public const int slotThirteen = 0x20143080 + GlobalConfig.AddressOffset;
        public const int slotFourteen = 0x20143084 + GlobalConfig.AddressOffset;
        public const int slotFifteen = 0x20143088 + GlobalConfig.AddressOffset;
        public const int slotSixteen = 0x2014308C + GlobalConfig.AddressOffset;
        public const int slotSeventeen = 0x20143090 + GlobalConfig.AddressOffset;
        public const int slotEighteen = 0x20143094 + GlobalConfig.AddressOffset;
        public const int slotNineteen = 0x20143098 + GlobalConfig.AddressOffset;
    }
    public class PlanetValues
    {
        public const int Florana = 2;
        public const int StarshipPhoenix = 3;
        public const int Marcadia = 4;
        public const int Daxx = 5;
        public const int AnnihilationNation = 7;
        public const int Aquatos = 8;
        public const int Tyhrranosis = 9;
        public const int ZeldrinStarport = 10;
        public const int ObaniGemini = 11;
        public const int Rilgar = 12;
        public const int HolostarStudios = 13;
        public const int Koros = 14;
        public const int Metropolis = 16;
        public const int Zeldrin = 17;
        public const int Aridia = 18;
        public const int QwarksHideout = 19;
        public const int ObaniDraco = 21;
        public const int Mylon = 22;
    }
    
    public class QuickSelectSlots
    {
        public const ulong oneOne = 0x201D4C60 + GlobalConfig.QuicksetOffset;
        public const ulong oneTwo = 0x201D4C64 + GlobalConfig.QuicksetOffset;
        public const ulong oneThree = 0x201D4C68 + GlobalConfig.QuicksetOffset;
        public const ulong oneFour = 0x201D4C6C + GlobalConfig.QuicksetOffset;
        public const ulong oneFive = 0x201D4C70 + GlobalConfig.QuicksetOffset;
        public const ulong oneSix = 0x201D4C74 + GlobalConfig.QuicksetOffset;
        public const ulong oneSeven = 0x201D4C78 + GlobalConfig.QuicksetOffset;
        public const ulong oneEight = 0x201D4C7C + GlobalConfig.QuicksetOffset;

        public const ulong twoOne = 0x201D4C80 + GlobalConfig.QuicksetOffset;
        public const ulong twoTwo = 0x201D4C84 + GlobalConfig.QuicksetOffset;
        public const ulong twoThree = 0x201D4C88 + GlobalConfig.QuicksetOffset;
        public const ulong twoFour = 0x201D4C8C + GlobalConfig.QuicksetOffset;
        public const ulong twoFive = 0x201D4C90 + GlobalConfig.QuicksetOffset;
        public const ulong twoSix = 0x201D4C94 + GlobalConfig.QuicksetOffset;
        public const ulong twoSeven = 0x201D4C98 + GlobalConfig.QuicksetOffset;
        public const ulong twoEight = 0x201D4C9C + GlobalConfig.QuicksetOffset;
    }
    
    public class DummyEXPAddresses
    {
        //Refer to EXP Controller
        public const int ShockBlaster = 0x20100004;
        public const int NitroLauncher = 0x20100008;
        public const int N60Storm = 0x201000C;
        public const int PlasmaWhip = 0x2010010;
        public const int Infector = 0x20100014;
        public const int SuckCannon = 0x20100018;
        public const int SpittingHydra = 0x2010001C;
        public const int AgentsOfDoom = 0x20100020;
        public const int FluxRifle = 0x20100024;
        public const int Annihilator = 0x20100024;
        public const int HoloShieldGlove = 0x2010002C;
        public const int DiskBladeGun = 0x20100030;
        public const int RiftInducer = 0x20100034;
        public const int QwackORay = 0x20100038;
        public const int RY3N0 = 0x2010003C;
        public const int MegaTurretGlove = 0x20100040;
        public const int LavaGun = 0x20100044;
        public const int ShieldCharger = 0x20100048;
        public const int Bouncer = 0x2010004C;
        public const int PlasmaCoil = 0x20100050;
        public static int[] allDummy = [ShockBlaster, NitroLauncher, N60Storm, PlasmaWhip, Infector, SuckCannon, SpittingHydra, AgentsOfDoom, FluxRifle, Annihilator, HoloShieldGlove, DiskBladeGun, RiftInducer, QwackORay, RY3N0, MegaTurretGlove, LavaGun, ShieldCharger, Bouncer, PlasmaCoil];
    }
}
