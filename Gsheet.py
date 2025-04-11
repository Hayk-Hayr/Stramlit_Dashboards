import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px

# Set up scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Looker Studio Dataset").worksheet("ATM_transaction_dataset")

# Load data into a DataFrame
data = pd.DataFrame(sheet.get_all_records())

# Display in Streamlit
st.title("📊 Google Sheets Streamlit Dashboard")
#st.dataframe(data)

data1 = data.groupby('ATM Name')['Card Type'].count().reset_index().rename(columns = {'Card Type' : "# of Transactions"})
bar = px.bar(data1, x='ATM Name', y='# of Transactions', title='Number of Transactions by ATM')
st.plotly_chart(bar)

radar = px.line_polar(data1, r = "# of Transactions", theta='ATM Name', line_close=True,  title='Health & Longevity Assessment Radar Chart')

st.plotly_chart(radar)

st.write(data1)