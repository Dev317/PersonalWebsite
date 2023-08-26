import os
import streamlit as st
from PIL import Image
from utils.config import get_config
from utils.image_util import get_circular_image


st.set_page_config(page_title="Minh's Website",
                   page_icon="✨",
                   initial_sidebar_state="auto")

ASSET_DIR = f"{os.getcwd()}/assets"
CONFIG = get_config()
PAGE = "About"


st.sidebar.markdown(f"""
### Copyright ©
```
author={{Vu Quang Minh}},
year={{2023}}
```
***
""",
unsafe_allow_html=True)

# Profile
PROFILE_SECTION = "profile"
profile_pic = get_circular_image(Image.open(f"{ASSET_DIR}/profile_pic.jpeg"))
col1, col2 = st.columns(spec=2, gap="small")
with col1:
    st.image(profile_pic,
            width=270,
            clamp=True,)
with col2:
    st.markdown(f"### {CONFIG[PAGE][PROFILE_SECTION]['name']}")
    st.code(f"{CONFIG[PAGE][PROFILE_SECTION]['description']}")
    st.markdown("**Contacts:**")
    st.write("📫 Gmail:", CONFIG[PAGE][PROFILE_SECTION]['email'])
    st.write("📱 Mobile:", CONFIG[PAGE][PROFILE_SECTION]['phone'])

# Social
st.write("\n\n")
SOCIAL_SECTION = "social"
container = st.container()
with container:
    icon1, icon2, icon3, icon4, icon5 = st.columns(spec=[1,1,1,1,1])
    with icon1:
        st.markdown(f"[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)]({CONFIG[PAGE][SOCIAL_SECTION]['github']})")
    with icon2:
        st.markdown(f"[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)]({CONFIG[PAGE][SOCIAL_SECTION]['medium']})")
    with icon3:
        st.markdown(f"[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)]({CONFIG[PAGE][SOCIAL_SECTION]['linkedin']})")
    with icon4:
        st.markdown(f"[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)]({CONFIG[PAGE][SOCIAL_SECTION]['instagram']})")
    with icon5:
        st.markdown(f"[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)]({CONFIG[PAGE][SOCIAL_SECTION]['facebook']})")

# Summary
st.write("\n\n")
SUMMARY_SECTION = "summary"
st.markdown("### 📖 Summary", unsafe_allow_html=True)
st.info(CONFIG[PAGE][SUMMARY_SECTION]['description'])

# Education
EDUCATION_SECTION = "education"
st.markdown("***")
st.subheader("👨‍🎓 Education")

def write_education(school, year, degree, description):
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(school)
    with col2:
        st.markdown(year)
    st.markdown(degree)
    st.markdown(description)

for i in CONFIG[PAGE][EDUCATION_SECTION]:
    write_education(school=i['school'],
                    year=i['year'],
                    degree=i['degree'],
                    description=i['description'])

# Technology stack
TECHNOLOGY_STACK_SECTION = "technology_stack"
st.markdown("***")
st.subheader("⚙️ Technology Stack")
st.write(CONFIG[PAGE][TECHNOLOGY_STACK_SECTION]['description'])

# Work Experience
WORK_EXPERIENCE_SECTION = "work_experience"
st.markdown('***')
st.subheader("💼 Experience")

def write_work(job, duration, company, description):
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"{job}")
    with col2:
        st.markdown(f"{duration}")
    st.markdown(company)
    st.markdown(description)

for i in CONFIG[PAGE][WORK_EXPERIENCE_SECTION]:
    write_work(
        job=i['job'],
        duration=i['duration'],
        company=i['company'],
        description=i['description']
    )
