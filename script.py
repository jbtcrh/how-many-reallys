import streamlit as st
import zoneinfo
import time
from datetime import datetime
from zoneinfo import ZoneInfo

st.title("So much")

tz_hers=ZoneInfo("Asia/Kolkata")
tz_his=ZoneInfo("Europe/Berlin")

time_between = (datetime.now(tz=tz_hers) - datetime(2025, 11, 21, 2, 30, tzinfo=tz_hers))
time_since = time_between.total_seconds() / 3600
days_since = time_between.days

message = "It's been a minute, my heart. Well, more than a minute. Just around __{days}__ days.".format(days=days_since)

really_scalar = 3 * (2**(time_since / 24))
# how_much = really_scalar * (1 + st.session_state.get("seasoning_input", 0) / 100)

def stream_message():
    for char in list(message):
        yield char
        time.sleep(0.03)

st.write(f"I really^({really_scalar:.2E}) like you.")
if st.button("Aren't you a curious thing?"):
    st.write_stream(stream_message)
    with st.popover("Still curious?"):
        st.write(f"In terms of hours, the series has been on for {time_since:.2f}!")
        with st.popover("More?"):
            st.write(f"{time_since*60:.0f} minutes and counting <3")
            with st.popover("Go ahead, let me disregard all good design practices."):
                st.write(f"That's {time_between.total_seconds():.2f} seconds of absolute *aboration*!")
    st.balloons()

# add seasoning but also add the ability to comment and store the pairs in a database, use a cache to calculate the value once per user session or on update
# st.number_input("Do you want to be greedy?", min_value=0, max_value=100, key="seasoning_input")

# st.snow()
