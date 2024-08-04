#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
import numpy as np
import time
from PIL import Image
from sympy import im

# im = Image.open('icon4.png')
st.set_page_config(page_title="Telecom churn app")
# st.image('title.png')
html_temp = """
    <div style="background-color:#f63350 ;padding:10px">
    <h2 style="color:white;text-align:center;">
    Telecommunication Churn Prediction App </h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
# left , right = st.columns(2)
# st.image('title.png')

model = load(open("classification.sav", "rb"))


def predict_price(
    voice_plan,
    intl_plan,
    intl_calls,
    intl_charge,
    day_mins,
    day_charge,
    eve_mins,
    night_mins,
    customer_calls,
):
    input = np.array(
        [
            [
                voice_plan,
                intl_plan,
                intl_calls,
                intl_charge,
                day_mins,
                day_charge,
                eve_mins,
                night_mins,
                customer_calls,
            ]
        ]
    ).astype(np.float64)
    prediction = model.predict(input)
    return prediction


def main():
    # voice_plan = st.text_input("Did the client subscribe for the voice plan?","Please Type 0 for No/ 1 for Yes")
    r = st.radio(
        "Did the client subscribe for the voice plan?",
        options=["Yes", "No"],
        horizontal=True,
    )
    if r == "yes":
        voice_plan = 1
    else:
        voice_plan = 0
    # intl_plan = st.text_input("Did the client subscribe for the international plan?","Please Type 0 for No/ 1 for Yes")
    r1 = st.radio(
        "Did the client subscribe for the international plan?",
        options=["Yes", "No"],
        horizontal=True,
    )
    if r1 == "yes":
        intl_plan = 1
    else:
        intl_plan = 0
    intl_calls = st.number_input("How many international calls did the client make?")
    intl_charge = st.text_input(
        "What is the charge on the client's usage of the international service?"
    )
    day_mins = st.text_input(
        "How many minutes did the customer use the service to make calls during the day?"
    )
    day_charge = st.text_input("What is the charge on the client's day calls?")
    eve_mins = st.text_input(
        "How many minutes did the customer use the service to make calls during the evening?"
    )
    night_mins = st.text_input(
        "How many minutes did the customer use the service to make calls during the night?"
    )
    customer_calls = st.text_input(
        "How many times did the client call the customer service?"
    )
    if st.button("Predict"):
        output = predict_price(
            voice_plan,
            intl_plan,
            intl_calls,
            intl_charge,
            day_mins,
            day_charge,
            eve_mins,
            night_mins,
            customer_calls,
        )
        if output == 0:
            # st.success('YES',icon="📉")
            st.success("YES")
            time.sleep(0.5)
            st.toast("This customer will likely churn 📉")
        else:
            # st.success('NO',icon="📈")
            st.success("NO")
            time.sleep(0.5)
            st.toast("This customer will likely not churn 📈")


if __name__ == "__main__":
    main()
 