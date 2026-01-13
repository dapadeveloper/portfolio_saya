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
# CUSTOM CSS (DARK THEME & GOLD ACCENT)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0f172a;
    }}

    /* Sidebar Styling - Terang agar kontras dengan Menu */
    section[data-testid="stSidebar"] {{
        background-color: #f8fafc !important;
    }}

    /* Profile Frame (Double Border Emas seperti contoh) */
    .profile-frame {{
        width: 300px;
        height: 300px;
        border-radius: 50%;
        padding: 12px;
        background: linear-gradient(135deg, #facc15, #a16207);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
    }}
    .profile-img-inner {{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 6px solid #0f172a;
        object-fit: cover;
    }}

    /* Navigasi Sidebar - Teks Gelap agar Terlihat */
    .nav-link {{
        color: #1e293b !important;
        font-weight: 600 !important;
    }}
    .nav-link:hover {{
        color: #eab308 !important;
    }}

    /* About Me Styling */
    .about-text {{
        color: #e2e8f0;
        line-height: 1.8;
        font-size: 17px;
    }}
    
    .info-tag {{
        display: inline-flex;
        align-items: center;
        background-color: #facc15;
        color: #0f172a;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        margin-right: 10px;
        margin-bottom: 10px;
    }}

    /* Project & Experience Cards */
    .card {{
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }}
    
    .gold-text {{
        color: #facc15;
        font-weight: 800;
    }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    if img_base64:
        st.markdown(f"""
            <div style="padding: 20px 0;">
                <img src="data:image/jpeg;base64,{img_base64}" 
                style="width:120px; height:120px; border-radius:50%; border:3px solid #eab308; display:block; margin:auto; object-fit:cover;">
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: #1e293b;'>Naufal Daffa</h3>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Skills", "Projects", "Experience", "Contact"],
        icons=["person", "cpu", "code-slash", "award", "envelope"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link": {"font-size": "15px", "text-align": "left", "color": "#1e293b"},
            "nav-link-selected": {"background-color": "#eab308", "color": "white"},
        }
    )
    st.write("---")
    st.info(" Gunadarma University")

# =====================
# KONTEN UTAMA
# =====================

if selected == "About Me":
    st.markdown("<h1 class='gold-text'>About Me</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown(f"""
        <div class="about-text">
            <p>Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science berusia 22 tahun dari Pemalang yang memiliki gairah besar dalam dunia <b>Data Science</b> dan <b>Machine Learning</b>.</p>
            <p>Saya berfokus pada pengolahan data mentah menjadi wawasan yang bermakna (insights) menggunakan Python. Saya memiliki pengalaman dalam membangun dashboard interaktif serta model deteksi objek.</p>
            <p>Selain teknis, pengalaman saya sebagai <b>Ketua Karang Taruna</b> dan <b>Ketua MPK</b> telah membentuk jiwa kepemimpinan dan kemampuan komunikasi saya dalam tim.</p>
            <br>
            <div class="info-tag"> Clean Code</div>
            <div class="info-tag"> Coffee Lover</div>
            <div class="info-tag"> Team Player</div>
            <div class="info-tag"> Problem Solver</div>
            <div class="info-tag"> Pemalang, Indonesia</div>
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
    st.markdown("<h2 class='gold-text'>Technical Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class='card'><h4>Languages</h4>
        <p style='color: #cbd5e1;'>Python, SQL, HTML/CSS, JavaScript, Java, PHP (Laravel)</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='card'><h4>Frameworks & Tools</h4>
        <p style='color: #cbd5e1;'>Pandas, Scikit-Learn, Streamlit, OpenCV, YOLO, Git, Figma</p></div>""", unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h2 class='gold-text'>Projects</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h4 style='color:#facc15;'> Air Quality Analysis</h4>
        <p style='color:#cbd5e1;'>Dashboard interaktif untuk memantau polusi udara menggunakan dataset real-time.</p>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank' style='color:#eab308; font-weight:bold;'>View Project →</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h2 class='gold-text'>Experience</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h4 style='color:#facc15;'>Ketua Karang Taruna</h4>
        <p style='color:#cbd5e1;'>Cikeas Gardenia (2022 - 2023)</p>
    </div>
    <div class='card'>
        <h4 style='color:#facc15;'>Ketua MPK</h4>
        <p style='color:#cbd5e1;'>SMK 1 Gunung Putri (2021 - 2022)</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h2 class='gold-text'>Contact</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <p style='color:#cbd5e1;'> Email: Fahmifalah081120@gmail.com</p>
        <p style='color:#cbd5e1;'> WhatsApp: +62 882-8959-2742</p>
        <p style='color:#cbd5e1;'> GitHub: dapadeveloper</p>
    </div>
    """, unsafe_allow_html=True)