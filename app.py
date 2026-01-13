import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# =====================
# CONFIG & ASSETS
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="🚀", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_gssu2dkm.json") # AI animation
lottie_data = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_6p8zic2y.json") # Data animation

# =====================
# CUSTOM CSS (Glassmorphism & Animations)
# =====================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
    }

    /* Glassmorphism card */
    .card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: transform 0.3s ease, border 0.3s ease;
        margin-bottom: 20px;
    }
    
    .card:hover {
        transform: translateY(-5px);
        border: 1px solid #38bdf8;
    }

    .gradient-text {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 15px;
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        margin: 5px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        font-size: 14px;
    }

    /* Hide Streamlit components */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR NAVIGATION (Modern)
# =====================
with st.sidebar:
    st.markdown("<h2 class='gradient-text'>Naufal Portfolio</h2>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Contact"],
        icons=["house", "cpu", "code-slash", "briefcase", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "transparent"},
            "icon": {"color": "#38bdf8", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px", "--hover-color": "rgba(56,189,248,0.1)"},
            "nav-link-selected": {"background-color": "rgba(56,189,248,0.2)", "border": "1px solid #38bdf8"},
        }
    )
    st.write("---")
    st.markdown("📍 Based in Pemalang, Indonesia")

# =====================
# HOME SECTION
# =====================
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h4>HELLO WORLD, I'M</h4>", unsafe_allow_html=True)
        st.markdown("<h1><span class='gradient-text'>Naufal Daffa Abdu Al Hafidl</span></h1>", unsafe_allow_html=True)
        st.write("### Machine Learning Engineer & Data Analyst")
        st.write("Mahasiswa Computer Science yang berfokus pada pemecahan masalah kompleks melalui data. Spesialisasi dalam membangun model prediktif dan visualisasi data interaktif.")
        
        if st.button("Download CV"):
            st.info("CV link logic here")
            
    with col2:
        st_lottie(lottie_ai, height=400)

    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Completed Projects", "10+", "+2 this month")
    with c2: st.metric("Data Analyzed", "1M+ rows", "PostgreSQL/BigQuery")
    with c3: st.metric("Model Accuracy", "94%", "XGBoost/YOLO")

# =====================
# SKILLS SECTION
# =====================
elif selected == "Skills":
    st.markdown("<h2 class='gradient-text'>Technical Arsenal</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h3>💻 Languages</h3>
            <span class='skill-tag'>Python</span><span class='skill-tag'>SQL</span>
            <span class='skill-tag'>Java</span><span class='skill-tag'>HTML/CSS</span>
            <span class='skill-tag'>JavaScript</span><span class='skill-tag'>PHP (Laravel)</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
            <h3>🧠 Machine Learning</h3>
            <span class='skill-tag'>Scikit-Learn</span><span class='skill-tag'>TensorFlow</span>
            <span class='skill-tag'>Computer Vision</span><span class='skill-tag'>NLP</span>
            <span class='skill-tag'>YOLOv3/v8</span><span class='skill-tag'>Pandas/NumPy</span>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card'>
            <h3>🛠️ Tools & DevOps</h3>
            <span class='skill-tag'>Git/GitHub</span><span class='skill-tag'>Streamlit</span>
            <span class='skill-tag'>Docker</span><span class='skill-tag'>Figma</span>
            <span class='skill-tag'>Tableau</span><span class='skill-tag'>Draw.io</span>
        </div>
        """, unsafe_allow_html=True)

# =====================
# PROJECTS SECTION
# =====================
elif selected == "Projects":
    st.markdown("<h2 class='gradient-text'>Featured Projects</h2>", unsafe_allow_html=True)
    
    def project_card(title, desc, tags, github_url):
        tags_html = "".join([f"<span class='skill-tag'>{tag}</span>" for tag in tags])
        st.markdown(f"""
        <div class='card'>
            <h3>{title}</h3>
            <p>{desc}</p>
            {tags_html}
            <br><br>
            <a href='{github_url}' target='_blank' style='text-decoration:none;'>
                <button style='background-color:#38bdf8; border:none; padding:8px 20px; border-radius:10px; color:#0f172a; font-weight:bold; cursor:pointer;'>
                    View on GitHub
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        project_card(
            "Human Movement Detection", 
            "Sistem deteksi real-time menggunakan YOLOv3 untuk mengidentifikasi pergerakan manusia dalam area terbatas.",
            ["OpenCV", "Deep Learning", "Python"],
            "https://github.com/dapadeveloper"
        )
    with col_b:
        project_card(
            "Air Quality Insight Dashboard", 
            "Analisis mendalam data polusi udara PM2.5 dengan visualisasi tren musiman.",
            ["Streamlit", "Plotly", "EDA"],
            "https://github.com/dapadeveloper"
        )

# =====================
# CONTACT SECTION
# =====================
elif selected == "Contact":
    st.markdown("<h2 class='gradient-text'>Let's Connect</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Saya terbuka untuk kolaborasi terkait data science dan machine learning.")
        st.info("📍 Pemalang, Jawa Tengah")
        st.write("📧 Fahmifalah081120@gmail.com")
        st.write("🐙 [GitHub: dapadeveloper](https://github.com/dapadeveloper)")
        
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            msg = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            if submit:
                st.success("Pesan terkirim! (Simulasi)")