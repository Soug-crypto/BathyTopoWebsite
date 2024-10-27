import os
import re
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

import traceback


def footer(pages=None, directory="pages", footer_css_styles=None):
    """Render the footer with navigation buttons.

    Args:
        pages (list of str, optional): List of page names for navigation buttons.
        directory (str): Directory to search for pages if none are provided.
        css_styles (Optional[str]): CSS styles for buttons. Defaults to predefined styles.
    """
    # Default CSS styles
    default_css_styles = """<style>
            .floater {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f8f8f8; /* Light gray background for a soft look */
                text-align: center;
                padding: 15px 0; /* Adjusted padding for a more compact appearance */
                font-size: 18px; /* Slightly larger font for better readability */
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
                z-index: 1000; /* Ensure it appears above other content */
                border-top: 1px solid #e1e1e1; /* Light border for separation */
            }
    </style>"""
    
    button_css_styles = """
            button {
                margin: 0 16px; /* Ample margin for spacious layout */
                color: #286589; /* Apple blue for buttons */
                background-color: #ffffff; /* Clean white background */
                border: 1px solid #eedccb; /* Blue border */
                padding: 10px 24px; /* Comfortable padding for a more balanced feel */
                border-radius: 10px; /* Slightly less rounded for a sleek look */
                font-weight: 600; /* Bold for emphasis */
                font-size: 12px; /* Consistent font size */
                transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s; /* Smooth transitions */
                cursor: pointer; /* Pointer cursor for buttons */
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
                outline: none; /* Remove default outline */
            }
            button:hover {
                background-color: #286589; 
                transform: translateY(-2px); /* Enhanced lift effect on hover */
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05); /* Deeper shadow on hover for more emphasis */
            }
            .button:focus {
                box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.4);
            }
            .footer {
                text-align: center;
                margin-top: 50px; 
                font-size: 0.9em;
                color: #888;
            } 

            .social-links a {
                color: #286589; 
                text-decoration: none;
                margin-right: 10px;
            }

            .social-links a:hover {
                text-decoration: underline;
            }
    """
    
    # Use default styles if none provided
    if footer_css_styles is None:
        footer_css_styles = default_css_styles

    # Check if the specified directory exists
    if pages is None:
        pages = read_pages_from_directory(directory)

    # Remove duplicates and standardize names
    pages = list(set(pages))

    # If no pages found, provide a warning
    if not pages:
        st.warning("No pages available for navigation. Please provide a valid list or ensure the directory contains .py files.")
        return

    try:
        # Start rendering the footer
        add_vertical_space(3)

        st.markdown(footer_css_styles, unsafe_allow_html=True)
        st.divider()

        cols = st.columns(len(pages))

        # Add buttons to each column
        for i, page in enumerate(pages):
            button_label = page.replace("_", " ").title()
            with cols[i]:
                with stylable_container(key=page, css_styles=button_css_styles):
                    if st.button(button_label, key=page):
                        switch_page(page)
       

       # Social Media Links
        st.markdown("""
            <div class="social-links">
            <a href="#" target="_blank">Facebook</a> | 
            <a href="#" target="_blank">LinkedIn</a> | 
            <a href="#" target="_blank">Instagram</a> | 
            <a href="#" target="_blank">Twitter</a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error rendering footer: {str(e)}")

def read_pages_from_directory(directory):
    """Read available page names from the specified directory.

    Args:
        directory (str): Directory to search for pages.

    Returns:
        list of str: List of standardized page names without the .py extension.
    """
    try:
        pages = [f[:-3] for f in os.listdir(directory) if f.endswith(".py")]
        standardized_pages = [standardize_page_name(page) for page in pages]
        return standardized_pages
    except FileNotFoundError:
        st.warning(f"Directory '{directory}' not found.")
        return []

def standardize_page_name(name):
    """Standardize the page name by removing leading numbers and underscores.

    Args:
        name (str): The original page name.

    Returns:
        str: The standardized page name.
    """
    # Remove leading numbers and underscores and convert to lowercase
    standardized_name = re.sub(r'^\d+[_-]?', '', name).strip().lower()
    return standardized_name