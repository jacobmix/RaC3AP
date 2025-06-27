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
 * Quicksetting(CurrentEquipment + 0x20):
 * English  : 20 1D4C60
 * Japanese : 20 1DDF20
 * diff: 92C0
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
 * Challenge mode flag:  EN:142692 JP:142612
 * VR Training JP: 1426E6 - ED + last clear flag
 * Anihilation JP: 1426EE -70B + last clear flag
 * Marcadia Mission JP: 1426B8 - BC
 * BlackWater Mission JP: 1426BD - BF ?
 * Metrostorm Mission JP: 1426C7 - CB 
 * 
 * VidComic Clear flag JP
 * 0x001426B4 xx54_231x
 *   ALL clear: 3E
 *   1-4 clear: 1E
 *   1-3 clear: 0E
 *   1-2 clear: 0A
 *   1-1 clear: 02
 *   Not clear: 00
 * 
 * Boss:
 * Giant Crank: 0x00142708 
 */
namespace RaC3AP
{
    public static class GlobalConfig
    {
        public const int AddressOffset = -0x80; // EN: 0x00, JP: -0x80
        public const int EquipmentOffset = 0x92C0; // EN: 0x00, JP: 0x92C0
        public const int VidComicOffset = 0x9300; // EN: 0x00, JP: 0x9300
        public const int TitaniumOffset = 0x9298; // EN: 0x00, JP: 0x9300
        /*
        public const int AddressOffset = 0x0; // EN: 0x00, JP: -0x80
        public const int QuicksetOffset = 0x0; // EN: 0x00, JP: 0xCDE0
        public const int CurrentEquipmentOffset = 0x0; // EN: 0x00, JP: 0x92C0
        */
        public const int NanotecExp = 0x00142694 + GlobalConfig.AddressOffset; //

        public const int DefeatNefarious = 0x0014270F + GlobalConfig.AddressOffset; // Nefariuos
        public const int DefeatBiobliterator = 0x00142BB6 + GlobalConfig.AddressOffset; // Biobliterator
    }

    public class WeaponUnlocks
    {
        //All weapon unlock addresses
        public const int unlockShockBlaster = 0x00142CC7 + GlobalConfig.AddressOffset;
        public const int unlockNitroLauncher = 0x00142D17 + GlobalConfig.AddressOffset;
        public const int unlockN60Storm = 0x00142CCF + GlobalConfig.AddressOffset;
        public const int unlockPlasmaWhip = 0x00142D1F + GlobalConfig.AddressOffset;
        public const int unlockInfector = 0x00142CD7 + GlobalConfig.AddressOffset;
        public const int unlockSuckCannon = 0x00142D27 + GlobalConfig.AddressOffset;
        public const int unlockSpittingHydra = 0x00142CE7 + GlobalConfig.AddressOffset;
        public const int unlockAgentsOfDoom = 0x00142CF7 + GlobalConfig.AddressOffset;
        public const int unlockFluxRifle = 0x00142D0F + GlobalConfig.AddressOffset;
        public const int unlockAnnihilator = 0x00142CDF + GlobalConfig.AddressOffset;
        public const int unlockHoloShieldGlove = 0x00142D07 + GlobalConfig.AddressOffset;
        public const int unlockDiskBladeGun = 0x00142CEF + GlobalConfig.AddressOffset;
        public const int unlockRiftInducer = 0x00142CFF + GlobalConfig.AddressOffset;
        public const int unlockQwackORay = 0x000142D2F + GlobalConfig.AddressOffset;
        public const int unlockRY3N0 = 0x00142D37 + GlobalConfig.AddressOffset;
        public const int unlockMegaTurretGlove = 0x00142CB5 + GlobalConfig.AddressOffset;
        public const int unlockLavaGun = 0x00142CB1 + GlobalConfig.AddressOffset;
        public const int unlockShieldCharger = 0x00142CB6 + GlobalConfig.AddressOffset;
        public const int unlockBouncer = 0x00142CB3 + GlobalConfig.AddressOffset;
        public const int unlockPlasmaCoil = 0x00142CB0 + GlobalConfig.AddressOffset;
    }

