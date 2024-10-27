import streamlit as st
from footer import footer
from header import header

from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_carousel import carousel

import reveal_slides as rs

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

welcome_css_styles = """
        .welcome-text {
            font-size: 20px; 
            text-align: center;
            margin: 30px 0;
            color: #2C2C2E;
            background-color: #ffffff; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
            line-height: 1.6; 
            font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            transition: transform 0.3s, box-shadow 0.3s; /* Smooth transitions for hover effects */
        }

        .welcome-text:hover {
            transform: translateY(-2px); 
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15); 
        }

        .highlight {
            color: #286589;
            font-weight: bold; 
"""


test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
        link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
    ),
    # dict(
    #     title="Slide 4",
    #     text="PANDAS",
    #     img="pandas.webp",
    # ),
]

def home_page():
    header()   
    add_vertical_space(6)



    carousel(
                items=test_items,
                slide=True,              # Enable sliding
                fade=False,             # Disable fade transition
                controls=True,          # Show controls
                indicators=True,        # Show indicators
                interval=3000,          # Change slides every 3 seconds
                pause="hover",          # Pause on hover
                wrap=True,              # Wrap around the carousel
                container_height=700,   # Set container height
                width=1.0,              # Full width
                key='custom_carousel'        # Unique key for the carousel
       )

    with stylable_container(
        key="welcome_text",
        css_styles= welcome_css_styles,
    ):
        st.markdown(
            '<div class="welcome-text">'
            'We provide <span class="highlight">high-precision surveying solutions</span> to various industries, '
            'leveraging advanced technologies and expertise.'
            '</div>', 
            unsafe_allow_html=True
        )


    # Define styles for Mission and Vision section, including the subheader
    mission_vision_css_styles = """
        <style>
            .mission-vision-section {
                background: linear-gradient(to right, #F9F9F9, #FFFFFF); 
                padding: 40px;
                border-radius: 12px; 
            }

            .subheader {
                font-size: 32px; 
                text-align: center;
                color: #1F1F1F; 
                margin: 30px 0; 
                font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
                font-weight: bold; 
                transition: color 0.3s, transform 0.3s; 
            }
            .subheader:hover {
                color: #286589; 
                transform: scale(1.05); 
            }

            .mission-vision {
                font-size: 28px; /
                text-align: center;
                color: #1F1F1F; 
                margin-bottom: 25px; 
                font-weight: 600; 
                transition: color 0.3s, transform 0.3s; 
            }
            .mission-vision:hover {
                color: #286589; 
                transform: scale(1.03); 
            }

            .mission-vision-text {
                font-size: 18px; 
                color: #3A3A3C; 
                line-height: 1.7; 
                padding: 20px; 
                background-color: #FFFFFF; 
                border: 1px solid #E1E1E1; 
                border-radius: 10px; 
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15); 
                margin-bottom: 30px; 
                transition: transform 0.3s, background-color 0.3s; 
            }
            .mission-vision-text:hover {
                transform: translateY(-2px); 
                background-color: #F1F1F1; 
            }

            .icon {
                vertical-align: middle; 
                margin-right: 8px; 
                width: 28px; 
                height: 28px; 
                transition: transform 0.3s; 
            }
            .icon:hover {
                transform: scale(1.1);
            }

            @media (max-width: 768px) {
                .mission-vision-section {
                    padding: 20px; 
                }
                .subheader {
                    font-size: 28px; 
                }
                .mission-vision {
                    font-size: 24px; 
                }
                .mission-vision-text {
                    font-size: 16px;
                }
            }
        </style>
    """
    st.markdown(mission_vision_css_styles, unsafe_allow_html=True)

    # Mission and Vision Section
    st.markdown("<div class='mission-vision-section'><h2 class='subheader'>Our Mission and Vision</h2>", unsafe_allow_html=True)

    mission_col, vision_col = st.columns(2)

    with mission_col:
        st.markdown("<h3 class='mission-vision'>Mission Statement</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div class='mission-vision-text'>"
            "<img src='https://img.icons8.com/material-outlined/28/286589/goal.png' class='icon'/>"
            "Empowering Libya’s development with accurate, reliable data that drives successful project outcomes."
            "</div>", 
            unsafe_allow_html=True
        )

    with vision_col:
        st.markdown("<h3 class='mission-vision'>Vision Statement</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div class='mission-vision-text'>"
            "<img src='https://img.icons8.com/material-outlined/28/286589/vision.png' class='icon'/>"  # Example icon
            "To be Libya’s trusted surveying partner, known for technological leadership and client dedication."
            "</div>", 
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)  # Closing the mission-vision-section div


    add_vertical_space(1)
    footer()


# Main application entry point
if __name__ == "__main__":
    home_page()






    # tagline_css_styles = """
    #         <style>
    #         .tagline {
    #             text-align: center; /* Center alignment for a balanced look */
    #             font-family: 'SF Pro Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; /* Apple-style font stack */
    #             font-size: 24px; /* Slightly larger font size for emphasis */
    #             font-weight: 500; /* Medium weight for visibility */
    #             color: #2C2C2E; /* Dark gray for text */
    #             margin: 0;
    #             padding: 20px; /* Reduced padding for better spacing */
    #             line-height: 1.6; /* Improved line height for readability */
    #             letter-spacing: 0.75px; /* Spacing between letters for clarity */
    #             border-radius: 8px; /* Rounded corners for a softer look */
    #             background-color: #FFFFFF; /* White background for contrast */
    #             box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
    #             transition: color 0.3s, background-color 0.3s; /* Smooth transitions for hover effects */
    #         }
    #         .tagline:hover {
    #             color: #286589; /* Change text color on hover for interactivity */
    #             background-color: #F1F1F1; /* Subtle background change on hover */
    #         }
    #         </style>
    # """

    # st.markdown(tagline_css_styles, unsafe_allow_html=True)
    # st.markdown('<div class="tagline">Delivering Precision Mapping Solutions for Land and Sea</div>', unsafe_allow_html=True)