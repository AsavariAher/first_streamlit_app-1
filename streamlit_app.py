import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build Your Own Fruit Smoothie')

import pandas 
from urllib.error import URLError

@streamlit.cache
def get_data():
    dataframe = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    return dataframe.set_index("Fruit")

try:
    dataframe = get_data()
    fruits_selected = streamlit.multiselect(
        "Select some fruits for your smoothie", list(dataframe.index), ["Strawberries", "Banana"]
    )
    if not fruits_selected:
        streamlit.error("Please select at least one fruit.")
    else:
        dataset = dataframe.loc[fruits_selected]
        streamlit.write("### Fruits Selected:", dataset.sort_index())

        dataset = dataset.T.reset_index()
        dataset = pandas.melt(dataset, id_vars=["index"]).rename(
            columns={"index": "Calories", "value": "Fruits"}
        )

except URLError as e:
    streamlit.error(
        """
        **Something went wrong.**

        Connection error: %s
    """
        % e.reason
    )

