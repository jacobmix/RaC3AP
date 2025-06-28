using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RaC3AP.Models
{
    public class Gadget(string name, ulong unlockAddress)
    {
        public int Unlock { get; set; } = 0;
        public string name = name;
        public ulong unlockAddress = unlockAddress;
    }
}
