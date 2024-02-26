import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from src.function.MostImpact import RankImpact


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

* Test
* Test2
"""


npays = st.slider('Nombre de pays', min_value=1, max_value=40, value=10, step=1)
nannee = st.slider('Nombre de D\'année', min_value=1, max_value=40, value=10,step=1)

most_impact = RankImpact(nannee,npays)
st.table(most_impact)

less_impact = RankImpact(nannee,npays,True)
st.table(less_impact)


print(most_impact)