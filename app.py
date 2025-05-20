import streamlit as st
from datetime import datetime, timedelta
import pytz

st.set_page_config(page_title="EST ↔ IST Visual Time Converter", layout="centered")

# Inject CSS + JS styled slider
st.markdown(f"""
<style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}

    .slider-container {{
        position: relative;
        width: 100%;
        margin: 50px 0;
    }}

    .time-scale {{
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: {text_color};
    }}

    input[type=range] {{
        width: 100%;
        -webkit-appearance: none;
        height: 15px;
        background: linear-gradient(to right, {thumb_color} 0%, {thumb_color} 100%);
        border-radius: 5px;
        outline: none;
    }}

    input[type=range]::-webkit-slider-thumb {{
        -webkit-appearance: none;
        appearance: none;
        width: 40px;
        height: 40px;
        background: {thumb_color};
        border-radius: 50%;
        cursor: pointer;
        transition: background 0.3s ease-in-out;
    }}

    .converted-time {{
        font-size: 1.8rem;
        margin-top: 30px;
        font-weight: 600;
        color: {text_color};
    }}

    .date-info {{
        font-size: 14px;
        color: gray;
        margin-top: -10px;
    }}
</style>

<div class="slider-container">
    <div class="time-scale">
        <span>12 AM</span><span>3 AM</span><span>6 AM</span><span>9 AM</span><span>12 PM</span><span>3 PM</span><span>6 PM</span><span>9 PM</span><span>11 PM</span>
    </div>
    <input type="range" min="0" max="23" value="12" id="hourSlider" oninput="updateISTTime(this.value)">
</div>

<div class="converted-time" id="istTime">IST: 9:30 PM</div>
<div class="date-info" id="dateToday">{datetime.now().strftime("%A, %d %B %Y")}</div>

<script>
    function updateISTTime(hourEST) {{
        const estTime = new Date();
        estTime.setHours(hourEST);
        estTime.setMinutes(0);
        estTime.setSeconds(0);

        const utcTime = estTime.getTime() + (5 * 60 * 60 + 30 * 60) * 1000; // EST → IST offset
        const istTime = new Date(utcTime);

        let hours = istTime.getHours();
        let ampm = hours >= 12 ? 'PM' : 'AM';
        let hour12 = hours % 12;
        hour12 = hour12 ? hour12 : 12;

        const timeString = `IST: ${hour12}:00 ${ampm}`;
        document.getElementById("istTime").innerText = timeString;
    }}
</script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aarav Shah</p>", unsafe_allow_html=True)
