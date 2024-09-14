import streamlit as st
import gspread

# link to test GSheet >> https://docs.google.com/spreadsheets/d/1WX-4NFs_ITvGuDNWMkODbS2_ZISG6SFjhx-Mg4dezr0/edit?usp=sharing

# Following instructions from >> https://docs.gspread.org/en/v6.1.2/oauth2.html#enable-api-access
#   Relevant project set-up on Google Developers Console >> https://console.cloud.google.com/apis/credentials?project=opportune-geode-435020-g8
#   Generated API Key from above project >> AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY




gApiKey = gspread.api_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

public_sheet = gApiKey.open_by_url('https://docs.google.com/spreadsheets/d/1WX-4NFs_ITvGuDNWMkODbS2_ZISG6SFjhx-Mg4dezr0/edit?usp=sharing')

# sh = gc.open_by_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

cellContents = (public_sheet.sheet1.get('B3'))




# val = worksheet.acell('B1').value

st.title("Web App Title")
st.write(
    "Write stuff here . . ."
)

st.write(cellContents as str)

