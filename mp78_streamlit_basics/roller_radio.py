from random import randint
import streamlit as st

side_options = [6, 10, 12, 20]
num_sides = st.radio("Number of sides:", side_options)

st.button("Roll")

roll = randint(1, num_sides)

st.write(f"You rolled a {roll}.")