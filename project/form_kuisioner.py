import streamlit as st
import pandas as pd
import os
import json
from save_data import save_response, connect

st.set_page_config(
    page_title="Form Kuisioner",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

hide_navbar = """
    <style>
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="stSidebarNav"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        div[data-testid="stSidebarCollapsedControl"] {display: none !important;}
    </style>
"""
st.markdown(hide_navbar, unsafe_allow_html=True)

st.title("KUISIONER TINGKAT KESADARAN KEAMANAN INFORMASI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "questions.json")

with open(json_path, "r", encoding="utf-8") as f:
    questions = json.load(f)


agreement = {
    1: "Sangat tidak setuju",
    2: "Tidak setuju",
    3: "Netral",
    4: "Setuju",
    5: "Sangat setuju"
}

agreement_inverse = {
    1 : "Sangat setuju",
    2: "Setuju",
    3: "Netral",
    4: "Tidak setuju",
    5: "Sangat tidak setuju"
}
frequency = {
    1: "Tidak Pernah",
    2: "Pernah",
    3: "Jarang",
    4: "Sering",
    5: "Sangat sering"
}

frequency_inverse = {
    
    1: "Sangat sering",
    2: "Sering",
    3: "Jarang",
    4: "Pernah",
    5: "Tidak Pernah"

}

knowledge = {
    1: "Tidak Tahu",
    2: "Kurang Tahu",
    3: "Cukup Tahu",
    4: "tahu",
    5: "sangat tahu"
}
DATA_FILE = "responses.csv"



with st.form("likert_form"):
    st.subheader("Identitas Pegawai")
    nama_pegawai = st.text_input("Nama")
    nip = st.text_input("NIP")
    #email = st.text_input("Email")
    usia = st.text_input("Usia")
    jk = st.radio(
        "Jenis Kelamin",
        ["Laki-laki", "Perempuan"],
    )
    pendidikan = st.selectbox(
        "-- Tingkat Pendidikan --",[
            "-- Tingkat Pendidikan --",
            "SMP",
            "SMA/Sederajat",
            "S1",
            "S2",
            "S3"
        ]
    )
    instansi = st.selectbox(
        "Asal Instansi",
        ["-- Pilih Instansi --",
         "Sekretariat Daerah",
         "Dinas Kependudukan dan Pencatatan Sipil",
         "Dinas Komunikasi dan Informatika",
         "Inspektorat",
         "DPMPTSP",
         "Dinas Pariwisata dan Ekonomi Kreatif",
         "Dinas Perumahan dan Kawasan Permukiman",
         "Badan Kesatuan Bangsa dan Politik",
         "Dinas Perpustakaan dan Kearsipan",
         "Badan Perencana Pembangunan Daerah",
         "Badan Pengelola Pajak dan Retribusi Daerah",
         "Badan Pengelola Keuangan dan Aset Daerah"]
    )

    def get_scale_for_question(questions):
        if questions["scale"] == "agreement":
            return agreement
        elif questions["scale"] == "frequency":
            return frequency
        if questions["scale"] == "agreement!":
            return agreement_inverse
        elif questions["scale"] == "frequency!":
            return frequency_inverse
        else:
            return knowledge
 
    def get_note_for_question(questions):
        if questions["note"] != "":
            return questions["note"]
        else:
            return ""
    
    st.subheader("Kuisioner")
    answers = []
    for i, q in enumerate(questions, start=1):
        st.write(f"**{i}. {q['question']}**")
        note = get_note_for_question(q)
        scale = get_scale_for_question(q)
        choice = st.radio(
            f"*{note}",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: scale[x],
            key=f"q{i}",
            label_visibility="collapsed" if note == "" else "visible"
        )
        answers.append(choice)

    submitted = st.form_submit_button("Kirim Jawaban")

if submitted:
    if nama_pegawai.strip() == "" or nip.strip() == "" or usia.strip() == "" or jk.strip() == "" or pendidikan == "-- Tingkat Pendidikan --" or instansi == "-- Pilih Instansi --":
        st.error("⚠️ Harap lengkapi identitas sebelum mengirim jawaban.")
    else:
        save_response({"nama_pegawai": nama_pegawai,  "nip": nip,"usia" : usia, "jk" : jk, "pendidikan" : pendidikan, "instansi": instansi}, answers)
        st.success("Terima kasih — jawaban Anda telah tersimpan ✅")
        st.switch_page("terima_kasih.py")
        
