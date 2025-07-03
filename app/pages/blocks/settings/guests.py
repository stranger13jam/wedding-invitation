import streamlit as st
from streamlit.column_config import TextColumn, LinkColumn, DatetimeColumn, CheckboxColumn

import pandas as pd

from utils import read_data, save_changes, insert_record
from pages.blocks.settings.users import users


DB_TABLE = "guests_expanded"
guests = read_data(source=DB_TABLE)


def user_name_by_id(id):
      # user = " ".join(users.loc[users.id == 1, ["last_name", "first_name", "middle_name"]].values[0].tolist())
      user = users.loc[users.id == id, ["last_name", "first_name", "middle_name"]]
      user = user.values[0]
      user = [n for n in user.tolist() if n]
      user = " ".join(user)

      return user


@st.dialog(title="Добавить гостя", width="large")
def add_guest_form(key="add_form"):
      prefix = f"{DB_TABLE}-{key}"
      
      st.selectbox(
            label="Гость",
            key=f"{prefix}-guest_id",
            options=users["id"],
            index=None,
            format_func=lambda id: user_name_by_id(id)
      )

      st.selectbox(
            label="Партнёр",
            key=f"{prefix}-partner_id",
            options=users["id"],
            index=None,
            format_func=lambda id: user_name_by_id(id)
      )

      st.text_area(
            label="Комментарий",
            key=f"{prefix}-note"
      )

      left, right = st.columns([3, 1], vertical_alignment="center")
      if right.button(
            label="Подтвердить",
            key=f"{prefix}-submit",
            type="primary",
            use_container_width=True
      ):

            columns = ["guest_id", "partner_id", "note"]
            values = [
                  st.session_state[f"{prefix}-guest_id"],
                  st.session_state[f"{prefix}-partner_id"],
                  st.session_state[f"{prefix}-note"]
            ]
            values = [str(v) if v else "''" for v in values]

            insert_record(target="guests", columns=columns, values=values)
            st.rerun()



def render():
      st.subheader("Список гостей")


      df = st.dataframe(
            data=guests,
            key=f"{DB_TABLE}-data",
            hide_index=True,
            column_order=["guest_name", "partner_name", "note", "invitation_link", "invitation_sent", "responded_at", "will_come", "wishes"],
            column_config={
                  "guest_name": TextColumn("Имя гостя"),
                  "partner_name": TextColumn("Имя партнёра"),
                  "note": TextColumn("Комментарий"),
                  "invitation_link": LinkColumn("Ссылка"),
                  "invitation_sent": CheckboxColumn("Приглашение отправлено"),
                  "responded_at": DatetimeColumn("Ответ получен"),
                  "will_come": CheckboxColumn("Придёт"),
                  "wishes": TextColumn("Вопросы и пожелания")
            },
      )


      left, right = st.columns([3, 1], vertical_alignment="center")
      right.button(
            label="Добавить гостя",
            key=f"{DB_TABLE}-add",
            type="primary",
            icon=":material/add_circle:",
            use_container_width=True
      )

      
      if st.session_state[f"{DB_TABLE}-add"]:
            add_guest_form()
