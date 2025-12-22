import streamlit as st
import sys
from pathlib import Path
import os

# Lấy thư mục gốc project (cha của 'app')
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Chạy streamlit từ root project để import app.*
# os.system(f"streamlit run app/Home.py")

home_page = st.Page(
    page="pages/1_Home.py",
    icon="🏠",
    default=True
)
project_1 = st.Page(
    page="pages/2_Dashboard.py",
    icon="📊"
)
project_2 = st.Page(
    page="pages/3_Realtime.py",
)
project_3 = st.Page(
    page="pages/4_MarketProfile.py",
)

pg = st.navigation(pages=[home_page,project_1,project_2,project_3])

pg.run()