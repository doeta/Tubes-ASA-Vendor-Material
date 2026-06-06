# Utils/Formatter.py

def FormatRupiah(Angka):
    """Mengubah integer menjadi format mata uang Rupiah yang rapi"""
    return f"Rp {Angka:,.0f}".replace(',', '.')
