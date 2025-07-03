import streamlit as st


def load_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def not_allowed():
      st.warning("У вас нет доступа к этой странице.")