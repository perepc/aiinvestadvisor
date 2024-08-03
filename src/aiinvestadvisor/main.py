#!/usr/bin/env python
import os
import streamlit as st
# from aiinvestadvisor.crew import AIInvestAdvisorCrew
from aiinvestadvisor.aiinvestadvisor.crew import AIInvestAdvisorCrew

os.environ['GROQ_API_KEY'] = ""


def run():
    """
    Run the crew.
    """

    _inputs = {
        'current_year': '2024',
        'company': 'Apple'

    }
    AIInvestAdvisorCrew().crew().kickoff(inputs=_inputs)


st.title("AI Invest Advisor")

with st.form(key='my_form'):
    groq_api_key = st.text_input(label="Groq API key: ")
    company = st.text_input(label="Company to analyze: ")
    submit_button = st.form_submit_button("Go!")

if submit_button:
    if not company:
        st.write("You must fill a company first!")
    else:
        if not groq_api_key:
            st.write("You must enter you Groq API key!")
        else:
            os.environ['GROQ_API_KEY'] = groq_api_key
            inputs = {
                'current_year': '2024',
                'company': company

            }
            result = AIInvestAdvisorCrew().crew().kickoff(inputs=inputs)
            st.markdown(result)