        public class Addresses
    {
        public const int ammoShockBlaster = 0x0014288C + GlobalConfig.AddressOffset;
        public const int ammoNitroLauncher = 0x001429CC + GlobalConfig.AddressOffset;
        public const int ammoN60Storm = 0x001428AC + GlobalConfig.AddressOffset;
        public const int ammoPlasmaWhip = 0x001429EC + GlobalConfig.AddressOffset;
        public const int ammoInfector = 0x001428CC + GlobalConfig.AddressOffset;
        public const int ammoSpittingHydra = 0x0014290C + GlobalConfig.AddressOffset;
        public const int ammoAgentsOfDoom = 0x0014294C + GlobalConfig.AddressOffset;
        public const int ammoFluxRifle = 0x001429AC + GlobalConfig.AddressOffset;
        public const int ammoAnnihilator = 0x001428EC + GlobalConfig.AddressOffset;
        public const int ammoHoloShieldGlove = 0x0014298C + GlobalConfig.AddressOffset;
        public const int ammoDiskBladeGun = 0x0014292C + GlobalConfig.AddressOffset;
        public const int ammoRiftInducer = 0x0014296C + GlobalConfig.AddressOffset;
        public const int ammoRY3N0 = 0x00142A4C + GlobalConfig.AddressOffset;
        public const int ammoMegaTurretGlove = 0x00142844 + GlobalConfig.AddressOffset;
        public const int ammoLavaGun = 0x00142834 + GlobalConfig.AddressOffset;
        public const int ammoShieldCharger = 0x00142848 + GlobalConfig.AddressOffset;
        public const int ammoBouncer = 0x0014283C + GlobalConfig.AddressOffset;
        public const int ammoPlasmaCoil = 0x00142830 + GlobalConfig.AddressOffset;


        public const int boltXPMultiplier = 0x001426BA + GlobalConfig.AddressOffset;
        public const int armorEquipped = 0x001426A0 + GlobalConfig.AddressOffset;
        public static byte currentArmor = 0;
        public const int weaponDisplay = 0x001A5E08 + GlobalConfig.AddressOffset;
        public const int boltIncrementDisplay = 0x001E0440 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponOne = 0x00142670 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponTwo = 0x00142674 + GlobalConfig.AddressOffset;
        public const int lastUsedWeaponThree = 0x00142678 + GlobalConfig.AddressOffset;

        public const int junkAddr1 = 0x0027DC00 + GlobalConfig.AddressOffset;
        public const int junkAddr2 = 0x0027DC04 + GlobalConfig.AddressOffset;

        public const int currentlyEquippedWeapon = 0x001D4C40 + GlobalConfig.EquipmentOffset;
    }
    public class GadgetAddresses
    {

        public const int hyperShot = 0x00142CAB + GlobalConfig.AddressOffset;
        public const int refractor = 0x00142CB2 + GlobalConfig.AddressOffset;
        public const int tyhrraGuise = 0x00142CBE + GlobalConfig.AddressOffset;
        public const int warpPad = 0x00142CBF + GlobalConfig.AddressOffset;
        public const int pda = 0x00142CC3 + GlobalConfig.AddressOffset;
        public const int chargeBoots = 0x00142CBD + GlobalConfig.AddressOffset;
        public const int gravBoots = 0x00142CAD + GlobalConfig.AddressOffset;
        public const int hacker = 0x00142CB4 + GlobalConfig.AddressOffset;
        public const int boltGrabberV2 = 0x00142CA7 + GlobalConfig.AddressOffset;
        public const int mapOMatic = 0x00142CA5 + GlobalConfig.AddressOffset;
        public const int nanoPak = 0x00142CC0 + GlobalConfig.AddressOffset;

