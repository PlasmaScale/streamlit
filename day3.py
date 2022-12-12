
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt

st.header("st.write")

st.write("Hello, *World*!, :sunglasses:")

st.write(1234)

df = pd.DataFrame(
    np.random.randn(4,2),
    columns = ["first column", "second column"]
)
st.write(df)

st.write("This is a dataframe: ", df)

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ["a", "b", "c"]
)

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
