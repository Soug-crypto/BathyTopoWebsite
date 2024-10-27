import streamlit as st
from footer import footer
from header import header


# Services Data with Experience
services = [
    {
        "title": "Oil and Gas Sector",
        "content": [
            "GeoLibya has established a prominent presence in the oil and gas industry, creating ground control networks for major companies. "
            "We have marked **57 wells** in the Al-Wafa field for Agip and established around **150 ground control points** for seismic surveys in the Ghadames Basin, alongside "
            "**45 ground control points** for magnetotelluric surveys in the Sirte Basin.",
            "Our geodetic solutions have also supported key players such as **Repsol**, for whom we developed networks linking the "
            "Murzuq and Kufra Basins to the international network (ITRF). We conducted airborne magnetic surveys and identified well locations in "
            "the NC187 concession field, assisting companies like **Wintershall**, **Oxy Libya**, **Statoil**, **OMV**, and **BG Companies** in enhancing their exploration efforts."
        ],
        "experience": [
            ("Agip Oil and Gas Company", [
                "Established **150 ground control points** for seismic surveys in the Ghadames Basin.",
                "Set up **45 ground control points** for magnetotelluric surveys in the Sirte Basin.",
                "Mapped **57 wells** in the Al-Wafa field."
            ]),
            ("Repsol", [
                "Developed geodetic networks for the Murzuq and Kufra Basins, linking them to the international network (ITRF).",
                "Conducted airborne magnetic surveys and identified well locations in the NC187 concession field."
            ]),
            ("Wintershall", [
                "Identified and marked sites of operational and non-operational wells, including future drilling sites."
            ]),
            ("Oxy Libya, Statoil, OMV, and BG Companies", [
                "Mapped various well locations for exploration."
            ]),
            ("Al-Mabrouk Oil Operations Company", [
                "Identified and marked oil and gas wells in the Al-Mabrouk field."
            ])
        ]
    },
    {
        "title": "Infrastructure and Water Management",
        "content": [
            "Beyond oil and gas, GeoLibya excels in infrastructure and water management. We mapped over **30,000 hectares** "
            "for the Great Man-Made River project and developed satellite maps for **225,000 hectares**, creating a geographic "
            "database for areas facing water shortages.",
            "In collaboration with the General Electricity Company, we mapped land and marine sites for power and desalination stations in major cities, "
            "including **Benghazi** and **Tripoli**. We also conducted marine mapping for the Port of Hamidiya and developed "
            "comprehensive plans for the Port of Al-Silisla in the Tajoura District."
        ],
        "experience": [
            ("Great Man-Made River Water Investment Authority", [
                "Mapped over **30,000 hectares** for the second phase of the Great Man-Made River project.",
                "Developed satellite maps for **225,000 hectares** and created a geographic database for areas affected by water shortages."
            ]),
            ("General Electricity Company", [
                "Mapped land and marine sites for power and desalination stations in Benghazi and Tripoli."
            ]),
            ("Port Authority", [
                "Conducted marine mapping of the Port of Hamidiya."
            ]),
            ("Tajoura District", [
                "Developed a general plan for the Port of Hamidiya and completed mapping for the Port of Al-Silisla."
            ])
        ]
    },
    {
        "title": "Agriculture and Environmental Planning",
        "content": [
            "In agriculture and environmental planning, we performed topographic mapping for **10,000 hectares** at the Wadi Al-Lawd project and "
            "mapped forest boundaries for public forests. Our collaboration with the Agricultural Research Center included surveying and soil studies for irrigated "
            "wheat across **100,000 hectares**. Additionally, we supported the General People’s Committee for Animal Wealth by mapping the "
            "Al-Kharmah Forest for the establishment of the Al-Amha poultry project."
        ],
        "experience": [
            ("Agriculture Sector Projects", [
                "Conducted topographic mapping for **10,000 hectares** at the Wadi Al-Lawd project and mapped forest boundaries for public forests."
            ]),
            ("Agricultural Research Center", [
                "Performed surveying and soil studies for irrigated wheat across **100,000 hectares**."
            ]),
            ("General People’s Committee for Animal Wealth", [
                "Mapped the Al-Kharmah Forest for the establishment of the Al-Amha poultry project."
            ])
        ]
    },
    {
        "title": "Real Estate and Urban Development",
        "content": [
            "Our contributions to urban development are significant. We surveyed over **72,000 properties** outside urban plans for the Real Estate "
            "Registration and Documentation Authority, facilitating real estate registration initiatives. We also mapped **87 coastal sites** for "
            "the Tourism Development Authority, promoting foreign investment along the Libyan coast. Our partnership with the United Nations Development Program led to "
            "the preparation of a base map for the historical oasis in Ghadames."
        ],
        "experience": []  # Add relevant experience data if available
    },
    {
        "title": "International Projects",
        "content": [
            "Internationally, we extend our expertise to projects in **Chad** and **Mali**, utilizing advanced satellite imagery. "
            "We've completed surveying and soil studies for the African Investment Company, covering **20,000 hectares** in Chad and "
            "**25,000 hectares** in Mali. The Libyan African Investment Company has also benefited from our comprehensive surveying and soil studies in these regions."
        ],
        "experience": []  # Add relevant experience data if available
    }
]

