import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gdown

# Set page configuration
st.set_page_config(page_title="My Streamlit App", page_icon=":cat:")

# Setting the title of the Streamlit app
st.title('Uber Data Analysis - April 2014')

url = "https://drive.google.com/uc?id=1qoK_zLLWWPjY3HaPN4WXH2q1OayJiQtz"
gdown.download(url, "uber-raw-data-apr14.csv", quiet=False)

# Reading the csv file into a pandas 
path = "uber-raw-data-apr14.csv"
df = pd.read_csv(path, delimiter = ',')

# Previewing the first 5 rows of the 
st.subheader('Preview of the dataset')
st.write(df.head())

# Previewing the last 5 rows of the 
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

# Setting the title of the Streamlit app
st.title("Creating a function for finding the day of the month example: def get_dom(dt): return dt.day data['dom'] = data['Date/Time'].map(get_dom)")

# Defining a function to extract the day of the month from a datetime object
def get_dom(dt):
    return dt.day

# Adding a new column to the  with the day of the month
df['day'] = df['Date/Time'].map(get_dom)

# Displaying the first 5 rows of the 
st.write('First 5 rows of the :')
st.write(df.head())

# Displaying the summary statistics for the 
st.write('Summary statistics for the :')
st.write(df.describe())

# Setting the title of the Streamlit app
st.title("Creating a function for finding the weekday and hours example: def get_weekday(dt): return dt.weekday() data['weekday']= data['Date/Time'].map(get_weekday")

# Defining a function to extract the weekday from a datetime object
def get_weekday(dt):
    return dt.weekday()

# Adding a new column to the  with the weekday
df['weekday'] = df['Date/Time'].map(get_weekday)

# Setting the title of the Streamlit app
st.title('Create a function for extracting the hours from the Date/Time')

# Defining a function to extract the hour from a datetime object
def get_hour(dt):
    return dt.hour

# Adding a new column to the  with the hour of the day
df['hour'] = df['Date/Time'].map(get_hour)

# Displaying the first 5 rows of the 
st.write(df.head())

# Displaying the descriptive statistics of the 
st.write(df.describe())

# Displaying the information about the , including the column data types and memory usage
st.write(df.info())

# Creating a histogram of the 'day' column with 30 bins and a width of 0.8
hist = df["day"].plot.hist(bins=30, rwidth=0.8, range=(0.5, 30.5), title="Frequency by DoM - Uber - April 2014")
plt.xlabel('Days of the month')

# Displaying the histogram using Streamlit's 'pyplot' method
st.pyplot()

# Setting the title of the Streamlit app
st.title('Creating a function for Grouping the data by date of month (dom) example: def count_rows(rows): return len(rows)')

# Convert the Date/Time column to datetime format using pandas to_datetime() method
df['Date/Time'] = df['Date/Time'].map(pd.to_datetime)

# Add new columns for day, weekday, and hour
def get_dom(dt):
    return dt.day #.day is an attribute

def get_weekday(dt):
    return dt.weekday() #.weekday() is a method

def get_hour(dt):
    return dt.hour #.hour is an attribute

df['day'] = df['Date/Time'].map(get_dom)
df['weekday']= df['Date/Time'].map(get_weekday)
df['hour'] = df['Date/Time'].map(get_hour)

# Group the data by day and count the number of rows
def count_rows(rows):
    return len(rows)

by_date = df.groupby('day').apply(count_rows)

# Line plot - Frequency by DoM
st.title("Line plot - Uber - April 2014")
st.line_chart(by_date)

# Bar chart - Frequency by DoM
st.title("Bar chart - Uber - April 2014")
plt.figure(figsize = (25, 15))
plt.bar(range(1, 31), by_date.sort_values())
plt.xticks(range(1, 31), by_date.sort_values().index)
plt.xlabel('Date of the month', fontsize=20)
plt.ylabel('Frequency', fontsize=20)
plt.title('Frequency by DoM - Uber - April 2014', fontsize=20)
st.pyplot()

# Histogram - Frequency by Hour
st.title("Histogram - Frequency by Hour - Uber - April 2014")
plt.hist(df.hour, bins=24, range = (-0.5, 24))
plt.xlabel('Hour of the day')
plt.ylabel('Frequency')
plt.title('Frequency by Hour - Uber - April 2014')
st.pyplot()