        public const int vidComic1 = 0x001D554F + GlobalConfig.VidComicOffset;
        public const int vidComic2 = 0x001D5551 + GlobalConfig.VidComicOffset;
        public const int vidComic3 = 0x001D5552 + GlobalConfig.VidComicOffset;
        public const int vidComic4 = 0x001D5550 + GlobalConfig.VidComicOffset;
        public const int vidComic5 = 0x001D5553 + GlobalConfig.VidComicOffset;
    }
    public class PlanetSlots
    {
        public const int slotOne = 0x00143050 + GlobalConfig.AddressOffset;
        public const int slotTwo = 0x00143054 + GlobalConfig.AddressOffset;
        public const int slotThree = 0x00143058 + GlobalConfig.AddressOffset;
        public const int slotFour = 0x0014305C + GlobalConfig.AddressOffset;
        public const int slotFive = 0x00143060 + GlobalConfig.AddressOffset;
        public const int slotSix = 0x00143064 + GlobalConfig.AddressOffset;
        public const int slotSeven = 0x00143068 + GlobalConfig.AddressOffset;
        public const int slotEight = 0x0014306C + GlobalConfig.AddressOffset;
        public const int slotNine = 0x00143070 + GlobalConfig.AddressOffset;
        public const int slotTen = 0x00143074 + GlobalConfig.AddressOffset;
        public const int slotEleven = 0x00143078 + GlobalConfig.AddressOffset;
        public const int slotTwelve = 0x0014307C + GlobalConfig.AddressOffset;
        public const int slotThirteen = 0x00143080 + GlobalConfig.AddressOffset;
        public const int slotFourteen = 0x00143084 + GlobalConfig.AddressOffset;
        public const int slotFifteen = 0x00143088 + GlobalConfig.AddressOffset;
        public const int slotSixteen = 0x0014308C + GlobalConfig.AddressOffset;
        public const int slotSeventeen = 0x00143090 + GlobalConfig.AddressOffset;
        public const int slotEighteen = 0x00143094 + GlobalConfig.AddressOffset;
        public const int slotNineteen = 0x00143098 + GlobalConfig.AddressOffset;
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
        public const ulong oneOne = 0x001D4C60 + GlobalConfig.EquipmentOffset;
        public const ulong oneTwo = 0x001D4C64 + GlobalConfig.EquipmentOffset;
        public const ulong oneThree = 0x001D4C68 + GlobalConfig.EquipmentOffset;
        public const ulong oneFour = 0x001D4C6C + GlobalConfig.EquipmentOffset;
        public const ulong oneFive = 0x001D4C70 + GlobalConfig.EquipmentOffset;
        public const ulong oneSix = 0x001D4C74 + GlobalConfig.EquipmentOffset;
        public const ulong oneSeven = 0x001D4C78 + GlobalConfig.EquipmentOffset;
        public const ulong oneEight = 0x001D4C7C + GlobalConfig.EquipmentOffset;

        public const ulong twoOne = 0x001D4C80 + GlobalConfig.EquipmentOffset;
        public const ulong twoTwo = 0x001D4C84 + GlobalConfig.EquipmentOffset;
        public const ulong twoThree = 0x001D4C88 + GlobalConfig.EquipmentOffset;
        public const ulong twoFour = 0x001D4C8C + GlobalConfig.EquipmentOffset;
        public const ulong twoFive = 0x001D4C90 + GlobalConfig.EquipmentOffset;
        public const ulong twoSix = 0x001D4C94 + GlobalConfig.EquipmentOffset;
        public const ulong twoSeven = 0x001D4C98 + GlobalConfig.EquipmentOffset;
        public const ulong twoEight = 0x001D4C9C + GlobalConfig.EquipmentOffset;
    }
    
    public class DummyEXPAddresses
    {
        //Refer to EXP Controller
        public const int ShockBlaster = 0x00100004;
        public const int NitroLauncher = 0x00100008;
        public const int N60Storm = 0x001000C;
        public const int PlasmaWhip = 0x0010010;
        public const int Infector = 0x00100014;
        public const int SuckCannon = 0x00100018;
        public const int SpittingHydra = 0x0010001C;
        public const int AgentsOfDoom = 0x00100020;
        public const int FluxRifle = 0x00100024;
        public const int Annihilator = 0x00100024;
        public const int HoloShieldGlove = 0x0010002C;
        public const int DiskBladeGun = 0x00100030;
        public const int RiftInducer = 0x00100034;
        public const int QwackORay = 0x00100038;
        public const int RY3N0 = 0x0010003C;
        public const int MegaTurretGlove = 0x00100040;
        public const int LavaGun = 0x00100044;
        public const int ShieldCharger = 0x00100048;
        public const int Bouncer = 0x0010004C;
        public const int PlasmaCoil = 0x00100050;
        public static int[] allDummy = [ShockBlaster, NitroLauncher, N60Storm, PlasmaWhip, Infector, SuckCannon, SpittingHydra, AgentsOfDoom, FluxRifle, Annihilator, HoloShieldGlove, DiskBladeGun, RiftInducer, QwackORay, RY3N0, MegaTurretGlove, LavaGun, ShieldCharger, Bouncer, PlasmaCoil];
    }
}
