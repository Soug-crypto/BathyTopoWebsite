import streamlit as st
from footer import footer

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("Our Services")
    
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

# Footer
st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)
footer()
