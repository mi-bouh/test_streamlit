# streamlit_app.py
import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")], position="hidden")
pg.run()