import streamlit 
streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favourites')
streamlit.text(' Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach & rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Fre-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
