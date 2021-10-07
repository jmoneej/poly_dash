import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json
from PIL import Image


def app():

    #st.set_page_config(layout="wide")
    st.title("Home Page")

    st.write("""
    Utilizing Streamlit for the polygon mega dashboard. Links to original queries are below.
    """
    )

    st.write ("""
    NOTE: Queries do not autorefresh, will need to be manually refreshed on Flipside to update data on graphs and tables in this interface.
    """)

    st.text ("")
    st.markdown("""
    ###### ORIGINAL QUERIES
    """)
    st.text ("https://app.flipsidecrypto.com/velocity/queries/5a7ac116-7647-44ce-a421-1316b0974b28 - Eth/Matic Vol")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/11edbedf-d84e-493d-b605-827298e317e2 - Eth Fees")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/eb1689f5-7b75-49d1-ba9e-e1f4eab489c9 - Syncing")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/5b112bae-b1e2-446c-b458-1eb31900d06e - Polygon Fees")

#-------------------------------------------------------

    st.markdown("""
    ---
    """)
    st.markdown("""
    #### USING STREAMLIT
    """)
    
    tutorial_1 = Image.open("tutorial_1.png")
    st.image(tutorial_1)

    st.caption ("""
    Hover over graphs and tables to reveal menu and fullscreen mode. Arrows point out to enlarge, and point in to make small again.
    """)
    st.text("")

    tutorial_2 = Image.open("tutorial_2.png")
    st.image(tutorial_2)
    st.text("")
    st.caption ("""
    The sidebar opens by default on each page. Simply click on the x to hide it and then click on the arrow to reveal it again. 
    The sidebar contains options to customize visualizations.
    """)
    st.text("")

    tutorial_3 = Image.open("tutorial_3.png")
    st.image(tutorial_3)
    st.text("")
    st.caption ("""
    Most sidebars are for diy visualizations. 
    Choose which columns from the corresponding table to display on the graph as well as the y-axis scale. Each plot will automatically be of a different color.
    """)
    st.text("")
   