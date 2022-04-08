import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build Your Own Fruit Smoothie')

import pandas 
@streamlit.cache
def get_data():
    dataframe = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    return dataframe.set_index("Fruit")

try:
    dataframe = get_data()
    smoothiefruitschosen = streamlit.multiselect(
        "Select Fruits for Your Smoothie", list(dataframe.index), ["Apple", "Banana"]
    )
    if not bowlingredients:
        streamlit.error("It can't be a fruit smoothie if you don't pick a fruit.")
    else:
        dataset = dataframe.loc[smoothiefruitschosen]
        streamlit.write("### Fruits in Smoothie", dataset.sort_index())

        dataset = dataset.T.reset_index()
        dataset = pandas.melt(dataset, id_vars=["index"]).rename(
            columns={"index": "Calories", "value": "Fruits in Smoothie"}
        )

except URLError as e:
    streamlit.error(
        """
        **Something went wrong.**

        Connection error: %s
    """
        % e.reason
    )
    

