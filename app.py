import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(page_title="Naufal Daffa | Portfolio", page_icon="📊", layout="wide")

def get_image_base64(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

img_profile = get_image_base64("Profile.jpg")
img_dashboard = get_image_base64("dashboard.jpg")
img_human = get_image_base64("human.jpg")
img_portofolio = get_image_base64("portofolio.jpg")

# =====================
# CSS PERBAIKAN WARNA (FIX CONTRAST)
# =====================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp {{ background-color: #0f172a !important; color: #f1f5f9 !important; }}

    /* Sidebar Fix */
    section[data-testid="stSidebar"] {{ background-color: #1e293b !important; border-right: 1px solid #334155; }}
    .sidebar-img {{ width: 120px; height: 120px; border-radius: 50%; border: 3px solid #facc15; object-fit: cover; display: block; margin: auto; }}

    /* Project Cards - Menghindari Warna Nabrak */
    .project-card {{ background-color: #facc15; border-radius: 15px; overflow: hidden; height: 100%; border: 1px solid #eab308; }}
    .project-content {{ padding: 20px; color: #0f172a !important; }} /* Teks Hitam di Latar Kuning */
    .project-tag {{ background: #0f172a; color: white; padding: 4px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; display: inline-block; margin: 2px; }}

    /* Contact Section Fix (Split Layout) */
    .contact-wrapper {{ 
        background-color: #facc15; 
        padding: 40px; 
        border-radius: 20px; 
        color: #0f172a !important; 
        display: flex; 
        flex-wrap: wrap;
        gap: 20px;
    }}
    .contact-info {{ flex: 1; min-width: 300px; }}
    .contact-form-container {{ 
        flex: 1.2; 
        background-color: #1e293b; 
        padding: 30px; 
        border-radius: 15px; 
        color: white !important; 
        min-width: 300px;
    }}
    
    /* Input Form Fix agar terlihat di latar gelap */
    .stTextInput input, .stTextArea textarea {{
        background-color: #334155 !important;
        color: white !important;
        border: 1px solid #475569 !important;
    }}
    label {{ color: #facc15 !important; font-weight: 600 !important; }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
with st.sidebar:
    if img_profile:
        st.markdown(f'<div style="padding: 20px 0;"><img src="data:image/jpeg;base64,{img_profile}" class="sidebar-img"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Naufal Daffa</h2>", unsafe_allow_html=True)
    selected = option_menu(None, ["About Me", "Skills", "Projects", "Experience", "Contact"], 
        icons=["person", "cpu", "code-slash", "award", "envelope"], default_index=0,
        styles={
            "nav-link": {"color": "#94a3b8"},
            "nav-link-selected": {"background-color": "#facc15", "color": "#0f172a", "font-weight": "800"}
        })

# =====================
# RENDER CONTENT
# =====================
if selected == "About Me":
    st.markdown("<h1>About <span style='color:#facc15'>Me</span></h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown(f"""<div style='font-size:18px; line-height:1.8; color:#cbd5e1;'>
        Halo! Saya <b>Naufal Daffa Abdu Al Hafidl</b>, mahasiswa Computer Science berusia 22 tahun dari Pemalang. 
        Saya berfokus pada pengolahan data mentah menjadi wawasan yang bermakna menggunakan Python.
        <br><br>
        <span class='project-tag' style='background:#facc15; color:#0f172a; padding:8px 15px;'>Data Science</span>
        <span class='project-tag' style='background:#facc15; color:#0f172a; padding:8px 15px;'>Machine Learning</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        if img_profile:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{img_profile}" style="width:300px; border-radius:50%; border:8px solid #facc15;"></div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown("<h1 style='text-align:center;'>Featured <span style='color:#facc15;'>Projects</span></h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    projects = [
        ("Air Quality Analysis", "Dashboard analisis tren polusi udara.", ["Python", "Streamlit"], img_dashboard, "https://air-quality-analysis-bjdvcvytswek2toxrkuwbe.streamlit.app/"),
        ("Human Detection", "Sistem deteksi gerakan berbasis YOLO.", ["Python", "OpenCV"], img_human, None),
        ("Portfolio Web", "Website portofolio interaktif kustom CSS.", ["Streamlit", "CSS"], img_portofolio, "https://portfoliosaya-hvqxtxdyyursjexk4hmorz.streamlit.app/")
    ]
    
    for i, (title, desc, tags, img, link) in enumerate(projects):
        with [c1, c2, c3][i]:
            img_html = f'data:image/jpeg;base64,{img}' if img else ""
            btn_html = f'<a href="{link}" target="_blank" style="color:#0f172a; font-weight:800; text-decoration:none;">🔗 Go to Website</a>' if link else '<span style="color:#475569; font-style:italic;">⚠️ Not Deployed</span>'
            st.markdown(f"""
            <div class="project-card">
                <div style="height:180px; background:white; display:flex; align-items:center;"><img src="{img_html}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="project-content">
                    <div style="font-size:20px; font-weight:800;">{title}</div>
                    <p style="font-size:14px;">{desc}</p>
                    {"".join([f'<span class="project-tag">{t}</span>' for t in tags])}
                    <div style="margin-top:15px;">{btn_html}</div>
                </div>
            </div>""", unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown("<h1 style='text-align:center; color:#facc15;'>Get In Touch</h1>", unsafe_allow_html=True)
    
    # Perbaikan: Layout Wrap untuk mencegah elemen bertabrakan
    st.markdown('<div class="contact-wrapper">', unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1.2])
    
    with col_left:
        st.markdown("### Let's work together")
        st.write("Feel free to reach out for collaborations!")
        st.markdown("📧 **Email:** Fahmifalah081120@gmail.com")
        st.markdown("🐙 **GitHub:** dapadeveloper")
        st.markdown("📍 **Location:** Pemalang, Indonesia")
        
    with col_right:
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            if st.form_submit_button("🚀 Send Message"):
                st.success("Message sent!")
    st.markdown('</div>', unsafe_allow_html=True)