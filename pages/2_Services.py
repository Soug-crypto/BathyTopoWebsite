import streamlit as st
from footer import footer
from header import header
# Improved CSS
custom_css = """
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
 h3 {
    color: #3D3D3D; 
    text-align: center;
    margin: 30px 0; 
    font-weight: 600; 
}

/* Paragraph and List Styles */
p, li {
    font-size: 16px; 
    line-height: 1.6; 
    margin: 0 0 10px; 
    text-align: left;
}

/* Service Title Styles */
.service-title {
    font-size: 18px; 
    font-weight: bold; 
    color: #333; 
    margin-bottom: 5px; 
}

/* Service Description Styles */
.service-description {
    font-size: 16px; 
    color: #333; 
    margin-bottom: 10px; 
}

/* Button Styles */
.streamlit-button {
    background-color: #007aff; 
    color: white; 
    border-radius: 5px; 
    padding: 12px 24px; 
    font-weight: bold; 
    border: none; 
    transition: background-color 0.3s ease, transform 0.2s ease; 
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Added shadow for depth */
}

.streamlit-button:hover {
    background-color: #0056b3; 
    transform: translateY(-2px); 
}

/* Expander Header Styles */
.streamlit-expanderHeader {
    background-color: #007aff; 
    color: white; 
    border-radius: 5px; 
    padding: 15px; 
    transition: background-color 0.3s ease; 
}

.streamlit-expanderHeader:hover {
    background-color: #0056b3; 
}

/* Expander Content Styles */
.streamlit-expanderContent {
    background-color: #ffffff; 
    padding: 20px; 
    border-radius: 5px; 
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Enhanced shadow for depth */
}

/* Footer Styles */
.footer {
    text-align: center;
    color: #999;
    font-size: 14px;
    padding: 20px 0;
    border-top: 1px solid #e0e0e0; 
    margin-top: 40px; 
}

/* Media Queries for Responsiveness */
@media (max-width: 768px) {
    h1 {
        font-size: 36px; /* Responsive font size */
    }
    .service-title {
        font-size: 20px; /* Smaller titles on mobile */
    }
    .streamlit-button {
        width: 100%; /* Full width buttons on mobile */
    }
}
"""




with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

header()
# Apply the CSS styles
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

st.title("Our Services")

# Introduction text
introduction_text = """
<div style="text-align: center; margin-bottom: 40px;">
    <p style="font-size: 18px; line-height: 1.6; color: #333;">
        At GeoLibya, we pride ourselves on delivering top-tier surveying and mapping solutions tailored to meet the diverse needs of our clients. 
        With cutting-edge technology and a team of experienced professionals, we ensure precision and reliability in every project.
        Our core services encompass a wide range of applications, from geodetic surveying to environmental monitoring, designed to support construction, urban planning, and sustainable development.
    </p>
    <p style="font-size: 18px; line-height: 1.6; color: #333;">
        Explore our offerings below to discover how we can help you achieve your goals with accurate and insightful data.
    </p>
</div>
"""

st.markdown(introduction_text, unsafe_allow_html=True)

st.subheader("Core Services")

services = [
    {
        "title": "Topographic and Geodetic Surveying",
        "description": "Comprehensive Terrain Mapping using GPS, UAVs, Total Stations, and LiDAR to measure elevations and determine locations.",
        "benefits": "Tailored solutions for construction, infrastructure development, urban planning, and environmental assessments."
    },
    {
        "title": "Real Estate Surveying",
        "description": "Legal Ownership Definition to accurately define and document land parcel ownership.",
        "benefits": "Ensuring clear and precise land ownership documentation."
    },
    {
        "title": "Marine Surveying (Bathymetric)",
        "description": "Underwater Precision Mapping with advanced sonar and echo-sounding technology.",
        "benefits": "Critical data for marine construction, dredging, port development, offshore construction, and environmental monitoring."
    },
    {
        "title": "3D Surveying",
        "description": "Detailed Model Creation using aerial photography and LiDAR for high-resolution 3D models.",
        "benefits": "Enhanced visualization for planning and analysis."
    },
    {
        "title": "Mapping Services",
        "description": "Detailed Area Mapping for various applications.",
        "benefits": "Accurate and detailed maps for diverse needs."
    },
    {
        "title": "Urban Planning and Development Support",
        "description": "Comprehensive Studies to support urban planning and area development.",
        "benefits": "Facilitating strategic planning and sustainable development."
    },
    {
        "title": "Surveying Consulting",
        "description": "Expert Advisory Services on land use, planning, and regulatory compliance.",
        "benefits": "Guidance for successful project execution."
    },
    {
        "title": "Environmental Change Monitoring",
        "description": "Monitoring Services to track and analyze changes in land use and environmental conditions over time.",
        "benefits": "Informed decision-making for environmental policies."
    },
    {
        "title": "Data Integration Services",
        "description": "GIS Integration to combine survey data with Geographic Information Systems (GIS) for enhanced analysis.",
        "benefits": "Improving data accessibility and usability."
    }
]

