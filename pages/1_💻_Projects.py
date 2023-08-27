import os
import streamlit as st
from utils.config import get_config
from PIL import Image
from streamlit_extras.badges import badge


st.header("Personal Workspace")
st.sidebar.markdown(f"""
Copyright ©
```
author={{Vu Quang Minh}},
year={{2023}}
```
***
""",
unsafe_allow_html=True)

ASSET_DIR = f"{os.getcwd()}/assets"
CONFIG = get_config()
PAGE = "Projects"

def get_project_names():
    names = []
    for i in CONFIG[PAGE]:
        names.append(CONFIG[PAGE][i]["project_name"])
    return names

project_names = get_project_names()
tabs = st.tabs(project_names)

for idx, tab in enumerate(tabs):
    with tab:
        proj_details = CONFIG[PAGE][project_names[idx]]
        st.image(Image.open(f"{ASSET_DIR}/{proj_details['image_path']}"))
        with st.expander("Details", expanded=True):
            badge(type="github",
                  url=proj_details['repo_link'],
                  name=proj_details['repo_name'])
            info = f"{proj_details['description']} \n\n Technologies: {proj_details['tech_stack']}"
            st.info(info, icon="🔥")

        st.markdown("***")

