import streamlit as st
import psycopg2
import pandas as pd
import textwrap
import pytz
from typing import Literal
import logging


LOG = logging.Logger(__name__)

msk_tz = pytz.timezone("Europe/Moscow")


def load_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



################ Database Utils ################


st_conn = st.connection("postgresql", type="sql")

secrets = st.secrets.connections.postgresql
db_config = {
      "host": secrets["host"],
      "port": secrets["port"],
      "dbname": secrets["database"],
      "user": secrets["username"],
      "password": secrets["password"]
}


def save_answer():
      # worksheet = sh.worksheet(ws_answers)
      
      # values = [
      #       datetime.now(tz=msk_tz).strftime('%Y-%m-%d %H:%M:%S'),
      #       st.session_state["questionnaire_name"],
      #       st.session_state["questionnaire_will_come"],
      #       st.session_state["questionnaire_partner_name"],
      #       st.session_state["questionnaire_wishes"]
      # ]

      # worksheet.append_row(values=values)
      st.success("Анкета отправлена")


def read_data(source: Literal["users", "guests", "guests_expanded", "contents"], is_template=False):
      if source == "guests_expanded":
            query = textwrap.dedent(f"""
                  SELECT
                        g.id,
                        g.guest_id,
                        CONCAT(ug.last_name, ' ', ug.first_name, ' ', ug.middle_name) AS guest_name,
                        g.partner_id,
                        CONCAT(up.last_name, ' ', up.first_name, ' ', up.middle_name) AS partner_name,
                        g.note,
                        ug.phone AS guest_phone,
                        ug.telegram AS guest_telegram,
                        g.invitation_link,
                        g.invitation_sent,
                        g.responded_at,
                        g.will_come,
                        g.wishes
                  FROM 
                        public.guests g 
                        LEFT JOIN public.users ug ON ug.id = g.guest_id
                        LEFT JOIN public.users up ON up.id = g.partner_id
            """)
      else:
            query = textwrap.dedent(f"""
                  SELECT *
                  FROM public.{source}
                  {"WHERE role != 'admin'" if source == "users" else ""}
                  {"LIMIT 0" if is_template else ""};
            """)

      return st_conn.query(
            sql=query,
            ttl=1,
            show_spinner=False
      )


def update_record(target, set_list, id):
      query = textwrap.dedent(f"""
            UPDATE public.{target}
            SET {", ".join(set_list)}
            WHERE id = {id};
      """)


      try:
            with psycopg2.connect(**db_config) as conn:
                  with conn.cursor() as cur:
                        cur.execute(query)
                  
                  conn.commit()
                  LOG.info(f"✅ Update was successful - {target} - id : {id}")
      except Exception as e:
            st.warning(f"❌ Error when updating {target}: {e}")


def insert_record(target: str, columns: list, values: list):
      query = textwrap.dedent(f"""
            INSERT INTO public.{target} ({", ".join(columns)})
            VALUES ({", ".join(values)});
      """)


      try:
            with psycopg2.connect(**db_config) as conn:
                  with conn.cursor() as cur:
                        cur.execute(query)
                  
                  conn.commit()
                  LOG.info(f"✅ Data insertion was successful - {target} - {columns} : {values}")
      except Exception as e:
            st.warning(f"❌ Error when updating {target}: {e}")


def delete_record(target, id):
      query = textwrap.dedent(f"""
            DELETE FROM public.{target}
            WHERE id = {id};
      """)


      try:
            with psycopg2.connect(**db_config) as conn:
                  with conn.cursor() as cur:
                        cur.execute(query)
                  
                  conn.commit()
                  LOG.info(f"✅ Deletion was successful - {target} - id : {id}")
      except Exception as e:
            st.warning(f"❌ Error when updating {target}: {e}")


def save_changes(target: Literal["users", "guests", "contents"], data: pd.DataFrame):
      """
      data: original data
      """

      # read data from session state
      to_update = st.session_state[f"{target}-data"]["edited_rows"]
      to_insert = st.session_state[f"{target}-data"]["added_rows"]
      to_delete = st.session_state[f"{target}-data"]["deleted_rows"]


      if not (to_update or to_insert or to_delete):
            st.warning("Нет изменений")
            return


      # update records
      for i in to_update:
            id = data.loc[i, "id"]
            set_list = [
                  f"{key}={"'" + value + "'" if isinstance(value, str) else value}"
                  for key, value in to_update[i].items()
            ]
            update_record(target, set_list, id)
      

      # insert records
      for record in to_insert:
            if not record:
                  continue

            columns = [key for key in record]
            values = [f"'{value}'" if isinstance(value, str) else value for value in record.values()]
            insert_record(target, columns, values)


      # delete records
      for i in to_delete:
            id = data.loc[i, "id"]
            delete_record(target, id)


      st.toast("Изменения сохранены", icon="🎉")


def validate_token(token: str, role: Literal["admin", "guest"]):
      if role == "admin":
            return token == st.secrets.constants.token["admin"]
