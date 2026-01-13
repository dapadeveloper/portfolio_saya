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

# Fungsi untuk memproses gambar lokal agar bisa dimanipulasi CSS
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
# CUSTOM CSS (FIX KONTRAS & LINGKARAN)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    /* Perbaikan Font Global */
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Perbaikan Sidebar agar Teks Terlihat Jelas */
    section[data-testid="stSidebar"] {{
        background-color: #f0f2f6 !important;
    }}

    /* CSS untuk Foto Profile Lingkaran Sempurna */
    .profile-img-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        margin-top: 10px;
    }}
    .profile-img {{
        width: 150px;
        height: 150px;
        border-radius: 50% !important;
        object-fit: cover;
        border: 4px solid #38bdf8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}

    /* Styling Teks Menu Navigasi (Warna Gelap agar Kontras) */
    .nav-link {{
        color: #1e293b !important; /* Biru Gelap Tajam */
        font-weight: 600 !important;
    }}
    .nav-link:hover {{
        color: #38bdf8 !important;
    }}
    
    /* Container untuk Experience & Skills */
    .card {{
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }}

    .gradient-text {{
        background: linear-gradient(90deg, #0ea5e9, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    # Menampilkan Foto Profile Lingkaran
    if img_base64:
        st.markdown(f"""
            <div class="profile-img-container">
                <img src="data:image/jepg;base64,{img_base64}" class="profile-img">
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: #0ea5e9; margin-bottom: 0;'>Naufal Daffa</h3>", unsafe_allow_html=True)
    st.write("##")

    # Navigasi Menu dengan Style Kontras
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "cpu", "code-slash", "award", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "5px", 
                "color": "#1e293b", # Warna teks utama menu
                "--hover-color": "#e0f2fe"
            },
            "nav-link-selected": {
                "background-color": "#38bdf8", 
                "color": "white", # Warna teks saat aktif
                "font-weight": "800"
            },
        }
    )
    
    st.write("---")
    st.markdown("<div style='background: #e0f2fe; padding: 15px; border-radius: 10px; color: #0369a1; font-size: 13px; text-align: center; font-weight: 600;'>Computer Science @ Gunadarma University</div>", unsafe_allow_html=True)

# =====================
# KONTEN UTAMA
# =====================
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3>Halo, Saya</h3>", unsafe_allow_html=True)
        st.markdown("<h1><span class='gradient-text'>Naufal Daffa Abdu Al Hafidl</span></h1>", unsafe_allow_html=True)
        st.write("Mahasiswa Computer Science yang berfokus pada **Data Analyst** dan **Machine Learning**. Berpengalaman dalam pengolahan data, analisis EDA, dan deployment dashboard.")
    
    with col2:
        if lottie_data:
            st_lottie(lottie_data, height=300, key="home")
        else:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.info("💡 Fokus pada solusi berbasis data.")

elif selected == "Skills":
    st.markdown("<h2 class='gradient-text'>Technical Skills</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class='card'><h4>Programming</h4>
        Python, SQL, HTML, CSS, JavaScript, Java, PHP (Laravel)</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'><h4>Tools & Others</h4>
        Pandas, Scikit-Learn, OpenCV, YOLOv3, Git/GitHub, Streamlit, Figma</div>""", unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h2 class='gradient-text'>Highlighted Projects</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h4>📊 Air Quality Analysis</h4>
        <p>Analisis tren polusi udara PM2.5 menggunakan Python dan Streamlit.</p>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank' style='color: #38bdf8; font-weight: bold;'>Lihat di GitHub →</a>
    </div>
    <div class='card'>
        <h4>🤖 Human Movement Detection</h4>
        <p>Deteksi gerakan manusia real-time dengan YOLOv3.</p>
        <a href='https://github.com/dapadeveloper' target='_blank' style='color: #38bdf8; font-weight: bold;'>Lihat di GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.markdown("<h2 class='gradient-text'>Experience</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <h4>Ketua Karang Taruna - Cikeas Gardenia</h4>
        <p style='color: #64748b;'>2022 - 2023</p>
    </div>
    <div class='card'>
        <h4>Ketua MPK - SMK 1 Gunung Putri</h4>
        <p style='color: #64748b;'>2021 - 2022</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h2 class='gradient-text'>Contact Me</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
        <p>Email: Fahmifalah081120@gmail.com</p>
        <p>📱 WhatsApp: +62 882-8959-2742</p>
        <p>🐙 GitHub: dapadeveloper</p>
    </div>
    """, unsafe_allow_html=True)