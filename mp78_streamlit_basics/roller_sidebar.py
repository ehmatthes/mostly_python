from random import randint

import altair as alt
import pandas as pd
import streamlit as st

# Input widgets
side_options = [6, 10, 12, 20]
num_sides = st.sidebar.radio("Number of sides:", side_options)
num_dice = st.sidebar.slider("Number of dice:", 1, 10, value=2)
num_rolls_sim = st.sidebar.slider("Number of rolls in simulation",
        1_000, 100_000, value=1_000, step=1_000)

# Roll calculation
rolls = [randint(1, num_sides) for _ in range(num_dice)]
roll = sum(rolls)

# Simulation rolls
sim_rolls = []
for _ in range(num_rolls_sim):
    sim_roll = sum(
        [randint(1, num_sides) for _ in range(num_dice)])
    sim_rolls.append(sim_roll)
df_sim = pd.DataFrame({"rolls": sim_rolls})

# Create histogram
chart = alt.Chart(df_sim).mark_bar().encode(
    alt.X("rolls", bin=True),
    y="count()",
)
chart.title = f"Simulation of {num_rolls_sim} rolls"

# Main page
st.title("Rolling Dice")
st.button("Roll!")

st.write("---")
st.subheader(roll)
st.write(str(rolls))

st.write("---")
st.altair_chart(chart)