for service in services:
    with st.expander(service['title'], expanded=False):
        st.markdown('<div class="expander">', unsafe_allow_html=True)
        st.markdown(f'<div class="service-title">{service["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="service-description">{service["description"]}</div>', unsafe_allow_html=True)
        st.write("**Benefits:** " + service['benefits'])
        st.markdown('</div>', unsafe_allow_html=True)

footer()




# import streamlit as st
# from footer import footer

# css = """

# h1 {
#     color: #007aff; 
#     text-align: center;
#     margin: 40px 0; 
#     font-size: 48px; 
#     letter-spacing: 1.5px; 
#     font-weight: 700; 
# }

# h2, h3 {
#     color: #3D3D3D; 
#     text-align: center;
#     margin: 30px 0; 
#     font-weight: 600; 
# }

# p, li {
#     font-size: 16px; 
#     line-height: 1.6; 
#     margin: 0 0 10px; 
# }

# .service-title {
#     font-size: 20px; 
#     font-weight: bold; 
#     color: #007aff; 
#     margin-bottom: 5px; 
# }

# .service-description {
#     font-size: 16px; 
#     color: #333; 
#     margin-bottom: 10px; 
# }

# .streamlit-button {
#     background-color: #007aff; 
#     color: white; 
#     border-radius: 5px; 
#     padding: 12px 24px; 
#     font-weight: bold; 
#     border: none; 
#     transition: background-color 0.3s ease, transform 0.2s ease; 
# }
# .streamlit-button:hover {
#     background-color: #0056b3; 
#     transform: translateY(-2px); 
# }

# .streamlit-expanderHeader {
#     background-color: #007aff; 
#     color: white; 
#     border-radius: 5px; 
#     padding: 15px; 
#     transition: background-color 0.3s ease; 
# }
# .streamlit-expanderHeader:hover {
#     background-color: #0056b3; 
# }

# .streamlit-expanderContent {
#     background-color: #ffffff; 
#     padding: 20px; 
#     border-radius: 5px; 
#     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Enhanced shadow for depth */
# }

# .footer {
#     text-align: center;
#     color: #999;
#     font-size: 14px;
#     padding: 20px 0;
#     border-top: 1px solid #e0e0e0; 
#     margin-top: 40px; 
# }

# /* Media Queries for Responsiveness */
# @media (max-width: 768px) {
#     h1 {
#         font-size: 36px; /* Responsive font size */
#     }
#     .service-title {
#         font-size: 18px; /* Smaller titles on mobile */
#     }
#     .streamlit-button {
#         width: 100%; /* Full width buttons on mobile */
#     }
# }
# """

# # Set page configuration
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# # Apply the CSS styles
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# st.title("Our Services")

# # Introduction text
# introduction_text = """
# <div style="text-align: center; margin-bottom: 40px;">
#     <p style="font-size: 18px; line-height: 1.6; color: #333;">
#         At GeoLibya, we pride ourselves on delivering top-tier surveying and mapping solutions tailored to meet the diverse needs of our clients. 
#         With cutting-edge technology and a team of experienced professionals, we ensure precision and reliability in every project.
#         Our core services encompass a wide range of applications, from geodetic surveying to environmental monitoring, designed to support construction, urban planning, and sustainable development.
#     </p>
#     <p style="font-size: 18px; line-height: 1.6; color: #333;">
#         Explore our offerings below to discover how we can help you achieve your goals with accurate and insightful data.
#     </p>
# </div>
# """

# st.markdown(introduction_text, unsafe_allow_html=True)

# st.subheader("Core Services")

# services = [
#     {
#         "title": "Topographic and Geodetic Surveying",
#         "description": "Comprehensive Terrain Mapping using GPS, UAVs, Total Stations, and LiDAR to measure elevations and determine locations.",
#         "benefits": "Tailored solutions for construction, infrastructure development, urban planning, and environmental assessments."
#     },
#     {
#         "title": "Real Estate Surveying",
#         "description": "Legal Ownership Definition to accurately define and document land parcel ownership.",
#         "benefits": "Ensuring clear and precise land ownership documentation."
#     },
#     {
#         "title": "Marine Surveying (Bathymetric)",
#         "description": "Underwater Precision Mapping with advanced sonar and echo-sounding technology.",
#         "benefits": "Critical data for marine construction, dredging, port development, offshore construction, and environmental monitoring."
#     },
#     {
#         "title": "3D Surveying",
#         "description": "Detailed Model Creation using aerial photography and LiDAR for high-resolution 3D models.",
#         "benefits": "Enhanced visualization for planning and analysis."
#     },
#     {
#         "title": "Mapping Services",
#         "description": "Detailed Area Mapping for various applications.",
#         "benefits": "Accurate and detailed maps for diverse needs."
#     },
#     {
#         "title": "Urban Planning and Development Support",
#         "description": "Comprehensive Studies to support urban planning and area development.",
#         "benefits": "Facilitating strategic planning and sustainable development."
#     },
#     {
#         "title": "Surveying Consulting",
#         "description": "Expert Advisory Services on land use, planning, and regulatory compliance.",
#         "benefits": "Guidance for successful project execution."
#     },
#     {
#         "title": "Environmental Change Monitoring",
#         "description": "Monitoring Services to track and analyze changes in land use and environmental conditions over time.",
#         "benefits": "Informed decision-making for environmental policies."
#     },
#     {
#         "title": "Data Integration Services",
#         "description": "GIS Integration to combine survey data with Geographic Information Systems (GIS) for enhanced analysis.",
#         "benefits": "Improving data accessibility and usability."
#     }
# ]

