import streamlit as st
from src.prediction import Insurance_Prediction
st.title("Insurance Prediction")
st.write("Description about your project")
Age =  st.number_input("Enter age : ")
Annual_Income_LPA =  st.number_input("Enter Annual_Income_LPA")
Policy_Term_Years =  st.number_input("Enter Policy_Term_Years")
Sum_Assured_Lakhs =  st.number_input("Enter Sum_Assured_Lakhs")
if st.button("predict"):
    model = Insurance_Prediction()
    result = model.prediction(Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs)
    st.success(result)