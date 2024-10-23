import streamlit as st
from footer import footer
from streamlit_extras.stylable_container import stylable_container

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

img_css_styles = """
    img {
        max-width: 100%; 
        height: auto; 
        padding: 0.5em;
        border-radius: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    img:hover {
        transform: scale(1.003);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
    }
"""
pages = ["home", "about", "contact"] 
btn_css_styles = """
    margin: 0 10px; 
    color: #007BFF; 
    background-color: white; 
    border: 1px solid #007BFF; 
    padding: 5px 10px; 
    border-radius: 5px; 
    transition: background-color 0.3s;
"""  
def home_page():
    # Logo and Title Section
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

    with col1:
        st.image("images/logo.png", width=200)  # Adjust path as needed

    with col2:
        st.markdown("<h1 style='text-align: left;'>GeoLibya</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: left;'>Mapping the Future, Above and Below.</h2>", unsafe_allow_html=True)
    st.markdown('<div class="tagline">Delivering Precision Mapping Solutions for Land and Sea</div>', unsafe_allow_html=True)

    with stylable_container(
        key="welcome_imagee",
        css_styles= img_css_styles,
    ):
        st.image("images/welcome_image.jpg", use_column_width=True)

    st.markdown(
        '<div class="welcome-text">'
        'We provide <strong style="color: #286589;">high-precision surveying solutions</strong> to various industries, '
        'leveraging advanced technologies and expertise.'
        '</div>', 
        unsafe_allow_html=True
    )

    # Mission and Vision Section
    st.subheader("Our Mission and Vision")
    mission_col, vision_col = st.columns(2)

    with mission_col:
        st.markdown("<h3 class='mission-vision'>Mission Statement</h3>", unsafe_allow_html=True)
        st.write(
            "Empowering Libya’s development with accurate, reliable data that drives successful project outcomes."
        )

    with vision_col:
        st.markdown("<h3 class='mission-vision'>Vision Statement</h3>", unsafe_allow_html=True)
        st.write(
            "To be Libya’s trusted surveying partner, known for technological leadership and client dedication."
        )

    st.divider()
    footer()

    # Footer
    st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)

# Main application entry point
if __name__ == "__main__":
    home_page()