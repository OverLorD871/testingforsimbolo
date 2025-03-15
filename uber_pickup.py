import streamlit as st
import numpy as np
import pandas as pd

st.title("Uber Pickups in NWY")

data_column = 'date/time'
data_url = r'E:\Simbolo Ai class\uber-raw-data-sep14.csv'

@st.cache_data
# avoid mutation "output" like this : "st.cache_data()".

def load_data(nrows):
    data = pd.read_csv(data_url, nrows = nrows)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis = 'columns', inplace = True)
    data[data_column] = pd.to_datetime(data[data_column])
    return data

data_load_state = st.text('Done! (using st.cache_data)')
data = load_data(10000)
data_load_state = st.text('Loading data... Done !')

# st.subheader('Raw Data')
# st.dataframe(data)
# #can use "st.write" but "st.dataframe()" is more standard.

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Histogram: Number of Pickups by hours')
hist_values = np.histogram(data[data_column].dt.hour, bins = 24, range = (0,24))[0]

st.bar_chart(hist_values) # to draw histogram use "st.bar_chart()"

# st.subheader('Map of all pickups')
# st.map(data)

# hour_to_filter=4
# filtered_data = data[data[data_column].dt.hour == hour_to_filter]
# st.subheader(f'Map of all Pickups at {hour_to_filter}:00')
# st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17) # min: 0h, max: 23h, default: 17h
filtered_data = data[data[data_column].dt.hour == hour_to_filter]
st.subheader(f'Map of all Pickups at {hour_to_filter}:00')
st.map(filtered_data)