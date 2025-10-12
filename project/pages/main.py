import streamlit as st



pages = {
    "" : [
        st.Page("dashboard.py", title="Dashboard"),
        st.Page("hasil_kuisioner.py", title="Hasil Kuisioner"),
        st.Page("proses_klaster.py", title="klaster"),
              ],
        
        "Akunmu" : [
              st.Page("akun.py", title="Akun"), 
              ]
}
    


pg = st.navigation(pages)
pg.run()

