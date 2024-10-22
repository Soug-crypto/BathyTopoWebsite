import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        background-color: #F5F5F5;
        color: #333;
    }
    h1, h2 {
        color: #1A1A1A;
    }
    .project-description {
        margin: 10px 0;
        padding: 15px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .filter-dropdown {
        margin-bottom: 20px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

def projects_page():
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

projects_page()
