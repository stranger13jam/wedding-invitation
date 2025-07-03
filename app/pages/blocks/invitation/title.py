import streamlit as st

from utils import read_data


def render():
      # config = read_data(source="config")

      # title = config.loc[config.code == "title", "value"].values[0]
      # date = config.loc[config.code == "date", "value"].values[0]
      # title_emoji = config.loc[config.code == "title_emoji", "value"].values[0]

      # invitation_start = config.loc[config.code == "invitation_start", "value"].values[0]
      # invitation_end = config.loc[config.code == "invitation_end", "value"].values[0]
      # invitation_plural = config.loc[config.code == "invitation_plural", "value"].values[0]
      # invitation_single = config.loc[config.code == "invitation_single", "value"].values[0]
      # invitation_emoji = config.loc[config.code == "invitation_emoji", "value"].values[0]

      title = "Мы женимся!"
      date = "19 октября 2025 года"
      title_emoji = "👰🏻🤵🏻"

      invitation_start = "И хотим пригласить"
      invitation_end = "разделить с нами радость от этого события."
      invitation_plural = "вас"
      invitation_single = "тебя"
      invitation_emoji = "🪩🫧🍸🤍🥂🫧✧˖°"

      left, right = st.columns([1.1, 1], vertical_alignment="top")

      with left:
            st.markdown(
                  unsafe_allow_html=True,
                  body=f"""
                  <div class="title">
                        <h1>{title}</h1>
                        <h4>{date}</h4>
                        <h1>{title_emoji}</h1>
                  </div>
                  """
            )
      with right:
            st.image(image="app/assets/photo.JPG")


      st.markdown(
            unsafe_allow_html=True,
            body=f"""
            <div class="title">
            <h3>
            {invitation_start if invitation_start else ""}
            {
                  "<span style='color: #B76E79;'>" + (
                        invitation_plural
                        if "guest" in st.session_state and st.session_state.guest["name"] and st.session_state.guest["partner_name"]
                        else invitation_single
                  ) + "</span>"
                  if invitation_plural and invitation_single
                  else ""
            }
            {invitation_end if invitation_end else ""}
            {"<div>" + invitation_emoji + "</div>" if invitation_emoji else ""}
            </h3>
            </div>
            """
      )

      # <h3>
                  #       {invitation_start}
                  #       <span style="color: #B76E79;">
                  #             {
                  #                   invitation_plural
                  #                   if "guest" in st.session_state and st.session_state.guest["name"] and st.session_state.guest["partner_name"]
                  #                   else invitation_single
                  #             }
                  #       </span>
                  #       {invitation_end}
                  # </h3>
                  # <h3>{invitation_emoji if invitation_emoji else ""}</h3>

      # st.markdown('<div class="title">', unsafe_allow_html=True)

      # if invitation_emoji:
      #       st.markdown(f"<h3 class='title'>{invitation_emoji}</h3>", unsafe_allow_html=True)

      # st.markdown("</div>", unsafe_allow_html=True)