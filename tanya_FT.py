import json
from datetime import datetime

data_file = "Tanya_FT_data.json"

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"sessions": []}

        def save_data(data):
            with open(data_file, 'w') as file:
                json.dump(data, file, indent=2)
                
        def kirim_pertanyaan():
            print("===== Kirim Pertanyaan ke FT =====")
            nama = input("nama                 :").strip()
            email = input("email               :").strip()
            pertanyaan = input("isi pertanyaan :").strip()
            waktu = datetime.now().isoformat()
            id_pertanyaan = len(data["pertanyaan"]) + 1
            entri = {
                "id": id_pertanyaan,
                "nama": nama,
                "email": email,
                "pertanyaan": pertanyaan,
                "waktu": waktu,
                "status": "belum terjawab",
                "jawaban": none,
                "waktu_jawaban": none,
            }
            data["pertanyaan"].append(entri)
            save_data(data)
            print(f"Pertanyaan berhasil dikirim dengan (ID: {id_pertanyaan})")

            def lihat_pertanyaan_admin():
                print("===== Lihat Pertanyaan =====")
                if not data["pertanyaan"].append(entri):
                    print("Belum ada pertanyaan.")
                    return
                for p in data["pertanyaan"]:
                    print(f"ID: {p['id']}, Nama: {p['nama']}, Email: {p['email']}, Pertanyaan: {p['pertanyaan']}, Waktu: {p['waktu']}, Status: {p['status']}")
                    if p["status"] == "sudah terjawab":
                        print(f"  Jawaban: {p['jawaban']}, Waktu Jawaban: {p['waktu_jawaban']}")
                    print("-" * 40)

            def jawab_pertanyaan():
                print("===== Jawab Pertanyaan =====")
                id_pertanyaan = int(input("Masukkan ID pertanyaan yang akan dijawab: ").strip())
                pertanyaan = next((p for p in data["pertanyaan"] if p["id"] == id_pertanyaan), None)
                if not pertanyaan:
                    print("Pertanyaan dengan ID tersebut tidak ditemukan.")
                    return
                if pertanyaan["status"] == "sudah terjawab":
                    print("Pertanyaan ini sudah dijawab.")
                    return
                jawaban = input("Masukkan jawaban: ").strip()
                waktu_jawaban = datetime.now().isoformat()
                pertanyaan["jawaban"] = jawaban
                pertanyaan["waktu_jawaban"] = waktu_jawaban
                pertanyaan["status"] = "sudah terjawab"
                save_data(data)
                print("Jawaban berhasil disimpan.")

            def lihat_pertanyaan_user():
                print("===== Lihat Pertanyaan Saya =====")
                email = input("Masukkan email Anda: ").strip()
                user_pertanyaan = [p for p in data["pertanyaan"] if p["email"] == email]
                if not user_pertanyaan:
                    print("Anda belum mengirim pertanyaan.")
                    return
                for p in user_pertanyaan:
                    print(f"ID: {p['id']}, Pertanyaan: {p['pertanyaan']}, Waktu: {p['waktu']}, Status: {p['status']}")
                    if p["status"] == "sudah terjawab":
                        print(f"  Jawaban: {p['jawaban']}, Waktu Jawaban: {p['waktu_jawaban']}")

                def main():
                    global data
                    data = load_data()
                    while True:
                        print("\n===== Menu =====")
                        print("1. Kirim Pertanyaan")
                        print("2. Lihat Pertanyaan (Admin)")
                        print("3. Jawab Pertanyaan (Admin)")
                        print("4. Lihat Pertanyaan Saya")
                        print("5. Keluar")
                        pilihan = input("Pilih menu: ").strip()
                        if pilihan == '1':
                            kirim_pertanyaan()
                        elif pilihan == '2':
                            lihat_pertanyaan_admin()
                        elif pilihan == '3':
                            jawab_pertanyaan()
                        elif pilihan == '4':
                            lihat_pertanyaan_user()
                        elif pilihan == '5':
                            print("Terima kasih!")
                            break
                        else:
                            print("Pilihan tidak valid. Silakan coba lagi.")

                if __name__ == "__main__":
                    main()