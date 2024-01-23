from random import randint
import streamlit as st

# Input widgets
side_options = [6, 10, 12, 20]
num_sides = st.radio("Number of sides:", side_options)
num_dice = st.slider("Number of dice:", 1, 10, value=2)

st.button("Roll")

# Roll calculation
rolls = [randint(1, num_sides) for _ in range(num_dice)]
roll = sum(rolls)

# Output message
st.write("---")
st.subheader(roll)
st.write(str(rolls))