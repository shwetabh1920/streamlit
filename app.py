import streamlit as st

st.title('Find the Largest Number')

st.write('Enter 3 numbers below:')
num1 = st.number_input('Number 1')
num2 = st.number_input('Number 2')
num3 = st.number_input('Number 3')

if st.button('Find Largest'):
    largest_num = max(num1, num2, num3)
    st.write(f'The largest number is: {largest_num}')