# for service in services:
#     with st.expander(service['title'], expanded=False):
#         st.markdown('<div class="expander">', unsafe_allow_html=True)
#         st.markdown(f'<div class="service-title">{service["title"]}</div>', unsafe_allow_html=True)
#         st.markdown(f'<div class="service-description">{service["description"]}</div>', unsafe_allow_html=True)
#         st.write("**Benefits:** " + service['benefits'])
#         st.markdown('</div>', unsafe_allow_html=True)

# footer()




# import streamlit as st
# from footer import footer

# with open('./files/style.css') as f:
#     css = f.read()

# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# st.title("Our Services")

# # Introduction text
# introduction_text = """
# <div style="text-align: center; margin-bottom: 40px;">
#     <p style="font-size: 18px; line-height: 1.6; color: #333;">
#         At GeoLibya, we pride ourselves on delivering top-tier surveying and mapping solutions tailored to meet the diverse needs of our clients. 
#         With cutting-edge technology and a team of experienced professionals, we ensure precision and reliability in every project.
#         Our core services encompass a wide range of applications, from geodetic surveying to environmental monitoring, designed to support construction, urban planning, and sustainable development.
#     </p>
#     <p style="font-size: 18px; line-height: 1.6; color: #333;">
#         Explore our offerings below to discover how we can help you achieve your goals with accurate and insightful data.
#     </p>
# </div>
# """

# st.markdown(introduction_text, unsafe_allow_html=True)

    
# st.subheader("Core Services")

# services = [
#     {
#         "title": "Topographic and Geodetic Surveying",
#         "description": "Comprehensive Terrain Mapping using GPS, UAVs, Total Stations, and LiDAR to measure elevations and determine locations.",
#         "benefits": "Tailored solutions for construction, infrastructure development, urban planning, and environmental assessments."
#     },
#     {
#         "title": "Real Estate Surveying",
#         "description": "Legal Ownership Definition to accurately define and document land parcel ownership.",
#         "benefits": "Ensuring clear and precise land ownership documentation."
#     },
#     {
#         "title": "Marine Surveying (Bathymetric)",
#         "description": "Underwater Precision Mapping with advanced sonar and echo-sounding technology.",
#         "benefits": "Critical data for marine construction, dredging, port development, offshore construction, and environmental monitoring."
#     },
#     {
#         "title": "3D Surveying",
#         "description": "Detailed Model Creation using aerial photography and LiDAR for high-resolution 3D models.",
#         "benefits": "Enhanced visualization for planning and analysis."
#     },
#     {
#         "title": "Mapping Services",
#         "description": "Detailed Area Mapping for various applications.",
#         "benefits": "Accurate and detailed maps for diverse needs."
#     },
#     {
#         "title": "Urban Planning and Development Support",
#         "description": "Comprehensive Studies to support urban planning and area development.",
#         "benefits": "Facilitating strategic planning and sustainable development."
#     },
#     {
#         "title": "Surveying Consulting",
#         "description": "Expert Advisory Services on land use, planning, and regulatory compliance.",
#         "benefits": "Guidance for successful project execution."
#     },
#     {
#         "title": "Environmental Change Monitoring",
#         "description": "Monitoring Services to track and analyze changes in land use and environmental conditions over time.",
#         "benefits": "Informed decision-making for environmental policies."
#     },
#     {
#         "title": "Data Integration Services",
#         "description": "GIS Integration to combine survey data with Geographic Information Systems (GIS) for enhanced analysis.",
#         "benefits": "Improving data accessibility and usability."
#     }
# ]

# for service in services:
#     with st.expander(service['title'], expanded=False):
#         st.markdown('<div class="expander">', unsafe_allow_html=True)
#         st.markdown(f'<div class="service-title">{service["title"]}</div>', unsafe_allow_html=True)
#         st.markdown(f'<div class="service-description">{service["description"]}</div>', unsafe_allow_html=True)
#         st.write("**Benefits:** " + service['benefits'])
#         st.markdown('</div>', unsafe_allow_html=True)

# # Footer
# footer()
