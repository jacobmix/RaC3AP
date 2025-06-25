// See https://aka.ms/new-console-template for more information
using Archipelago.Core;
using Archipelago.Core.Models;
using Archipelago.Core.Util;
using Archipelago.Core.GameClients;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using RaC3AP.Models;
using System.Net;
using System.Numerics;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Xml.Linq;
using static System.Reflection.Metadata.BlobBuilder;

public class cPCSX2Client : IGameClient
{
    public bool IsConnected { get; set; }
    public int ProcId { get; set; }
    public string ProcessName { get; set; }
    public cPCSX2Client()
    {

        ProcessName = "pcsx2-qt";

        ProcId = Memory.GetProcessID(ProcessName);
    }
    public bool Connect()
    {
        Console.WriteLine($"Connecting to {ProcessName}");
        if (ProcId == 0)
        {
            Console.WriteLine($"{ProcessName} not found.");
            return false;
        }
        IsConnected = true;
        return true;
    }
}


namespace RaC3AP
{
    public static class Program
    {   

        public static string GameVersion { get; set; } = "0";
        public static bool IsConnected { get; set; } = false;
        public static ArchipelagoClient Client { get; set; }
        public static GameState CurrentGameState = new GameState();
        
        public static ulong[] AvailableSlots = [PlanetSlots.slotOne, PlanetSlots.slotTwo, PlanetSlots.slotThree, PlanetSlots.slotFour, PlanetSlots.slotFive, PlanetSlots.slotSix, PlanetSlots.slotSeven, PlanetSlots.slotEight, PlanetSlots.slotNine, PlanetSlots.slotTen, PlanetSlots.slotEleven, PlanetSlots.slotTwelve, PlanetSlots.slotThirteen, PlanetSlots.slotFourteen, PlanetSlots.slotFifteen, PlanetSlots.slotSixteen, PlanetSlots.slotSeventeen, PlanetSlots.slotEighteen, PlanetSlots.slotNineteen];
        public static ulong[] QuickSelect = [QuickSelectSlots.oneOne, QuickSelectSlots.oneTwo, QuickSelectSlots.oneThree, QuickSelectSlots.oneFour, QuickSelectSlots.oneFive, QuickSelectSlots.oneSix, QuickSelectSlots.oneSeven, QuickSelectSlots.oneEight, QuickSelectSlots.twoOne, QuickSelectSlots.twoTwo, QuickSelectSlots.twoThree, QuickSelectSlots.twoFour, QuickSelectSlots.twoFive, QuickSelectSlots.twoSix, QuickSelectSlots.twoSeven, QuickSelectSlots.twoEight];
        public static ulong[] lastUsed = [Addresses.lastUsedWeaponOne, Addresses.lastUsedWeaponTwo, Addresses.lastUsedWeaponThree];
        public static int currentMultiplier = 2;
        public static Weapon ShockBlaster = new Weapon("Shock Blaster", WeaponVersionData.ADDexpShockBlaster, WeaponVersionData.ADDversionShockBlaster, WeaponUnlocks.unlockShockBlaster, DummyEXPAddresses.ShockBlaster);
        public static Weapon NitroLauncher = new Weapon("Nitro Launcher", WeaponVersionData.ADDexpNitroLauncher, WeaponVersionData.ADDversionNitroLauncher, WeaponUnlocks.unlockNitroLauncher, DummyEXPAddresses.NitroLauncher);
        public static Weapon N60Storm = new Weapon("N60 Storm", WeaponVersionData.ADDexpN60Storm, WeaponVersionData.ADDversionN60Storm, WeaponUnlocks.unlockN60Storm, DummyEXPAddresses.N60Storm);
        public static Weapon PlasmaWhip = new Weapon("Plasma Whip", WeaponVersionData.ADDexpPlasmaWhip, WeaponVersionData.ADDversionPlasmaWhip, WeaponUnlocks.unlockPlasmaWhip, DummyEXPAddresses.PlasmaWhip);
        public static Weapon Infector = new Weapon("Infector", WeaponVersionData.ADDexpInfector, WeaponVersionData.ADDversionInfector, WeaponUnlocks.unlockInfector, DummyEXPAddresses.Infector);
        public static Weapon SuckCannon = new Weapon("Suck Cannon", WeaponVersionData.ADDexpSuckCannon, WeaponVersionData.ADDversionSuccCannon, WeaponUnlocks.unlockSuckCannon, DummyEXPAddresses.SuckCannon);
        public static Weapon SpittingHydra = new Weapon("Spitting Hydra", WeaponVersionData.ADDexpSpittingHydra, WeaponVersionData.ADDversionSpittingHydra, WeaponUnlocks.unlockSpittingHydra, DummyEXPAddresses.SpittingHydra);
        public static Weapon AgentsOfDoom = new Weapon("Agents Of Doom", WeaponVersionData.ADDexpAgentsOfDoom,WeaponVersionData.ADDversionAgentsOfDoom, WeaponUnlocks.unlockAgentsOfDoom, DummyEXPAddresses.AgentsOfDoom);
        public static Weapon FluxRifle = new Weapon("Flux Rifle", WeaponVersionData.ADDexpFluxRifle, WeaponVersionData.ADDversionFluxRifle, WeaponUnlocks.unlockFluxRifle, DummyEXPAddresses.FluxRifle);
        public static Weapon Annihilator = new Weapon("Annihilator", WeaponVersionData.ADDexpAnnihilator,WeaponVersionData.ADDversionAnnihilator, WeaponUnlocks.unlockAnnihilator, DummyEXPAddresses.Annihilator);
        public static Weapon HoloShieldGlove = new Weapon("Holo Shield Glove", WeaponVersionData.ADDexpHoloShieldGlove, WeaponVersionData.ADDversionHoloShieldGlove, WeaponUnlocks.unlockHoloShieldGlove, DummyEXPAddresses.HoloShieldGlove);
        public static Weapon DiskBladeGun = new Weapon("Disk Blade Gun", WeaponVersionData.ADDexpDiskBladeGun, WeaponVersionData.ADDversionDiskBladeGun, WeaponUnlocks.unlockDiskBladeGun, DummyEXPAddresses.DiskBladeGun);
        public static Weapon RiftInducer = new Weapon("Rift Inducer", WeaponVersionData.ADDexpRiftInducer, WeaponVersionData.ADDversionRiftInducer, WeaponUnlocks.unlockRiftInducer, DummyEXPAddresses.RiftInducer);
        public static Weapon QwackORay = new Weapon("Qwack-O-Ray", WeaponVersionData.ADDexpQwackORay, WeaponVersionData.ADDversionQwackORay, WeaponUnlocks.unlockQwackORay, DummyEXPAddresses.QwackORay);
        public static Weapon RY3N0 = new Weapon("RY3N0", WeaponVersionData.ADDexpRY3N0, WeaponVersionData.ADDversionRY3N0, WeaponUnlocks.unlockRY3N0, DummyEXPAddresses.RY3N0);
        public static Weapon MegaTurretGlove = new Weapon("Mega Turret Glove", WeaponVersionData.ADDexpMegaTurretGlove, WeaponVersionData.ADDversionMegaTurretGlove, WeaponUnlocks.unlockMegaTurretGlove, DummyEXPAddresses.MegaTurretGlove);
        public static Weapon LavaGun = new Weapon("Lava Gun", WeaponVersionData.ADDexpLavaGun, WeaponVersionData.ADDversionLavaGun, WeaponUnlocks.unlockLavaGun, DummyEXPAddresses.LavaGun);
        public static Weapon ShieldCharger = new Weapon("Shield Charger", WeaponVersionData.ADDexpShieldCharger,WeaponVersionData.ADDversionShieldCharger, WeaponUnlocks.unlockShieldCharger, DummyEXPAddresses.ShieldCharger);
        public static Weapon Bouncer = new Weapon("Bouncer", WeaponVersionData.ADDexpBouncer, WeaponVersionData.ADDversionBouncer, WeaponUnlocks.unlockBouncer, DummyEXPAddresses.Bouncer);
        public static Weapon PlasmaCoil = new Weapon("Plasma Coil", WeaponVersionData.ADDexpPlasmaCoil, WeaponVersionData.ADDversionPlasmaCoil, WeaponUnlocks.unlockPlasmaCoil, DummyEXPAddresses.PlasmaCoil);
        public static Weapon[] allWeapons = { ShockBlaster, NitroLauncher, N60Storm, PlasmaWhip, Infector, SuckCannon, SpittingHydra, AgentsOfDoom, FluxRifle, Annihilator, HoloShieldGlove, DiskBladeGun, RiftInducer, QwackORay, RY3N0, MegaTurretGlove, LavaGun, ShieldCharger, Bouncer, PlasmaCoil };
        public static Planet Marcadia = new Planet(PlanetValues.Marcadia);
        public static Planet Daxx = new Planet(PlanetValues.Daxx);
        public static Planet AnnihilationNation = new Planet(PlanetValues.AnnihilationNation);
        public static Planet Aquatos = new Planet(PlanetValues.Aquatos);
        public static Planet Tyhrranosis = new Planet(PlanetValues.Tyhrranosis);
        public static Planet ZeldrinStarport = new Planet(PlanetValues.ZeldrinStarport);
        public static Planet ObaniGemini = new Planet(PlanetValues.ObaniGemini);
        public static Planet Rilgar = new Planet (PlanetValues.Rilgar);
        public static Planet HolostarStudios = new Planet(PlanetValues.HolostarStudios);
        public static Planet Koros = new Planet(PlanetValues.Koros);
        public static Planet Metropolis = new Planet(PlanetValues.Metropolis);
        public static Planet Zeldrin = new Planet(PlanetValues.Zeldrin);
        public static Planet Aridia = new Planet(PlanetValues.Aridia);
        public static Planet QwarksHideout = new Planet(PlanetValues.QwarksHideout);
        public static Planet ObaniDraco = new Planet(PlanetValues.ObaniDraco);
        public static Planet Mylon = new Planet(PlanetValues.Mylon);
        public static Planet[] allPlanets = { Marcadia, Daxx, AnnihilationNation, Aquatos, Tyhrranosis, ZeldrinStarport, ObaniGemini, Rilgar, HolostarStudios, Koros, Metropolis, Zeldrin, Aridia, QwarksHideout, ObaniDraco, Mylon };

