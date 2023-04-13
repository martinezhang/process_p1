import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gdown

# Setting the title of the Streamlit app
st.title('Uber Data Analysis - April 2014')

url = "https://drive.google.com/uc?id=1qoK_zLLWWPjY3HaPN4WXH2q1OayJiQtz"
gdown.download(url, "uber-raw-data-apr14.csv", quiet=False)

# Reading the csv file into a pandas dataframe
path = "uber-raw-data-apr14.csv"
df = pd.read_csv(path, delimiter = ',')

# Previewing the first 5 rows of the dataframe
st.subheader('Preview of the dataset')
st.write(df.head())

# Previewing the last 5 rows of the dataframe
st.subheader('Last few rows of the dataset')
st.write(df.tail())

# Transforming the 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Creating a function for finding the day of the month
def get_dom(dt):
    return dt.day

# Adding a new column with the day of the month
df['dom'] = df['Date/Time'].map(get_dom)

# Creating a function for finding the weekday and hours
def get_weekday(dt):
    return dt.weekday()

# Adding a new column with the weekday
df['weekday'] = df['Date/Time'].map(get_weekday)

# Adding a new column with the hour of the day
df['hour'] = df['Date/Time'].dt.hour

# Analyzing the day of month
st.subheader('Frequency by Day of the Month')
hist_values = np.histogram(df['dom'], bins=30, range=(0.5, 30.5))[0]
st.bar_chart(hist_values)

# Analyzing the weekday
st.subheader('Frequency by Weekday')
hist_values = np.histogram(df['weekday'], bins=7, range=(-0.5, 6.5))[0]
st.bar_chart(hist_values)

# Analyzing the hour of the day
st.subheader('Frequency by Hour of the Day')
hist_values = np.histogram(df['hour'], bins=24, range=(0, 24))[0]
st.line_chart(hist_values)
