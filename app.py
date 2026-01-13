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

# Fungsi memproses gambar (Base64) agar CSS bisa mengatur posisi secara presisi
def get_image_base64(path):
    try:
        img = Image.open(path)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

# Fungsi Animasi Aman
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_data = load_lottieurl("https://lottie.host/8086054a-7e61-4876-803a-345339247f1d/Uj0X0I3Gid.json")
img_base64 = get_image_base64("Profile.jpg")

# =====================
# CUSTOM CSS (DARK MODE & UI DESIGN)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    /* Global Dark Background */
    .stApp {{
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
    }}

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Sidebar Dark Theme */
    section[data-testid="stSidebar"] {{
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }}

    /* Sidebar Image Circle */
    .sidebar-img {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid #facc15;
        object-fit: cover;
        display: block;
        margin: auto;
    }}

    /* About Me Photo - Frame Ganda */
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

    /* Tags Styling */
    .info-tag {{
        display: inline-flex;
        align-items: center;
        background-color: #facc15;
        color: #0f172a;
        padding: 8px 18px;
        border-radius: 25px;
        font-weight: 800;
        font-size: 14px;
        margin-right: 12px;
        margin-bottom: 12px;
    }}

    /* Card Experience & Projects */
    .card {{
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }}

    /* SKILLS PROGRESS BAR STYLE */
    .skill-card {{
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #334155;
        height: 100%;
    }}
    .skill-header {{
        color: #facc15;
        font-weight: 800;
        margin-bottom: 20px;
        font-size: 20px;
    }}
    .skill-label-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 5px;
        margin-top: 15px;
    }}
    .skill-name {{
        color: #f1f5f9;
        font-weight: 600;
        font-size: 14px;
    }}
    .skill-value {{
        color: #cbd5e1;
        font-size: 13px;
    }}
    .progress-bg {{
        background-color: #334155;
        border-radius: 10px;
        width: 100%;
        height: 8px;
    }}
    .progress-fill {{
        background-color: #3b82f6;
        height: 100%;
        border-radius: 10px;
    }}

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
# KONTEN UTAMA
# =====================

# FUNGSI HELPER SKILL BAR
def render_skill(name, percent):
    st.markdown(f"""
        <div class="skill-label-container">
            <span class="skill-name">{name}</span>
            <span class="skill-value">{percent}%</span>
        </div>
        <div class="progress-bg">
            <div class="progress-fill" style="width: {percent}%;"></div>
        </div>
    """, unsafe_allow_html=True)

if selected == "About Me":
    st.markdown("<h1 style='font-size: 3.5rem; color: #f1f5f9;'>About <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown(f"""
        <div style="color: #cbd5e1; line-height: 1.8; font-size: 18px;">
            <p>Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>.</p>
            <p>Saya berfokus pada pengolahan data mentah menjadi wawasan yang bermakna (insights) menggunakan Python. Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.</p>
            <p>Selain teknis, pengalaman saya sebagai <b>Ketua Karang Taruna</b> dan <b>Ketua MPK</b> telah membentuk jiwa kepemimpinan saya.</p>
            <br>
            <div class="info-tag">💻 Clean Code</div>
            <div class="info-tag">☕ Coffee Lover</div>
            <div class="info-tag">👥 Team Player</div>
            <div class="info-tag">📍 Pemalang, Indonesia</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if img_base64:
            st.markdown(f"""
            <div class="profile-frame">
                <img src="data:image/jpeg;base64,{img_base64}" class="profile-img-inner">
            </div>
            """, unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown("<h1 style='text-align: center; color: #facc15;'>Skills & Technologies</h1>", unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown('<div class="skill-card"><div class="skill-header">Frontend</div>', unsafe_allow_html=True)
        render_skill("HTML", 85)
        render_skill("CSS", 80)
        render_skill("JavaScript", 70)
        render_skill("Tailwind CSS", 75)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-card"><div class="skill-header">Backend</div>', unsafe_allow_html=True)
        render_skill("Python", 90)
        render_skill("SQL", 85)
        render_skill("PHP (Laravel)", 70)
        render_skill("Flask", 60)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="skill-card"><div class="skill-header">Tools</div>', unsafe_allow_html=True)
        render_skill("Git / GitHub", 85)
        render_skill("Figma", 80)
        render_skill("Pandas", 85)
        render_skill("Scikit-Learn", 75)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='color: #f1f5f9;'>Featured <span style='color: #facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color: #facc15;'>📊 Air Quality Analysis</h3>
        <p style='color: #cbd5e1;'>Analisis tren polusi udara menggunakan Python dan Streamlit.</p>
        <a href='#' style='color: #3b82f6; text-decoration: none;'>View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h1 style='color: #f1f5f9;'>Experience</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color: #facc15;'>Ketua Karang Taruna</h3>
        <p style='color: #cbd5e1;'>Cikeas Gardenia | 2022 - 2023</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='color: #f1f5f9;'>Contact <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <p>📧 Email: Fahmifalah081120@gmail.com</p>
        <p>🐙 GitHub: dapadeveloper</p>
    </div>
    """, unsafe_allow_html=True)