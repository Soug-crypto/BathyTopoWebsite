import streamlit as st

# Custom CSS for improved styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        background-color: #F9F9F9; /* Lighter background for a modern look */
        color: #333;
        line-height: 1.6; /* Improve readability */
    }
    h1 {
        color: #2C3E50; /* Dark blue */
        text-align: center;
        margin-bottom: 30px; /* More space below title */
    }
    h2, h3 {
        color: #34495E; /* Lighter blue for subheaders */
        text-align: center;
        margin: 25px 0; /* Consistent spacing */
    }
    
    .fact {
        font-weight: bold;
        color: #2980B9; /* Distinct blue for facts */
    }
    .project-title {
        font-weight: bold;
        margin-top: 15px; /* More space above titles */
    }
    .footer {
        text-align: center;
        margin-top: 50px; /* More space above footer */
        font-size: 0.9em; /* Slightly larger footer text */
        color: #888;
    }
    /* Custom styles for the expander */
    .streamlit-expanderHeader {
        background-color: #46A748; /* Change header background color */
        color: white; /* Change header text color */
        border-radius: 5px; /* Rounded corners for the header */
        padding: 10px; /* Padding for the header */
        transition: background-color 0.3s ease; /* Smooth transition */
    }
    .streamlit-expanderHeader:hover {
        background-color: #46A748; /* Change background on hover */
    }
    .streamlit-expanderContent {
        background-color: #ecf0f1; /* Light background for content */
        padding: 15px; /* Padding for the content */
        border-radius: 5px; /* Rounded corners for the content */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.title("Facts and Figures")


# Introduction
st.write(
    "At GeoLibya, our leadership team boasts extensive experience in modernizing Libya’s geodetic infrastructure. "
    "This solid foundation empowers us to deliver precise geodetic measurements and calculations across various sectors."
)
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

# Expander for each service with experience
for service in services:
    with st.expander(service['title'], expanded=False):
        for paragraph in service['content']:
            st.write(paragraph)
        
        # Experience overview within each expander
        if service['experience']:  # Check if experience is not empty
            st.markdown('<h3>Overview of Experience</h3>', unsafe_allow_html=True)
            for project, activities in service['experience']:
                if activities:  # Check if activities is not empty
                    st.markdown(f'<div class="project-title">{project}</div>', unsafe_allow_html=True)
                    for activity in activities:
                        st.write(f"• {activity}")

# Conclusion
st.write(
    "These diverse projects underscore GeoLibya's commitment to delivering high-quality geodetic and mapping solutions that drive economic growth and sustainable development, both in Libya and beyond. "
    "With a trusted track record serving clients like Repsol, Statoil, and the General Electricity Company, we consistently strive for excellence in every endeavor."
)

# Footer
st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)
