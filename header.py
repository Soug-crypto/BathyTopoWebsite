
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# from streamlit_float import *



with open('./files/style.css') as f:
    css = f.read()

logo_css_styles = """
    img {
        max-width: 100%; 
        height: auto; 
        padding: 0.5em;
        border-radius: 1em;
        # box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }

    img:hover {
        transform: scale(1.003);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05); 
    }
"""

title_css_styles = """
        h1 {
            text-align: left;
            font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            font-size: 48px;
            font-weight: bold;
            color: #333;
            margin: 0;
            padding-top: 40px;
            padding-bottom: 10px;
        }

        h2 {
            text-align: left;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 24px;
            font-weight: normal;
            color: #777;
            margin: 0;
            padding-top: 0;
            padding-bottom: 20px;
        }
"""



def header():
    # Logo and Title Section
    col1, col2 = st.columns([1, 2])  

    with col1:
        with stylable_container(
            key="logo",
            css_styles= logo_css_styles,
        ):
            st.image("images/logo.png", width=175)  
    col1.float()

    with col2:
        with stylable_container(
            key="title-sub",
            css_styles= title_css_styles,
        ):
            st.markdown("<h1>GeoLibya</h1>", unsafe_allow_html=True)
            st.markdown("<h2>Mapping the Future, Above and Below.</h2>", unsafe_allow_html=True)
    col2.float()