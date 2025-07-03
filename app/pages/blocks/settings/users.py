import streamlit as st
from streamlit.column_config import TextColumn

from utils import read_data, save_changes


DB_TABLE = "users"
users = read_data(source=DB_TABLE)


def render():
      st.subheader("Пользователи")


      df = st.data_editor(
            data=users,
            key=f"{DB_TABLE}-data",
            hide_index=True,
            use_container_width=True,
            column_order=["last_name", "first_name", "middle_name", "short_name", "phone", "telegram"],
            column_config={
                  "last_name": TextColumn("Фамилия"),
                  "first_name": TextColumn("Имя"),
                  "middle_name": TextColumn("Отчество"),
                  "short_name": TextColumn("Уменьшительное Имя"),
                  "phone": TextColumn("Телефон"),
                  "telegram": TextColumn("Телеграм")
            },
            num_rows="dynamic"
      )


      has_unsaved_changes = any([
            bool(st.session_state[f"{DB_TABLE}-data"]["edited_rows"]),
            all([
                  bool(st.session_state[f"{DB_TABLE}-data"]["added_rows"]),
                  any(bool(value) for value in st.session_state[f"{DB_TABLE}-data"]["added_rows"])
            ]),
            bool(st.session_state[f"{DB_TABLE}-data"]["deleted_rows"])
      ])

     
      left ,right = st.columns([3, 1], vertical_alignment="center")
      if has_unsaved_changes:
            left.warning(
                  "Есть несохранённые изменения"
            )
      right.button(
            label="Сохранить",
            key=f"{DB_TABLE}-save",
            type="primary",
            icon=":material/save:",
            use_container_width=True,
            on_click=save_changes,
            kwargs={
                  "target": DB_TABLE,
                  "data": users
            },
            disabled=not has_unsaved_changes
      )
