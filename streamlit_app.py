import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.function.plus_touché import plus_touche


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

* Test
* Test2
"""

st.table(plus_touche(10,10))