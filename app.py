import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from io import BytesIO
import os

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

# Fungsi konversi gambar ke Base64 (untuk menangani file lokal JPG)
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return None

img_base64 = get_image_base64("Profile.jpg")
dashboard_base64 = get_image_base64("dashboard.jpg")

# =====================
# CUSTOM CSS
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp {{ background-color: #0f172a !important; color: #f1f5f9 !important; }}
    
    /* Sidebar */
    section[data-testid="stSidebar"] {{ background-color: #1e293b !important; border-right: 1px solid #334155; }}
    .sidebar-img {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid #facc15; object-fit: cover; display: block; margin: auto; }}

    /* Profile Frame (About Me) */
    .profile-frame {{ width: 350px; height: 350px; border-radius: 50%; padding: 10px; background: linear-gradient(135deg, #facc15, #854d0e); display: flex; justify-content: center; align-items: center; margin: auto; }}
    .profile-img-inner {{ width: 100%; height: 100%; border-radius: 50%; border: 8px solid #0f172a; object-fit: cover; }}

    /* Skill Bars */
    .skill-card {{ background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; height: 100%; }}
    .progress-bg {{ background-color: #334155; border-radius: 10px; width: 100%; height: 8px; margin-bottom: 15px; }}
    .progress-fill {{ background-color: #3b82f6; height: 100%; border-radius: 10px; }}

    /* Project Cards (Kuning Terang) */
    .project-card {{ background-color: #facc15; border-radius: 15px; overflow: hidden; height: 100%; transition: 0.3s; border: 1px solid #eab308; }}
    .project-card:hover {{ transform: translateY(-10px); box-shadow: 0 12px 24px rgba(0,0,0,0.4); }}
    .project-img-box {{ background-color: white; height: 200px; overflow: hidden; border-bottom: 2px solid #eab308; }}
    .project-img-box img {{ width: 100%; height: 100%; object-fit: cover; }} /* Memastikan dashboard.jpg pas */
    .project-content {{ padding: 20px; color: #0f172a; }}
    .project-tag {{ background: #0f172a; color: white; padding: 4px 10px; border-radius: 15px; font-size: 11px; margin-right: 5px; font-weight: 600; display: inline-block; margin-bottom: 5px; }}
    
    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    if img_base64:
        st.markdown(f'<div style="padding: 20px 0;"><img src="data:image/jpeg;base64,{img_base64}" class="sidebar-img"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Naufal Daffa</h2>", unsafe_allow_html=True)
    selected = option_menu(None, ["About Me", "Skills", "Projects", "Experience", "Contact"], 
        icons=["person", "cpu", "code-slash", "award", "envelope"], default_index=0,
        styles={"nav-link": {"color": "#94a3b8"}, "nav-link-selected": {"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"}})

# =====================
# MAIN SECTIONS
# =====================
if selected == "About Me":
    st.markdown("<h1 style='font-size: 3rem;'>About <span style='color:#facc15'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown(f"""<div style='font-size:18px; line-height:1.8; color:#cbd5e1;'>
        Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>. 
        Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.
        <br><br>
        <div style='margin-top: 10px;'>
            <span class='project-tag' style='background:#facc15; color:#0f172a; font-size: 14px; padding: 8px 16px;'>Clean Code</span>
            <span class='project-tag' style='background:#facc15; color:#0f172a; font-size: 14px; padding: 8px 16px;'>Coffee Lover</span>
            <span class='project-tag' style='background:#facc15; color:#0f172a; font-size: 14px; padding: 8px 16px;'>Team Player</span>
        </div>
        </div>""", unsafe_allow_html=True)
    with col2:
        if img_base64:
            st.markdown(f'<div class="profile-frame"><img src="data:image/jpeg;base64,{img_base64}" class="profile-img-inner"></div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown("<h1 style='text-align:center;'>Skills & <span style='color:#facc15'>Technologies</span></h1>", unsafe_allow_html=True)
    def render_s(n, p):
        st.markdown(f'<div style="display:flex; justify-content:space-between;"><span>{n}</span><span>{p}%</span></div><div class="progress-bg"><div class="progress-fill" style="width:{p}%;"></div></div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="skill-card"><h3>Programming</h3>', unsafe_allow_html=True)
        render_s("Python", 90); render_s("SQL", 85); render_s("PHP", 70); render_s("Java", 65)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="skill-card"><h3>Web Dev</h3>', unsafe_allow_html=True)
        render_s("HTML/CSS", 85); render_s("JavaScript", 70); render_s("Streamlit", 85); render_s("Laravel", 75)
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="skill-card"><h3>Tools & AI</h3>', unsafe_allow_html=True)
        render_s("Pandas", 85); render_s("YOLO", 75); render_s("Git", 85); render_s("Figma", 70)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='text-align:center;'>Featured <span style='color:#facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        img_tag = f'data:image/jpeg;base64,{dashboard_base64}' if dashboard_base64 else "https://via.placeholder.com/400x250"
        st.markdown(f"""
        <div class="project-card">
            <div class="project-img-box"><img src="{img_tag}"></div>
            <div class="project-content">
                <div style="font-size:22px; font-weight:800; margin-bottom:10px;">Air Quality Analysis</div>
                <div style="font-size:14px; margin-bottom:15px;">Dashboard interaktif untuk memantau data kualitas udara PM2.5 di berbagai stasiun pemantau secara real-time.</div>
                <div><span class="project-tag">Python</span><span class="project-tag">Pandas</span><span class="project-tag">Streamlit</span></div>
                <div style="margin-top:15px;"><a href="https://github.com/dapadeveloper" style="color:#0f172a; font-weight:800; text-decoration:none;">💻 View Code</a></div>
            </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='project-card'><div class='project-content'><h3>Human Detection</h3><p>Deteksi gerakan berbasis computer vision.</p></div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='project-card'><div class='project-content'><h3>Portfolio Web</h3><p>Website portofolio interaktif ini.</p></div></div>", unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h1>Experience</h1>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h3>Ketua Karang Taruna</h3><p style='color:#facc15'>Cikeas Gardenia (2022-2023)</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card' style='margin-top:15px;'><h3>Ketua MPK</h3><p style='color:#facc15'>SMK 1 Gunung Putri (2021-2022)</p></div>", unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='color:#facc15'>Contact Me</h1>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h4>📧 Fahmifalah081120@gmail.com</h4><h4>🐙 GitHub: dapadeveloper</h4></div>", unsafe_allow_html=True)