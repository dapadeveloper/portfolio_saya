import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# =====================
# CONFIG & ASSETS
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", layout="wide")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_gssu2dkm.json")

# =====================
# CUSTOM CSS
# =====================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
    }

    .card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: 0.3s;
        height: 100%;
    }
    
    .card:hover {
        border: 1px solid #38bdf8;
        background: rgba(56, 189, 248, 0.05);
    }

    .gradient-text {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .skill-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 10px;
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        margin: 4px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        font-size: 13px;
    }

    .github-btn {
        background-color: #38bdf8;
        color: #0f172a !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 15px;
        transition: 0.3s;
    }
    
    .github-btn:hover {
        background-color: #f8fafc;
        transform: scale(1.05);
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    st.markdown("<h2 class='gradient-text'>Naufal Daffa</h2>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "cpu", "code-slash", "award", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "transparent"},
            "icon": {"color": "#38bdf8", "font-size": "20px"}, 
            "nav-link-selected": {"background-color": "rgba(56,189,248,0.2)", "border": "1px solid #38bdf8"},
        }
    )
    st.write("---")
    st.info("Computer Science @ Gunadarma University")

# =====================
# HOME
# =====================
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h4>HELLO WORLD, I'M</h4>", unsafe_allow_html=True)
        st.markdown("<h1><span class='gradient-text'>Naufal Daffa Abdu Al Hafidl</span></h1>", unsafe_allow_html=True)
        st.write("### Data Analyst & Machine Learning Enthusiast")
        st.write("""
            Saya adalah mahasiswa berusia 22 tahun dari Pemalang dengan minat kuat di bidang pengolahan data, 
            analisis eksploratif (EDA), visualisasi data, serta pengembangan model machine learning.
        """)
    with col2:
        if lottie_ai: st_lottie(lottie_ai, height=350)

# =====================
# SKILLS
# =====================
elif selected == "Skills":
    st.markdown("<h2 class='gradient-text'>Technical Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
            <h3>Programming Languages</h3>
            <span class='skill-tag'>Python</span> <span class='skill-tag'>Java</span>
            <span class='skill-tag'>SQL (MySQL, PostgreSQL)</span> <span class='skill-tag'>HTML & CSS</span>
            <span class='skill-tag'>JavaScript</span> <span class='skill-tag'>PHP (Laravel)</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
            <h3>Tools & Frameworks</h3>
            <span class='skill-tag'>Streamlit</span> <span class='skill-tag'>Git & GitHub</span>
            <span class='skill-tag'>Scikit-Learn</span> <span class='skill-tag'>OpenCV & YOLO</span>
            <span class='skill-tag'>Figma</span> <span class='skill-tag'>Pandas & Matplotlib</span>
        </div>
        """, unsafe_allow_html=True)

# =====================
# PROJECTS
# =====================
elif selected == "Projects":
    st.markdown("<h2 class='gradient-text'>Highlighted Projects</h2>", unsafe_allow_html=True)
    
    # Project data dengan link spesifik Anda
    projects = [
        {
            "title": "Air Quality Analysis",
            "desc": "Proyek analisis kualitas udara (Dataset PM2.5) menggunakan EDA mendalam dan visualisasi interaktif untuk melihat tren polusi.",
            "tech": ["Python", "Pandas", "Streamlit", "Matplotlib"],
            "link": "https://github.com/dapadeveloper/air-quality-analysis"
        },
        {
            "title": "Human Movement Detection",
            "desc": "Sistem Computer Vision untuk mendeteksi pergerakan manusia menggunakan YOLOv3.",
            "tech": ["Python", "OpenCV", "Deep Learning"],
            "link": "https://github.com/dapadeveloper"
        }
    ]

    for p in projects:
        tags = "".join([f"<span class='skill-tag'>{t}</span>" for t in p['tech']])
        st.markdown(f"""
        <div class='card' style='margin-bottom: 25px;'>
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            {tags}<br>
            <a href='{p['link']}' target='_blank' class='github-btn'>🚀 View on GitHub</a>
        </div>
        """, unsafe_allow_html=True)

# =====================
# EXPERIENCE
# =====================
elif selected == "Experience":
    st.markdown("<h2 class='gradient-text'>Experience</h2>", unsafe_allow_html=True)
    exp_data = [
        {"year": "2022-2023", "role": "Ketua Karang Taruna", "org": "Cikeas Gardenia"},
        {"year": "2021-2022", "role": "Ketua MPK", "org": "SMK 1 Gunung Putri"}
    ]
    for e in exp_data:
        st.markdown(f"""
        <div class='card' style='margin-bottom: 15px;'>
            <h4>{e['role']} | {e['org']}</h4>
            <p style='color:#38bdf8'>{e['year']}</p>
        </div>
        """, unsafe_allow_html=True)

# =====================
# CONTACT
# =====================
elif selected == "Contact":
    st.markdown("<h2 class='gradient-text'>Contact</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
        <p>Email: Fahmifalah081120@gmail.com</p>
        <p>WhatsApp: +62 882-8959-2742</p>
        <p>GitHub: <a href='https://github.com/dapadeveloper' style='color:#38bdf8'>github.com/dapadeveloper</a></p>
    </div>
    """, unsafe_allow_html=True)