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

# FUNGSI UNTUK MERENDER GAMBAR LOKAL KE HTML (BASE64)
def get_image_base64(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                data = f.read()
                return base64.b64encode(data).decode()
        except:
            return None
    return None

# Load semua gambar lokal
img_profile = get_image_base64("Profile.jpg")
img_dashboard = get_image_base64("dashboard.jpg")
img_human = get_image_base64("human.jpg")
img_portofolio = get_image_base64("portofolio.jpg")

# =====================
# CUSTOM CSS (DARK MODE & UI)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp {{ background-color: #0f172a !important; color: #f1f5f9 !important; }}
    html, body, [class*="css"] {{ font-family: 'Plus Jakarta Sans', sans-serif; }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{ background-color: #1e293b !important; border-right: 1px solid #334155; }}
    .sidebar-img {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid #facc15; object-fit: cover; display: block; margin: auto; }}

    /* Profile Frame About Me */
    .profile-frame {{ width: 350px; height: 350px; border-radius: 50%; padding: 10px; background: linear-gradient(135deg, #facc15, #854d0e); display: flex; justify-content: center; align-items: center; margin: auto; }}
    .profile-img-inner {{ width: 100%; height: 100%; border-radius: 50%; border: 8px solid #0f172a; object-fit: cover; display: block; }}

    /* Skill Card & Progress Bar */
    .skill-card {{ background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; height: 100%; }}
    .skill-header {{ color: #facc15; font-weight: 800; margin-bottom: 20px; font-size: 20px; text-transform: uppercase; }}
    .progress-bg {{ background-color: #334155; border-radius: 10px; width: 100%; height: 8px; margin-bottom: 15px; }}
    .progress-fill {{ background-color: #3b82f6; height: 100%; border-radius: 10px; }}
    .skill-label {{ display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 4px; }}

    /* Project Card Grid (Kuning Kontras) */
    .project-card {{ background-color: #facc15; border-radius: 15px; overflow: hidden; height: 100%; transition: 0.3s; border: 1px solid #eab308; }}
    .project-card:hover {{ transform: translateY(-10px); box-shadow: 0 12px 24px rgba(0,0,0,0.4); }}
    .project-img-box {{ background-color: #ffffff; height: 200px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
    .project-img-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    .project-content {{ padding: 20px; color: #0f172a; }}
    .project-tag {{ background: #0f172a; color: white; padding: 4px 10px; border-radius: 15px; font-size: 11px; margin-right: 5px; font-weight: 600; display: inline-block; margin-bottom: 5px; }}

    /* Contact Section Styling */
    .contact-container {{ background-color: #facc15; padding: 40px; border-radius: 20px; color: #0f172a; margin-top: 20px; }}
    .contact-info-box {{ display: flex; align-items: center; margin-bottom: 25px; }}
    .contact-icon {{ background-color: #0f172a; color: #facc15; width: 45px; height: 45px; border-radius: 10px; display: flex; justify-content: center; align-items: center; margin-right: 15px; font-size: 18px; }}
    .form-box {{ background-color: #1e293b; padding: 30px; border-radius: 20px; color: white; }}
    .stForm {{ border: none !important; padding: 0 !important; }}
    
    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    if img_profile:
        st.markdown(f'<div style="padding: 20px 0;"><img src="data:image/jpeg;base64,{img_profile}" class="sidebar-img"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Naufal Daffa</h2>", unsafe_allow_html=True)
    selected = option_menu(None, ["About Me", "Skills", "Projects", "Experience", "Contact"], 
        icons=["person", "cpu", "code-slash", "award", "envelope"], default_index=0,
        styles={"nav-link": {"color": "#94a3b8"}, "nav-link-selected": {"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"}})

# =====================
# HELPER FUNCTIONS
# =====================
def skill_bar(name, percent):
    st.markdown(f'<div class="skill-label"><span>{name}</span><span>{percent}%</span></div><div class="progress-bg"><div class="progress-fill" style="width: {percent}%;"></div></div>', unsafe_allow_html=True)

def render_project(title, desc, tags, img_b64, link_url=None, is_deployed=True):
    img_src = f'src="data:image/jpeg;base64,{img_b64}"' if img_b64 else 'src="" alt="Image Not Found"'
    t_html = "".join([f'<span class="project-tag">{t}</span>' for t in tags])
    action_html = f'<a href="{link_url}" target="_blank" style="color:#0f172a; font-weight:800; text-decoration:none;">🔗 Go to Website</a>' if is_deployed and link_url else '<span style="color:#475569; font-weight:600; font-style:italic;">⚠️ Belum di-deploy</span>'

    st.markdown(f"""
    <div class="project-card">
        <div class="project-img-box"><img {img_src}></div>
        <div class="project-content">
            <div style="font-size: 22px; font-weight: 800; margin-bottom: 10px;">{title}</div>
            <div style="font-size: 14px; line-height: 1.5; margin-bottom: 15px; min-height: 60px;">{desc}</div>
            <div>{t_html}</div>
            <div style="margin-top:15px;">{action_html}</div>
        </div>
    </div>""", unsafe_allow_html=True)

# =====================
# MAIN CONTENT
# =====================
if selected == "About Me":
    st.markdown("<h1>About <span style='color:#facc15'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown(f"""<div style='font-size:18px; line-height:1.8; color:#cbd5e1;'>
        Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>. 
        Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.
        Mantan Ketua Karang Taruna dan Ketua MPK yang memiliki jiwa kepemimpinan kuat.
        <br><br>
        <span class='project-tag' style='background:#facc15; color:#0f172a; font-size:14px; padding:8px 15px;'>Clean Code</span>
        <span class='project-tag' style='background:#facc15; color:#0f172a; font-size:14px; padding:8px 15px;'>Coffee Lover</span>
        <span class='project-tag' style='background:#facc15; color:#0f172a; font-size:14px; padding:8px 15px;'>Team Player</span>
        <span class='project-tag' style='background:#facc15; color:#0f172a; font-size:14px; padding:8px 15px;'>Pemalang, Indonesia</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        if img_profile:
            st.markdown(f'<div class="profile-frame"><img src="data:image/jpeg;base64,{img_profile}" class="profile-img-inner"></div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown("<h1 style='text-align:center;'>Skills & <span style='color:#facc15'>Technologies</span></h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="skill-card"><div class="skill-header">Programming</div>', unsafe_allow_html=True)
        skill_bar("Python", 90); skill_bar("SQL", 85); skill_bar("PHP", 70); skill_bar("Java", 65)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="skill-card"><div class="skill-header">Web Dev</div>', unsafe_allow_html=True)
        skill_bar("HTML/CSS", 85); skill_bar("JavaScript", 70); skill_bar("Streamlit", 85); skill_bar("Laravel", 75)
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="skill-card"><div class="skill-header">Tools & AI</div>', unsafe_allow_html=True)
        skill_bar("Pandas", 85); skill_bar("YOLO", 75); skill_bar("Git", 85); skill_bar("Figma", 70)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='text-align:center;'>Featured <span style='color:#facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        render_project("Air Quality Analysis", "Dashboard interaktif analisis data kualitas udara PM2.5 real-time.", ["Python", "Pandas", "Streamlit"], img_dashboard, link_url="https://air-quality-analysis-bjdvcvytswek2toxrkuwbe.streamlit.app/")
    with col2:
        render_project("Human Detection", "Sistem deteksi gerakan manusia menggunakan Computer Vision dan YOLO.", ["Python", "OpenCV", "YOLO"], img_human, is_deployed=False)
    with col3:
        render_project("Portfolio Web", "Website portofolio ini dibangun dengan custom CSS dan Streamlit.", ["Streamlit", "CSS", "UI/UX"], img_portofolio, link_url="https://portfoliosaya-hvqxtxdyyursjexk4hmorz.streamlit.app/")

elif selected == "Experience":
    st.markdown("<h1>Experience</h1>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h3>Ketua Karang Taruna</h3><p style='color:#facc15'>Cikeas Gardenia (2022-2023)</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card' style='margin-top:15px;'><h3>Ketua MPK</h3><p style='color:#facc15'>SMK 1 Gunung Putri (2021-2022)</p></div>", unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='text-align: center; color: #facc15;'>Get In <span style='color: white;'>Touch</span></h1>", unsafe_allow_html=True)
    st.markdown('<div class="contact-container">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.2], gap="large")
    with c1:
        st.markdown("<h2 style='color: #0f172a; font-weight: 800;'>Let's work together</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #334155;'>Feel free to reach out for collaborations or just a friendly hello!</p>", unsafe_allow_html=True)
        for d in [{"i":"📧","l":"Email","v":"Fahmifalah081120@gmail.com"}, {"i":"🐙","l":"GitHub","v":"dapadeveloper"}, {"i":"📍","l":"Location","v":"Pemalang, Indonesia"}]:
            st.markdown(f'<div class="contact-info-box"><div class="contact-icon">{d["i"]}</div><div><div style="font-weight:800; font-size:14px;">{d["l"]}</div><div>{d["v"]}</div></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="form-box">', unsafe_allow_html=True)
        with st.form("c_form"):
            st.text_input("Name", placeholder="Your Name")
            st.text_input("Email", placeholder="Your Email")
            st.text_area("Message", placeholder="Your Message")
            if st.form_submit_button("🚀 Send Message"): st.success("Pesan terkirim!")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)