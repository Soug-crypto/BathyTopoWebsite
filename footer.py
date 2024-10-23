import os
import re
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import traceback

def footer(pages=None, directory="pages", css_styles=None):
    """Render the footer with navigation buttons.

    Args:
        pages (list of str, optional): List of page names for navigation buttons.
        directory (str): Directory to search for pages if none are provided.
        css_styles (Optional[str]): CSS styles for buttons. Defaults to predefined styles.
    """
    # Default CSS styles
    default_css_styles = """
            floater {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.1);
            }
            footer button {
                margin: 0 10px;
                color: #007BFF;
                background-color: white;
                border: 1px solid #007BFF;
                padding: 5px 10px;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            footer button:hover {
                background-color: #e7f1ff;
            }
    """
    
    # Use default styles if none provided
    if css_styles is None:
        css_styles = default_css_styles

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

        st.markdown('<footer class="floater">', unsafe_allow_html=True)

        cols = st.columns(len(pages))

        # Add buttons to each column
        for i, page in enumerate(pages):
            button_label = page.replace("_", " ").title()
            with cols[i]:
                with stylable_container(key=page, css_styles=css_styles):
                    if st.button(button_label, key=page):
                        switch_page(page)
        
        st.markdown('</footer>', unsafe_allow_html=True)

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

def render_footer_html(buttons):
    """Render the HTML for the footer.

    Args:
        buttons (str): HTML string containing buttons for navigation.
    """
    st.markdown(
        f"""
        <style>
            .footer {{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.1);
            }}
            .footer button {{
                margin: 0 10px;
                color: #007BFF;
                background-color: white;
                border: 1px solid #007BFF;
                padding: 5px 10px;
                border-radius: 5px;  
                transition: background-color 0.3s;  
            }}

        </style>
        <div class="footer">
            {buttons}
        </div>
        """,
        unsafe_allow_html=True
    )

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