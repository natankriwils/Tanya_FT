import json
from datetime import datetime

data_file = "Tanya_FT_data.json"

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pertanyaan": []}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=2)

def main():
    global data
    data = load_data()

    while True:
        print("\n===== Sistem Tanya FT =====")
        print("1. Masuk sebagai Pemohon")
        print("2. Masuk sebagai Respon")
        print("3. Keluar")
        pilihan = input("Pilih peran (1/2/3): ").strip()

        if pilihan == '1':
            menu_Pemohon()

        elif pilihan == '2':
            ADMIN_PASSWORD = "validasi123" 
            while True:
                pw = input("Validasi(tekan Enter untuk batal): ").strip()

                if pw == "":
                    print("Batal. Kembali ke menu utama.")
                    break

                if pw == ADMIN_PASSWORD:
                    respon_after_auth()
                    break
                else:
                    print("Kode validasi salah")

        elif pilihan == '3':
            print("Terima kasih telah menggunakan Tanya FT!")
            break

        else:
            print("Pilihan tidak valid.")

def menu_Pemohon():
    while True:
        print("\n===== Menu Pemohon =====")
        print("1. Kirim Pertanyaan")
        print("2. Lihat Pertanyaan Saya")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1/2/3): ").strip()

        if pilihan == '1':
            kirim_pertanyaan()
        elif pilihan == '2':
            lihat_pertanyaan_user()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

def kirim_pertanyaan():
    print("\n===== Kirim Pertanyaan ke FT =====")
    nama = input("Nama              : ").strip()
    email = input("Email             : ").strip()
    pertanyaan = input("Isi pertanyaan    : ").strip()
    waktu = datetime.now().isoformat()

    id_pertanyaan = len(data["pertanyaan"]) + 1
    entri = {
        "id": id_pertanyaan,
        "nama": nama,
        "email": email,
        "pertanyaan": pertanyaan,
        "waktu": waktu,
        "status": "belum terjawab",
        "jawaban": None,
        "waktu_jawaban": None,
    }
    data["pertanyaan"].append(entri)
    save_data(data)
    print(f"\n✅ Pertanyaan berhasil dikirim dengan ID: {id_pertanyaan}")

def lihat_pertanyaan_user():
    print("\n===== Lihat Pertanyaan Saya =====")
    email = input("Masukkan email Anda: ").strip()
    user_pertanyaan = [p for p in data["pertanyaan"] if p["email"] == email]
    if not user_pertanyaan:
        print("Anda belum mengirim pertanyaan.")
        return
    for p in user_pertanyaan:
        print(f"\nID: {p['id']}")
        print(f"Pertanyaan: {p['pertanyaan']}")
        print(f"Status: {p['status']}")
        if p["status"] == "sudah terjawab":
            print(f"Jawaban: {p['jawaban']}")
            print(f"Waktu Jawaban: {p['waktu_jawaban']}")
        print("-" * 40)

def lihat_pertanyaan_Respon():
    print("\n===== Lihat Semua Pertanyaan =====")
    if not data["pertanyaan"]:
        print("Belum ada pertanyaan.")
        return
    for p in data["pertanyaan"]:
        print(f"\nID: {p['id']}")
        print(f"Nama: {p['nama']}")
        print(f"Email: {p['email']}")
        print(f"Pertanyaan: {p['pertanyaan']}")
        print(f"Waktu: {p['waktu']}")
        print(f"Status: {p['status']}")
        if p["status"] == "sudah terjawab":
            print(f"Jawaban: {p['jawaban']}")
            print(f"Waktu Jawaban: {p['waktu_jawaban']}")
        print("-" * 40)

def respon_after_auth():
    while True:
        lihat_pertanyaan_Respon()
        print("\n1. Jawab Pertanyaan")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1/2): ").strip()
        if pilihan == '1':
            jawab_pertanyaan()
            continue
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid.")

def jawab_pertanyaan():
    print("\n===== Jawab Pertanyaan =====")
    while True:
        s = input("Masukkan ID pertanyaan (Enter untuk batal): ").strip()
        if s == "":
            print("Batal. Kembali ke menu Respon.")
            return
        try:
            id_pertanyaan = int(s)
        except ValueError:
            print("ID tidak valid. Masukkan angka atau tekan Enter untuk batal.")
            continue

        pertanyaan = next((p for p in data["pertanyaan"] if p["id"] == id_pertanyaan), None)
        if not pertanyaan:
            print("Pertanyaan tidak ditemukan. Periksa ID dan coba lagi.")
            continue
        if pertanyaan["status"] == "sudah terjawab":
            print("Pertanyaan ini sudah dijawab.")
            continue

        jawaban = input("Masukkan jawaban: ").strip()
        waktu_jawaban = datetime.now().isoformat()
        pertanyaan["jawaban"] = jawaban
        pertanyaan["waktu_jawaban"] = waktu_jawaban
        pertanyaan["status"] = "sudah terjawab"
        save_data(data)
        print("\n✅ Jawaban berhasil disimpan.")
        return

if __name__ == "__main__":
    main()
