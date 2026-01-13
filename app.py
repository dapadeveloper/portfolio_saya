import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Naufal Daffa | Data Analyst & Machine Learning",
    layout="wide",
)

# =====================
# GLOBAL STYLE
# =====================
st.markdown(
    """
    <style>
    .main {background-color: #0e1117;}
    h1, h2, h3, h4 {color: #ffffff;}
    p, li {color: #d1d5db; font-size: 16px;}
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================
# SIDEBAR
# =====================
st.sidebar.title("🚀 Navigation")
menu = st.sidebar.radio("", ["Home", "About", "Skills", "Projects", "Experience", "Contact"])

# =====================
# HOME
# =====================
if menu == "Home":
    st.markdown("""
    <div class='card'>
        <h1>Hi, I'm Naufal Daffa Abdu Al Hafidl 👋</h1>
        <h3>Data Analyst & Machine Learning Enthusiast</h3>
        <p>
        Saya mahasiswa Computer Science Universitas Gunadarma dengan minat kuat di bidang
        <b>Data Analysis, Machine Learning, dan Dashboard Development</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Experience", "Data & ML")
    col2.metric("Projects", "5+")
    col3.metric("Tools", "Python, SQL, ML")

# =====================
# ABOUT
# =====================
elif menu == "About":
    st.markdown("""
    <div class='card'>
    <h2>About Me</h2>
    <p>
    Saya adalah mahasiswa berusia 22 tahun dari Pemalang dengan pengalaman dalam
    pengolahan data, analisis eksploratif (EDA), visualisasi data, serta pengembangan
    dan evaluasi model machine learning menggunakan Python.
    </p>
    <p>
    Selain itu, saya memiliki pemahaman UI/UX menggunakan Figma dan draw.io untuk
    mendukung pembuatan dashboard dan presentasi data.
    </p>
    </div>
    """, unsafe_allow_html=True)

# =====================
# SKILLS
# =====================
elif menu == "Skills":
    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
        <h3>Programming</h3>
        <ul>
            <li>Python</li>
            <li>SQL (MySQL, PostgreSQL)</li>
            <li>HTML, CSS, JavaScript</li>
            <li>Laravel</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
        <h3>Tools & Others</h3>
        <ul>
            <li>Git & GitHub</li>
            <li>Streamlit</li>
            <li>Figma & Draw.io</li>
            <li>Canva, Capcut</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# =====================
# PROJECTS
# =====================
elif menu == "Projects":
    st.markdown("<h2>Highlighted Projects</h2>", unsafe_allow_html=True)

    projects = [
        {
            "title": "Human Movement Detection",
            "desc": "Deteksi gerakan manusia menggunakan YOLOv3 dan computer vision.",
            "tech": "Python, OpenCV, YOLOv3"
        },
        {
            "title": "Air Quality Analysis",
            "desc": "Analisis kualitas udara (PM2.5) dengan EDA dan dashboard interaktif.",
            "tech": "Python, Pandas, Streamlit"
        },
        {
            "title": "Sales Prediction (RFM)",
            "desc": "Capstone project prediksi harga dan strategi pemasaran berbasis RFM.",
            "tech": "Machine Learning, Regression"
        }
    ]

    for p in projects:
        st.markdown(f"""
        <div class='card'>
        <h3>{p['title']}</h3>
        <p>{p['desc']}</p>
        <p><b>Tech:</b> {p['tech']}</p>
        </div>
        """, unsafe_allow_html=True)

# =====================
# EXPERIENCE
# =====================
elif menu == "Experience":
    st.markdown("<h2>Experience & Organization</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>Ketua MPK – SMK 1 Gunung Putri</h3>
    <p>2021 – 2022</p>
    <ul>
        <li>Memimpin dan mengorganisir kegiatan MPK</li>
        <li>Mengelola event besar (Hari Kartini, Class Meeting)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>Ketua Karang Taruna – Cikeas Gardenia</h3>
    <p>2022 – 2023</p>
    <ul>
        <li>Mengorganisir acara Agustusan dan Sumpah Pemuda</li>
        <li>Meningkatkan kerja sama tim</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =====================
# CONTACT
# =====================
elif menu == "Contact":
    st.markdown("""
    <div class='card'>
    <h2>Contact</h2>
    <p>Email: Fahmifalah081120@gmail.com</p>
    <p>WhatsApp: +62 882-8959-2742</p>
    <p>GitHub: github.com/dapadeveloper</p>
    </div>
    """, unsafe_allow_html=True)