import streamlit as st


def render():
      left, right = st.columns([1.1, 1], vertical_alignment="top")

      with left:
            st.markdown(
                  unsafe_allow_html=True,
                  body=f"""
                  <div class="title">
                        <h1>Мы женимся!</h1>
                        <h4>19 октября 2025 года</h4>
                        <h1>👰🏻🤵🏻</h1>
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
                        И хотим пригласить <span style='color: #B76E79;'>тебя</span> разделить с нами радость от этого события
                  </h3>
                  <h3>
                        🪩🫧🍸🤍🥂🫧✧˖°
                  </h3>
            </div>
            """
      )