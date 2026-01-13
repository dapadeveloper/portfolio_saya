import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# =====================
# CONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

# Fungsi Animasi dengan Proteksi Error
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load animasi (Gunakan URL yang lebih stabil)
lottie_data = load_lottieurl("https://lottie.host/8086054a-7e61-4876-803a-345339247f1d/Uj0X0I3Gid.json")

# =====================
# CUSTOM CSS
# =====================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .main { background-color: #f8fafc; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Foto Profile Lingkaran */
    .profile-container {
        display: flex;
        justify-content: center;
        padding-top: 20px;
    }
    .profile-img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #38bdf8;
    }

    /* Card Styling */
    .card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #0ea5e9, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
    }
    
    .skill-tag {
        display: inline-block;
        padding: 5px 12px;
        background: #f1f5f9;
        color: #475569;
        border-radius: 8px;
        margin: 4px;
        font-size: 13px;
        font-weight: 600;
    }
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    # Profile Photo Lingkaran
    st.markdown(
        f'<div class="profile-container"><img src="https://raw.githubusercontent.com/dapadeveloper/portfolio_saya/main/Profile.jpg" class="profile-img"></div>', 
        unsafe_allow_html=True
    )
    
    st.markdown("<h2 style='text-align: center; color: #1e293b; margin-top: 10px;'>Naufal Daffa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Data Analyst & ML</p>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "cpu", "code-slash", "award", "envelope"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link": {"font-size": "15px", "text-align": "left", "color": "#475569"},
            "nav-link-selected": {"background-color": "#f0f9ff", "color": "#0ea5e9", "border-left": "4px solid #0ea5e9"},
        }
    )

# =====================
# CONTENT
# =====================
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3>Halo! Saya</h3>", unsafe_allow_html=True)
        st.markdown("<h1><span class='gradient-text'>Naufal Daffa Abdu Al Hafidl</span></h1>", unsafe_allow_html=True)
        st.write("Mahasiswa Computer Science Universitas Gunadarma yang berfokus pada analisis data dan machine learning.")
    
    with col2:
        # Perbaikan Error: Hanya tampilkan animasi jika data berhasil dimuat
        if lottie_data:
            st_lottie(lottie_data, height=300, key="home_anim")
        else:
            st.image("https://via.placeholder.com/300x300.png?text=Data+Analyst", caption="[Animasi gagal dimuat]")

elif selected == "Skills":
    st.subheader(" Technical Skills")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class='card'><h4>Languages</h4>
        <span class='skill-tag'>Python</span><span class='skill-tag'>SQL</span><span class='skill-tag'>HTML/CSS</span>
        <span class='skill-tag'>Java</span><span class='skill-tag'>JavaScript</span></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'><h4>Tools</h4>
        <span class='skill-tag'>Pandas</span><span class='skill-tag'>Scikit-Learn</span><span class='skill-tag'>Streamlit</span>
        <span class='skill-tag'>Git</span><span class='skill-tag'>Figma</span></div>""", unsafe_allow_html=True)

elif selected == "Projects":
    st.subheader(" Featured Projects")
    st.markdown("""
    <div class='card'>
        <h4>Air Quality Analysis Dashboard</h4>
        <p>Analisis tren polusi udara menggunakan Python dan Streamlit.</p>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank'>Lihat di GitHub</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    st.subheader("Experience")
    st.info("Ketua Karang Taruna Cikeas Gardenia (2022-2023)")
    st.info("Ketua MPK SMK 1 Gunung Putri (2021-2022)")

elif selected == "Contact":
    st.subheader("Hubungi Saya")
    st.write("Email: Fahmifalah081120@gmail.com")
    st.write("WhatsApp: +62 882-8959-2742")