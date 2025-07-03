import streamlit as st
from streamlit.components.v1 import iframe


def render():
      st.markdown(
            unsafe_allow_html=True,
            body="""
            <h1 class="title">
                  Анкета гостя
            </h1>
            """
      )

      
      # with st.form(key="questionnaire_form"):
      #       st.markdown(
      #             unsafe_allow_html=True,
      #             body="""
      #             <div class="title">
      #                   Пожалуйста, подтвердите своё присутствие на свадьбе <strong>до</strong>:
      #                   <h4>1 сентября 2025 г.</h4>
      #             </div>
      #             """
      #       )

      #       st.text_input(
      #             label="Имя и фамилия",
      #             placeholder="Введите ваше имя и фамилию",
      #             key="questionnaire_name"
      #       )

      #       st.radio(
      #             label="Вы будете на свадьбе?",
      #             options=["Да", "Нет"],
      #             format_func=lambda option: "Да, конечно" if option == "Да" else "Нет, к сожалению",
      #             index=0,
      #             key="questionnaire_will_come"
      #       )

      #       st.text_input(
      #             label="Имя и фамилия вашего партнера",
      #             placeholder="Введите имя и фамилию вашего партнера, если вы будете не один/не одна",
      #             key="questionnaire_partner_name"
      #       )

      #       st.text_area(
      #             label="Ваши пожелания или вопросы",
      #             placeholder="Напишите ваши пожелания или вопросы",
      #             key="questionnaire_wishes"
      #       )

      #       if st.form_submit_button(
      #             label="Отправить",
      #             type="primary",
      #             use_container_width=True
      #       ):
      #             if st.session_state["questionnaire_name"] and st.session_state["questionnaire_will_come"]:
      #                   # save_answer()
      #                   st.success("Анкета отправлена")
      #             else:
      #                   st.warning("Пожалуйста, укажите ваши имя и фамилию")


      iframe(
            src="https://docs.google.com/forms/d/e/1FAIpQLSey60ENX0HRIQNg0ZWG3ghQu0D5wF-We-lrITbR5IZVhZ9kaA/viewform?embedded=true",
            height=600,
            scrolling=True
      )
