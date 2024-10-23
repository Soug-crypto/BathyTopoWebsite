import streamlit as st
from footer import footer

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


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
footer()
