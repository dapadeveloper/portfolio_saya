import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from io import BytesIO

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

# Fungsi memproses gambar agar pas di lingkaran (Base64)
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
# CUSTOM CSS (UI/UX PREMIUM)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    /* Background Utama Dark Mode */
    .stApp {{
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
    }}

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }}

    .sidebar-img {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid #facc15;
        object-fit: cover;
        display: block;
        margin: auto;
    }}

    /* Profile Frame About Me (Pas Presisi) */
    .profile-frame {{
        width: 350px;
        height: 350px;
        border-radius: 50%;
        padding: 10px;
        background: linear-gradient(135deg, #facc15, #854d0e);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
    }}
    .profile-img-inner {{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 8px solid #0f172a;
        object-fit: cover;
        display: block;
    }}

    /* Skill Card & Progress Bar */
    .skill-card {{
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #334155;
        height: 100%;
    }}
    .skill-header {{ color: #facc15; font-weight: 800; margin-bottom: 20px; font-size: 20px; text-transform: uppercase; }}
    .skill-label-container {{ display: flex; justify-content: space-between; margin-bottom: 5px; margin-top: 15px; }}
    .skill-name {{ color: #f1f5f9; font-weight: 600; font-size: 14px; }}
    .skill-value {{ color: #cbd5e1; font-size: 13px; }}
    .progress-bg {{ background-color: #334155; border-radius: 10px; width: 100%; height: 8px; }}
    .progress-fill {{ background-color: #3b82f6; height: 100%; border-radius: 10px; }}

    /* Project Card Grid (Model Kuning Kontras) */
    .project-card {{
        background-color: #facc15;
        border-radius: 15px;
        overflow: hidden;
        height: 100%;
        transition: transform 0.3s ease;
        border: 1px solid #eab308;
    }}
    .project-card:hover {{ transform: translateY(-10px); box-shadow: 0 10px 20px rgba(0,0,0,0.3); }}
    .project-image-container {{ background-color: white; height: 180px; overflow: hidden; }}
    .project-image-container img {{ width: 100%; height: 100%; object-fit: cover; }}
    .project-content {{ padding: 20px; color: #0f172a; }}
    .project-title {{ font-size: 20px; font-weight: 800; margin-bottom: 10px; }}
    .project-desc {{ font-size: 13px; line-height: 1.5; margin-bottom: 15px; min-height: 70px; }}
    .project-tag {{
        display: inline-block;
        background-color: #0f172a;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 10px;
        margin-right: 5px;
        margin-bottom: 5px;
        font-weight: 600;
    }}
    .project-links {{ margin-top: 15px; display: flex; gap: 15px; }}
    .project-links a {{ color: #0f172a; text-decoration: none; font-weight: 700; font-size: 13px; }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR NAVIGATION
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
# HELPER FUNCTIONS
# =====================
def render_skill(name, percent):
    st.markdown(f"""
        <div class="skill-label-container">
            <span class="skill-name">{name}</span>
            <span class="skill-value">{percent}%</span>
        </div>
        <div class="progress-bg"><div class="progress-fill" style="width: {percent}%;"></div></div>
    """, unsafe_allow_html=True)

def render_project_card(title, desc, tags, link_web="#", link_code="#"):
    tags_html = "".join([f'<span class="project-tag">{tag}</span>' for tag in tags])
    st.markdown(f"""
        <div class="project-card">
            <div class="project-image-container">
                <img src="https://via.placeholder.com/400x250/FFFFFF/0F172A?text={title.replace(' ', '+')}">
            </div>
            <div class="project-content">
                <div class="project-title">{title}</div>
                <div class="project-desc">{desc}</div>
                <div class="project-tags">{tags_html}</div>
                <div class="project-links">
                    <a href="{link_web}">🔗 Website</a>
                    <a href="{link_code}">💻 Code</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# =====================
# MAIN CONTENT
# =====================
if selected == "About Me":
    st.markdown("<h1 style='font-size: 3.5rem; color: #f1f5f9;'>About <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.markdown("""<div style='color:#cbd5e1; font-size:18px; line-height:1.8;'>
        Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>.
        Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek. 
        Mantan Ketua Karang Taruna dan Ketua MPK yang memiliki jiwa kepemimpinan kuat.</div>""", unsafe_allow_html=True)
        st.write("##")
        st.markdown("""
        <span class='project-tag' style='padding:8px 15px; font-size:14px; background:#facc15; color:#0f172a;'>Clean Code</span>
        <span class='project-tag' style='padding:8px 15px; font-size:14px; background:#facc15; color:#0f172a;'>Team Player</span>
        <span class='project-tag' style='padding:8px 15px; font-size:14px; background:#facc15; color:#0f172a;'>Problem Solver</span>
        """, unsafe_allow_html=True)
    with col2:
        if img_base64:
            st.markdown(f'<div class="profile-frame"><img src="data:image/jpeg;base64,{img_base64}" class="profile-img-inner"></div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown("<h1 style='text-align: center; color: #facc15;'>Skills & Technologies</h1>", unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown('<div class="skill-card"><div class="skill-header">Programming</div>', unsafe_allow_html=True)
        render_skill("Python", 90); render_skill("SQL", 85); render_skill("Java", 70); render_skill("PHP", 75)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="skill-card"><div class="skill-header">Web Dev</div>', unsafe_allow_html=True)
        render_skill("HTML", 85); render_skill("CSS", 80); render_skill("JavaScript", 65); render_skill("Streamlit", 85)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="skill-card"><div class="skill-header">Tools & AI</div>', unsafe_allow_html=True)
        render_skill("Pandas", 85); render_skill("YOLO", 75); render_skill("Git", 85); render_skill("Figma", 70)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='text-align: center; color: #facc15;'>Featured Projects</h1>", unsafe_allow_html=True)
    st.write("##")
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        render_project_card("Air Quality Analysis", "Dashboard analisis tren polusi udara real-time.", ["Python", "Streamlit", "Pandas"])
    with c2:
        render_project_card("Human Detection", "Sistem Computer Vision deteksi gerakan berbasis YOLO.", ["Python", "OpenCV", "YOLO"])
    with c3:
        render_project_card("Portfolio Web", "Website portofolio interaktif dengan kustom CSS.", ["Streamlit", "CSS", "UI/UX"])

elif selected == "Experience":
    st.markdown("<h1 style='color: #f1f5f9;'>Experience</h1>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h3>Ketua Karang Taruna</h3><p style='color:#facc15'>Cikeas Gardenia | 2022 - 2023</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h3>Ketua MPK</h3><p style='color:#facc15'>SMK 1 Gunung Putri | 2021 - 2022</p></div>", unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='color: #facc15;'>Contact Me</h1>", unsafe_allow_html=True)
    st.markdown("<div class='skill-card'><h4>📧 Email: Fahmifalah081120@gmail.com</h4><h4>🐙 GitHub: dapadeveloper</h4></div>", unsafe_allow_html=True)