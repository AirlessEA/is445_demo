# INSTRUCTIONS:
# 1. Open a "Terminal" by: View --> Terminal OR just the "Terminal" through the hamburger menu
# 2. run in terminal with: streamlit run streamlit_app.py
# 3. click the "Open in Browser" link that pops up OR click on "Ports" and copy the URL
# 4. Open a Simple Browswer with View --> Command Palette --> Simple Browser: Show
# 5. use the URL from prior steps as intput into this simple browser


import streamlit as st
import altair as alt
 
st.title('Streamlit App for IS445: ID5662')

st.text("The URL for this app is: https://is445demo-fcu4etl5btv9xwd5vwjq5r.streamlit.app/")
st.text("The URL for its GitHub repo is: https://github.com/AirlessEA/is445_demo")

alt.X("monthdate(date):T", title="Date (Month Year)"),

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather - 2001 to 2006")