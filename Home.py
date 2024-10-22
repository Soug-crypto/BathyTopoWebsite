import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        background-color: #F5F5F5;
        color: #333;
        line-height: 1.6;
    }
    
    h1, h2, h3 {
        color: #1A1A1A;
        text-align: center; /* Center headers for consistency */
    }
    
    .logo {
        text-align: center; 
        margin: 20px 0;
    }
    
    .title {
        text-align: left; /* Center the title */
        margin: 20px 0;
        font-weight: medium; /* Bold title for emphasis */
    }
    
    .tagline {
        font-size: 20px; /* Increase font size for emphasis */
        font-weight: medium; /* Make it bold */
        text-align: center; /* Center the tagline */
        color: #1A1A1A; /* Distinct color */
        margin: 10px 0; /* Add margin for spacing */
        padding: 10px; /* Add padding for emphasis */
        border: 1px solid #1A1A1A; /* Border to highlight */
        border-radius: 8px; /* Rounded corners */
    }
    
    .welcome-text {
        font-size: 22px;
        text-align: center;
        margin: 20px 0;
        color: ##286589;
        background-color: #ffffff;
        padding: 15px;
        border-radius: 5px; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Subtle shadow for depth */
    }
    
    .mission-vision {
        font-size: 20px;
        margin: 10px 0;
        padding: 10px; /* Padding for clarity */
        background-color: #f9f9f9; /* Light background */
        border-left: 3px solid #286589; /* Left border for emphasis */
    }
    
    .separator {
        margin: 40px 0;
        border: 1px solid #E0E0E0;
    }

    .footer {
        text-align: center;
        margin-top: 50px; 
        font-size: 0.9em;
        color: #888;
    }
    
    /* Responsive design for better mobile viewing */
    @media (max-width: 600px) {
        .tagline {
            font-size: 20px; /* Adjust font size on smaller screens */
        }
        .welcome-text {
            font-size: 18px; /* Adjust welcome text size */
        }
    }
    </style>
    """, 
    unsafe_allow_html=True
)

def home_page():
    # Logo and Title Section
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

    with col1:
        st.image("images/logo.png", width=200)  # Adjust path as needed

    with col2:
        # st.title("GeoLibya")
        # st.header("Mapping the Future, Above and Below.")
        st.markdown("<h1 style='text-align: left;'>GeoLibya</h1>", unsafe_allow_html=True)

        st.markdown("<h2 style='text-align: left;'>Mapping the Future, Above and Below.</h2>", unsafe_allow_html=True)


    # Improved Tagline
    st.markdown('<div class="tagline">Delivering Precision Mapping Solutions for Land and Sea</div>', unsafe_allow_html=True)

    # Welcome Section with Image

    # st.image("images/welcome_image.jpg", use_column_width=True)
    st.markdown(
        """
        <style>
        .image-container {
            text-align: center; 
            margin: 20px 0; 
            border-radius: 12px; 
            overflow: hidden; 
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s;
        }
        
        .image-container img {
            width: 100%; 
            border-radius: 12px; 
            transition: transform 0.3s;
        }
        
        .image-container:hover {
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        }

        /* Optional: Add a subtle background color */
        .image-container {
            background-color: #ffffff; /* Light background for contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Image with enhanced styling
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("images/welcome_image.jpg", use_column_width=True)  
    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced welcome text with improved styling
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
    
    # Separator
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)



    # with open('./files/wave.css') as f:
    #     css = f.read()

    # st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)

# Main application entry point
if __name__ == "__main__":
    home_page()