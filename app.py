import streamlit as st
from multiapp import MultiApp
from apps import home, syncing_dash, eth_matic_vol, polygon_fees, eth_fees # import your app modules here

app = MultiApp()

st.set_page_config(layout="wide")
st.markdown("""
# POLYGON MEGA DASH
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Syncing", syncing_dash.app)
app.add_app("Eth-Matic Vol", eth_matic_vol.app)
app.add_app("Polygon Fees", polygon_fees.app)
app.add_app("Eth Fees", eth_fees.app)



# The main app
app.run()