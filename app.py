import streamlit as st
from datetime import datetime, timedelta
import pytz

# Streamlit page config
st.set_page_config(page_title="EST ↔ IST Time Converter", layout="centered")

# Theme selection
theme = st.radio("Choose Theme", ["Light", "Dark"], horizontal=True)

# Theme-dependent styling
if theme == "Dark":
    bg_color = "#0e1117"
    text_color = "#f5f5f5"
    thumb_color = "#1f77b4"
    slider_track = "#444"
else:
    bg_color = "#ffffff"
    text_color = "#000000"
    thumb_color = "#007acc"
    slider_track = "#ddd"

# Inject HTML/CSS/JS for custom UI
st.markdown(f"""
<style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .slider-container {{
        margin-top: 40px;
    }}
    .time-scale {{
        display: flex;
        justify-content: space-between;
        color: {text_color};
        font-size: 13px;
        margin-bottom: 10px;
    }}
    input[type=range] {{
        -webkit-appearance: none;
        width: 100%;
        height: 10px;
        background: {slider_track};
        border-radius: 5px;
        outline: none;
    }}
    input[type=range]::-webkit-slider-thumb {{
        -webkit-appearance: none;
        appearance: none;
        width: 32px;
        height: 32px;
        background: {thumb_color};
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 0 5px rgba(0,0,0,0.2);
    }}
    .converted-time {{
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 25px;
        color: {text_color};
    }}
    .date-label {{
        font-size: 13px;
        color: gray;
        margin-top: -8px;
    }}
</style>

<div class="slider-container">
    <div class="time-scale">
        <span>12 AM</span><span>3 AM</span><span>6 AM</span><span>9 AM</span>
        <span>12 PM</span><span>3 PM</span><span>6 PM</span><span>9 PM</span><span>11 PM</span>
    </div>
    <input type="range" min="0" max="23" value="12" id="hourSlider" oninput="updateIST(this.value)">
</div>

<div class="converted-time" id="istTime">IST: 9:30 PM</div>
<div class="date-label" id="dateLabel">{datetime.now().strftime("%A, %d %B %Y")}</div>

<script>
    function updateIST(hourEST) {{
        const offset = 10.5; // IST is UTC+5:30, EST is UTC-5 (so 10.5 hours difference)
        const istHour = (parseInt(hourEST) + offset) % 24;
        const istFormatted = formatHour(istHour);
        document.getElementById("istTime").innerText = `IST: ` + istFormatted;
    }}

    function formatHour(hour) {{
        const hourInt = parseInt(hour);
        const ampm = hourInt >= 12 ? 'PM' : 'AM';
        let hr = hourInt % 12;
        hr = hr === 0 ? 12 : hr;
        return hr + ":00 " + ampm;
    }}
</script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aarav Shah</p>", unsafe_allow_html=True)
