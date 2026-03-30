import streamlit as st

pages = {st.Page("Page 1.py", title="Create your account")}

pg = st.navigation(pages)
pg.run()
