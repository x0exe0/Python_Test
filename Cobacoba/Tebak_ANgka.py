import random

print("=== GAME TEBAK ANGKA ===")

batas_bawah = 1
batas_atas = 100

angka_rahasia = random.randint(batas_bawah, batas_atas)
jumlah_tebakan = 0

while True:
    print(f"\nTebak angka antara {batas_bawah} dan {batas_atas}")
    
    tebakan = int(input("Masukkan tebakan kamu: "))
    jumlah_tebakan += 1

    if tebakan < batas_bawah or tebakan > batas_atas:
        print("⚠ Angka di luar range!")
        continue

    if tebakan > angka_rahasia:
        print("Terlalu besar!")
        batas_atas = tebakan - 1

    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")
        batas_bawah = tebakan + 1

    else:
        print(f"\n🎉 BENAR! Angkanya adalah {angka_rahasia}")
        print(f"Kamu menebak dalam {jumlah_tebakan} percobaan.")
        break