# Histogram - Frequency by Weekday
st.title("Histogram - Frequency by Weekday - Uber - April 2014")
plt.hist(df.weekday, bins=7, rwidth=0.8, range=(-0.5, 6.5))
plt.xlabel('Day of the week')
plt.ylabel('Frequency')
plt.title('Frequency by Weekday - Uber - April 2014')
st.pyplot()

# Histogram - Frequency by Weekday and Hour
df2 = df.groupby(['weekday', 'hour']).apply(count_rows).unstack()
st.subheader("Group the data by weekday and hour using .apply(count_rows).unstack()")
st.write(df2)

# Setting the title of the Streamlit app
st.title('Create heatmap using seaborn.heatmap for the grouped data')

# Add weekday column
df['weekday'] = df['Date/Time'].dt.weekday

# create heatmap using seaborn
heatmap = sns.heatmap(df2, linewidths = .5)
# customize heatmap
plt.title('Heatmap by Hour and weekdays - Uber - April 2014',fontsize=15)
heatmap.set_yticklabels(('Mar Mer Jeu Ven Sam Dim Lun').split(), rotation='horizontal')

# display heatmap using Streamlit
st.pyplot()

# Create a histogram of latitude values
plt.hist(df['Lat'], bins=100, range=(40.5, 41), color='r', alpha=0.5, label='Latitude')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.title('Latitude - Uber - April 2014')
st.pyplot()

# Create a histogram of longitude values
plt.hist(df['Lon'], bins=100, range=(-74.1, -73.9), color='g', alpha=0.5, label='Longitude')
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.title('Longitude - Uber - April 2014')
st.pyplot()

# Create a scatter plot of latitude and longitude
plt.figure(figsize=(10, 10), dpi=100)
plt.title('Longitude and Latitude distribution - Uber - April 2014', fontsize=15)
plt.hist(df['Lon'], bins=100, range=(-74.1, -73.9), color='g', alpha=0.5, label='Longitude')
plt.legend(loc='best')
plt.twiny()
plt.hist(df['Lat'], bins=100, range=(40.5, 41), color='r', alpha=0.5, label='Latitude')
plt.legend(loc='upper left')
st.pyplot()

# Create a scatter plot of latitude and longitude colored by weekday
plt.figure(figsize=(15, 15), dpi=100)
plt.title('Scatter plot - Uber - April 2014')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(df['Lat'], df['Lon'], s=0.8, alpha=0.4)
plt.ylim(-74.1, -73.8)
plt.xlim(40.7, 40.9)
st.pyplot()

# Create a scatter plot of latitude and longitude colored by weekday
dico = {0: 'yellow', 1: 'yellow', 2: 'blue', 3: 'yellow', 4: 'yellow', 5: 'yellow', 6: 'yellow'}
plt.figure(figsize=(15, 15), dpi=100)
plt.title('Scatter Plot - Uber - April 2014')
x = df["Lat"]
y = df["Lon"]
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.scatter(x, y, s=0.7, alpha=0.4, c=df["weekday"].map(dico))
plt.ylim(-74.1, -73.8)
plt.xlim(40.7, 40.9)
st.pyplot()

import pydeck as pdk

DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
LAND_COVER = [[[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]]
INITIAL_VIEW_STATE = pdk.ViewState(latitude=49.254, longitude=-123.13, zoom=11, max_zoom=16, pitch=45, bearing=0)

polygon = pdk.Layer(
    "PolygonLayer",
    LAND_COVER,
    stroked=False,
    # processes the data as a flat longitude-latitude pair:
    get_polygon="-",
    get_fill_color=[0, 0, 0, 20],
)

geojson = pdk.Layer(
    "GeoJsonLayer",
    DATA_URL,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation="properties.valuePerSqm / 20",
    get_fill_color="[255, 255, properties.growth * 255]",
    get_line_color=[255, 255, 255],
)

deck = pdk.Deck(layers=[polygon, geojson], initial_view_state=INITIAL_VIEW_STATE)

st.pydeck_chart(pdk_st.pydeck_to_json(deck))