# Introduction and conclusion texts
introduction_text = (
    "<p>At <strong>GeoLibya</strong>, our leadership team brings a wealth of experience in modernizing Libya’s geodetic infrastructure. "
    "This strong foundation enables us to deliver <strong>accurate geodetic measurements</strong> and calculations across various sectors, "
    "driving innovation and efficiency in our projects.<p>"
)

conclusion_text = (
    "<p>Our diverse projects highlight <strong>GeoLibya's</strong> unwavering commitment to delivering "
    "<strong>high-quality geodetic and mapping solutions</strong> that drive <strong>economic growth</strong> "
    "and <strong>sustainable development</strong> both in Libya and beyond. "
    "With a proven track record of excellence in serving esteemed clients such as <strong>Repsol</strong>, "
    "<strong>Statoil</strong>, and the <strong>General Electricity Company</strong>, "
    "we consistently strive to exceed expectations in every endeavor.<p>"
)

# Custom CSS for a refined look
custom_css = """
h1 {
    color: #1A1A1A; 
    text-align: center;
    margin: 60px 0; 
    font-size: 48px; 
    letter-spacing: 1.5px; 
    font-weight: 700;
}

h2, h3 {
    color: #3D3D3D; 
    text-align: center;
    margin: 30px 0; 
    font-weight: 600; 
}

p, li {
    font-size: 16px; 
    line-height: 1.6; 
}

.streamlit-button {
    background-color: #007aff; 
    color: white; 
    border-radius: 5px; 
    padding: 10px 20px; 
    font-weight: bold; 
    transition: background-color 0.3s ease; 
}
.streamlit-button:hover {
    background-color: #0056b3; 
}

.streamlit-expanderHeader {
    background-color: #007aff; 
    color: white; 
    border-radius: 5px; 
    padding: 12px; 
    transition: background-color 0.3s ease; 
}
.streamlit-expanderHeader:hover {
    background-color: #0056b3; 
}

.streamlit-expanderContent {
    background-color: #ffffff; 
    padding: 20px; 
    border-radius: 5px; 
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); 
}

.footer {
    text-align: center;
    color: #999;
    font-size: 14px;
    padding: 20px 0;
    border-top: 1px solid #e0e0e0; 
    margin-top: 40px; 
}
"""

# Function to render service expander with experience
def render_service_expander(service):
    with st.expander(service['title'], expanded=False):
        for paragraph in service['content']:
            st.markdown(paragraph, unsafe_allow_html=True)

        if service.get('experience'):
            st.markdown('<h3>Overview of Experience</h3>', unsafe_allow_html=True)
            render_experience(service['experience'])

# Function to render experience details
def render_experience(experience):
    for project, activities in experience:
        st.markdown(f'<div class="project-title">{project}</div>', unsafe_allow_html=True)
        for activity in activities:
            st.write(f"• {activity}")

# Load custom CSS from external file (if necessary)
def load_css(file_path):
    with open(file_path) as f:
        return f.read()

# Set up page configuration
def configure_page():
    st.set_page_config(
        page_title="GeoLibya Projects & Industries",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items=None
    )

# Apply CSS styles
def apply_styles(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Main function to orchestrate the app
def main():
    # Load and apply external CSS
    css = load_css('./files/style.css')
    apply_styles(css)

    apply_styles(custom_css)
    header()

    st.markdown("<h1>Our Expertise in Mapping Solutions</h1>", unsafe_allow_html=True)
    st.markdown(introduction_text, unsafe_allow_html=True)
    st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)

    for service in services:
        render_service_expander(service)

    st.markdown(conclusion_text, unsafe_allow_html=True)


    footer()

if __name__ == "__main__":
    configure_page()
    main()