import streamlit as st

from utils import read_data


def not_allowed() -> None:
      st.warning("У вас нет доступа к этой странице.")


def welcome() -> None:
      # token = st.session_state.token
      # type = st.session_state.role

      st.success("greeting welcome")

      # data = read_data(source=type)
      # name = data.loc[data.token == token, "name"].values[0]
      
      # st.session_state[type] = {
      #       "name": name
      # }
      # if type == "guest":
      #       partner_name = data.loc[data.token == token, "partner_name"].values[0]
      #       st.session_state[type]["partner_name"] = partner_name
      # else:
      #       partner_name = None

      # st.markdown(
      #       unsafe_allow_html=True,
      #       body=f"""
      #       <div class="title" style="margin-bottom: 40px">
      #             {
      #                   "<h1>" + name + (" и " + partner_name if partner_name else "") + "</h1>"
      #             }
      #       </div>
      #       """
      # )
