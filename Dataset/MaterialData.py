# Dataset/MaterialData.py
import random
from Settings import ScaleFactor

# =====================================================================
# KATALOG DATA MATERIAL PROYEK GEDUNG BERTINGKAT (3-5 LANTAI)
# Simulasi: Pembangunan Gedung Bertingkat ~2000 m2 Total
# Harga dan kuantitas disesuaikan dengan skala proyek realistis
# =====================================================================

Catalog = {
    # --- PEKERJAAN STRUKTUR & PONDASI (BOBOT TINGGI: 1.5) ---
    "Semen Portland (500 Sak)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Semen Gresik", "RealCost": 27_500_000, "Quality": 90},
            {"Id": "Semen Tiga Roda", "RealCost": 29_000_000, "Quality": 92},
            {"Id": "Semen Padang", "RealCost": 26_000_000, "Quality": 85},
            {"Id": "Semen Merah Putih", "RealCost": 24_500_000, "Quality": 80}
        ]
    },
    "Besi Beton 12mm Ulir (500 Batang)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Krakatau Steel (KS)", "RealCost": 57_500_000, "Quality": 95},
            {"Id": "Master Steel (MS)", "RealCost": 54_000_000, "Quality": 88},
            {"Id": "Cakra Steel (CS)", "RealCost": 51_000_000, "Quality": 85},
            {"Id": "Besi Polos Standar", "RealCost": 42_500_000, "Quality": 70}
        ]
    },
    "Pasir Cor Lumajang (50 Truk)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Tambang Semeru", "RealCost": 90_000_000, "Quality": 94},
            {"Id": "Tambang Brantas", "RealCost": 82_500_000, "Quality": 88},
            {"Id": "Tambang Lokal A", "RealCost": 75_000_000, "Quality": 82},
            {"Id": "Tambang Lokal B", "RealCost": 70_000_000, "Quality": 75}
        ]
    },
    "Batu Split 1-2 cm (50 Truk)": {
        "PriorityWeight": 1.5,
        "Vendors": [
            {"Id": "Quarry Merapi", "RealCost": 110_000_000, "Quality": 95},
            {"Id": "Quarry Clereng", "RealCost": 100_000_000, "Quality": 89},
            {"Id": "Quarry Lokal 1", "RealCost": 92_500_000, "Quality": 83},
            {"Id": "Quarry Lokal 2", "RealCost": 85_000_000, "Quality": 78}
        ]
    },

    # --- PEKERJAAN DINDING & ATAP (BOBOT MENENGAH-TINGGI: 1.2-1.3) ---
    "Bata Ringan Hebel (100 Kubik)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Citicon", "RealCost": 65_000_000, "Quality": 92},
            {"Id": "Grand Elephant", "RealCost": 62_000_000, "Quality": 88},
            {"Id": "Bricon", "RealCost": 58_000_000, "Quality": 85},
            {"Id": "Focon", "RealCost": 55_000_000, "Quality": 80}
        ]
    },
    "Baja Ringan Kanal C (500 Batang)": {
        "PriorityWeight": 1.3,
        "Vendors": [
            {"Id": "Taso", "RealCost": 52_500_000, "Quality": 95},
            {"Id": "CBM", "RealCost": 46_000_000, "Quality": 87},
            {"Id": "Kencana", "RealCost": 44_000_000, "Quality": 84},
            {"Id": "Prima Inti", "RealCost": 40_000_000, "Quality": 77}
        ]
    },
    "Genteng Beton Flat (5000 Pcs)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Monier", "RealCost": 42_500_000, "Quality": 93},
            {"Id": "Kanmuri", "RealCost": 40_000_000, "Quality": 90},
            {"Id": "Mutiara", "RealCost": 36_000_000, "Quality": 84},
            {"Id": "Cisangkan", "RealCost": 34_000_000, "Quality": 79}
        ]
    },

    # --- PEKERJAAN MEP / UTILITAS (BOBOT MENENGAH: 1.0-1.2) ---
    "Pipa PVC 4 Inch (200 Batang)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Wavin / Rucika AW", "RealCost": 26_000_000, "Quality": 95},
            {"Id": "Maspion AW", "RealCost": 23_200_000, "Quality": 88},
            {"Id": "Trilliun", "RealCost": 21_600_000, "Quality": 84},
            {"Id": "Langit PVC", "RealCost": 19_200_000, "Quality": 75}
        ]
    },
    "Kabel Listrik NYM 3x2.5 (50 Roll)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Supreme", "RealCost": 42_500_000, "Quality": 96},
            {"Id": "Eterna", "RealCost": 39_000_000, "Quality": 91},
            {"Id": "Extrana", "RealCost": 36_000_000, "Quality": 85},
            {"Id": "Kitani", "RealCost": 32_500_000, "Quality": 78}
        ]
    },
    "Tandon Air Stainless 1000L (5 Unit)": {
        "PriorityWeight": 1.0,
        "Vendors": [
            {"Id": "Penguin", "RealCost": 17_500_000, "Quality": 92},
            {"Id": "Profil Tank", "RealCost": 16_250_000, "Quality": 88},
            {"Id": "Excel", "RealCost": 14_500_000, "Quality": 82},
            {"Id": "Mpoin", "RealCost": 13_000_000, "Quality": 76}
        ]
    },

    # --- PEKERJAAN FINISHING & ARSITEKTURAL (BOBOT RENDAH: 0.8) ---
    "Cat Tembok Eksterior 20L (50 Pail)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Dulux Weathershield", "RealCost": 92_500_000, "Quality": 96},
            {"Id": "Nippon Paint Elastex", "RealCost": 80_000_000, "Quality": 90},
            {"Id": "Jotun Jotashield", "RealCost": 86_000_000, "Quality": 94},
            {"Id": "Avitex Eksterior", "RealCost": 62_500_000, "Quality": 82}
        ]
    },
    "Keramik Lantai 60x60 (200 Dus)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Roman Granit", "RealCost": 50_000_000, "Quality": 95},
            {"Id": "Milan", "RealCost": 42_000_000, "Quality": 88},
            {"Id": "Platinum", "RealCost": 36_000_000, "Quality": 82},
            {"Id": "Kia", "RealCost": 34_000_000, "Quality": 78}
        ]
    },
    "Plafon Gypsum 9mm (500 Lembar)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "Jayaboard", "RealCost": 37_500_000, "Quality": 94},
            {"Id": "Elephant", "RealCost": 34_000_000, "Quality": 88},
            {"Id": "Knauf", "RealCost": 31_000_000, "Quality": 85},
            {"Id": "A-Plus", "RealCost": 27_500_000, "Quality": 79}
        ]
    },
    "Kusen Aluminium 3 Inch (100 Batang)": {
        "PriorityWeight": 0.8,
        "Vendors": [
            {"Id": "YKK AP", "RealCost": 70_000_000, "Quality": 96},
            {"Id": "Alexindo", "RealCost": 57_500_000, "Quality": 89},
            {"Id": "Alcomexindo", "RealCost": 49_000_000, "Quality": 83},
            {"Id": "Dacon", "RealCost": 42_500_000, "Quality": 76}
        ]
    },
    "Waterproofing Dak (20 Pail)": {
        "PriorityWeight": 1.2,
        "Vendors": [
            {"Id": "Aquaproof Pro", "RealCost": 22_000_000, "Quality": 92},
            {"Id": "Sikalastic", "RealCost": 24_000_000, "Quality": 95},
            {"Id": "Nippon Elastex", "RealCost": 19_200_000, "Quality": 85},
            {"Id": "No Drop", "RealCost": 16_800_000, "Quality": 80}
        ]
    }
}

def LoadProcessedData():
    """Memuat data 15 kategori material dan mereduksi nilainya berdasarkan ScaleFactor"""
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
    """Menduplikasi data untuk pengujian algoritma dalam beban kerja berat (N=50 atau N=200)"""
    BaseMaterials = LoadProcessedData()
    Materials = list(BaseMaterials)

    while len(Materials) < TargetSize:
        Template = random.choice(BaseMaterials)
        NewVendors = []
        for v in Template:
            Variation = random.uniform(0.9, 1.1)
            NewRealCost = int(v['RealCost'] * Variation)
            NewVendors.append({
                'Id': f"{v['Id']} Variant-{len(Materials)+1}",
                'RealCost': NewRealCost,
                'Cost': NewRealCost // ScaleFactor,
                'Quality': v['Quality'],
                'WeightedScore': v['WeightedScore']
            })
        Materials.append(NewVendors)
    return Materials
