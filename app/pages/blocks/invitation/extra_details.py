import streamlit as st



def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <div class="title">
                  <h1>Детали</h1>
                  <div>
                        Здесь будут какие-то детали по нашему мероприятию.
                  </div>
            </div>
            """
      )