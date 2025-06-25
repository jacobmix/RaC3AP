using Archipelago.Core.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Archipelago.Core;

namespace RaC3AP.Models
{
    public class Weapon(string weaponName, ulong expAddress, ulong versionAddress, ulong unlockAddress, ulong dummyExpAddress)
    {


        public int Unlock { get; set; } = 0;
        public int EXP { get; set; } = 0;
        public long realEXP { get; set; } = 0;
        public int Ammo { get; set; } = 0;
        public int Pointer {  get; set; } = 0;
        public int Version { get; set; } = 0;


        public string weaponName = weaponName;
        public ulong expAddressDumb = dummyExpAddress;
        public ulong expAddress = expAddress;
        public ulong versionAddress = versionAddress;
        public ulong unlockAddress = unlockAddress;
        public int unlockWait = 0;
    }
}
