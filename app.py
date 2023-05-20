import streamlit as st
import pandas as pd

st.write("""
# Division of two numbers


""")

st.header("User Input Parameters")

def user_input_features():
	Dividend = st.number_input("DIVIDEND")
	Divisor = st.number_input("DIVISOR")
	
	data = {'DIVIDEND' : Dividend, 'DIVISOR' : Divisor}
	
	features = pd.DataFrame(data, index = [0])
	return features
	
df = user_input_features()
	
submit = st.form(key='my-form').form_submit_button('Submit')

st.header('Answer :')
if submit:
	if (df['DIVISOR'] == 0).bool():
		st.subheader("Not a number")
	else:
	    st.subheader(round((df['DIVIDEND']/df['DIVISOR']),4)[0])


