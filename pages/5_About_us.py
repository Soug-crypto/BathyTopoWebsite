import streamlit as st
from footer import footer
import base64
from streamlit_card import card


with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Title styling */
        .about-title {
            font-size: 48px; /* Slightly larger for prominence */
            font-weight: 800; /* Bolder weight for impact */
            color: #1d1d1f; /* Darker color for better contrast */
            text-align: center; /* Centered title */
            margin-bottom: 40px; /* More space below */
            letter-spacing: 1.5px; /* Increased letter spacing for elegance */
            text-transform: uppercase; /* Uppercase for modern feel */
        }

        /* Subheader styling */
        .about-subheader {
            font-size: 30px; /* Slightly larger for emphasis */
            font-weight: 600; /* Medium boldness */
            color: #3a3a3c; /* Soft dark color for subtlety */
            text-align: center; /* Centered subheader */
            margin-bottom: 30px; /* Space below subheader */
            letter-spacing: 0.8px; /* Subtle letter spacing */
        }

        /* Text block styling */
        .about-text {
            font-size: 18px; /* Maintain readability */
            color: #333; /* Dark color for text */
            text-align: center; /* Centered text */
            line-height: 1.6; /* Improved line height for readability */
            margin: 0 auto; /* Centered block */
            max-width: 800px; /* Max width for better layout */
            padding: 35px; /* Slightly increased padding */
            background-color: rgba(255, 255, 255, 0.98); /* Almost opaque background */
            border-radius: 15px; /* Softer corners */
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.01); /* More depth */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effect */
        }

        /* Hover effect for text block */
        .about-text:hover {
            transform: translateY(-5px); /* Slightly more lift on hover */
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.03); /* Enhanced shadow on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Render the section
st.markdown('<div class="about-title">About Us</div>', unsafe_allow_html=True)
st.markdown('<div class="about-subheader">Company Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="about-text">GeoLibya is a leading provider of high-precision surveying solutions in Libya, specializing in topographic and bathymetric surveys. We support a wide range of industries, including construction, environmental studies, urban planning, oil, and marine projects.</div>', unsafe_allow_html=True)


# Function to convert an image to base64
def image_to_base64(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    return "data:image/png;base64," + encoded.decode("utf-8")

# Leadership Team with Image Cards

st.markdown("""
    <style>
        /* Leadership Team section styling */
        .leadership-title {
            font-size: 42px; /* Larger title for maximum emphasis */
            font-weight: 800; /* Bolder for a stronger impact */
            color: #1a1a1a; /* Slightly darker color for enhanced contrast */
            text-align: center; /* Centered title for symmetry */
            margin-bottom: 50px; /* Increased space below title */
            letter-spacing: 2px; /* Increased letter spacing for a modern look */
            text-transform: uppercase; /* Modern touch */
            font-family: "Helvetica Neue", Arial, sans-serif; /* Clean font choice */
            transition: color 0.3s ease; /* Smooth color transition on hover */
        }

        .leadership-title:hover {
            color: #007aff; /* Change color on hover for interaction */
        }

        .leadership-subtitle {
            font-size: 26px; /* Slightly larger for subheader */
            font-weight: 600; /* Semi-bold for distinction */
            color: #555; /* Softer dark color for subheader */
            text-align: center; /* Centered subheader */
            margin-bottom: 40px; /* Increased space below subheader */
            letter-spacing: 0.5px; /* Slight letter spacing */
            font-family: "Helvetica Neue", Arial, sans-serif; /* Consistent font */
            line-height: 1.5; /* Improved line height for readability */
        }
    </style>
