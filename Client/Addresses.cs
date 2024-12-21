using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RaC3AP
{
    public class Addresses
    {
        //All weapon unlock addresses

        public const int unlockShockBlaster = 0x20142CC7;
        public const int unlockNitroLauncher = 0x20142D17;
        public const int unlockN60Storm = 0x20142CCF;
        public const int unlockPlasmaWhip = 0x20142D1F;
        public const int unlockInfector = 0x20142CD7;
        public const int unlockSuckCannon = 0x20142D27;
        public const int unlockSpittingHydra = 0x20142CE7;
        public const int unlockAgentsOfDoom = 0x20142CF7;
        public const int unlockFluxRifle = 0x20142D0F;
        public const int unlockAnnihilator = 0x20142CDF;
        public const int unlockHoloShieldGlove = 0x20142D07;
        public const int unlockDiskBladeGun = 0x20142CEF;
        public const int unlockRiftInducer = 0x20142CFF;
        public const int unlockQwackORay = 0x020142D2F;
        public const int unlockRY3N0 = 0x20142D37;
        public const int unlockMegaTurretGlove = 0x20142CB5;
        public const int unlockLavaGun = 0x20142CB1;
        public const int unlockShieldCharger = 0x20142CB6;
        public const int unlockBouncer = 0x20142CB3;
        public const int unlockPlasmaCoil = 0x20142CB0;


        public const int ammoShockBlaster = 0x2014288C;
        public const int ammoNitroLauncher = 0x201429CC;
        public const int ammoN60Storm = 0x201428AC;
        public const int ammoPlasmaWhip = 0x201429EC;
        public const int ammoInfector = 0x201428CC;
        public const int ammoSpittingHydra = 0x2014290C;
        public const int ammoAgentsOfDoom = 0x2014294C;
        public const int ammoFluxRifle = 0x201429AC;
        public const int ammoAnnihilator = 0x201428EC;
        public const int ammoHoloShieldGlove = 0x2014298C;
        public const int ammoDiskBladeGun = 0x2014292C;
        public const int ammoRiftInducer = 0x2014296C;
        public const int ammoRY3N0 = 0x20142A4C;
        public const int ammoMegaTurretGlove = 0x20142844;
        public const int ammoLavaGun = 0x20142834;
        public const int ammoShieldCharger = 0x20142848;
        public const int ammoBouncer = 0x2014283C;
        public const int ammoPlasmaCoil = 0x20142830;
        

        public const int boltXPMultiplier = 0x201426BA;
        public const int armorEquipped = 0x201426A0;
        public const int currentArmor = 0;
        public const int currentEquippedWeapon = 0x201D4C40;
        public const int weaponDisplay = 0x201A5E08;
        public const int boltIncrementDisplay = 0x201E0440;
        public const int currentlyEquippedWeapon = 0x201D4C40;
        public const int lastUsedWeaponTwo = 0x20142674;
        public const int lastUsedWeaponThree = 0x20142678;
    }
    

    public class GadgetAddresses
    {

        public const int hyperShot = 0x20142CAB;
        public const int refractor = 0x20142CB2;
        public const int tyhrraGuise = 0x20142CBE;
        public const int warpPad = 0x20142CBF;
        public const int pda = 0x20142CC3;
        public const int chargeBoots = 0x20142CBD;
        public const int gravBoots = 0x20142CAD;
        public const int hacker = 0x20142CB4;
        public const int boltGrabberV2 = 0x20142CA7;
        public const int mapOMatic = 0x20142CA5;
        public const int nanoPak = 0x20142CC0;

        public const int vidComic1 = 0x201D554F;
        public const int vidComic2 = 0x201D5551;
        public const int vidComic3 = 0x201D5552;
        public const int vidComic4 = 0x201D5550;
        public const int vidComic5 = 0x201D5553;
    }
    public class PlanetSlots
    {
        public const int slotOne = 0x20143050;
        public const int slotTwo = 0x20143054;
        public const int slotThree = 0x20143058;
        public const int slotFour = 0x2014305C;
        public const int slotFive = 0x20143060;
        public const int slotSix = 0x20143064;
        public const int slotSeven = 0x20143068;
        public const int slotEight = 0x2014306C;
        public const int slotNine = 0x20143070;
        public const int slotTen = 0x20143074;
        public const int slotEleven = 0x20143078;
        public const int slotTwelve = 0x2014307C;
        public const int slotThirteen = 0x20143080;
        public const int slotFourteen = 0x20143084;
        public const int slotFifteen = 0x20143088;
        public const int slotSixteen = 0x2014308C;
        public const int slotSeventeen = 0x20143090;
        public const int slotEighteen = 0x20143094;
        public const int slotNineteen = 0x20143098;
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
        public const ulong oneOne = 0x201D4C60;
        public const ulong oneTwo = 0x201D4C64;
        public const ulong oneThree = 0x201D4C68;
        public const ulong oneFour = 0x201D4C6C;
        public const ulong oneFive = 0x201D4C70;
        public const ulong oneSix = 0x201D4C74;
        public const ulong oneSeven = 0x201D4C78;
        public const ulong oneEight = 0x201D4C7C;

        public const ulong twoOne = 0x201D4C80;
        public const ulong twoTwo = 0x201D4C84;
        public const ulong twoThree = 0x201D4C88;
        public const ulong twoFour = 0x201D4C8C;
        public const ulong twoFive = 0x201D4C90;
        public const ulong twoSix = 0x201D4C94;
        public const ulong twoSeven = 0x201D4C98;
        public const ulong twoEight = 0x201D4C9C;
    }
    
    public class DummyEXPAddresses
    {
        //Refer to EXP Controller
        public const int ShockBlaster = 0x2500B000;
        public const int NitroLauncher = 0x2500B004;
        public const int N60Storm = 0x2500B008;
        public const int PlasmaWhip = 0x2500B00C;
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