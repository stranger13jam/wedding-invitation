import streamlit as st


def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <h1 class="title">
                  Дресс-код
            </h1>
            """
      )

      colors = [
            {"code": "#e6d3c4", "name": "Бежевый"},
            {"code": "#f2e8df", "name": "Молочный"},
            {"code": "#c9b7ad", "name": "Пудровый"},
            {"code": "#d8c0a8", "name": "Кофейный"},
            {"code": "#faf5f0", "name": "Светлый розовый"},
            {"code": "#e5ccc1", "name": "Карамель"},
            {"code": "#e6d3c4", "name": "Бежевый"},
            {"code": "#f2e8df", "name": "Молочный"},
            {"code": "#c9b7ad", "name": "Пудровый"},
            {"code": "#d8c0a8", "name": "Кофейный"},
            {"code": "#faf5f0", "name": "Светлый розовый"},
            {"code": "#e5ccc1", "name": "Карамель"}
      ]

      html_dresscode = ""
      html_dresscode += '<div class="dresscode">'
      html_dresscode += '<div class="dresscode-colors-list">'

      for i, color in enumerate(colors):
            html_dresscode += '<div class="dresscode-color-item">'
            html_dresscode += f'<div class="dresscode-color-circle" style="background-color: {color["code"]};"></div>'
            html_dresscode += color["name"]
            html_dresscode += '</div>'

      html_dresscode += '</div>'
      html_dresscode += '</div>'

      st.markdown(
            unsafe_allow_html=True,
            body="""
            <div class="title">
                  Наш дресс-код в пастельных тонах.
                  Просим воздержаться от белого, чёрного и красного цветов.
                  <br/>
                  А ниже - цветовая гамма для вдохновения.
            </div>
            """
      )
      st.markdown(html_dresscode, unsafe_allow_html=True)
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <div class="title">
                  Но самое главное - прихватите с собой хорошее настроение!
            </div>
            """
      )