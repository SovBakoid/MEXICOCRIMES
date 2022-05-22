import streamlit as st



st.header("Мини визуализации про преступность в Мехико сити")

st.write("""
Я нашел данные про каждое отдельное преступление, совершенное в Мехико,
 сопоставил данные с координатами, чутка порылся и получил вот такую карту.""")

with st.echo(code_location="above"):
    import plotly.express as px
    import numpy as np
    import pandas as pd
    from PIL import Image
    import requests
    from io import BytesIO
    import altair as alt
    import seaborn as sns
    import matplotlib.pyplot as plt
    import urllib.request

    pd.read_csv("")

