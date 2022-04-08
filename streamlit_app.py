import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build Your Own Fruit Smoothie')

import pandas 
import altair 

from urllib.error import URLError

@streamlit.cache
def get_data():
    dataframe = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    return dataframe.set_index("Fruit")

try:
    dataframe = get_data()
    bowlingredients = streamlit.multiselect(
        "Build Your Own Fruit Smoothie", list(dataframe.index), ["Apple", "Banana"]
    )
    if not bowlingredients:
        streamlit.error("Please select at least one fruit.")
    else:
        dataset = dataframe.loc[bowlingredients]
        #dataset /= 1000000.0
        streamlit.write("### Fruits in BYOB", dataset.sort_index())

        dataset = dataset.T.reset_index()
        dataset = pandas.melt(dataset, id_vars=["index"]).rename(
            columns={"index": "Calories", "value": "Fruits in BYOB"}
        )

except URLError as e:
    streamlit.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
    

