import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64
from io import BytesIO

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

# Fungsi memproses gambar (Base64)
def get_image_base64(path):
    try:
        img = Image.open(path)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

img_base64 = get_image_base64("Profile.jpg")

# =====================
# CUSTOM CSS (DARK MODE & UI)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp {{ background-color: #0f172a !important; color: #f1f5f9 !important; }}
    html, body, [class*="css"] {{ font-family: 'Plus Jakarta Sans', sans-serif; }}

    /* Sidebar Dark */
    section[data-testid="stSidebar"] {{ background-color: #1e293b !important; border-right: 1px solid #334155; }}
    .sidebar-img {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid #facc15; object-fit: cover; display: block; margin: auto; }}

    /* About Me Photo Frame */
    .profile-frame {{ width: 350px; height: 350px; border-radius: 50%; padding: 10px; background: linear-gradient(135deg, #facc15, #854d0e); display: flex; justify-content: center; align-items: center; margin: auto; }}
    .profile-img-inner {{ width: 100%; height: 100%; border-radius: 50%; border: 8px solid #0f172a; object-fit: cover; display: block; }}

    /* SKILLS MODEL (Sesuai Gambar Contoh) */
    .skill-card {{ background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; height: 100%; }}
    .skill-header {{ color: #facc15; font-weight: 800; margin-bottom: 20px; font-size: 20px; text-transform: uppercase; }}
    .skill-label-container {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; margin-top: 15px; }}
    .skill-name {{ color: #f1f5f9; font-weight: 600; font-size: 14px; }}
    .skill-value {{ color: #cbd5e1; font-size: 13px; }}
    .progress-bg {{ background-color: #334155; border-radius: 10px; width: 100%; height: 8px; }}
    .progress-fill {{ background-color: #3b82f6; height: 100%; border-radius: 10px; }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    if img_base64:
        st.markdown(f'<div style="padding: 20px 0;"><img src="data:image/jpeg;base64,{img_base64}" class="sidebar-img"></div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #f1f5f9; font-weight: 800;'>Naufal Daffa</h3>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Skills", "Projects", "Experience", "Contact"],
        icons=["person-fill", "cpu-fill", "code-slash", "award-fill", "envelope-fill"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent", "padding": "0"},
            "nav-link": {"font-size": "15px", "text-align": "left", "color": "#94a3b8"},
            "nav-link-selected": {"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"},
        }
    )

# =====================
# RENDER SKILL BAR
# =====================
def render_skill(name, percent):
    st.markdown(f"""
        <div class="skill-label-container">
            <span class="skill-name">{name}</span>
            <span class="skill-value">{percent}%</span>
        </div>
        <div class="progress-bg"><div class="progress-fill" style="width: {percent}%;"></div></div>
    """, unsafe_allow_html=True)

# =====================
# MAIN CONTENT
# =====================
if selected == "About Me":
    st.markdown("<h1 style='font-size: 3rem; color: #f1f5f9;'>About <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown("""<div style='color:#cbd5e1; font-size:18px; line-height:1.8;'>
        Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>.
        Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek. 
        Mantan Ketua Karang Taruna dan Ketua MPK yang memiliki jiwa kepemimpinan kuat.</div>""", unsafe_allow_html=True)
    with col2:
        if img_base64:
            st.markdown(f'<div class="profile-frame"><img src="data:image/jpeg;base64,{img_base64}" class="profile-img-inner"></div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown("<h1 style='text-align: center; color: #facc15;'>Skills & Technologies</h1>", unsafe_allow_html=True)
    st.write("##")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown('<div class="skill-card"><div class="skill-header">Programming</div>', unsafe_allow_html=True)
        render_skill("Python", 90)
        render_skill("SQL", 85)
        render_skill("Java", 70)
        render_skill("PHP (Laravel)", 75)
        render_skill("JavaScript", 65)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-card"><div class="skill-header">Web Development</div>', unsafe_allow_html=True)
        render_skill("HTML", 85)
        render_skill("CSS", 80)
        render_skill("Streamlit", 85)
        render_skill("Flask", 60)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="skill-card"><div class="skill-header">Data & AI Tools</div>', unsafe_allow_html=True)
        render_skill("Pandas", 85)
        render_skill("Scikit-Learn", 80)
        render_skill("OpenCV / YOLO", 75)
        render_skill("Git / GitHub", 85)
        render_skill("Figma", 70)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1>Projects</h1>", unsafe_allow_html=True)
    st.info("Air Quality Analysis Dashboard & Human Movement Detection.")

elif selected == "Experience":
    st.markdown("<h1>Experience</h1>", unsafe_allow_html=True)
    st.write("- Ketua Karang Taruna Cikeas Gardenia (2022-2023)")
    st.write("- Ketua MPK SMK 1 Gunung Putri (2021-2022)")

elif selected == "Contact":
    st.markdown("<h1>Contact</h1>", unsafe_allow_html=True)
    st.write("Email: Fahmifalah081120@gmail.com")