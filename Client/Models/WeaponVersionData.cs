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

        public const int AddressOffset = -0x80; // EN: 0x00, JP: -0x80
        public const int ADDexpShockBlaster = 0x00142E7C + AddressOffset;
        public const int ADDexpNitroLauncher = 0x00142FBC + AddressOffset;
        public const int ADDexpN60Storm = 0x00142E9C + AddressOffset;
        public const int ADDexpPlasmaWhip = 0x00142FDC + AddressOffset;
        public const int ADDexpInfector = 0x00142EBC + AddressOffset;
        public const int ADDexpSuckCannon = 0x00142FFC + AddressOffset;
        public const int ADDexpSpittingHydra = 0x00142EFC + AddressOffset;
        public const int ADDexpAgentsOfDoom = 0x00142F3C + AddressOffset;
        public const int ADDexpFluxRifle = 0x00142F9C + AddressOffset;
        public const int ADDexpAnnihilator = 0x00142EDC + AddressOffset;
        public const int ADDexpHoloShieldGlove = 0x00142F7C + AddressOffset;
        public const int ADDexpDiskBladeGun = 0x00142F1C + AddressOffset;
        public const int ADDexpRiftInducer = 0x00142F5C + AddressOffset;
        public const int ADDexpQwackORay = 0x0014301C + AddressOffset;
        public const int ADDexpRY3N0 = 0x0014303C + AddressOffset;
        public const int ADDexpMegaTurretGlove = 0x00142E34 + AddressOffset;
        public const int ADDexpLavaGun = 0x00142E24 + AddressOffset;
        public const int ADDexpShieldCharger = 0x00142E38 + AddressOffset;
        public const int ADDexpBouncer = 0x00142E2C + AddressOffset;
        public const int ADDexpPlasmaCoil = 0x00142E20 + AddressOffset;
        public static ulong[] allADDExp = [ADDexpShockBlaster, ADDexpNitroLauncher, ADDexpN60Storm, ADDexpPlasmaWhip, ADDexpInfector, ADDexpSuckCannon, ADDexpSpittingHydra, ADDexpAgentsOfDoom, ADDexpFluxRifle, ADDexpAnnihilator, ADDexpHoloShieldGlove, ADDexpDiskBladeGun, ADDexpRiftInducer, ADDexpQwackORay, ADDexpRY3N0, ADDexpMegaTurretGlove, ADDexpLavaGun, ADDexpShieldCharger, ADDexpBouncer, ADDexpPlasmaCoil];


        public const int ADDversionShockBlaster = 0x001425E7 + AddressOffset;
        public const int ADDversionNitroLauncher = 0x00142637 + AddressOffset;
        public const int ADDversionN60Storm = 0x001425EF + AddressOffset;
        public const int ADDversionPlasmaWhip = 0x0014263F + AddressOffset;
        public const int ADDversionInfector = 0x001425F7 + AddressOffset;
        public const int ADDversionSuccCannon = 0x00142647 + AddressOffset;
        public const int ADDversionSpittingHydra = 0x00142607 + AddressOffset;
        public const int ADDversionAgentsOfDoom = 20142617 + AddressOffset;
        public const int ADDversionFluxRifle = 0x0014262F + AddressOffset;
        public const int ADDversionAnnihilator = 0x001425FF + AddressOffset;
        public const int ADDversionHoloShieldGlove = 0x00142627 + AddressOffset;
        public const int ADDversionDiskBladeGun = 0x0014260F + AddressOffset;
        public const int ADDversionRiftInducer = 0x0014261F + AddressOffset;
        public const int ADDversionQwackORay = 0x0014264F + AddressOffset;
        public const int ADDversionRY3N0 = 0x00142657 + AddressOffset;
        public const int ADDversionMegaTurretGlove = 0x001425D5 + AddressOffset;
        public const int ADDversionLavaGun = 0x001425D1 + AddressOffset;
        public const int ADDversionShieldCharger = 0x001425D6 + AddressOffset;
        public const int ADDversionBouncer = 0x001425D3 + AddressOffset;
        public const int ADDversionPlasmaCoil = 0x001425D0 + AddressOffset;
         
    }
}
