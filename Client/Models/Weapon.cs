using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sly1AP.Models
{
    public class Weapon(ulong expAddress, ulong versionAddress, ulong unlockAddress, ulong dummyExpAddress)
    {
        public int Unlock { get; set; } = 0;
        public int EXP { get; set; } = 0;
        public int realEXP { get; set; } = 0;
        public int Ammo { get; set; } = 0;
        public int Pointer {  get; set; } = 0;
        public int Version { get; set; } = 0;


        public ulong expAddressDumb = dummyExpAddress;
        public ulong expAddress = expAddress;
        public ulong versionAddress = versionAddress;
        public ulong unlockAddress = unlockAddress;
    }
}
