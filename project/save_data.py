import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
from .connect import connect
        
def save_response(identity, answers):
    connect()
    timestamp = datetime.utcnow().isoformat()
    row = {
        "timestamp": timestamp,
        "nama_pegawai": identity["nama_pegawai"],
        "nip": identity["nip"],
        #"email": identity["email"],
        "jk": identity["jk"],
        "status" : identity["status"],
        "usia": identity["usia"],
        "pendidikan": identity["pendidikan"],
        "instansi": identity["instansi"]
    }
    for i, ans in enumerate(answers, start=1):
        row[f"q{i}"] = ans

    ref = db.reference("/responsekertas")
    ref.push(row)
    
