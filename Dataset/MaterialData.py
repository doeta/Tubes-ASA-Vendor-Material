# Dataset/MaterialData.py
import random
from Settings import ScaleFactor

# dataset material proyek (25 kategori)

Catalog = {
    # pekerjaan struktur & pondasi (prioritas tinggi)
    "Tiang Pancang Mini Pile 25x25 (1000 Meter)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Wika Beton", "RealCost": 237_000_000, "Quality": 96},
            {"Id": "Jaya Beton / KSPS", "RealCost": 205_000_000, "Quality": 90},
            {"Id": "Tiga Pilar Sejahtera", "RealCost": 178_000_000, "Quality": 82},
            {"Id": "Pancang Lokal Non-SNI", "RealCost": 144_000_000, "Quality": 68}
        ]
    },
    "Beton Ready Mix K350 (500 Kubik)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Jayamix / Holcim", "RealCost": 510_000_000, "Quality": 96},
            {"Id": "SCG Readymix", "RealCost": 482_500_000, "Quality": 90},
            {"Id": "Pionir Beton", "RealCost": 460_000_000, "Quality": 83},
            {"Id": "Batching Plant Lokal", "RealCost": 437_500_000, "Quality": 72}
        ]
    },
    "Multipleks Phenolic Bekisting 12mm (200 Lembar)": {
        "PriorityWeight": 1.4,
        "Vendors": [
            {"Id": "Film Face Import Korindo", "RealCost": 45_000_000, "Quality": 95},
            {"Id": "Film Face Standar Sinar Mas", "RealCost": 37_000_000, "Quality": 88},
            {"Id": "Phenolic Lokal", "RealCost": 29_600_000, "Quality": 78},
            {"Id": "Multiplek Biasa", "RealCost": 22_400_000, "Quality": 65}
        ]
    },
    "Semen Portland (500 Sak / 50Kg)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Semen Tiga Roda", "RealCost": 39_250_000, "Quality": 95},
            {"Id": "Semen Gresik", "RealCost": 35_750_000, "Quality": 92},
            {"Id": "Semen Merah Putih", "RealCost": 36_000_000, "Quality": 88},
            {"Id": "Semen Padang / SCG", "RealCost": 34_500_000, "Quality": 85}
        ]
    },
    "Besi Beton 12mm Ulir (500 Batang)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Krakatau Steel (KS)", "RealCost": 49_500_000, "Quality": 98},
            {"Id": "Master Steel (MS)", "RealCost": 47_250_000, "Quality": 92},
            {"Id": "Cakra Steel (CS)", "RealCost": 40_750_000, "Quality": 85},
            {"Id": "Besi Polos Standar", "RealCost": 31_000_000, "Quality": 60}
        ]
    },
    "Pasir Cor Pengecoran (50 Truk)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Pasir Cor Super Muntilan", "RealCost": 130_000_000, "Quality": 95},
            {"Id": "Pasir Cor Standar Muntilan", "RealCost": 105_000_000, "Quality": 88},
            {"Id": "Pasir Lokal Weleri", "RealCost": 85_000_000, "Quality": 75},
            {"Id": "Pasir Abu / Curah", "RealCost": 60_000_000, "Quality": 60}
        ]
    },
    "Batu Split Koral Beton 1-2 cm (50 Truk)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Batu Split Premium Quarry Merapi", "RealCost": 215_625_000, "Quality": 95},
            {"Id": "Koral Beton Standar Menengah", "RealCost": 167_500_000, "Quality": 88},
            {"Id": "Batu Split Truk Engkel", "RealCost": 125_000_000, "Quality": 75},
            {"Id": "Batu Split Kualitas Rendah", "RealCost": 85_000_000, "Quality": 60}
        ]
    },

    # pekerjaan dinding & atap (prioritas menengah)
    "Bata Ringan Hebel AAC (100 Kubik)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Citicon", "RealCost": 72_000_000, "Quality": 95},
            {"Id": "Grand Elephant", "RealCost": 69_000_000, "Quality": 90},
            {"Id": "Bricon", "RealCost": 66_000_000, "Quality": 88},
            {"Id": "Focon", "RealCost": 61_000_000, "Quality": 80}
        ]
    },
    "Baja Ringan Rangka Atap Kanal C (500 Batang)": {
        "PriorityWeight": 1.3,
        "Vendors": [
            {"Id": "Taso", "RealCost": 64_500_000, "Quality": 96},
            {"Id": "Kencana", "RealCost": 52_500_000, "Quality": 92},
            {"Id": "CBM", "RealCost": 54_950_000, "Quality": 85},
            {"Id": "Prima Inti", "RealCost": 37_500_000, "Quality": 70}
        ]
    },
    "Genteng Beton Proteksi Geometri Flat (5000 Pcs)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Monier Excel Plano", "RealCost": 48_000_000, "Quality": 95},
            {"Id": "Cisangkan Multiline", "RealCost": 47_750_000, "Quality": 94},
            {"Id": "Mutiara", "RealCost": 34_000_000, "Quality": 85},
            {"Id": "Garuda / Purnama", "RealCost": 23_000_000, "Quality": 75}
        ]
    },
    "Kaca Tempered Fasad 10mm (100 m2)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Asahimas Flat Glass", "RealCost": 85_000_000, "Quality": 96},
            {"Id": "Mulia Glass Indah", "RealCost": 72_000_000, "Quality": 90},
            {"Id": "SIG Glass", "RealCost": 58_000_000, "Quality": 82},
            {"Id": "Kaca Tempered Lokal", "RealCost": 42_000_000, "Quality": 68}
        ]
    },

    # jaringan utilitas MEP (prioritas bervariasi)
    "Pipa Distribusi uPVC Tipe AW 4 Inch (200 Btg/6m)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Wavin / Rucika AW", "RealCost": 91_176_000, "Quality": 96},
            {"Id": "Maspion AW", "RealCost": 74_060_000, "Quality": 88},
            {"Id": "Trilliun AW", "RealCost": 57_020_000, "Quality": 80},
            {"Id": "Pipa C/D Lokal Grade 4", "RealCost": 26_950_000, "Quality": 65}
        ]
    },
    "Pompa Booster Air Gedung (2 Unit)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Grundfos CME", "RealCost": 57_000_000, "Quality": 96},
            {"Id": "Wilo MHI", "RealCost": 45_000_000, "Quality": 90},
            {"Id": "DAB Esybox", "RealCost": 35_000_000, "Quality": 82},
            {"Id": "Shimizu PS", "RealCost": 25_000_000, "Quality": 72}
        ]
    },
    "Reservoir Tangki Air Stainless 1000L (5 Unit)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Penguin Stainless", "RealCost": 42_750_000, "Quality": 96},
            {"Id": "Profil Tank Stainless", "RealCost": 32_500_000, "Quality": 90},
            {"Id": "Excel Standar", "RealCost": 23_250_000, "Quality": 82},
            {"Id": "Penampung Plastik Basic", "RealCost": 15_000_000, "Quality": 70}
        ]
    },
    "Panel Listrik LVMDP Utama 200A (1 Set)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Schneider Electric", "RealCost": 27_000_000, "Quality": 96},
            {"Id": "ABB", "RealCost": 22_000_000, "Quality": 90},
            {"Id": "Chint / Siemens Lokal", "RealCost": 15_000_000, "Quality": 82},
            {"Id": "Panel Modifikasi Lokal", "RealCost": 8_000_000, "Quality": 65}
        ]
    },
    "Panel Box MCB Distribusi 3 Phase (10 Set)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Schneider Domae", "RealCost": 28_500_000, "Quality": 95},
            {"Id": "Hager", "RealCost": 22_000_000, "Quality": 88},
            {"Id": "Chint", "RealCost": 15_200_000, "Quality": 80},
            {"Id": "MCB Box Lokal", "RealCost": 9_500_000, "Quality": 68}
        ]
    },
    "Jaringan Induk Kabel Listrik NYM 3x2.5mm (50 Roll/50m)": {
        "PriorityWeight": 1.3,
        "Vendors": [
            {"Id": "Supreme", "RealCost": 87_500_000, "Quality": 98},
            {"Id": "Eterna", "RealCost": 69_945_000, "Quality": 92},
            {"Id": "Extrana", "RealCost": 63_750_000, "Quality": 85},
            {"Id": "Kabelindo / Akko", "RealCost": 18_625_000, "Quality": 60}
        ]
    },
    "AC Cassette 2 PK (10 Unit)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Daikin Inverter", "RealCost": 240_490_000, "Quality": 96},
            {"Id": "Mitsubishi Heavy", "RealCost": 198_000_000, "Quality": 92},
            {"Id": "Panasonic Standard", "RealCost": 165_000_000, "Quality": 85},
            {"Id": "AC Non-Inverter Standar", "RealCost": 119_700_000, "Quality": 72}
        ]
    },
    "Pintu Fire Door Tahan Api 120 Menit (5 Unit)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Megadoor UL Listed", "RealCost": 62_500_000, "Quality": 96},
            {"Id": "Maxdoor", "RealCost": 49_000_000, "Quality": 90},
            {"Id": "Fortress", "RealCost": 37_500_000, "Quality": 82},
            {"Id": "Fire Door Lokal", "RealCost": 27_500_000, "Quality": 70}
        ]
    },

    # pekerjaan finishing & arsitektur (prioritas rendah)
    "Pelapis Dinding Cat Eksterior Tahan Cuaca 20L (50 Pail)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Nippon Weatherbond", "RealCost": 176_050_000, "Quality": 96},
            {"Id": "Nippon Spotless", "RealCost": 104_700_000, "Quality": 90},
            {"Id": "Mowilex Precoat WPS", "RealCost": 72_900_000, "Quality": 85},
            {"Id": "Avitex / Bondall", "RealCost": 46_225_000, "Quality": 70}
        ]
    },
    "Granit Lantai 60x60 Lobi Utama (200 Dus)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Granito Salsa Premium", "RealCost": 57_000_000, "Quality": 96},
            {"Id": "Niro Granite", "RealCost": 46_000_000, "Quality": 90},
            {"Id": "Garuda Tile Granit", "RealCost": 35_000_000, "Quality": 82},
            {"Id": "Granit Import China", "RealCost": 24_000_000, "Quality": 70}
        ]
    },
    "Keramik Lantai Ruang Standar 60x60 (200 Dus)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Roman Gol. A", "RealCost": 35_400_000, "Quality": 95},
            {"Id": "Roman Gol. C", "RealCost": 30_400_000, "Quality": 88},
            {"Id": "Milan Strata", "RealCost": 17_000_000, "Quality": 78},
            {"Id": "Porselen Lokal", "RealCost": 13_000_000, "Quality": 65}
        ]
    },
    "Partisi Atap Papan Plafon Gypsum 9mm (500 Lembar)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Jayaboard WR/Tahan Air", "RealCost": 69_000_000, "Quality": 96},
            {"Id": "Jayaboard Standar", "RealCost": 42_500_000, "Quality": 90},
            {"Id": "Elephant / Knauf", "RealCost": 27_500_000, "Quality": 82},
            {"Id": "Papan Gipsum A-Plus", "RealCost": 26_000_000, "Quality": 75}
        ]
    },
    "Ekstrusi Kusen Jendela Aluminium 3 Inchi (100 Batang)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "YKK AP Anodized", "RealCost": 35_000_000, "Quality": 96},
            {"Id": "Alexindo Profil", "RealCost": 19_600_000, "Quality": 89},
            {"Id": "Dacon Ekstrusi", "RealCost": 15_000_000, "Quality": 83},
            {"Id": "Alumunium Lokal Z", "RealCost": 10_200_000, "Quality": 76}
        ]
    },
    "Sistem Insulasi Pelapis Waterproofing Dak Atap (20 Pail)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Sikalastic 590 Pro", "RealCost": 32_440_000, "Quality": 96},
            {"Id": "Mowilex Sealer", "RealCost": 29_160_000, "Quality": 90},
            {"Id": "No Drop Waterproof", "RealCost": 18_000_000, "Quality": 82},
            {"Id": "Aquaproof Campuran", "RealCost": 16_000_000, "Quality": 78}
        ]
    }
}

