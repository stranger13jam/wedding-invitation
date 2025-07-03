import streamlit as st
from streamlit_extras.customize_running import center_running
center_running()

from utils import load_css, not_allowed


load_css("app/assets/style.css")


if "token" in st.query_params or "token" in st.session_state:
      token = st.query_params.token if "token" in st.query_params else st.session_state.token
      st.session_state.token = token

      is_admin = token == st.secrets.tokens.admin
      is_guest = token == st.secrets.tokens.guest

      if is_admin:
            st.session_state.role = "admin"
            pages = [
                  st.Page(page="pages/invitation.py", title="Приглашение", icon=":material/event:", default=True)
            ]
      elif is_guest:
            st.session_state.role = "guest"
            pages = [
                  st.Page(page="pages/invitation.py", title="Приглашение", icon=":material/event:", default=True)
            ]
      else:
            pages = [
                  st.Page(page=not_allowed)
            ]
else:
      pages = [
            st.Page(page=not_allowed)
      ]

pg = st.navigation(pages=pages, position="sidebar")
pg.run()