        public static int GameCompletion { get; set; } = 0;
        public static async Task Main()
        {
            // Console.SetBufferSize(Console.BufferWidth, 32766);
            Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
            ThreadPool.SetMinThreads(500, 500);

            Console.WriteLine("RaC 3 Archipelago Randomizer");

            await Initialise();

            Console.WriteLine("Beginning main loop.");
            while (true)
            {
                if (!IsConnected)
                {
                    Console.WriteLine("Not connected to Archipelago. Press any key to exit.");
                    Console.ReadKey();
                    return;
                };
                UpdateValues();


                await Task.Delay(1000);
            }
        }

        private static async Task Initialise()
        {
#if DEBUG
            string Address = "192.168.20.150:38281";
            string SlotName = "Player1";
            string Password = "";
#else
            Console.Write("Enter Address: ");
            string Address = Console.ReadLine();
            Console.Write("Enter Slot Name: ");
            string SlotName = Console.ReadLine();
            Console.Write("Enter Password: ");
            string Password = Console.ReadLine();
#endif
            IsConnected = await ConnectAsync(Address, SlotName, Password);
        }

        static async Task<bool> ConnectAsync(string address, string playerName, string password)
        {
            // Avoid Bug of Archipelago.Core v0.3.25, which is "System.ArgumentException: 'CurrentProcId has not been set'"
            //var client = new PCSX2Client();
            var client = new cPCSX2Client();

            var pcsx2Connected = client.Connect();
            if (!pcsx2Connected)
            {
                Console.WriteLine("Failed to connect to PCSX2.");
                return false;
            }
            Console.WriteLine($"Connected to PCSX2.");

            Console.WriteLine($"Connecting to Archipelago.");
            ArchipelagoClient Client = new(client);
            Memory.GlobalOffset = Memory.GetPCSX2Offset();

            //Set the game completion flag to 0, so boss locations won't be sent unintentionally.
            Memory.Write(GlobalConfig.DefeatNefarious, 0);

            await Client.Connect(address, "Ratchet and Clank 3 Up your Arsenal");
            var locations = Helpers.GetLocations();
            // Fix location Address for JP version
            var _i = 0;
            foreach (var location in locations)
            {
                var offset = 0;
                if (0x001BBB29 <= location.Address && location.Address <= 0x001BBB50) // Titanium Bolt
                    offset = GlobalConfig.TitaniumOffset;
                else if (0x001D554F <= location.Address && location.Address <= 0x001D5553) // VidComic
                    offset = GlobalConfig.VidComicOffset;
                else if (0x00100004 <= location.Address && location.Address <= 0x0010004C) // Weapon Dummy EXP
                    offset = 0;
                else // Others
                    offset = GlobalConfig.AddressOffset;
                var tmp = (long)location.Address + offset;
                locations[_i].Address = (ulong)tmp;
                _i++;
            }
            Console.WriteLine($"0x{locations[0].Address:X}");
            Console.WriteLine($"0x{locations[1].Address:X}");
            Console.WriteLine($"0x{locations[2].Address:X}");

            await Client.Login(playerName, password);
            Client.PopulateLocations(locations);
            //On startup, set all values to 0. That way, the game won't overwrite Archipelago's values with the loaded game's values.
            UpdateStart();
            ConfigureOptions(Client.Options);


            

            var SentLocations = Client.GameState.CompletedLocations;
            var ItemsReceived = Client.GameState.ReceivedItems;
            var NewItems = new List<Item>(ItemsReceived);
            var NewLocations = new List<Location>(SentLocations);
            foreach (var item in NewItems)
            {
                if (item.Id >= 50001452 & item.Id <= 50001466)
                {
                    UpdatePlanets(item.Id);
                }
                if (item.Id >= 50001400 & item.Id <= 50001419)
                {
                    UpdateWeapons(item.Id);
                }
                if (item.Id >= 50001420 & item.Id <= 50001439)
                {
                    UpdateUpgrades(item.Id);
                }
                if (item.Id >= 50001440 & item.Id <= 50001449 || item.Id >= 50001467 && item.Id <= 50001471)
                {
                    UpdateGadgets(item.Id);
                }
                if (item.Id == 50001480)
                {
                    UpdateArmor();
                }
            }
            Client.ItemReceived += (e, args) =>
            {
                Console.WriteLine($"Received: " + args.Item.Name);
                if (args.Item.Id >= 50001452 & args.Item.Id <= 50001466)
                {
                    UpdatePlanets(args.Item.Id);
                }
                if (args.Item.Id >= 50001400 & args.Item.Id <= 50001419)
                {
                    UpdateWeapons(args.Item.Id);
                }
                if (args.Item.Id >= 50001420 & args.Item.Id <= 50001439)
                {
                    UpdateUpgrades(args.Item.Id);
                }
                if (args.Item.Id >= 50001440 & args.Item.Id <= 50001449 || args.Item.Id >= 50001467 && args.Item.Id <= 50001471)
                {
                    UpdateGadgets(args.Item.Id);
                }
                if (args.Item.Id == 50001480)
                {
                    UpdateArmor();
                }
            };
            return true;
        }
        public static void ConfigureOptions(Dictionary<string, object> options)
        {
            var Options = new ArchipelagoOptions();
            if (options == null)
            {
                Console.WriteLine("Options dictionary is null.");
                return;
            }
            if (options.ContainsKey("StartingWeapon"))
            {
                string StartingWeapon = Convert.ToString(options["StartingWeapon"]);

                if (StartingWeapon == "Shock Blaster" & Memory.ReadInt(WeaponUnlocks.unlockShockBlaster) == 0)
                {
                    ShockBlaster.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockShockBlaster, ShockBlaster.Unlock);
                    Memory.Write(Addresses.ammoShockBlaster, 30);
                }
                if (StartingWeapon == "Nitro Launcher" & Memory.ReadInt(WeaponUnlocks.unlockNitroLauncher) == 0)
                {
                    NitroLauncher.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockNitroLauncher, NitroLauncher.Unlock);
                    Memory.Write(Addresses.ammoNitroLauncher, 8);
                }
                if (StartingWeapon == "N60 Storm" & Memory.ReadInt(WeaponUnlocks.unlockN60Storm) == 0)
                {
                    N60Storm.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockN60Storm, N60Storm.Unlock);
                    Memory.Write(Addresses.ammoN60Storm, 150);
                }
                if (StartingWeapon == "Plasma Whip" & Memory.ReadInt(WeaponUnlocks.unlockPlasmaWhip) == 0)
                {
                    PlasmaWhip.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockPlasmaWhip, PlasmaWhip.Unlock);
                    Memory.Write(Addresses.ammoPlasmaWhip, 25);

                }
                if (StartingWeapon == "Infector" & Memory.ReadInt(WeaponUnlocks.unlockInfector) == 0)
                {
                    Infector.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockInfector, Infector.Unlock);
                    Memory.Write(Addresses.ammoInfector, 15);

                }
                if (StartingWeapon == "Suck Cannon" & Memory.ReadInt(WeaponUnlocks.unlockSuckCannon) == 0)
                {
                    SuckCannon.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockSuckCannon, SuckCannon.Unlock);

                }
                if (StartingWeapon == "Spitting Hydra" & Memory.ReadInt(WeaponUnlocks.unlockSpittingHydra) == 0)
                {
                    SpittingHydra.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockSpittingHydra, SpittingHydra.Unlock);
                    Memory.Write(Addresses.ammoSpittingHydra, 15);

                }
                if (StartingWeapon == "Agents Of Doom" & Memory.ReadInt(WeaponUnlocks.unlockAgentsOfDoom) == 0)
                {
                    AgentsOfDoom.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockAgentsOfDoom, AgentsOfDoom.Unlock);
                    Memory.Write(Addresses.ammoAgentsOfDoom, 6);

                }
                if (StartingWeapon == "Flux Rifle" & Memory.ReadInt(WeaponUnlocks.unlockFluxRifle) == 0)
                {
                    FluxRifle.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockFluxRifle, FluxRifle.Unlock);
                    Memory.Write(Addresses.ammoFluxRifle, 10);

                }
                if (StartingWeapon == "Annihilator" & Memory.ReadInt(WeaponUnlocks.unlockAnnihilator) == 0)
                {
                    Annihilator.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockAnnihilator, Annihilator.Unlock);
                    Memory.Write(Addresses.ammoAnnihilator, 20);

                }
                if (StartingWeapon == "Holo Shield Glove" & Memory.ReadInt(WeaponUnlocks.unlockHoloShieldGlove) == 0)
                {
                    HoloShieldGlove.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockHoloShieldGlove, HoloShieldGlove.Unlock);
                    Memory.Write(Addresses.ammoHoloShieldGlove, 8);

                }
                if (StartingWeapon == "Disk Blade Gun" & Memory.ReadInt(WeaponUnlocks.unlockDiskBladeGun) == 0)
                {
                    DiskBladeGun.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockDiskBladeGun, DiskBladeGun.Unlock);
                    Memory.Write(Addresses.ammoDiskBladeGun, 25);

                }
                if (StartingWeapon == "Rift Inducer" & Memory.ReadInt(WeaponUnlocks.unlockRiftInducer) == 0)
                {
                    RiftInducer.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockRiftInducer, RiftInducer.Unlock);
                    Memory.Write(Addresses.ammoRiftInducer, 8);

                }
                if (StartingWeapon == "Qwack O Ray" & Memory.ReadInt(WeaponUnlocks.unlockQwackORay) == 0)
                {
                    QwackORay.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockQwackORay, QwackORay.Unlock);

                }
                if (StartingWeapon == "RY3N0" & Memory.ReadInt(WeaponUnlocks.unlockRY3N0) == 0)
                {
                    RY3N0.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockRY3N0, RY3N0.Unlock);
                    Memory.Write(Addresses.ammoRY3N0, 25);

                }
                if (StartingWeapon == "Mega Turret Glove" & Memory.ReadInt(WeaponUnlocks.unlockMegaTurretGlove) == 0)
                {
                    MegaTurretGlove.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockMegaTurretGlove, MegaTurretGlove.Unlock);
                    Memory.Write(Addresses.ammoMegaTurretGlove, 10);

                }
                if (StartingWeapon == "Lava Gun" & Memory.ReadInt(WeaponUnlocks.unlockLavaGun) == 0)
                {
                    LavaGun.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockLavaGun, LavaGun.Unlock);
                    Memory.Write(Addresses.ammoLavaGun, 150);

                }
                if (StartingWeapon == "Shield Charger" & Memory.ReadInt(WeaponUnlocks.unlockShieldCharger) == 0)
                {
                    ShieldCharger.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockShieldCharger, ShieldCharger.Unlock);
                    Memory.Write(Addresses.ammoShieldCharger, 3);

                }
                if (StartingWeapon == "Bouncer" & Memory.ReadInt(WeaponUnlocks.unlockBouncer) == 0)
                {
                    Bouncer.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockBouncer, Bouncer.Unlock);
                    Memory.Write(Addresses.ammoBouncer, 10);

                }
                if (StartingWeapon == "Plasma Coil" & Memory.ReadInt(WeaponUnlocks.unlockPlasmaCoil) == 0)
                {
                    PlasmaCoil.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockPlasmaCoil, PlasmaCoil.Unlock);
                    Memory.Write(Addresses.ammoPlasmaCoil, 15);

                }
            }

            if (options.ContainsKey("BoltandXPMultiplier"))
            {
                string boltAndXPMultiplier = Convert.ToString(options["BoltandXPMultiplier"]);
                Console.WriteLine(boltAndXPMultiplier);

                if (boltAndXPMultiplier == "x1") 
                { }
                if (boltAndXPMultiplier == "x2")
                {
                    currentMultiplier = 1;
                    Console.WriteLine(Convert.ToString(currentMultiplier));
                    Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);
                }
                if (boltAndXPMultiplier == "x4")
                {
                    currentMultiplier = 3;
                    Console.WriteLine(Convert.ToString(currentMultiplier));
                    Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);
                }
                if (boltAndXPMultiplier == "x6")
                {
                    currentMultiplier = 5;
                    Console.WriteLine(Convert.ToString(currentMultiplier));
                    Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);
                }
                if (boltAndXPMultiplier == "x8")
                {
                    currentMultiplier = 7;
                    Console.WriteLine(Convert.ToString(currentMultiplier));
                    Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);
                }
                if (boltAndXPMultiplier == "x10")
                {
                    currentMultiplier = 9;
                    Console.WriteLine(Convert.ToString(currentMultiplier));
                    Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);
                }
            }
        }
        public static void UpdatePlanets(long id)
        {
            Memory.WriteByte(AvailableSlots[0], 1);
            Memory.WriteByte(AvailableSlots[1], 2);
            Memory.WriteByte(AvailableSlots[2], 3);
            switch (id)
            {
                case 50001452:
                    {
                        Marcadia.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[3], Marcadia.Number);
                        break;
                    }
                case 50001453:
                    {
                        AnnihilationNation.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[4], AnnihilationNation.Number);
                        break;
                    }
                case 50001454:
                    {
                        Aquatos.Unlock = 1;
                        Memory.Write(AvailableSlots[5], Aquatos.Number);
                        break;
                    }
                case 50001455:
                    {
                        Tyhrranosis.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[6], Tyhrranosis.Number);
                        break;
                    }
                case 50001456:
                    {
                        Daxx.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[7], Daxx.Number);
                        break;
                    }
                case 50001457:
                    {
                        ObaniGemini.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[8], ObaniGemini.Number);
                        break;
                    }
                case 50001458:
                    {
                        Rilgar.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[9], Rilgar.Number); 
                        break;
                    }
                case 50001459:
                    {
                        HolostarStudios.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[10], HolostarStudios.Number);
                        break;
                    }
                case 50001460:
                    {
                        ObaniDraco.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[11], ObaniDraco.Number);
                        break;
                    }
                case 50001461:
                    {
                        ZeldrinStarport.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[12], ZeldrinStarport.Number);
                        break;
                    }
                case 50001462:
                    {
                        Metropolis.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[13], Metropolis.Number);
                        break;
                    }
                case 50001463:
                    {
                        Zeldrin.Unlock = 1;                                            
                        Memory.WriteByte(AvailableSlots[14], Zeldrin.Number);
                        break;
                    }
                case 50001464:
                    {
                        Aridia.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[15], Aridia.Number);
                        break;
                    }
                case 50001465:
                    {
                        QwarksHideout.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[16], QwarksHideout.Number);
                        break;
                    }
                case 50001466:
                    {
                        Koros.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[17], Koros.Number);
                        break;
                    }
                case 50001467:
                    {
                        Mylon.Unlock = 1;
                        Memory.WriteByte(AvailableSlots[18], Mylon.Number);
                        break;
                    }
            }

        }
        public static void UpdateWeapons(long id)
        {
            //Sets the unlock property in the weapon to 1
            //Then writes the value to the memory

            switch (id)
                {
                case 50001400:
                    ShockBlaster.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockShockBlaster, ShockBlaster.Unlock);
                    break;
                case 50001401:
                    NitroLauncher.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockNitroLauncher, NitroLauncher.Unlock);
                    break;
                case 50001402:
                    N60Storm.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockN60Storm, N60Storm.Unlock);
                    break;
                case 50001403:
                    PlasmaWhip.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockPlasmaWhip, PlasmaWhip.Unlock);
                    break;
                case 50001404:
                    Infector.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockInfector, Infector.Unlock);
                    break;
                case 50001405:
                    SuckCannon.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockSuckCannon, SuckCannon.Unlock);
                    break;
                case 50001406:
                    SpittingHydra.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockSpittingHydra, SpittingHydra.Unlock);
                    break;
                case 50001407:
                    AgentsOfDoom.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockAgentsOfDoom, AgentsOfDoom.Unlock);
                    break;
                case 50001408:
                    FluxRifle.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockFluxRifle, FluxRifle.Unlock);
                    break;
                case 50001409:
                    Annihilator.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockAnnihilator, Annihilator.Unlock);
                    break;
                case 50001410:
                    HoloShieldGlove.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockHoloShieldGlove, HoloShieldGlove.Unlock);
                    break;
                case 50001411:
                    DiskBladeGun.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockDiskBladeGun, DiskBladeGun.Unlock);
                    break;
                case 50001412:
                    RiftInducer.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockRiftInducer, RiftInducer.Unlock);
                    break;
                case 50001413:
                    QwackORay.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockQwackORay, QwackORay.Unlock);
                    break;
                case 50001414:
                    RY3N0.Unlock = 1;
                    Memory.Write(WeaponUnlocks.unlockRY3N0, RY3N0.Unlock);
                    break;
                case 50001415:
                    MegaTurretGlove.Unlock = 1;
                    Memory.WriteBit(WeaponUnlocks.unlockMegaTurretGlove, 5, Convert.ToBoolean(MegaTurretGlove.Unlock));
                    break;
                case 50001416:
                    LavaGun.Unlock = 1;
                    Memory.WriteBit(WeaponUnlocks.unlockLavaGun, 1, Convert.ToBoolean(LavaGun.Unlock));
                    break;
                case 50001417:
                    ShieldCharger.Unlock = 1;
                    Memory.WriteBit(WeaponUnlocks.unlockShieldCharger, 6, Convert.ToBoolean(LavaGun.Unlock));
                    break;
                case 50001418:
                    Bouncer.Unlock = 1;
                    Memory.WriteBit(WeaponUnlocks.unlockBouncer, 3, Convert.ToBoolean(Bouncer.Unlock));
                    break;
                case 50001419:
                    PlasmaCoil.Unlock = 1;
                    Memory.WriteBit(WeaponUnlocks.unlockPlasmaCoil, 0, Convert.ToBoolean(PlasmaCoil.Unlock));
                    break;
            }
        } 
        public static void UpdateUpgrades(long id)
        {
            //Increments the pointer value in the given weapon, then uses that value as an array pointer for version number + exp value
            //Then writes those values to the memory
            switch (id)
            {
                case 50001420:
                    ShockBlaster.Pointer++;
                    ShockBlaster.EXP = WeaponVersionData.ARRexpShockBlaster[ShockBlaster.Pointer];
                    ShockBlaster.Version = WeaponVersionData.ARRversionShockBlaster[ShockBlaster.Pointer];
                    Memory.Write(WeaponVersionData.ADDexpShockBlaster, ShockBlaster.EXP);
                    Memory.Write(WeaponVersionData.ADDversionShockBlaster, ShockBlaster.Version);
                    break;
                case 50001421:
                    NitroLauncher.Pointer++;
                    NitroLauncher.EXP = WeaponVersionData.ARRexpNitroLauncher[NitroLauncher.Pointer];
                    NitroLauncher.Version = WeaponVersionData.ARRversionNitroLauncher[NitroLauncher.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionNitroLauncher, NitroLauncher.Version);
                    Memory.Write(WeaponVersionData.ADDexpNitroLauncher, NitroLauncher.EXP);
                    break;
                case 50001422:
                    N60Storm.Pointer++;
                    N60Storm.EXP = WeaponVersionData.ARRexpN60Storm[N60Storm.Pointer];
                    N60Storm.Version = WeaponVersionData.ARRversionN60Storm[N60Storm.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionN60Storm, N60Storm.Version);
                    Memory.Write(WeaponVersionData.ADDexpN60Storm, N60Storm.EXP);
                    break;
                case 50001423:
                    PlasmaWhip.Pointer++;
                    PlasmaWhip.EXP = WeaponVersionData.ARRexpPlasmaWhip[PlasmaWhip.Pointer];
                    PlasmaWhip.Version = WeaponVersionData.ARRversionPlasmaWhip[PlasmaWhip.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionPlasmaWhip, PlasmaWhip.Version);
                    Memory.Write(WeaponVersionData.ADDexpPlasmaWhip, PlasmaWhip.EXP);
                    break;
                case 50001424:
                    Infector.Pointer++; 
                    Infector.EXP = WeaponVersionData.ARRexpInfector[Infector.Pointer];
                    Infector.Version = WeaponVersionData.ARRversionInfector[PlasmaWhip.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionPlasmaWhip, PlasmaWhip.Version);
                    Memory.Write(WeaponVersionData.ADDexpInfector, Infector.EXP);
                    break;
                case 50001425:
                    SuckCannon.Pointer++;
                    SuckCannon.EXP = WeaponVersionData.ARRexpSuckCannon[SuckCannon.Pointer];
                    SuckCannon.Version = WeaponVersionData.ARRversionSuccCannon[SuckCannon.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionSuccCannon, SuckCannon.Version);
                    Memory.Write(WeaponVersionData.ADDexpSuckCannon, SuckCannon.EXP);
                    break;
                case 50001426:
                    SpittingHydra.Pointer++;
                    SpittingHydra.EXP = WeaponVersionData.ARRexpSpittingHydra[SpittingHydra.Pointer];
                    SpittingHydra.Version = WeaponVersionData.ARRversionSpittingHydra[SpittingHydra.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionSpittingHydra, SpittingHydra.Version);
                    Memory.Write(WeaponVersionData.ADDexpSpittingHydra, SpittingHydra.EXP); 
                    break;
                case 50001427:
                    AgentsOfDoom.Pointer++;
                    AgentsOfDoom.EXP = WeaponVersionData.ARRexpAgentsOfDoom[AgentsOfDoom.Pointer];
                    AgentsOfDoom.Version = WeaponVersionData.ARRversionAgentsOfDoom[AgentsOfDoom.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionAgentsOfDoom, AgentsOfDoom.Version);
                    Memory.Write(WeaponVersionData.ADDexpAgentsOfDoom, AgentsOfDoom.EXP);
                    break;
                case 50001428:
                    FluxRifle.Pointer++;
                    FluxRifle.EXP = WeaponVersionData.ARRexpFluxRifle[FluxRifle.Pointer];
                    FluxRifle.Version = WeaponVersionData.ARRversionFluxRifle[FluxRifle.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionFluxRifle, FluxRifle.Version);
                    Memory.Write(WeaponVersionData.ADDexpFluxRifle, FluxRifle.EXP);
                    break;
                case 50001429:
                    Annihilator.Pointer++;
                    Annihilator.EXP = WeaponVersionData.ARRexpAnnihilator[Annihilator.Pointer];
                    Annihilator.Version = WeaponVersionData.ARRversionAnnihilator[Annihilator.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionAnnihilator, Annihilator.Version);
                    Memory.Write(WeaponVersionData.ADDexpAnnihilator, Annihilator.EXP);
                    break;
                case 50001430:
                    HoloShieldGlove.Pointer++;
                    HoloShieldGlove.EXP = WeaponVersionData.ARRexpHoloShieldGlove[HoloShieldGlove.Pointer];
                    HoloShieldGlove.Version = WeaponVersionData.ARRversionHoloShieldGlove[HoloShieldGlove.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionHoloShieldGlove, HoloShieldGlove.Version);
                    Memory.Write(WeaponVersionData.ADDexpHoloShieldGlove, HoloShieldGlove.EXP);
                    break;
                case 50001431:
                    DiskBladeGun.Pointer++;
                    DiskBladeGun.EXP = WeaponVersionData.ARRexpDiskBladeGun[DiskBladeGun.Pointer];
                    DiskBladeGun.Version = WeaponVersionData.ARRversionDiskBladeGun[DiskBladeGun.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionDiskBladeGun, DiskBladeGun.Version);
                    Memory.Write(WeaponVersionData.ADDexpDiskBladeGun, DiskBladeGun.EXP);
                    break;
                case 50001432:
                    RiftInducer.Pointer++;
                    RiftInducer.EXP = WeaponVersionData.ARRexpRiftInducer[RiftInducer.Pointer];
                    RiftInducer.Version = WeaponVersionData.ARRversionRiftInducer[RiftInducer.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionRiftInducer, RiftInducer.Version);
                    Memory.Write(WeaponVersionData.ADDexpRiftInducer, RiftInducer.EXP);
                    break;
                case 50001433:
                    QwackORay.Pointer++;
                    QwackORay.EXP = WeaponVersionData.ARRexpQwackORay[QwackORay.Pointer];
                    QwackORay.Version = WeaponVersionData.ARRversionQwackORay[QwackORay.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionQwackORay, QwackORay.Version);
                    Memory.Write(WeaponVersionData.ADDexpQwackORay, QwackORay.EXP);
                    break;
                case 50001434:
                    RY3N0.Pointer++;
                    RY3N0.EXP = WeaponVersionData.ARRexpRY3N0[RY3N0.Pointer];
                    RY3N0.Version = WeaponVersionData.ARRversionRY3N0[RY3N0.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionRY3N0, RY3N0.Version);
                    Memory.Write(WeaponVersionData.ADDexpRY3N0, RY3N0.EXP);
                    break;
                case 50001435:
                    MegaTurretGlove.Pointer++;
                    MegaTurretGlove.EXP = WeaponVersionData.ARRexpMegaTurretGlove[MegaTurretGlove.Pointer];
                    MegaTurretGlove.Version = WeaponVersionData.ARRversionMegaTurretGlove[MegaTurretGlove.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionMegaTurretGlove, MegaTurretGlove.Version);
                    Memory.Write(WeaponVersionData.ADDexpMegaTurretGlove, MegaTurretGlove.EXP);
                    break;
                case 50001436:
                    LavaGun.Pointer++;
                    LavaGun.EXP = WeaponVersionData.ARRexpLavaGun[LavaGun.Pointer];
                    LavaGun.Version = WeaponVersionData.ARRversionLavaGun[LavaGun.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionLavaGun, LavaGun.Version);
                    Memory.Write(WeaponVersionData.ADDexpLavaGun, LavaGun.EXP);
                    break;
                case 50001437:
                    ShieldCharger.Pointer++;
                    ShieldCharger.EXP = WeaponVersionData.ARRexpShieldCharger[ShieldCharger.Pointer];
                    ShieldCharger.Version = WeaponVersionData.ARRversionShieldCharger[ShieldCharger.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionShieldCharger, ShieldCharger.Version);
                    Memory.Write(WeaponVersionData.ADDexpShieldCharger, ShieldCharger.EXP);
                    break;
                case 50001438:
                    Bouncer.Pointer++;
                    Bouncer.EXP = WeaponVersionData.ARRexpBouncer[Bouncer.Pointer];
                    Bouncer.Version = WeaponVersionData.ARRversionBouncer[Bouncer.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionBouncer, Bouncer.Version);
                    Memory.Write(WeaponVersionData.ADDexpBouncer, Bouncer.EXP);
                    break;
                case 50001439:
                    PlasmaCoil.Pointer++;
                    PlasmaCoil.EXP = WeaponVersionData.ARRexpPlasmaCoil[PlasmaCoil.Pointer];
                    PlasmaCoil.Version = WeaponVersionData.ARRversionPlasmaCoil[PlasmaCoil.Pointer];
                    Memory.Write(WeaponVersionData.ADDversionPlasmaCoil, PlasmaCoil.Version);
                    Memory.Write(WeaponVersionData.ADDexpPlasmaCoil, PlasmaCoil.EXP);
                    break;

            }
        }
        public static void UpdateGadgets(long id)
        {
            switch (id)
            {
                case 50001440:
                    Memory.WriteBit(GadgetAddresses.hacker, 1, true);
                    break;
                case 50001441:
                    Memory.WriteBit(GadgetAddresses.hyperShot, 1, true);
                    break;
                case 50001442:
                    Memory.WriteBit(GadgetAddresses.refractor, 1, true);
                    break;
                case 50001443:
                    Memory.WriteBit(GadgetAddresses.tyhrraGuise, 1, true);
                    break;
                case 50001444:
                    Memory.WriteBit(GadgetAddresses.gravBoots, 1, true);
                    break;
                case 50001445:
                    Memory.WriteBit(GadgetAddresses.boltGrabberV2, 1, true);
                    break;
                case 50001446:
                    Memory.WriteBit(GadgetAddresses.mapOMatic, 1, true);
                    break;
                case 50001447:
                    Memory.WriteBit(GadgetAddresses.nanoPak, 1, true);
                    break;
                case 50001448:
                    Memory.WriteBit(GadgetAddresses.warpPad, 1, true);
                    break;
                case 50001449:
                    Memory.WriteBit(GadgetAddresses.pda, 1, true);
                    break;
                case 50001467:
                    {
                        Memory.WriteBit(GadgetAddresses.vidComic1, 1, true);
                        break;
                    }
                case 50001468:
                    {
                        Memory.WriteBit(GadgetAddresses.vidComic2, 1, true);
                        break;
                    }
                case 50001469:
                    {
                        Memory.WriteBit(GadgetAddresses.vidComic3, 1, true);
                        break;
                    }
                case 50001470:
                    {
                        Memory.WriteBit(GadgetAddresses.vidComic4, 1, true);
                        break;
                    }
                case 50001471:
                    {
                        Memory.WriteBit(GadgetAddresses.vidComic5, 1, true);
                        break;
                    }
            }
        }
        public static void UpdateArmor()
        {
            int i = Memory.ReadInt(Addresses.currentArmor) + 1;
            Memory.Write(Addresses.currentArmor, i);
        }
        public static void UpdateJunk(long id)
        {
            //Junk
            //Don't continuously update these or else they'll never go down!
            if (id == 10020020)
            {
                var Lives = Memory.ReadInt(Addresses.junkAddr1);
                Lives += 1;
                Memory.Write(Addresses.junkAddr1, Lives);
            }
            if (id == 10020019)
            {
                var Charms = Memory.ReadInt(Addresses.junkAddr2);
                if (Charms < 2)
                {
                    Charms += 1;
                    Memory.Write(Addresses.junkAddr2, Charms);
                }
                else
                {
                    var Lives = Memory.ReadInt(Addresses.junkAddr1);
                    Lives += 1;
                    Memory.Write(Addresses.junkAddr1, Lives);
                }
            }
            return;
        }
        public static void UpdateValues()
        {
            Memory.WriteByte(Addresses.armorEquipped, Addresses.currentArmor);

            // Fix Bolt mulipiler
            Memory.Write(Addresses.boltXPMultiplier, currentMultiplier);

            foreach (var weapon in allWeapons)
            {
                ulong k = Addresses.currentlyEquippedWeapon;
                byte m = Memory.ReadByte(Addresses.currentlyEquippedWeapon);
                if (weapon.Unlock == 0 && weapon.Unlock != Memory.ReadInt(weapon.unlockAddress))
                {
                    /* HACK: Wait for Location get is detected */
                    if (weapon.unlockWait > 0)
                        Memory.WriteBit(weapon.unlockAddress, 0, false);
                    weapon.unlockWait++;
                }
                else
                    weapon.unlockWait = 0;

                if (m >= 39 && m <= 43 && ShockBlaster.Unlock == 0 && Memory.ReadByte(k) == 39)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 119 && m <= 123 && NitroLauncher.Unlock == 0 && Memory.ReadByte(k) == 119)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 47 && m <= 51 && N60Storm.Unlock == 0 && Memory.ReadByte(k) == 47)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 127 && m <= 131 && PlasmaWhip.Unlock == 0 && Memory.ReadByte(k) == 127)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 55 && m <= 59 && Infector.Unlock == 0 && Memory.ReadByte(k) == 55)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 135 && m <= 139 && SuckCannon.Unlock == 0 && Memory.ReadByte(k) == 135)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 71 && m <= 72 && SpittingHydra.Unlock == 0 && Memory.ReadByte(k) == 71)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 87 && m <= 91 && AgentsOfDoom.Unlock == 0 && Memory.ReadByte(k) == 87)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 111 && m <= 115 && FluxRifle.Unlock == 0 && Memory.ReadByte(k) == 111)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 63 && m <= 67 && Annihilator.Unlock == 0 && Memory.ReadByte(k) == 63)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 103 && m <= 107 && HoloShieldGlove.Unlock == 0 && Memory.ReadByte(k) == 103)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 95 && m <= 99 && RiftInducer.Unlock == 0 && Memory.ReadByte(k) == 95)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 143 && m <= 147 && QwackORay.Unlock == 0 && Memory.ReadByte(k) == 143)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m >= 151 && m <= 155 && RY3N0.Unlock == 0 && Memory.ReadByte(k) == 151)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 21 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(k) == 21)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 17 && LavaGun.Unlock == 0 && Memory.ReadByte(k) == 17)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 22 && ShieldCharger.Unlock == 0 && Memory.ReadByte(k) == 22)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 19 && Bouncer.Unlock == 0 && Memory.ReadByte(k) == 19)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 16 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(k) == 16)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }

            }
            VerifyLastUsed();
            PlanetCycler();
            WeaponCycler();
            //EXPController();
        }
        public static void GetValues()
        {
            foreach (var weapon in allWeapons)
            {
                weapon.Unlock = 0;
                weapon.EXP = 0;
                weapon.Pointer = 0;
                if (CurrentGameState.CustomValues.ContainsKey(weapon.weaponName))
                {
                    Memory.Write(weapon.expAddressDumb, Convert.ToInt32(CurrentGameState.CustomValues[weapon.weaponName]));
                    Console.WriteLine("Testing to See if it gets here or not");

                }
                else
                {
                    CurrentGameState.CustomValues.Add(weapon.weaponName, 0);
                    Console.WriteLine("Only show this in the Else Statement");
                }
            }
        }
        public static void UpdateStart()
        {
            removeAllWeapons();
            removeAllGadgets();
            removeAllPlanets();
            GetValues();
        }

        
        
        //Below are all helper functions
        
        public static void EXPController()
        {
            foreach(var weapon in allWeapons)
            {
                int j = Memory.ReadInt(weapon.expAddress);                                              // int J gets initialized to whatever the current EXP value is for the weapon
                j = (j - weapon.EXP)*(currentMultiplier + 1) + Memory.ReadInt(weapon.expAddressDumb);   // It then gets the breakpoint value removed from it to give the raw amount gained, which then gets multiplied by the current multiplier then adds the current value of expAddressDumb
                Memory.Write(weapon.expAddressDumb, j);                                                 // J gets written to the dummy address for locations checks for whichever weapon it is
                CurrentGameState.CustomValues[weapon.weaponName] = j;                                   // J then gets added to the CustomValues within the GameState to save in between loads
                Console.WriteLine(Convert.ToInt32(CurrentGameState.CustomValues[weapon.weaponName]));
                Memory.Write(weapon.expAddress, weapon.EXP);                                            // Current EXP value then gets reset back to whatever weapon.EXP is set to
            }
        }
        public static void WeaponCycler()
        {
            foreach (var weapon in allWeapons)
            {
                if (weapon.Unlock == 0)
                {
                    VerifyQuickSelect(Memory.ReadByte(weapon.versionAddress));
                }
            }
        }
        public static void VerifyQuickSelect(int address)
        {
            // Cycles through the quick select menu, checking every slot for the weapon version value inside
            // If the value matches the weapon's version, and the weapon is currently not unlocked, it will remove that weapon
            foreach(var slot in QuickSelect)
            {
                if (address >= 39 && address <= 43 && ShockBlaster.Unlock == 0 && Memory.ReadByte(slot) == 39)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 119 && address <= 123 && NitroLauncher.Unlock == 0 && Memory.ReadByte(slot) == 119)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 47 && address <= 51 && N60Storm.Unlock == 0 && Memory.ReadByte(slot) == 47)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 127 && address <= 131 && PlasmaWhip.Unlock == 0 && Memory.ReadByte(slot) == 127)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 55 && address <= 59 && Infector.Unlock == 0 && Memory.ReadByte(slot) == 55)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 135 && address <= 139 && SuckCannon.Unlock == 0 && Memory.ReadByte(slot) == 135)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 71 && address <= 72 && SpittingHydra.Unlock == 0 && Memory.ReadByte(slot) == 71)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 87 && address <= 91 && AgentsOfDoom.Unlock == 0 && Memory.ReadByte(slot) == 87)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 111 && address <= 115 && FluxRifle.Unlock == 0 && Memory.ReadByte(slot) == 111)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 63 && address <= 67 && Annihilator.Unlock == 0 && Memory.ReadByte(slot) == 63)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 103 && address <= 107 && HoloShieldGlove.Unlock == 0 && Memory.ReadByte(slot) == 103)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 95 && address <= 99 && RiftInducer.Unlock == 0 && Memory.ReadByte(slot) == 95)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 143 && address <= 147 && QwackORay.Unlock == 0 && Memory.ReadByte(slot) == 143)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address >= 151 && address <= 155 && RY3N0.Unlock == 0 && Memory.ReadByte(slot) == 151)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 21 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(slot) == 21)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 17 && LavaGun.Unlock == 0 && Memory.ReadByte(slot) == 17)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 22 && ShieldCharger.Unlock == 0 && Memory.ReadByte(slot) == 22)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 19 && Bouncer.Unlock == 0 && Memory.ReadByte(slot) == 19)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 16 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(slot) == 16)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
            }
        }

        public static void PlanetCycler()
        {
            foreach (var planet in allPlanets)
            {
                if (planet.Unlock == 0)
                {
                    VerifyPlanetSlots(planet.Number);
                }
            }
        }
        public static void VerifyPlanetSlots(int number)
        {
            foreach(var slot in AvailableSlots)
            {
                if(number == 4 && Marcadia.Unlock == 0 && Memory.ReadByte(slot) == 4)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if(number == 5 && Daxx.Unlock == 0 && Memory.ReadByte(slot) == 5)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if(number == 7 && AnnihilationNation.Unlock == 0 && Memory.ReadByte(slot) == 7)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if(number == 8 && Aquatos.Unlock == 0 && Memory.ReadByte(slot) == 8)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 9 && Tyhrranosis.Unlock == 0 && Memory.ReadByte(slot) == 9)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 10 && ZeldrinStarport.Unlock == 0 && Memory.ReadByte(slot) == 10)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 11 && ObaniGemini.Unlock == 0 && Memory.ReadByte(slot) == 11)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 12 && Rilgar.Unlock == 0 && Memory.ReadByte(slot) == 12)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 13 && HolostarStudios.Unlock == 0 && Memory.ReadByte(slot) == 13)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 14 && Koros.Unlock == 0 && Memory.ReadByte(slot) == 14)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 16 && Metropolis.Unlock == 0 && Memory.ReadByte(slot) == 16)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 17 && Zeldrin.Unlock == 0 && Memory.ReadByte(slot) == 17)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 18 && Aridia.Unlock == 0 && Memory.ReadByte(slot) == 18)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 19 && QwarksHideout.Unlock == 0 && Memory.ReadByte(slot) == 19)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 20 && ObaniDraco.Unlock == 0 && Memory.ReadByte(slot) == 20)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (number == 21 && Mylon.Unlock == 0 && Memory.ReadByte(slot) == 21)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
            }
        }
        public static void VerifyLastUsed()
        {
            byte m = Memory.ReadByte(lastUsed[1]);
            foreach (ulong slot in lastUsed)
            {
                if (m >= 39 && m <= 43 && ShockBlaster.Unlock == 0 && Memory.ReadByte(slot) == 39)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 119 && m <= 123 && NitroLauncher.Unlock == 0 && Memory.ReadByte(slot) == 119)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 47 && m <= 51 && N60Storm.Unlock == 0 && Memory.ReadByte(slot) == 47)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 127 && m <= 131 && PlasmaWhip.Unlock == 0 && Memory.ReadByte(slot) == 127)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 55 && m <= 59 && Infector.Unlock == 0 && Memory.ReadByte(slot) == 55)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 135 && m <= 139 && SuckCannon.Unlock == 0 && Memory.ReadByte(slot) == 135)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 71 && m <= 72 && SpittingHydra.Unlock == 0 && Memory.ReadByte(slot) == 71)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 87 && m <= 91 && AgentsOfDoom.Unlock == 0 && Memory.ReadByte(slot) == 87)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 111 && m <= 115 && FluxRifle.Unlock == 0 && Memory.ReadByte(slot) == 111)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 63 && m <= 67 && Annihilator.Unlock == 0 && Memory.ReadByte(slot) == 63)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 103 && m <= 107 && HoloShieldGlove.Unlock == 0 && Memory.ReadByte(slot) == 103)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 95 && m <= 99 && RiftInducer.Unlock == 0 && Memory.ReadByte(slot) == 95)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 143 && m <= 147 && QwackORay.Unlock == 0 && Memory.ReadByte(slot) == 143)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m >= 151 && m <= 155 && RY3N0.Unlock == 0 && Memory.ReadByte(slot) == 151)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 21 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(slot) == 21)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 17 && LavaGun.Unlock == 0 && Memory.ReadByte(slot) == 17)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 22 && ShieldCharger.Unlock == 0 && Memory.ReadByte(slot) == 22)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 19 && Bouncer.Unlock == 0 && Memory.ReadByte(slot) == 19)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 16 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(slot) == 16)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
            }
        }
        public static int ShipSlots()
        {
            foreach(var slot in AvailableSlots)
            {
                int i = 3;
                if(Memory.ReadByte(slot) == 0)
                {
                    return i;
                }
                i++;
            }
            // This should never happen, but if it does please fix later
            return 0;
        }


        public static void unlockAllWeapons()
        {
            // Sets all weapon unlock addresses to 1
            foreach (var field in typeof(WeaponUnlocks).GetFields(BindingFlags.Public | BindingFlags.Static | BindingFlags.FlattenHierarchy))
            {
                if (field.IsLiteral && !field.IsInitOnly) // const fields only
                {
                    int value = (int)field.GetRawConstantValue();
                    Memory.Write((ulong)value, 1);
                }
            }
        }
        public static void removeAllWeapons()
        {
            // Sets all weapon unlock addresses to 0
            foreach (var field in typeof(WeaponUnlocks).GetFields(BindingFlags.Public | BindingFlags.Static | BindingFlags.FlattenHierarchy))
            {
                if (field.IsLiteral && !field.IsInitOnly) // const fields only
                {
                    int value = (int)field.GetRawConstantValue();
                    Memory.Write((ulong)value, 0);
                }
            }
        }
        public static void unlockAllGadgets()
        {

            // Sets all gadget unlock addresses to 1
            foreach (var field in typeof(GadgetAddresses).GetFields(BindingFlags.Public | BindingFlags.Static | BindingFlags.FlattenHierarchy))
            {
                if (field.IsLiteral && !field.IsInitOnly) // const fields only
                {
                    int value = (int)field.GetRawConstantValue();
                    Memory.Write((ulong)value, 1);
                }
            }
        }
        public static void removeAllGadgets()
        {

            // Sets all gadget unlock addresses to 0
            foreach (var field in typeof(GadgetAddresses).GetFields(BindingFlags.Public | BindingFlags.Static | BindingFlags.FlattenHierarchy))
            {
                if (field.IsLiteral && !field.IsInitOnly) // const fields only
                {
                    int value = (int)field.GetRawConstantValue();
                    Memory.Write((ulong)value, 0);
                }
            }
        }
        public static void removeAllPlanets()
        {
            foreach (var address in AvailableSlots)
            {
                Memory.WriteByte(address, 0);
            }
        }
    }


    //Pattern series of hex addresses that always remain static throughout the games lifecycle
    //Mask is an array of shit you're looking for, x is for what you want, ? is for what you don't want
    //FindSignature() gets BaseAddress(), the Length of the Search, Pattern and Mask as parameters
    //Length of search determined by MODULEINFO.SizeOfImage (not exposed yet), Function is called GetModuleInfo() and takes moduleName as parameter which is the name of the executable without .exe on the end



}

