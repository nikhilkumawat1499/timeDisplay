import streamlit as st
from PIL import Image
import datetime
import time

def main():
    st.title("Fancy Current Time Display")
    
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

    # Display the current time in a black box
    time_placeholder = st.empty()
    # Display Shinchan dancing GIF
    st.image(
            "shinchan.webp", # I prefer to load the GIFs using GIPHY
            width=400, # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_placeholder.markdown(f'<div class="time-box"><p class="time-display">{current_time}</p></div>', unsafe_allow_html=True)
        time.sleep(1)


if __name__ == "__main__":
    main()


