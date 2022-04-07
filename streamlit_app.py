import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')



import pandas 
import altair 

from urllib.error import URLError

@streamlit.cache
def get_data():
    dataframe = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    return dataframe.set_index("Calories")

try:
    dataframe = get_data()
    countries = streamlit.multiselect(
        "Choose ", list(dataframe.index), ["Avocado", "Grapes"]
    )
    if not countries:
        streamlit.error("Please select at least one fruit.")
    else:
        dataset = dataframe.loc[countries]
        dataset /= 1000000.0
        streamlit.write("### Gross Agricultural Production ($B)", dataset.sort_index())

        dataset = dataset.T.reset_index()
        dataset = pandas.melt(dataset, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            altair.Chart(dataset)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=altair.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Calories:N",
            )
        )
        streamlit.altair_chart(chart, use_container_width=True)
except URLError as e:
    streamlit.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
    