def LoadProcessedData():
    # proses data catalog dan apply scale factor
    Materials = []
    for MatName, MatData in Catalog.items():
        Weight = MatData["PriorityWeight"]
        ProcessedVendors = []
        for v in MatData["Vendors"]:
            ProcessedVendors.append({
                'Id': f"{v['Id']} ({MatName})",
                'RealCost': v['RealCost'],
                'Cost': v['RealCost'] // ScaleFactor,
                'Quality': v['Quality'],
                'WeightedScore': v['Quality'] * Weight
            })
        Materials.append(ProcessedVendors)
    return Materials

def GenerateMassiveData(TargetSize=50):
    # generate dummy data untuk stress test
    BaseMaterials = LoadProcessedData()
    Materials = list(BaseMaterials)

    while len(Materials) < TargetSize:
        Template = random.choice(BaseMaterials)
        NewVendors = []
        for v in Template:
            # random harga +- 10%
            Variation = random.uniform(0.9, 1.1)
            NewRealCost = int(v['RealCost'] * Variation)
            NewVendors.append({
                'Id': f"{v['Id']} Distribusi Mutasi Variasi-{len(Materials)+1}",
                'RealCost': NewRealCost,
                'Cost': NewRealCost // ScaleFactor,
                'Quality': v['Quality'],
                'WeightedScore': v['WeightedScore']
            })
        Materials.append(NewVendors)
    return Materials
