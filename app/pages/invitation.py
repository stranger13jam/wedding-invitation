from streamlit_extras.let_it_rain import rain

from pages.greeting import welcome
from pages.blocks.invitation import title, countdown, details, schedule, dresscode, extra_details, questionnaire, contacts


# welcome()


title.render()
countdown.render()
details.render()
schedule.render()
dresscode.render()
extra_details.render()
questionnaire.render()
contacts.render()


rain(
      emoji="❤️",
      font_size=40,
      falling_speed=10,
      animation_length="infinite",
)