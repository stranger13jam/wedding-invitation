import streamlit as st

import pandas as pd


LATITUDE = 55.876142
LONGITUDE = 37.436041


def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <h1 class="title">
                  Где и когда
            </h1>
            """
      )


      left, center, right = st.columns([8, 1, 5], vertical_alignment="center")

      df = pd.DataFrame({
            "latitude": [LATITUDE],
            "longitude": [LONGITUDE],
      })

      with left:
            st.map(data=df, zoom=11, size=11)

      with right:
            html_details = f"""
            <div style="line-height: 1.7;">
                  <strong style="color: #b76e79; font-weight: bold;">Усадьба «Лесной берег»</strong>
                  <br>
                  <strong>Адрес</strong>: город Москва, улица Свободы, дом 78Б, строение 1
                  <br>
                  <strong>Координаты</strong>: {LATITUDE}, {LONGITUDE}
            </div>
            """
            
            html_calendar = """
            <table class="calendar">
                  <caption>Октябрь 2025</caption>
                  <tr>
                        <th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Вс</th>
                  </tr>
                  <tr>
                        <td class="empty"></td><td class="empty"></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td>
                  </tr>
                  <tr>
                        <td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td>
                  </tr>
                  <tr>
                        <td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td class="highlight">19</td>
                  </tr>
                  <tr>
                        <td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td>
                  </tr>
                  <tr>
                        <td>27</td><td>28</td><td>29</td><td>30</td><td>31</td><td class="empty"></td><td class="empty"></td>
                  </tr>
            </table>
            """

            st.markdown(html_details, unsafe_allow_html=True)
            st.html("<div></div>")
            st.link_button(
                  label="Как проехать",
                  url="https://yandex.ru/maps/-/CHgeN28N",
                  type="primary"
            )

            st.markdown(html_calendar, unsafe_allow_html=True)
            st.caption("19 октября 2025 года - сохраняем дату")