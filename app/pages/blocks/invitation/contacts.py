import streamlit as st


def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <h1 class="title">
                  Контакты
            </h1>
            """
      )

      st.markdown(
            unsafe_allow_html=True,
            body="""
            <div class="title">
                  <caption>Вы всегда можете связаться с нами, чтобы задать вопросы, не терпящие отлагательств, или позвать на чашечку чая:</caption>
            </div>
            """
      )

      contacts = [
            {"name": "Аня", "phone": "+7 916 388 02 33", "tg_link": "https://t.me/annajkf"},
            {"name": "Лёша", "phone": "+7 999 863 32 49", "tg_link": "https://t.me/stranger13jam"}
      ]

      for i, contact in enumerate(contacts):
            st.markdown(
                  unsafe_allow_html=True,
                  body=f"""
                  <div class="contacts-row">
                        <div class="info">
                              <div class="name">{contact["name"]}</div>
                              <div class="phone">{contact["phone"]}</div>
                        </div>
                        <div class="actions">
                              <a href={contact["tg_link"]} target="_blank" title="">
                                    <svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="120" cy="120" r="120" fill="#0088cc"/>
                                    <path d="M179.8 73.7L53.7 122.4c-2.6 1-2.4 4.9 0.3 5.6l31.3 8.3 12 39.7c0.7 2.3 3.6 3.1 5.5 1.6l17.1-14 35.7 26.3c2.1 1.6 5.1 0.4 5.7-2.2l22.3-105.7c0.5-2.4-1.8-4.4-4.3-3.7z" fill="#fff"/>
                                    </svg>
                              </a>
                        </div>
                  </div>
                  """
            )
