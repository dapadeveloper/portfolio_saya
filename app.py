import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# =====================
# CONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

# Fungsi Animasi
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie_data = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_6p8zic2y.json")

# =====================
# CUSTOM CSS (Design Enak Dipandang)
# =====================
st.markdown("""
    <style>
    /* Mengatur Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Background Utama */
    .main {
        background-color: #f8fafc;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Foto Profile Lingkaran */
    .profile-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
        height: 150px;
        border-radius: 50%; /* Membuat Lingkaran */
        object-fit: cover;
        border: 4px solid #38bdf8;
        margin-bottom: 10px;
    }

    /* Card Styling (Soft Shadow) */
    .card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #38bdf8;
    }

    /* Text Styling */
    .gradient-text {
        background: linear-gradient(90deg, #0ea5e9, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
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
        border: 1px solid #e2e8f0;
    }

    /* Hide Streamlit Footer */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR (Navigasi & Profile)
# =====================
with st.sidebar:
    # Foto Profile Lingkaran via HTML agar presisi
    st.markdown(f'<img src="https://raw.githubusercontent.com/dapadeveloper/portfolio_saya/main/Profile.jpg" class="profile-img">', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #1e293b; font-size: 22px;'>Naufal Daffa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 14px;'>Data Analyst & ML Enthusiast</p>", unsafe_allow_html=True)
    
    st.write("##")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "cpu", "code-slash", "award", "envelope"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent", "padding": "0"},
            "icon": {"color": "#64748b", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "15px", 
                "text-align": "left", 
                "color": "#475569",
                "padding": "12px"
            },
            "nav-link-selected": {
                "background-color": "#f0f9ff", 
                "color": "#0ea5e9", 
                "font-weight": "700",
                "border-left": "4px solid #0ea5e9"
            },
        }
    )
    
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 12px; color: #94a3b8;'>Gunadarma University 🎓</p>", unsafe_allow_html=True)

# =====================
# KONTEN UTAMA
# =====================

# --- HOME ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h3>Halo! Saya</h3>", unsafe_allow_html=True)
        st.markdown("<h1><span class='gradient-text'>Naufal Daffa Abdu Al Hafidl</span></h1>", unsafe_allow_html=True)
        st.write("""
            Mahasiswa Computer Science berusia 22 tahun yang berfokus pada **Data Science** dan **Machine Learning**. 
            Senang mengeksplorasi data untuk menemukan insight yang bermakna dan membangun solusi cerdas dengan Python.
        """)
        if st.button("Lihat Project Saya"):
            st.balloons()
    with col2:
        st_lottie(lottie_data, height=300)

# --- SKILLS ---
elif selected == "Skills":
    st.markdown("<h2 class='gradient-text'>Keahlian Teknis</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h4>Programming</h4>
            <span class='skill-tag'>Python</span><span class='skill-tag'>SQL</span>
            <span class='skill-tag'>Java</span><span class='skill-tag'>JavaScript</span>
            <span class='skill-tag'>HTML/CSS</span><span class='skill-tag'>PHP (Laravel)</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
            <h4>Data & ML Tools</h4>
            <span class='skill-tag'>Pandas</span><span class='skill-tag'>Scikit-Learn</span>
            <span class='skill-tag'>OpenCV</span><span class='skill-tag'>Streamlit</span>
            <span class='skill-tag'>GitHub</span><span class='skill-tag'>Tableau</span>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS ---
elif selected == "Projects":
    st.markdown("<h2 class='gradient-text'>Project Pilihan</h2>", unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class='card'>
        <h4>Air Quality Analysis Dashboard</h4>
        <p style='font-size: 14px; color: #64748b;'>Analisis interaktif kualitas udara PM2.5 menggunakan Python dan Streamlit.</p>
        <span class='skill-tag'>Data Analysis</span><span class='skill-tag'>Python</span>
        <br><br>
        <a href='https://github.com/dapadeveloper/air-quality-analysis' target='_blank' style='text-decoration: none; color: white; background: #0ea5e9; padding: 8px 16px; border-radius: 8px; font-size: 14px;'>Buka di GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    # Project 2
    st.markdown("""
    <div class='card'>
        <h4> Human Movement Detection</h4>
        <p style='font-size: 14px; color: #64748b;'>Deteksi pergerakan manusia secara real-time dengan YOLOv3.</p>
        <span class='skill-tag'>Computer Vision</span><span class='skill-tag'>YOLO</span>
        <br><br>
        <a href='https://github.com/dapadeveloper' target='_blank' style='text-decoration: none; color: white; background: #0ea5e9; padding: 8px 16px; border-radius: 8px; font-size: 14px;'>Buka di GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# --- EXPERIENCE ---
elif selected == "Experience":
    st.markdown("<h2 class='gradient-text'>Pengalaman Organisasi</h2>", unsafe_allow_html=True)
    
    experiences = [
        {"role": "Ketua Karang Taruna", "org": "Cikeas Gardenia", "year": "2022 - 2023"},
        {"role": "Ketua MPK", "org": "SMK 1 Gunung Putri", "year": "2021 - 2022"}
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class='card'>
            <h4 style='margin-bottom: 0;'>{exp['role']}</h4>
            <p style='color: #0ea5e9; font-weight: 600; margin-bottom: 10px;'>{exp['org']}</p>
            <p style='font-size: 13px; color: #94a3b8;'>{exp['year']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- CONTACT ---
elif selected == "Contact":
    st.markdown("<h2 class='gradient-text'>Hubungi Saya</h2>", unsafe_allow_html=True)
    st.write("Saya selalu terbuka untuk diskusi atau peluang kerja sama.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class='card'>
            <p><b>Email:</b> Fahmifalah081120@gmail.com</p>
            <p><b>WhatsApp:</b> +62 882-8959-2742</p>
            <p><b>GitHub:</b> dapadeveloper</p>
        </div>
        """, unsafe_allow_html=True)