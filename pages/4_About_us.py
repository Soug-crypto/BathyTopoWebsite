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
    .about-section {
        margin: 20px 0;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
    }
    .team-member {
        text-align: center;
        margin: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 50px; /* More space above footer */
        font-size: 0.9em; /* Slightly larger footer text */
        color: #888;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

    st.title("About Us")
    st.subheader("Company Overview")
    
    # st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.write("""
        GeoLibya is a leading provider of high-precision surveying solutions in Libya, specializing in topographic and bathymetric surveys.
        We support a wide range of industries, including construction, environmental studies, urban planning, oil, and marine projects.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Mission and Vision
    st.subheader("Mission and Vision")
    # st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.write("""
        - **Mission:** To empower Libya’s development with accurate, reliable data that drives successful project outcomes across various industries.
        - **Vision:** To be Libya’s most trusted surveying partner, known for technological leadership, quality, and a dedication to client success.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Leadership Team with Image Cards
    st.subheader("Leadership Team")
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
    
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            st.markdown('<div class="team-member">', unsafe_allow_html=True)
            st.image(member['img'], width=120)
            st.write(f"**{member['name']}** - _{member['title']}_")
            st.write(member['bio'])
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Certifications & Affiliations
    st.subheader("Certifications & Affiliations")
    # st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.write("""
        - ISO 9001:2015
        - Member of [Industry Association]
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)
