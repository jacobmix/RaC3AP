using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace RaC3AP.Models
{
    public class WeaponVersionData
    {

        //ARRAY POSITION MUST COINCIDE WITH WEAPON VERSION OTHERWISE IT WILL AUTO UPGRADE TO THE NEXT VERSION
        public static int[] ARRexpShockBlaster = { 0, 4800, 12800, 22400, 32000 };
        public static int[] ARRexpNitroLauncher = { 0, 6400, 16000, 35200, 83200 };
        public static int[] ARRexpN60Storm = { 0, 6400, 16000, 48000, 57600 };
        public static int[] ARRexpPlasmaWhip = { 0, 6400, 25600, 57600, 105600 };
        public static int[] ARRexpInfector = { 0, 12800, 25600, 64000, 121600 };
        public static int[] ARRexpSuckCannon = { 0, 6400, 19200, 38400, 76800 };
        public static int[] ARRexpSpittingHydra = { 0, 9600, 28800, 57600, 96000 };
        public static int[] ARRexpAgentsOfDoom = { 0, 12800, 32000, 96000, 192000 };
        public static int[] ARRexpFluxRifle = { 0, 6400, 19200, 48000, 92800 };
        public static int[] ARRexpAnnihilator = { 0, 25600, 76800, 204800, 396800 };
        public static int[] ARRexpHoloShieldGlove = { 0, 4800, 14400, 43200, 86400 };
        public static int[] ARRexpDiskBladeGun = { 0, 22400, 67200, 195200, 387200 };
        public static int[] ARRexpRiftInducer = { 0, 25600, 76800, 204800, 396800 };
        public static int[] ARRexpQwackORay = { 0, 32000, 96000, 256000, 512000 };
        public static int[] ARRexpRY3N0 = { 0, 640000, 1600000, 2880000, 4480000 };
        public static int[] ARRexpMegaTurretGlove = { 0, 12800, 32000, 64000, 112000 };
        public static int[] ARRexpLavaGun = { 0, 19200, 48000, 86400, 134400 };
        public static int[] ARRexpShieldCharger = { 0, 70400, 160000, 307200, 537600 };
        public static int[] ARRexpBouncer = { 0, 80000, 272000, 592000, 976000};
        public static int[] ARRexpPlasmaCoil = { 0, 256000, 576000, 960000, 1408000};

        public static int[] ARRversionShockBlaster = { 39, 40, 41, 42, 43 };
        public static int[] ARRversionNitroLauncher = { 119, 120, 121, 122, 123 };
        public static int[] ARRversionN60Storm = { 47, 48, 49, 50, 51 };
        public static int[] ARRversionPlasmaWhip = { 127, 128, 129, 130, 131 };
        public static int[] ARRversionInfector = { 55, 56, 57, 58, 59 };
        public static int[] ARRversionSuccCannon = { 135, 136, 137, 138, 139 };
        public static int[] ARRversionSpittingHydra = { 71, 72, 73, 74, 75 };
        public static int[] ARRversionAgentsOfDoom = { 87, 88, 89, 90, 91 };
        public static int[] ARRversionFluxRifle = { 111, 112, 113, 114, 115 };
        public static int[] ARRversionAnnihilator = { 63, 64, 65, 66, 67 };
        public static int[] ARRversionHoloShieldGlove = { 103, 104, 105, 106, 107 };
        public static int[] ARRversionDiskBladeGun = { 79, 80, 81, 82, 83 };
        public static int[] ARRversionRiftInducer = { 95, 96, 97, 98, 99 };
        public static int[] ARRversionQwackORay = { 143, 144, 145, 146, 147 };
        public static int[] ARRversionRY3N0 = { 151, 152, 153, 154, 155 };
        public static int[] ARRversionMegaTurretGlove = { 21, 162, 168, 169, 170 };
        public static int[] ARRversionLavaGun = { 17, 161, 174, 175, 176 };
        public static int[] ARRversionShieldCharger = { 22, 167, 192, 193, 194 };
        public static int[] ARRversionBouncer = { 19, 166, 180, 181, 182 };
        public static int[] ARRversionPlasmaCoil = { 16, 160, 186, 187, 188 };
        public static byte versionWrench = 9;


        public const int ADDexpShockBlaster = 0x20142E7C;
        public const int ADDexpNitroLauncher = 0x20142FBC;
        public const int ADDexpN60Storm = 0x20142E9C;
        public const int ADDexpPlasmaWhip = 0x20142FDC;
        public const int ADDexpInfector = 0x20142EBC;
        public const int ADDexpSuckCannon = 0x20142FFC;
        public const int ADDexpSpittingHydra = 0x20142EFC;
        public const int ADDexpAgentsOfDoom = 0x20142F3C;
        public const int ADDexpFluxRifle = 0x20142F9C;
        public const int ADDexpAnnihilator = 0x20142EDC;
        public const int ADDexpHoloShieldGlove = 0x20142F7C;
        public const int ADDexpDiskBladeGun = 0x20142F1C;
        public const int ADDexpRiftInducer = 0x20142F5C;
        public const int ADDexpQwackORay = 0x2014301C;
        public const int ADDexpRY3N0 = 0x2014303C;
        public const int ADDexpMegaTurretGlove = 0x20142E34;
        public const int ADDexpLavaGun = 0x20142E24;
        public const int ADDexpShieldCharger = 0x20142E38;
        public const int ADDexpBouncer = 0x20142E2C;
        public const int ADDexpPlasmaCoil = 0x20142E20;
        public static ulong[] allADDExp = [ADDexpShockBlaster, ADDexpNitroLauncher, ADDexpN60Storm, ADDexpPlasmaWhip, ADDexpInfector, ADDexpSuckCannon, ADDexpSpittingHydra, ADDexpAgentsOfDoom, ADDexpFluxRifle, ADDexpAnnihilator, ADDexpHoloShieldGlove, ADDexpDiskBladeGun, ADDexpRiftInducer, ADDexpQwackORay, ADDexpRY3N0, ADDexpMegaTurretGlove, ADDexpLavaGun, ADDexpShieldCharger, ADDexpBouncer, ADDexpPlasmaCoil];


        public const int ADDversionShockBlaster = 0x201425E7;
        public const int ADDversionNitroLauncher = 0x20142637;
        public const int ADDversionN60Storm = 0x201425EF;
        public const int ADDversionPlasmaWhip = 0x2014263F;
        public const int ADDversionInfector = 0x201425F7;
        public const int ADDversionSuccCannon = 0x20142647;
        public const int ADDversionSpittingHydra = 0x20142607;
        public const int ADDversionAgentsOfDoom = 20142617;
        public const int ADDversionFluxRifle = 0x2014262F;
        public const int ADDversionAnnihilator = 0x201425FF;
        public const int ADDversionHoloShieldGlove = 0x20142627;
        public const int ADDversionDiskBladeGun = 0x2014260F;
        public const int ADDversionRiftInducer = 0x2014261F;
        public const int ADDversionQwackORay = 0x2014264F;
        public const int ADDversionRY3N0 = 0x20142657;
        public const int ADDversionMegaTurretGlove = 0x201425D5;
        public const int ADDversionLavaGun = 0x201425D1;
        public const int ADDversionShieldCharger = 0x201425D6;
        public const int ADDversionBouncer = 0x201425D3;
        public const int ADDversionPlasmaCoil = 0x201425D0;
         
    }
}
