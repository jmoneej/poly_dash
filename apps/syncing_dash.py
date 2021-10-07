import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json


def app():

    #st.set_page_config(layout="wide")
    st.title("State Syncing")
    st.text ("https://app.flipsidecrypto.com/velocity/queries/eb1689f5-7b75-49d1-ba9e-e1f4eab489c9")
    st.text("")
    st.text("Syncing table is composed of values from polygon.udm_events where origin_address = '0x0000000000000000000000000000000000000000'")
    st.text("")
    st.text("sum(amount_usd) as syncying_sum")
    st.text("avg(amount_usd) as syncying_avg, etc")

    sync_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/eb1689f5-7b75-49d1-ba9e-e1f4eab489c9/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
    
    st.markdown("""
    """)
    st.markdown("""
    ### State Syncing Table and Graphs - Base Table
    """)

    st.sidebar.header("Filter Symbol Here For Sum Date:")
    symbol = st.sidebar.multiselect(
        "Select the Symbol(s)",
        options = sync_flipside_df['SYMBOL'].unique(),
        default = sync_flipside_df['SYMBOL'].unique()
    )

    sum_symbol_selection = sync_flipside_df.query(
        "SYMBOL == @symbol"
    )

    st.dataframe(sync_flipside_df)



    sync_sum_symbol = px.bar(
        sum_symbol_selection,
        x = "SYNC_DAY",
        y = "SYNCYING_SUM",
        color = "SYMBOL",
        title = "<b>Syncing Sum By Date</b>",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    

    st.plotly_chart(sync_sum_symbol)

    
 

    # ------------------------------------------------

    st.sidebar.header("Filter Symbol Here For BBs:")
    bb_symbol = st.sidebar.multiselect(
        "Select the Symbol(s) for BBs",
        options = sync_flipside_df['SYMBOL'].unique(),
        default = sync_flipside_df['SYMBOL'].max()
    )

    BB_symbol_selection = sync_flipside_df.query(
        "SYMBOL == @bb_symbol"
    )

    #st.markdown("""
    #    ### Bollinger Bands
    #    """)

    sync_b_bands = px.line(
        BB_symbol_selection,
        x = "SYNC_DAY",
        y=['Z1', 'ZN1', 'SYNCYING_MED'],
        color = "SYMBOL",
        title = "<b>Bollinger Bands</b>",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )

    st.plotly_chart(sync_b_bands)

#---------------------------------------------------------
    st.sidebar.markdown("---")

    st.sidebar.header("DIY / Build Your Own Chart:")
    tx_symbol = st.sidebar.multiselect(
        "Select the Symbol(s) for TX counts",
        options = sync_flipside_df['SYMBOL'].unique(),
        default = sync_flipside_df['SYMBOL'].max()
    )

    tx_symbol_selection = sync_flipside_df.query(
        "SYMBOL == @tx_symbol"
    )

   
    columns = st.sidebar.multiselect(
        "Select the columns to plot",
        options = sync_flipside_df.columns,
        default = sync_flipside_df.columns.min()
    )

    sync_tx_count = px.line(
        tx_symbol_selection,
        x = "SYNC_DAY",
        y = columns,
        color = "SYMBOL",
        title = "<b>DIY / Choose your own adventure - Sync</b>",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )

    st.plotly_chart(sync_tx_count)