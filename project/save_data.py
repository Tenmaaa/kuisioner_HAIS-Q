import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

def connect():
    gcp_sa = st.secrets["gcp_service_account"]
    cred = credentials.Certificate(dict(gcp_sa))  # pastikan file JSON-nya di folder yang sama
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://kuisioner-haisq-default-rtdb.firebaseio.com/'
        })
        
def save_response(identity, answers):
    connect()
    timestamp = datetime.utcnow().isoformat()
    row = {
        "timestamp": timestamp,
        "nama_pegawai": identity["nama_pegawai"],
        "nip": identity["nip"],
        #"email": identity["email"],
        "jk": identity["jk"],
        "usia": identity["usia"],
        "pendidikan": identity["pendidikan"],
        "instansi": identity["instansi"]
    }
    for i, ans in enumerate(answers, start=1):
        row[f"q{i}"] = ans

    ref = db.reference("/response")
    ref.push(row)
