import streamlit as st
import pandas as pd
import time 
from datetime import datetime
import os

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")


file_path = os.path.join("dtr", "Attendance", "Attendance_" + date + ".csv")

# Try to read the CSV file
try:
    df = pd.read_csv(file_path)
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    # If the file is not found, create an empty DataFrame
    df = pd.DataFrame(columns=["NAME", "TIME"])  # Add appropriate column names
    st.warning(f"No attendance file found for {date}.\nAn empty DataFrame is displayed.")