// See https://aka.ms/new-console-template for more information
using System.Net;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using Archipelago.Core;
using Archipelago.Core.Models;
using Archipelago.Core.Util;
using Archipelago.MultiClient.Net.Packets;
using Archipelago.PCSX2;
using Newtonsoft.Json;
using RaC3AP.Models;
using static System.Reflection.Metadata.BlobBuilder;

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
        public static ulong[] lastUsed = [0x20142670, 0x20142674, 0x20142678];
        public static int currentMultiplier = 2;
        public static Weapon ShockBlaster = new Weapon("Shock Blaster", WeaponVersionData.ADDexpShockBlaster, WeaponVersionData.ADDversionShockBlaster, Addresses.unlockShockBlaster, DummyEXPAddresses.ShockBlaster);
        public static Weapon NitroLauncher = new Weapon("Nitro Launcher", WeaponVersionData.ADDexpNitroLauncher, WeaponVersionData.ADDversionNitroLauncher, Addresses.unlockNitroLauncher, DummyEXPAddresses.NitroLauncher);
        public static Weapon N60Storm = new Weapon("N60 Storm", WeaponVersionData.ADDexpN60Storm, WeaponVersionData.ADDversionN60Storm, Addresses.unlockN60Storm, DummyEXPAddresses.N60Storm);
        public static Weapon PlasmaWhip = new Weapon("Plasma Whip", WeaponVersionData.ADDexpPlasmaWhip, WeaponVersionData.ADDversionPlasmaWhip, Addresses.unlockPlasmaWhip, DummyEXPAddresses.PlasmaWhip);
        public static Weapon Infector = new Weapon("Infector", WeaponVersionData.ADDexpInfector, WeaponVersionData.ADDversionInfector, Addresses.unlockInfector, DummyEXPAddresses.Infector);
        public static Weapon SuckCannon = new Weapon("Suck Cannon", WeaponVersionData.ADDexpSuckCannon, WeaponVersionData.ADDversionSuccCannon, Addresses.unlockSuckCannon, DummyEXPAddresses.SuckCannon);
        public static Weapon SpittingHydra = new Weapon("Spitting Hydra", WeaponVersionData.ADDexpSpittingHydra, WeaponVersionData.ADDversionSpittingHydra, Addresses.unlockSpittingHydra, DummyEXPAddresses.SpittingHydra);
        public static Weapon AgentsOfDoom = new Weapon("Agents Of Doom", WeaponVersionData.ADDexpAgentsOfDoom,WeaponVersionData.ADDversionAgentsOfDoom, Addresses.unlockAgentsOfDoom, DummyEXPAddresses.AgentsOfDoom);
        public static Weapon FluxRifle = new Weapon("Flux Rifle", WeaponVersionData.ADDexpFluxRifle, WeaponVersionData.ADDversionFluxRifle, Addresses.unlockFluxRifle, DummyEXPAddresses.FluxRifle);
        public static Weapon Annihilator = new Weapon("Annihilator", WeaponVersionData.ADDexpAnnihilator,WeaponVersionData.ADDversionAnnihilator, Addresses.unlockAnnihilator, DummyEXPAddresses.Annihilator);
        public static Weapon HoloShieldGlove = new Weapon("Holo Shield Glove", WeaponVersionData.ADDexpHoloShieldGlove, WeaponVersionData.ADDversionHoloShieldGlove, Addresses.unlockHoloShieldGlove, DummyEXPAddresses.HoloShieldGlove);
        public static Weapon DiskBladeGun = new Weapon("Disk Blade Gun", WeaponVersionData.ADDexpDiskBladeGun, WeaponVersionData.ADDversionDiskBladeGun, Addresses.unlockDiskBladeGun, DummyEXPAddresses.DiskBladeGun);
        public static Weapon RiftInducer = new Weapon("Rift Inducer", WeaponVersionData.ADDexpRiftInducer, WeaponVersionData.ADDversionRiftInducer, Addresses.unlockRiftInducer, DummyEXPAddresses.RiftInducer);
        public static Weapon QwackORay = new Weapon("Qwack-O-Ray", WeaponVersionData.ADDexpQwackORay, WeaponVersionData.ADDversionQwackORay, Addresses.unlockQwackORay, DummyEXPAddresses.QwackORay);
        public static Weapon RY3N0 = new Weapon("RY3N0", WeaponVersionData.ADDexpRY3N0, WeaponVersionData.ADDversionRY3N0, Addresses.unlockRY3N0, DummyEXPAddresses.RY3N0);
        public static Weapon MegaTurretGlove = new Weapon("Mega Turret Glove", WeaponVersionData.ADDexpMegaTurretGlove, WeaponVersionData.ADDversionMegaTurretGlove, Addresses.unlockMegaTurretGlove, DummyEXPAddresses.MegaTurretGlove);
        public static Weapon LavaGun = new Weapon("Lava Gun", WeaponVersionData.ADDexpLavaGun, WeaponVersionData.ADDversionLavaGun, Addresses.unlockLavaGun, DummyEXPAddresses.LavaGun);
        public static Weapon ShieldCharger = new Weapon("Shield Charger", WeaponVersionData.ADDexpShieldCharger,WeaponVersionData.ADDversionShieldCharger, Addresses.unlockShieldCharger, DummyEXPAddresses.ShieldCharger);
        public static Weapon Bouncer = new Weapon("Bouncer", WeaponVersionData.ADDexpBouncer, WeaponVersionData.ADDversionBouncer, Addresses.unlockBouncer, DummyEXPAddresses.Bouncer);
        public static Weapon PlasmaCoil = new Weapon("Plasma Coil", WeaponVersionData.ADDexpPlasmaCoil, WeaponVersionData.ADDversionPlasmaCoil, Addresses.unlockPlasmaCoil, DummyEXPAddresses.PlasmaCoil);
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
            Console.Write("Enter Address: ");
            string Address = Console.ReadLine();
            Console.Write("Enter Slot Name: ");
            string SlotName = Console.ReadLine();
            Console.Write("Enter Password: ");
            string Password = Console.ReadLine();
            IsConnected = await ConnectAsync(Address, SlotName, Password);
        }

        static async Task<bool> ConnectAsync(string address, string playerName, string password)
        {
            PCSX2Client client = new PCSX2Client();
            var pcsx2Connected = client.Connect();
            if (!pcsx2Connected)
            {
                Console.WriteLine("Failed to connect to PCSX2.");
                return false;
            }
            Console.WriteLine($"Connected to PCSX2.");

            //Set the game completion flag to 0, so boss locations won't be sent unintentionally.
            Memory.Write(0x2027DC18, 0);

            Console.WriteLine($"Connecting to Archipelago.");
            ArchipelagoClient Client = new(client);
            await Client.Connect(address, "Ratchet and Clank 3 Up your Arsenal");
            var locations = Helpers.GetLocations();
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

                if (StartingWeapon == "Shock Blaster" & Memory.ReadInt(Addresses.unlockShockBlaster) == 0)
                {
                    ShockBlaster.Unlock = 1;
                    Memory.Write(Addresses.unlockShockBlaster, ShockBlaster.Unlock);
                    Memory.Write(Addresses.ammoShockBlaster, 30);
                }
                if (StartingWeapon == "Nitro Launcher" & Memory.ReadInt(Addresses.unlockNitroLauncher) == 0)
                {
                    NitroLauncher.Unlock = 1;
                    Memory.Write(Addresses.unlockNitroLauncher, NitroLauncher.Unlock);
                    Memory.Write(Addresses.ammoNitroLauncher, 8);
                }
                if (StartingWeapon == "N60 Storm" & Memory.ReadInt(Addresses.unlockN60Storm) == 0)
                {
                    N60Storm.Unlock = 1;
                    Memory.Write(Addresses.unlockN60Storm, N60Storm.Unlock);
                    Memory.Write(Addresses.ammoN60Storm, 150);
                }
                if (StartingWeapon == "Plasma Whip" & Memory.ReadInt(Addresses.unlockPlasmaWhip) == 0)
                {
                    PlasmaWhip.Unlock = 1;
                    Memory.Write(Addresses.unlockPlasmaWhip, PlasmaWhip.Unlock);
                    Memory.Write(Addresses.ammoPlasmaWhip, 25);

                }
                if (StartingWeapon == "Infector" & Memory.ReadInt(Addresses.unlockInfector) == 0)
                {
                    Infector.Unlock = 1;
                    Memory.Write(Addresses.unlockInfector, Infector.Unlock);
                    Memory.Write(Addresses.ammoInfector, 15);

                }
                if (StartingWeapon == "Suck Cannon" & Memory.ReadInt(Addresses.unlockSuckCannon) == 0)
                {
                    SuckCannon.Unlock = 1;
                    Memory.Write(Addresses.unlockSuckCannon, SuckCannon.Unlock);

                }
                if (StartingWeapon == "Spitting Hydra" & Memory.ReadInt(Addresses.unlockSpittingHydra) == 0)
                {
                    SpittingHydra.Unlock = 1;
                    Memory.Write(Addresses.unlockSpittingHydra, SpittingHydra.Unlock);
                    Memory.Write(Addresses.ammoSpittingHydra, 15);

                }
                if (StartingWeapon == "Agents Of Doom" & Memory.ReadInt(Addresses.unlockAgentsOfDoom) == 0)
                {
                    AgentsOfDoom.Unlock = 1;
                    Memory.Write(Addresses.unlockAgentsOfDoom, AgentsOfDoom.Unlock);
                    Memory.Write(Addresses.ammoAgentsOfDoom, 6);

                }
                if (StartingWeapon == "Flux Rifle" & Memory.ReadInt(Addresses.unlockFluxRifle) == 0)
                {
                    FluxRifle.Unlock = 1;
                    Memory.Write(Addresses.unlockFluxRifle, FluxRifle.Unlock);
                    Memory.Write(Addresses.ammoFluxRifle, 10);

                }
                if (StartingWeapon == "Annihilator" & Memory.ReadInt(Addresses.unlockAnnihilator) == 0)
                {
                    Annihilator.Unlock = 1;
                    Memory.Write(Addresses.unlockAnnihilator, Annihilator.Unlock);
                    Memory.Write(Addresses.ammoAnnihilator, 20);

                }
                if (StartingWeapon == "Holo Shield Glove" & Memory.ReadInt(Addresses.unlockHoloShieldGlove) == 0)
                {
                    HoloShieldGlove.Unlock = 1;
                    Memory.Write(Addresses.unlockHoloShieldGlove, HoloShieldGlove.Unlock);
                    Memory.Write(Addresses.ammoHoloShieldGlove, 8);

                }
                if (StartingWeapon == "Disk Blade Gun" & Memory.ReadInt(Addresses.unlockDiskBladeGun) == 0)
                {
                    DiskBladeGun.Unlock = 1;
                    Memory.Write(Addresses.unlockDiskBladeGun, DiskBladeGun.Unlock);
                    Memory.Write(Addresses.ammoDiskBladeGun, 25);

                }
                if (StartingWeapon == "Rift Inducer" & Memory.ReadInt(Addresses.unlockRiftInducer) == 0)
                {
                    RiftInducer.Unlock = 1;
                    Memory.Write(Addresses.unlockRiftInducer, RiftInducer.Unlock);
                    Memory.Write(Addresses.ammoRiftInducer, 8);

                }
                if (StartingWeapon == "Qwack O Ray" & Memory.ReadInt(Addresses.unlockQwackORay) == 0)
                {
                    QwackORay.Unlock = 1;
                    Memory.Write(Addresses.unlockQwackORay, QwackORay.Unlock);

                }
                if (StartingWeapon == "RY3N0" & Memory.ReadInt(Addresses.unlockRY3N0) == 0)
                {
                    RY3N0.Unlock = 1;
                    Memory.Write(Addresses.unlockRY3N0, RY3N0.Unlock);
                    Memory.Write(Addresses.ammoRY3N0, 25);

                }
                if (StartingWeapon == "Mega Turret Glove" & Memory.ReadInt(Addresses.unlockMegaTurretGlove) == 0)
                {
                    MegaTurretGlove.Unlock = 1;
                    Memory.Write(Addresses.unlockMegaTurretGlove, MegaTurretGlove.Unlock);
                    Memory.Write(Addresses.ammoMegaTurretGlove, 10);

                }
                if (StartingWeapon == "Lava Gun" & Memory.ReadInt(Addresses.unlockLavaGun) == 0)
                {
                    LavaGun.Unlock = 1;
                    Memory.Write(Addresses.unlockLavaGun, LavaGun.Unlock);
                    Memory.Write(Addresses.ammoLavaGun, 150);

                }
                if (StartingWeapon == "Shield Charger" & Memory.ReadInt(Addresses.unlockShieldCharger) == 0)
                {
                    ShieldCharger.Unlock = 1;
                    Memory.Write(Addresses.unlockShieldCharger, ShieldCharger.Unlock);
                    Memory.Write(Addresses.ammoShieldCharger, 3);

                }
                if (StartingWeapon == "Bouncer" & Memory.ReadInt(Addresses.unlockBouncer) == 0)
                {
                    Bouncer.Unlock = 1;
                    Memory.Write(Addresses.unlockBouncer, Bouncer.Unlock);
                    Memory.Write(Addresses.ammoBouncer, 10);

                }
                if (StartingWeapon == "Plasma Coil" & Memory.ReadInt(Addresses.unlockPlasmaCoil) == 0)
                {
                    PlasmaCoil.Unlock = 1;
                    Memory.Write(Addresses.unlockPlasmaCoil, PlasmaCoil.Unlock);
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
                        Memory.WriteByte(0x2014305C, Marcadia.Number);
                        break;
                    }
                case 50001453:
                    {
                        AnnihilationNation.Unlock = 1;
                        Memory.WriteByte(0x20143060, AnnihilationNation.Number);
                        break;
                    }
                case 50001454:
                    {
                        Aquatos.Unlock = 1;
                        Memory.Write(0x20143064, Aquatos.Number);
                        break;
                    }
                case 50001455:
                    {
                        Tyhrranosis.Unlock = 1;
                        Memory.WriteByte(0x20143068, Tyhrranosis.Number);
                        break;
                    }
                case 50001456:
                    {
                        Daxx.Unlock = 1;
                        Memory.WriteByte(0x2014306C, Daxx.Number);
                        break;
                    }
                case 50001457:
                    {
                        ObaniGemini.Unlock = 1;
                        Memory.WriteByte(0x20143070, ObaniGemini.Number);
                        break;
                    }
                case 50001458:
                    {
                        Rilgar.Unlock = 1;
                        Memory.WriteByte(0x20143074, Rilgar.Number); 
                        break;
                    }
                case 50001459:
                    {
                        HolostarStudios.Unlock = 1;
                        Memory.WriteByte(0x20143078, HolostarStudios.Number);
                        break;
                    }
                case 50001460:
                    {
                        ObaniDraco.Unlock = 1;
                        Memory.WriteByte(0x2014307C, ObaniDraco.Number);
                        break;
                    }
                case 50001461:
                    {
                        ZeldrinStarport.Unlock = 1;
                        Memory.WriteByte(0x20143080, ZeldrinStarport.Number);
                        break;
                    }
                case 50001462:
                    {
                        Metropolis.Unlock = 1;
                        Memory.WriteByte(0x20143084, Metropolis.Number);
                        break;
                    }
                case 50001463:
                    {
                        Zeldrin.Unlock = 1;                                            
                        Memory.WriteByte(0x20143088, Zeldrin.Number);
                        break;
                    }
                case 50001464:
                    {
                        Aridia.Unlock = 1;
                        Memory.WriteByte(0x2014308C, Aridia.Number);
                        break;
                    }
                case 50001465:
                    {
                        QwarksHideout.Unlock = 1;
                        Memory.WriteByte(0x20143090, QwarksHideout.Number);
                        break;
                    }
                case 50001466:
                    {
                        Koros.Unlock = 1;
                        Memory.WriteByte(0x20143094, Koros.Number);
                        break;
                    }
                case 50001467:
                    {
                        Mylon.Unlock = 1;
                        Memory.WriteByte(0x20143098, Mylon.Number);
                        break;
                    }
            }

        }
        public static void UpdateWeapons(long id)
        {

            //Sets the unlock property in the weapon to 1
            //Then writes the value to the memory

            switch(id)
                {
                case 50001400:
                    ShockBlaster.Unlock = 1;
                    Memory.Write(Addresses.unlockShockBlaster, ShockBlaster.Unlock);
                    break;
                case 50001401:
                    NitroLauncher.Unlock = 1;
                    Memory.Write(Addresses.unlockNitroLauncher, NitroLauncher.Unlock);
                    break;
                case 50001402:
                    N60Storm.Unlock = 1;
                    Memory.Write(Addresses.unlockN60Storm, N60Storm.Unlock);
                    break;
                case 50001403:
                    PlasmaWhip.Unlock = 1;
                    Memory.Write(Addresses.unlockPlasmaWhip, PlasmaWhip.Unlock);
                    break;
                case 50001404:
                    Infector.Unlock = 1;
                    Memory.Write(Addresses.unlockInfector, Infector.Unlock);
                    break;
                case 50001405:
                    SuckCannon.Unlock = 1;
                    Memory.Write(Addresses.unlockSuckCannon, SuckCannon.Unlock);
                    break;
                case 50001406:
                    SpittingHydra.Unlock = 1;
                    Memory.Write(Addresses.unlockSpittingHydra, SpittingHydra.Unlock);
                    break;
                case 50001407:
                    AgentsOfDoom.Unlock = 1;
                    Memory.Write(Addresses.unlockAgentsOfDoom, AgentsOfDoom.Unlock);
                    break;
                case 50001408:
                    FluxRifle.Unlock = 1;
                    Memory.Write(Addresses.unlockFluxRifle, FluxRifle.Unlock);
                    break;
                case 50001409:
                    Annihilator.Unlock = 1;
                    Memory.Write(Addresses.unlockAnnihilator, Annihilator.Unlock);
                    break;
                case 50001410:
                    HoloShieldGlove.Unlock = 1;
                    Memory.Write(Addresses.unlockHoloShieldGlove, HoloShieldGlove.Unlock);
                    break;
                case 50001411:
                    DiskBladeGun.Unlock = 1;
                    Memory.Write(Addresses.unlockDiskBladeGun, DiskBladeGun.Unlock);
                    break;
                case 50001412:
                    RiftInducer.Unlock = 1;
                    Memory.Write(Addresses.unlockRiftInducer, RiftInducer.Unlock);
                    break;
                case 50001413:
                    QwackORay.Unlock = 1;
                    Memory.Write(Addresses.unlockQwackORay, QwackORay.Unlock);
                    break;
                case 50001414:
                    RY3N0.Unlock = 1;
                    Memory.Write(Addresses.unlockRY3N0, RY3N0.Unlock);
                    break;
                case 50001415:
                    MegaTurretGlove.Unlock = 1;
                    Memory.WriteBit(Addresses.unlockMegaTurretGlove, 5, Convert.ToBoolean(MegaTurretGlove.Unlock));
                    break;
                case 50001416:
                    LavaGun.Unlock = 1;
                    Memory.WriteBit(Addresses.unlockLavaGun, 1, Convert.ToBoolean(LavaGun.Unlock));
                    break;
                case 50001417:
                    ShieldCharger.Unlock = 1;
                    Memory.WriteBit(Addresses.unlockShieldCharger, 6, Convert.ToBoolean(LavaGun.Unlock));
                    break;
                case 50001418:
                    Bouncer.Unlock = 1;
                    Memory.WriteBit(Addresses.unlockBouncer, 3, Convert.ToBoolean(Bouncer.Unlock));
                    break;
                case 50001419:
                    PlasmaCoil.Unlock = 1;
                    Memory.WriteBit(Addresses.unlockPlasmaCoil, 0, Convert.ToBoolean(PlasmaCoil.Unlock));
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
                var Lives = Memory.ReadInt(0x2027DC00);
                Lives += 1;
                Memory.Write(0x2027DC00, Lives);
            }
            if (id == 10020019)
            {
                var Charms = Memory.ReadInt(0x2027DC04);
                if (Charms < 2)
                {
                    Charms += 1;
                    Memory.Write(0x2027DC04, Charms);
                }
                else
                {
                    var Lives = Memory.ReadInt(0x2027DC00);
                    Lives += 1;
                    Memory.Write(0x2027DC00, Lives);
                }
            }
            return;
        }
        public static void UpdateValues()
        {
            Memory.WriteByte(Addresses.armorEquipped, Addresses.currentArmor);
            foreach (var weapon in allWeapons)
            {
                ulong k = Addresses.currentlyEquippedWeapon;
                byte m = Memory.ReadByte(Addresses.currentlyEquippedWeapon);
                if (weapon.Unlock == 0 && weapon.Unlock != Memory.ReadInt(weapon.unlockAddress))
                {
                    Memory.WriteBit(weapon.unlockAddress, 0, false);
                }
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
                if (m == 21 || m == 162 || m == 168 || m == 169 || m == 170 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(k) == 21)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 17 || m == 161 || m == 174 || m == 175 || m == 176 && LavaGun.Unlock == 0 && Memory.ReadByte(k) == 17)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 22 || m == 167 || m == 192 || m == 193 || m == 194 && ShieldCharger.Unlock == 0 && Memory.ReadByte(k) == 22)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 19 || m == 166 || m == 180 || m == 181 || m == 182 && Bouncer.Unlock == 0 && Memory.ReadByte(k) == 19)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }
                if (m == 16 || m == 160 || m == 186 || m == 187 || m == 188 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(k) == 16)
                {
                    Memory.WriteByte(k, 9);
                    break;
                }

            }
            VerifyLastUsed();
            PlanetCycler();
            WeaponCycler();
            EXPController();
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
                if (address == 21 || address == 162 || address == 168 || address == 169 || address == 170 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(slot) == 21)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 17 || address == 161 || address == 174 || address == 175 || address == 176 && LavaGun.Unlock == 0 && Memory.ReadByte(slot) == 17)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 22 || address == 167 || address == 192 || address == 193 || address == 194 && ShieldCharger.Unlock == 0 && Memory.ReadByte(slot) == 22)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 19 || address == 166 || address == 180 || address == 181 || address == 182 && Bouncer.Unlock == 0 && Memory.ReadByte(slot) == 19)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (address == 16 || address == 160 || address == 186 || address == 187 || address == 188 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(slot) == 16)
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
            byte m = Memory.ReadByte(0x20142674);
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
                if (m == 21 || m == 162 || m == 168 || m == 169 || m == 170 && MegaTurretGlove.Unlock == 0 && Memory.ReadByte(slot) == 21)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 17 || m == 161 || m == 174 || m == 175 || m == 176 && LavaGun.Unlock == 0 && Memory.ReadByte(slot) == 17)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 22 || m == 167 || m == 192 || m == 193 || m == 194 && ShieldCharger.Unlock == 0 && Memory.ReadByte(slot) == 22)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 19 || m == 166 || m == 180 || m == 181 || m == 182 && Bouncer.Unlock == 0 && Memory.ReadByte(slot) == 19)
                {
                    Memory.WriteByte(slot, 0);
                    break;
                }
                if (m == 16 || m == 160 || m == 186 || m == 187 || m == 188 && PlasmaCoil.Unlock == 0 && Memory.ReadByte(slot) == 16)
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
            Memory.Write(0x20142CC7, 1);
            Memory.Write(0x20142D17, 1);
            Memory.Write(0x20142CCF, 1);
            Memory.Write(0x20142D1F, 1);
            Memory.Write(0x20142CD7, 1);
            Memory.Write(0x20142D27, 1);
            Memory.Write(0x20142CE7, 1);
            Memory.Write(0x20142CF7, 1);
            Memory.Write(0x20142D0F, 1);
            Memory.Write(0x20142CDF, 1);
            Memory.Write(0x20142D07, 1);
            Memory.Write(0x20142CEF, 1);
            Memory.Write(0x20142CFF, 1);
            Memory.Write(0x20142D2F, 1);
            Memory.Write(0x20142D37, 1);
            Memory.WriteBit(0x20142CB5, 5, true);
            Memory.WriteBit(0x20142CB1, 1, true);
            Memory.WriteBit(0x20142CB6, 6, true);
            Memory.WriteBit(0x20142CB3, 3, true);
            Memory.WriteBit(0x20142CB0, 0, true);

        }
        public static void removeAllWeapons()
        {

            // Sets all weapon unlock addresses to 1

            Memory.Write(0x20142CC7, 0);
            Memory.Write(0x20142D17, 0);
            Memory.Write(0x20142CCF, 0);
            Memory.Write(0x20142D1F, 0);
            Memory.Write(0x20142CD7, 0);
            Memory.Write(0x20142D27, 0);
            Memory.Write(0x20142CE7, 0);
            Memory.Write(0x20142CF7, 0);
            Memory.Write(0x20142D0F, 0);
            Memory.Write(0x20142CDF, 0);
            Memory.Write(0x20142D07, 0);
            Memory.Write(0x20142CEF, 0);
            Memory.Write(0x20142CFF, 0);
            Memory.Write(0x20142D2F, 0);
            Memory.Write(0x20142D37, 0);
            Memory.WriteBit(0x20142CB5, 5, false);
            Memory.WriteBit(0x20142CB1, 1, false);
            Memory.WriteBit(0x20142CB6, 6, false);
            Memory.WriteBit(0x20142CB3, 3, false);
            Memory.WriteBit(0x20142CB0, 0, false);
        }
        public static void unlockAllGadgets()
        {

            // Sets all gadget unlock addresses to 0

            Memory.Write(0x20142CAB, 1); //Hypershot
            Memory.Write(0x20142CB2, 1); //Refractor
            Memory.Write(0x20142CBE, 1); //Tyhrra-Guise
            Memory.Write(0x20142CBF, 1); //WarpPad
            Memory.Write(0x20142CC3, 1); //PDA
            Memory.Write(0x20142CBD, 1); //Charge Boots
            Memory.Write(0x20142CAD, 1); //Grav-Boots
            Memory.Write(0x20142CB4, 1); //Hacker
            Memory.Write(0x20142CA7, 1); //Bolt Grabber V2
            Memory.Write(0x20142CA5, 1); //Map O Matic
            Memory.Write(0x20142CC0, 1); //NanoPak
            Memory.WriteBit(0x201D554F, 8, true); //Vidcomic 1
            Memory.WriteBit(0x201D5551, 1, true); //Vidcomic 2
            Memory.WriteBit(0x201D5552, 2, true); //Vidcomic 3
            Memory.WriteBit(0x201D5550, 0, true); //Vidcomic 4
            Memory.WriteBit(0x201D5553, 3, true); //Vidcomic 5

        }
        public static void removeAllGadgets()
        {

            // Sets all gadget unlock addresses to 0

            Memory.Write(0x20142CAB, 0); //Hypershot
            Memory.Write(0x20142CB2, 0); //Refractor
            Memory.Write(0x20142CBE, 0); //Tyhrra-Guise
            Memory.Write(0x20142CBF, 0); //WarpPad
            Memory.Write(0x20142CC3, 0); //PDA
            Memory.Write(0x20142CBD, 0); //Charge Boots
            Memory.Write(0x20142CAD, 0); //Grav-Boots
            Memory.Write(0x20142CB4, 0); //Hacker
            Memory.Write(0x20142CA7, 0); //Bolt Grabber V2
            Memory.Write(0x20142CA5, 0); //Map O Matic
            Memory.Write(0x20142CC0, 0); //NanoPak
            Memory.WriteBit(0x201D554F, 7, false); //Vidcomic 1
            Memory.WriteBit(0x201D5551, 1, false); //Vidcomic 2
            Memory.WriteBit(0x201D5552, 2, false); //Vidcomic 3
            Memory.WriteBit(0x201D5550, 0, false); //Vidcomic 4
            Memory.WriteBit(0x201D5553, 3, false); //Vidcomic 5

        }
        public static void removeAllPlanets()
        {
            Memory.WriteByte(AvailableSlots[0], 0);
            Memory.WriteByte(AvailableSlots[1], 0);
            Memory.WriteByte(AvailableSlots[2], 0);
            Memory.WriteByte(AvailableSlots[3], 0);
            Memory.WriteByte(AvailableSlots[4], 0);
            Memory.WriteByte(AvailableSlots[5], 0);
            Memory.WriteByte(AvailableSlots[6], 0);
            Memory.WriteByte(AvailableSlots[7], 0);
            Memory.WriteByte(AvailableSlots[8], 0);
            Memory.WriteByte(AvailableSlots[9], 0);
            Memory.WriteByte(AvailableSlots[10], 0);
            Memory.WriteByte(AvailableSlots[11], 0);
            Memory.WriteByte(AvailableSlots[12], 0);
            Memory.WriteByte(AvailableSlots[13], 0);
            Memory.WriteByte(AvailableSlots[14], 0);
            Memory.WriteByte(AvailableSlots[15], 0);
            Memory.WriteByte(AvailableSlots[16], 0);
            Memory.WriteByte(AvailableSlots[17], 0);

        }
    }


    //Pattern series of hex addresses that always remain static throughout the games lifecycle
    //Mask is an array of shit you're looking for, x is for what you want, ? is for what you don't want
    //FindSignature() gets BaseAddress(), the Length of the Search, Pattern and Mask as parameters
    //Length of search determined by MODULEINFO.SizeOfImage (not exposed yet), Function is called GetModuleInfo() and takes moduleName as parameter which is the name of the executable without .exe on the end



}

