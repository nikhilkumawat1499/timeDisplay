import streamlit as st
from PIL import Image
import datetime
import time
import pytz

def main():
    st.title("Genz time display, instead of looking at watch, just scan the QR code !!")
    
    # Center-align the title
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            font-size: 36px;
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Style for the time display box
    st.markdown(
        """
        <style>
        .time-box {
            background-color: #000000; /* black color */
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .time-display {
            font-size: 48px;
            color: #ffffff; /* white color for text inside the box */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

     # Display the current time and date in a black box
    time_date_placeholder = st.empty()
    # Display Shinchan dancing GIF
    st.image(
            "shinchan.webp", # I prefer to load the GIFs using GIPHY
            width=400, # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )
    while True:
        ist = pytz.timezone('Asia/Kolkata')
        current_datetime = datetime.datetime.now(ist)
        current_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        current_day = current_datetime.strftime("%A")
        current_date = current_datetime.strftime("%d %B %Y")
        display_content = f'<div class="time-box"><p class="time-display">Day: {current_day}</p><p class="time-display">Date: {current_date}</p><p class="time-display">Time: {current_time}</p></div>'
        time_date_placeholder.markdown(display_content, unsafe_allow_html=True)
        time.sleep(1)


if __name__ == "__main__":
    main()


