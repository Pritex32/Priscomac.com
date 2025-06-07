import streamlit as st

st.set_page_config(
    page_title="priscomac",
    page_icon="🌟", 
    layout='wide' , # emoji or path to icon
    initial_sidebar_state="collapsed"  # options: "auto", "expanded", "collapsed"
)
# Inject Bootstrap CSS from CDN
from PIL import Image
# Simple colored horizontal bar
image='IMG-20250531-WA0006 (2).jpg'
open_image=Image.open(image)
resize=open_image.resize((100,50))
col1,col2=st.columns([3,1])
with col1:
     col3,col4=st.columns([1,5])
     with col3:
          st.write(resize,width=60)
          
     with col4:
         st.header(f"Priscomac Data Solutions")
    
    
with col2:
    st.markdown('call: +2347037567690')


menu = ["Home", "Services", "Projects", "Contact"]
choice = st.radio("Navigate 👇", menu, horizontal=True)

# Simple colored horizontal bar
st.markdown("""
<div style='
    background-color: #4CAF50;
    height: 5px;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
'></div>
""", unsafe_allow_html=True)

if choice == "Home":
    st.header("🧠 About Us")
    st.markdown("""

At Priscomac,
                 we are committed to providing solutions through data. 
                As a forward-thinking data science company, we help individuals, 
                businesses, and organizations turn complex data into clear, actionable insights.
                Driven by the belief that **data is a powerful tool** for solving real-world problems, 
                we offer cutting-edge analytics, predictive modeling, and tailored solutions that 
                empower smarter decision-making. Whether you're beginning your data journey or aiming 
                to scale your analytics efforts, Priscomac is here to support you with expertise, innovation, and integrity.
                """)
    st.markdown("### 📌 [**👉 Book Now**]('https://github.com/Pritex32/rocky_art_booking_service')")


    
    st.markdown("---")

    col1,col2=st.columns([3,1])
    with col1:
         st.subheader('Vision')
         st.info("To empower people and businesses by delivering innovative, data-driven solutions to real-world problems.")
    with col2:
        st.subheader('Mission')
        st.info("To lead the way in data science innovation — turning information into insight, and insight into intelligent action for a better tomorrow.")
elif choice == "Services":
    st.header("Priscomac Core Services:")
    st.markdown("""
- Data Analysis & Visualization: Discover insights and create dashboards.

- Predictive Modeling & Machine Learning: Forecasting, classification, and recommendations.

- Data Cleaning & Preparation: Organize and preprocess data for analysis.

- Business Intelligence & Strategy: Turn data into actionable business plans.

- Natural Language Processing: Analyze text data like reviews or social media.

- Data Engineering & Automation: Build pipelines and automate data tasks.

- Custom Apps & Software: Develop data-driven applications and dashboards.
- Cloud computing, computer vision & model deployment               

- Training & Workshops: Teach data skills to individuals or teams.

- Advanced Analytics: Conduct A/B tests, pricing optimization, and customer analytics.

""")
elif choice == "Projects":
    st.header("Projects")
    if st.button('View Projects'):
         st.markdown('https://pritex32.github.io/prisca.github.io/')
elif choice == "Contact":
    st.header("Contact")
    if st.button('Contact us'):
         st.markdown('https://www.linkedin.com/in/prisca-ukanwa-800a1117a/')
