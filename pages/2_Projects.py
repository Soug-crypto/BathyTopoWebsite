import streamlit as st
from footer import footer

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("Projects & Industries")
st.subheader("Our Expertise in Mapping Solutions")
st.write("We serve various industries including construction, oil & gas, and environmental monitoring.")

# Filter Dropdowns
st.markdown('<div class="filter-dropdown">', unsafe_allow_html=True)
industry_filter = st.selectbox("Select Industry", ["All", "Construction", "Oil & Gas", "Environmental Monitoring"])
project_type_filter = st.selectbox("Select Project Type", ["All", "Topographic", "Bathymetric"])
st.markdown('</div>', unsafe_allow_html=True)

# Example Projects
st.subheader("Featured Projects")

if industry_filter == "Construction":
    st.markdown('<div class="project-description">', unsafe_allow_html=True)
    st.write("**Project A:** [Brief description]")
    st.markdown('</div>', unsafe_allow_html=True)
elif industry_filter == "Oil & Gas":
    st.markdown('<div class="project-description">', unsafe_allow_html=True)
    st.write("**Project B:** [Brief description]")
    st.markdown('</div>', unsafe_allow_html=True)
elif industry_filter == "Environmental Monitoring":
    st.markdown('<div class="project-description">', unsafe_allow_html=True)
    st.write("**Project C:** [Brief description]")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.write("Select an industry to view projects.")

# Footer
st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)
footer()
