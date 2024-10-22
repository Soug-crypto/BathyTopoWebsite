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
    .contact-form {
        margin: 20px 0;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
    }
    .social-links {
        margin-top: 10px;
        text-align: center;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #45A049;
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


st.title("Contact Us")
st.subheader("Get in Touch")

# Contact Form
with st.form("contact_form", clear_on_submit=True):
    # st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success("Thank you for your message!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Office Locations
st.subheader("Our Offices")
st.write("Address: [Your Address]")
st.write("Phone: [Your Phone Number]")
st.write("Email: [Your Email Address]")

# Social Media Links
st.subheader("Follow Us")
st.markdown("""
    <div class="social-links">
    [Facebook](#) | [LinkedIn](#) | [Instagram](#) | [Twitter](#)
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 GeoLibya. All rights reserved.</div>', unsafe_allow_html=True)