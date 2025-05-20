import streamlit as st
from datetime import datetime, timedelta
import pytz

st.set_page_config(page_title="EST ↔ IST Time Converter", layout="centered")

# --- UI Styling (Optional but clean)
st.markdown("""
    <style>
        .time-block {
            font-size: 1.5rem;
            font-weight: 600;
            padding: 10px;
            background-color: #f0f2f6;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🕒 EST ↔ IST Time Converter")

# --- Time Picker (Slider Style)
st.subheader("Select Time in EST (US Eastern Time)")

selected_hour = st.slider("Hour (EST)", min_value=0, max_value=23, value=12)
selected_minute = st.slider("Minute (EST)", min_value=0, max_value=59, value=0)

# --- Timezone conversion
est = pytz.timezone("US/Eastern")
ist = pytz.timezone("Asia/Kolkata")

now = datetime.now()
base_est_time = est.localize(datetime(now.year, now.month, now.day, selected_hour, selected_minute))
converted_ist_time = base_est_time.astimezone(ist)

# --- Display
st.markdown("<div class='time-block'>🗽 EST: {} (UTC{})</div>".format(
    base_est_time.strftime("%I:%M %p"), base_est_time.strftime("%z")), unsafe_allow_html=True)

st.markdown("<div class='time-block'>🇮🇳 IST: {} (UTC{})</div>".format(
    converted_ist_time.strftime("%I:%M %p"), converted_ist_time.strftime("%z")), unsafe_allow_html=True)

# --- Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aarav Shah</p>", unsafe_allow_html=True)
