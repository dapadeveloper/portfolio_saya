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
# CUSTOM CSS (DARK MODE & PHOTO ALIGNMENT)
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

    /* About Me Photo - Memastikan "Pas" di Lingkaran */
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
        border: 6px solid #0f172a; /* Warna background utama */
        object-fit: cover; /* Memastikan foto mengisi lingkaran dengan pas */
        display: block;
    }}

    /* Text Contras Fix */
    .about-text {{
        color: #cbd5e1;
        line-height: 1.8;
        font-size: 18px;
    }}
    
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

    /* Projects & Skills Cards */
    .card {{
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }}

    /* Header & Footer hide */
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
        styles={{
            "container": {{"background-color": "transparent", "padding": "0"}},
            "nav-link": {{"font-size": "15px", "text-align": "left", "color": "#94a3b8"}},
            "nav-link-selected": {{"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"}},
        }}
    )

# =====================
# MAIN CONTENT
# =====================

if selected == "About Me":
    st.markdown("<h1 style='font-size: 3rem; color: #f1f5f9;'>About <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown(f"""
        <div class="about-text">
            <p>Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science yang berfokus pada <b>Data Science</b> dan <b>Machine Learning</b>.</p>
            <p>Saya berfokus pada pengolahan data mentah menjadi wawasan yang bermakna (insights) menggunakan Python. Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.</p>
            <p>Selain teknis, pengalaman saya sebagai <b>Ketua Karang Taruna</b> dan <b>Ketua MPK</b> telah membentuk jiwa kepemimpinan saya.</p>
            <br>
            <div class="info-tag">💻 Clean Code</div>
            <div class="info-tag">☕ Coffee Lover</div>
            <div class="info-tag">👥 Team Player</div>
            <div class="info-tag">🧩 Problem Solver</div>
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
    st.markdown("<h1 style='color: #f1f5f9;'>My <span style='color: #facc15;'>Skills</span></h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class='card'><h3 style='color:#facc15'>Languages</h3>
        <p>Python, SQL, HTML/CSS, JavaScript, Java, PHP (Laravel)</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'><h3 style='color:#facc15'>Tools</h3>
        <p>Pandas, Scikit-Learn, OpenCV, YOLO, Git, Streamlit, Figma</p></div>""", unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='color: #f1f5f9;'>Featured <span style='color: #facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color:#facc15'>📊 Air Quality Analysis</h3>
        <p>Analisis tren polusi udara menggunakan Python dan Streamlit.</p>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank' style='color:#facc15; font-weight:bold;'>View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h1 style='color: #f1f5f9;'>Experience</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color:#facc15'>Ketua Karang Taruna</h3>
        <p>Cikeas Gardenia (2022 - 2023)</p>
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