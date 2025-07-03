import streamlit as st
from streamlit_extras.customize_running import center_running
center_running()

from utils import load_css


load_css("app/assets/style.css")


pages = [
      st.Page(page="pages/invitation.py", title="Приглашение", icon=":material/event:", default=True)
]


pg = st.navigation(pages=pages, position="sidebar")
pg.run()