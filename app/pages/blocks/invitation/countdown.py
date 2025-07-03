import streamlit as st

from datetime import datetime
import pytz

msk_tz = pytz.timezone("Europe/Moscow")
event_date = datetime(2025, 10, 19, 14, 0, 0, tzinfo=msk_tz)


@st.fragment(run_every="1s")
def render():
      st.markdown(
            unsafe_allow_html=True,
            body=f"""
            <h1 class="title">
                  До свадьбы осталось
            </h1>
            """
      )

      # timer calculation starts
      now = datetime.now(tz=msk_tz)
      remaining = event_date - now

      days = remaining.days
      hours, rem = divmod(remaining.seconds, 3600)
      minutes, seconds = divmod(rem, 60)
      # timer calculation ends


      html_countdown = f"""
      <div class="countdown-timer">
            <div>
                  <div class="time-unit">{days}</div>
                  <div class="time-unit-label">дней</div>
            </div>
            <div>
                  <div class="time-unit">{hours:02}</div>
                  <div class="time-unit-label">часов</div>
            </div>
            <div>
                  <div class="time-unit">{minutes:02}</div>
                  <div class="time-unit-label">минут</div>
            </div>
            <div>
                  <div class="time-unit">{seconds:02}</div>
                  <div class="time-unit-label">секунд</div>
            </div>
      </div>
      """

      st.markdown(html_countdown, unsafe_allow_html=True)

