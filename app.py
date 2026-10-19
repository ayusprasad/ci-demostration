import streamlit as st
from math_utils import square, cube, fifth_power

st.set_page_config(page_title="Power Calculator", page_icon="⚡")

st.title("⚡ Power Calculator")
st.markdown("Calculate exponential powers for any integer or floating point number.")

n = st.number_input("Enter a number:", value=2, step=1)

col1, col2, col3 = st.columns(3)
col1.metric("Square (n²)", f"{square(n):,}")
col2.metric("Cube (n³)", f"{cube(n):,}")
col3.metric("Fifth Power (n⁵)", f"{fifth_power(n):,}")