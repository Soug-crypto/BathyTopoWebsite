import streamlit as st
from footer import footer
from header import header
from streamlit_extras.add_vertical_space import add_vertical_space

with open('./files/style.css') as f:
    css = f.read()

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Inline CSS styles
st.markdown("""
    <style>
        .contact-form {
            background: #ffffff;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin: auto;
            width: 90%;  /* Full width with padding */
            max-width: 600px;  /* Limit width for better readability */
        }

        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            transition: border-color 0.3s;
        }

        .contact-form input:focus, .contact-form textarea:focus {
            border-color: #007aff; /* Change to your primary color */
            box-shadow: 0 0 5px rgba(0, 122, 255, 0.5);
        }        
    </style>
""", unsafe_allow_html=True)

header()

# Main title and subtitle
st.title("Contact Us")
add_vertical_space(3)
st.subheader("Get in Touch")

# Contact Form
with st.form("contact_form", clear_on_submit=True):
    
    name = st.text_input("Your Name", placeholder="Enter your name", key="name_input")
    email = st.text_input("Your Email", placeholder="Enter your email", key="email_input")
    message = st.text_area("Your Message", placeholder="Type your message here...", key="message_input")
    
    submitted = st.form_submit_button("Submit") 
    if submitted:
        st.success("Thank you for your message!")

add_vertical_space(3)

# Office Locations
st.subheader("Our Offices")
st.write("Address: [Your Address]")
st.write("Phone: [Your Phone Number]")
st.write("Email: [Your Email Address]")



# Footer
footer()





# import streamlit as st
# from footer import footer
# from header import header


# with open('./files/style.css') as f:
#     css = f.read()

# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# header()
# st.title("Contact Us")
# st.subheader("Get in Touch")

# # Contact Form
# with st.form("contact_form", clear_on_submit=True):
#     # st.markdown('<div class="contact-form">', unsafe_allow_html=True)
#     name = st.text_input("Your Name")
#     email = st.text_input("Your Email")
#     message = st.text_area("Your Message")
#     submitted = st.form_submit_button("Submit")
    
#     if submitted:
#         st.success("Thank you for your message!")
    
#     st.markdown('</div>', unsafe_allow_html=True)

# # Office Locations
# st.subheader("Our Offices")
# st.write("Address: [Your Address]")
# st.write("Phone: [Your Phone Number]")
# st.write("Email: [Your Email Address]")

# # Social Media Links
# st.subheader("Follow Us")
# st.markdown("""
#     <div class="social-links">
#     [Facebook](#) | [LinkedIn](#) | [Instagram](#) | [Twitter](#)
#     </div>
# """, unsafe_allow_html=True)

# # Footer
# footer()
