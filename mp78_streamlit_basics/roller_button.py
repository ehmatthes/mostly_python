from random import randint
import streamlit as st

st.button("Roll")

roll = randint(1, 6)

st.write(f"You rolled a {roll}.")