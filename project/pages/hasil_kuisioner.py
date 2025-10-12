import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# --- Fungsi koneksi ke Firebase ---
def connect():
    if not firebase_admin._apps:
        cred = credentials.Certificate("kuisioner_haisq.json")  # pastikan file JSON ada di folder yang sama
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://kuisioner-haisq-default-rtdb.firebaseio.com/'  # ganti dengan URL database kamu
        })
        print("✅ Berhasil terhubung ke Firebase.\n")

# --- Jalankan koneksi Firebase ---
connect()

# --- Ambil data dari Firebase ---
ref = db.reference("/response")  # pastikan path ini sesuai dengan tempat kamu menyimpan data
data = ref.get()

if data:
    # Ubah dictionary ke list
    rows = [value for value in data.values()]

    # Ubah ke DataFrame untuk tampilan tabel rapi
    df = pd.DataFrame(rows)

    print("📋 Data Kuisioner Pegawai:\n")
    print(df)

    print("\nTotal responden:", len(df))

else:
    print("⚠️ Tidak ada data ditemukan di Firebase.")
