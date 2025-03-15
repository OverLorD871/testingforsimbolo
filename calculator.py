import streamlit as st
import numpy as np

st.title ('Calculator Demo')
st.caption ('This is The Calculator App DEMO further enhancements are needed.')

number = st.number_input('Insert a Number')
st.write('The Current Number is', number)

snumber = st.number_input('Insert a second Number')

addition = (number + snumber)
multiply = (number * snumber)
subtraction = (number - snumber)
division = (number / snumber) if snumber != 0 else 'undefined'

left, middle, middle2, right = st.columns(4)

if left.button("Add", use_container_width=True):
    left.markdown(f'The addition of {number} and {snumber} is {addition}')

if middle.button("Multiply", use_container_width=True):
    middle.markdown(f'The multiplication of {number} and {snumber} is {multiply}')

if middle2.button("Subtract", use_container_width=True):
    middle2.markdown(f'The subtraction of {number} and {snumber} is {subtraction}')

if right.button("Divide", use_container_width=True):
    right.markdown(f'The division of {number} and {snumber} is {division}')