""", unsafe_allow_html=True)

# Render the section title
st.markdown('<div class="leadership-title">Leadership Team</div>', unsafe_allow_html=True)
st.markdown('<div class="leadership-subtitle">Meet the Visionaries Behind GeoLibya</div>', unsafe_allow_html=True)

team_members = [
    {
        "name": "Co-Founder 1 Name", 
        "title": "Chief Executive Officer (CEO)", 
        "bio": "Over X years of experience in topographic and bathymetric surveys, leading high-profile projects across Libya.", 
        "img": "images/cofounder1.jpg"
    },
    {
        "name": "Co-Founder 2 Name", 
        "title": "Chief Operating Officer (COO)", 
        "bio": "Expert in operational management and surveying technologies, focusing on innovative solutions.", 
        "img": "images/cofounder2.jpg"
    }
]

# Create columns for each team member
cols = st.columns(len(team_members))
for col, member in zip(cols, team_members):
    with col:
        # Convert image to base64
        image_data = image_to_base64(member['img'])
        
        # Create a card for each team member
        with st.container():
            card(
                title=member['name'],
                text=f"_{member['title']}_\n\n{member['bio']}",
                image=image_data,
                styles = {
                    "card": {
                        "display": "flex",
                        "flex-direction": "column",
                        "justify-content": "flex-end",
                        "align-items": "flex-start",
                        "width": "100%",
                        "height": "400px",
                        "border-radius": "25px",  # Slightly larger border radius
                        "box-shadow": "0 4px 20px rgba(0,0,0,0.1)",  # Softer shadow
                        "background-color": "#ffffff",  # Clean white background
                        "padding": "20px", 
                    },
                    "title": {
                        "font-size": "20px",  # Slightly smaller font size for balance
                        "font-weight": "600",
                        "color": "#ffffff",  # Bright white for the title
                        "text-align": "left",
                        "margin-bottom": "10px",  # Increased margin for spacing
                        "background-color": "rgba(0, 0, 0, 0.5)",  # Lighter dark background
                        "border-radius": "15px",  # Rounded corners for the title background
                        "padding": "8px 12px",  # More padding for a comfortable touch
                    },
                    "text": {
                        "font-size": "15px",  # Slightly larger for readability
                        "font-family": "Helvetica, Arial, sans-serif",
                        "color": "#ffffff",  # Bright white for better contrast
                        "text-align": "left",
                        "background-color": "rgba(0, 0, 0, 0.4)",  # Softer background for text
                        "border-radius": "15px",  # Rounded corners
                        "padding": "8px 12px",  # More padding for readability
                        "margin-top": "5px",  # Added margin for spacing from title
                    },
                    "filter": {
                        "background-color": "rgba(0, 0, 0, 0)" 
                    },
                    "div": {
                        "width": "100%",
                    }
                }
            )




st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* Certifications section styling */
        .certifications-title {
            font-size: 42px; 
            font-weight: 700; 
            color: #1c1c1e; 
            text-align: center; 
            margin-bottom: 40px; 
            letter-spacing: 1.5px; 
            text-transform: uppercase; 
            font-family: "Helvetica Neue", Arial, sans-serif;
        }

        .certification-item {
            display: flex; 
            align-items: center; 
            justify-content: flex-start; 
            margin: 15px 0; 
            padding: 15px 20px; 
            background-color: rgba(255, 255, 255, 0.95); 
            border-radius: 12px; 
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); 
            transition: background-color 0.3s ease, transform 0.3s ease; 
            border: 1px solid rgba(0, 0, 0, 0.05); 
        }

        .certification-item:hover {
            background-color: rgba(240, 240, 240, 0.9); 
            transform: translateY(-2px);
        }

        .certification-icon {
            margin-right: 15px; 
            font-size: 24px; 
            color: #007aff; 
        }

        .certifications-list {
            font-size: 18px; 
            color: #2c2c2e; 
            text-align: left; 
            line-height: 1.6; 
            margin: 0 auto; 
            max-width: 700px; 
            padding: 30px; 
            background-color: rgba(255, 255, 255, 0.98); 
            border-radius: 15px; 
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); 
        }
    </style>
""", unsafe_allow_html=True)

# Render the section
st.markdown('<div class="certifications-title">Certifications & Affiliations</div>', unsafe_allow_html=True)

# List of certifications with professional icons
certifications = [
    '<i class="fas fa-certificate certification-icon"></i> ISO 9001:2015',
    '<i class="fas fa-building certification-icon"></i> Member of [Industry Association]'
]

# Render the list with icons
for cert in certifications:
    st.markdown(f'<div class="certification-item">{cert}</div>', unsafe_allow_html=True)


# Footer
st.divider()
footer()






# st.title("About Us")
# st.subheader("Company Overview")

# st.write("""
#     GeoLibya is a leading provider of high-precision surveying solutions in Libya, specializing in topographic and bathymetric surveys.
#     We support a wide range of industries, including construction, environmental studies, urban planning, oil, and marine projects.
# """)

# cols = st.columns(len(team_members))
# for col, member in zip(cols, team_members):
#     with col:
#         st.markdown('<div class="team-member">', unsafe_allow_html=True)
#         st.write(f"**{member['name']}** - _{member['title']}_")
#         st.write(member['bio'])
#         st.markdown('</div>', unsafe_allow_html=True)



# # Certifications & Affiliations
# st.subheader("Certifications & Affiliations")
# st.write("""
#     - ISO 9001:2015
#     - Member of [Industry Association]
# """)
