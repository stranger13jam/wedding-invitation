import streamlit as st


def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <h1 class="title">
                  План дня
            </h1>
            """
      )

      schedule = [
            {"time": "14:00", "icon": "🧑‍🤝‍🧑", "desc": "Сбор гостей"},
            {"time": "15:00", "icon": "💒", "desc": "Церемония"},
            {"time": "16:00", "icon": "🍽️", "desc": "Банкет"},
            {"time": "19:00", "icon": "🎉", "desc": "Вечеринка и танцы"},
            {"time": "22:00", "icon": "🌙", "desc": "Завершение вечера"}
      ]

      st.markdown('<div class="stepper">', unsafe_allow_html=True)

      for i, step in enumerate(schedule):
            st.markdown(
                  unsafe_allow_html=True,
                  body=f"""
                  <div class="step">
                        <div class="icon">{step["icon"]}</div>
                        <div class="time">{step["time"]}</div>
                        <div class="desc">{step["desc"]}</div>
                  </div>
                  """
            )

            if i < len(schedule) - 1:
                  st.markdown('<div class="stepper-divider"></div>', unsafe_allow_html=True)

      st.markdown("</div>", unsafe_allow_html=True)
