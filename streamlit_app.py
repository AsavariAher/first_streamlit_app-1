import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas
@st.cache
df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/smew/country_code_to_currency_code.csv")
return df.set_index("Country")


    

