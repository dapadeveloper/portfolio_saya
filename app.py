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

# Fungsi untuk memproses gambar agar bisa dimanipulasi CSS
def get_image_base64(path):
    try:
        img = Image.open(path)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

# Fungsi Animasi Aman (Proteksi Error)
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_data = load_lottieurl("https://lottie.host/8086054a-7e61-4876-803a-345339247f1d/Uj0X0I3Gid.json")
img_base64 = get_image_base64("Profile.jpg")

# =====================
# CUSTOM CSS (PREMIUM DESIGN)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Sidebar Background - Putih Bersih */
    section[data-testid="stSidebar"] {{
        background-color: #ffffff !important;
        border-right: 1px solid #f1f5f9;
    }}

    /* Sidebar Image - Circle dengan Border Emas */
    .sidebar-img {{
        width: 130px;
        height: 130px;
        border-radius: 50%;
        border: 4px solid #facc15;
        object-fit: cover;
        display: block;
        margin: auto;
    }}

    /* Warna Teks Navigasi Sidebar - Gelap & Tajam */
    .nav-link {{
        color: #1e293b !important; /* Warna Biru Gelap agar Terlihat Jelas */
        font-weight: 600 !important;
        margin-bottom: 5px;
    }}
    .nav-link:hover {{
        color: #facc15 !important;
    }}

    /* Profile Frame About Me (Double Border Emas) */
    .profile-frame {{
        width: 380px;
        height: 380px;
        border-radius: 50%;
        padding: 12px;
        background: linear-gradient(135deg, #facc15, #a16207);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }}
    .profile-img-inner {{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 8px solid #ffffff; /* Border putih pemisah */
        object-fit: cover;
    }}

    /* About Me Teks - Abu Gelap agar Nyaman Dibaca */
    .about-text {{
        color: #334155;
        line-height: 1.8;
        font-size: 18px;
    }}
    
    /* Info Tags - Kuning Cerah */
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
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}

    /* Card Experience & Projects */
    .card {{
        background: #ffffff;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR NAVIGATION
# =====================
with st.sidebar:
    if img_base64:
        st.markdown(f'<div style="padding: 20px 0;"><img src="data:image/jpeg;base64,{img_base64}" class="sidebar-img"></div>', unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: #0f172a; font-weight: 800;'>Naufal Daffa</h3>", unsafe_allow_html=True)
    st.write("##")

    selected = option_menu(
        menu_title=None,
        options=["About Me", "Skills", "Projects", "Experience", "Contact"],
        icons=["person-fill", "cpu-fill", "code-slash", "award-fill", "envelope-fill"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent", "padding": "0"},
            "nav-link": {"font-size": "16px", "text-align": "left", "padding": "12px"},
            "nav-link-selected": {"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"},
        }
    )
    st.write("---")
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px;'>Gunadarma University 🎓</p>", unsafe_allow_html=True)

# =====================
# MAIN CONTENT
# =====================

if selected == "About Me":
    st.markdown("<h1 style='font-size: 3.5rem; color: #0f172a; margin-bottom: 0;'>About <span style='color: #facc15;'>Me</span></h1>", unsafe_allow_html=True)
    st.write("##")
    
    col1, col2 = st.columns([1.4, 1], gap="large")
    
    with col1:
        st.markdown(f"""
        <div class="about-text">
            <p>Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science berusia 22 tahun yang memiliki gairah besar dalam dunia <b>Data Science</b> dan <b>Machine Learning</b>.</p>
            <p>Saya berfokus pada pengolahan data mentah menjadi wawasan yang bermakna (insights) menggunakan Python. Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.</p>
            <p>Selain teknis, pengalaman saya sebagai <b>Ketua Karang Taruna</b> dan <b>Ketua MPK</b> telah membentuk jiwa kepemimpinan dan kemampuan komunikasi saya dalam tim.</p>
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
    st.markdown("<h1 style='color: #0f172a;'>Technical <span style='color: #facc15;'>Skills</span></h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class='card'><h3>💻 Programming</h3>
        <p style='color: #475569; font-size: 18px;'>Python, SQL, HTML/CSS, JavaScript, Java, PHP (Laravel)</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'><h3>🧠 Tools & ML</h3>
        <p style='color: #475569; font-size: 18px;'>Pandas, Scikit-Learn, OpenCV, YOLO, Git/GitHub, Streamlit, Figma</p></div>""", unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='color: #0f172a;'>My <span style='color: #facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color: #0f172a;'>📊 Air Quality Analysis Dashboard</h3>
        <p style='color: #64748b;'>Dashboard interaktif untuk memantau polusi udara menggunakan Python dan Streamlit.</p>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank' style='color: #a16207; font-weight: bold; text-decoration: none;'>View Project →</a>
    </div>
    <div class='card'>
        <h3 style='color: #0f172a;'>🤖 Human Movement Detection</h3>
        <p style='color: #64748b;'>Sistem Computer Vision untuk deteksi gerakan real-time berbasis YOLO.</p>
        <a href='https://github.com/dapadeveloper' target='_blank' style='color: #a16207; font-weight: bold; text-decoration: none;'>View Project →</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h1 style='color: #0f172a;'>Experience</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h3 style='color: #0f172a;'>Ketua Karang Taruna</h3>
        <p style='color: #facc15; font-weight: bold;'>Cikeas Gardenia (2022 - 2023)</p>
    </div>
    <div class='card'>
        <h3 style='color: #0f172a;'>Ketua MPK</h3>
        <p style='color: #facc15; font-weight: bold;'>SMK 1 Gunung Putri (2021 - 2022)</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='color: #0f172a;'>Get In <span style='color: #facc15;'>Touch</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <p style='font-size: 18px; color: #1e293b;'>📧 <b>Email:</b> Fahmifalah081120@gmail.com</p>
        <p style='font-size: 18px; color: #1e293b;'>📱 <b>WhatsApp:</b> +62 882-8959-2742</p>
        <p style='font-size: 18px; color: #1e293b;'>🐙 <b>GitHub:</b> dapadeveloper</p>
    </div>
    """, unsafe_allow_html=True)