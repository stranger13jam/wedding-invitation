import streamlit as st


def render():
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