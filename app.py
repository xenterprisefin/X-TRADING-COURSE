import streamlit as st

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="Xfloos Academy", layout="wide", page_icon="💰")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تصميم الحاوية لضبط الأبعاد ومنع القطع */
    .video-main-container {
        width: 100%;
        max-width: 1000px;
        margin: auto;
        border: 2px solid #d4af37;
        border-radius: 15px;
        overflow: hidden;
        background-color: #000;
        box-shadow: 0 10px 50px rgba(0,0,0,0.8);
    }

    /* ضبط نسبة العرض للارتفاع 16:9 عشان مفيش حاجة تتقطع */
    .responsive-iframe {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 */
        height: 0;
        overflow: hidden;
    }
    .responsive-iframe iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }

    h1, h2 { color: #d4af37 !important; text-align: center; font-family: sans-serif; }
    .stRadio > label { font-weight: bold; color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. البيانات ---
lessons = {
    "طريقة حساب مكسب": "nhmjYNcFhFw",
    "X - Trading": "x_bvpU0uBqY",
    "السلوك السعري": "LdIlZRknmzg",
    "التوقيت": "BX4YIRs_LMc",
    "استراتيجية العرض والطلب": "zuN6lCpF8n4",
    "مناطق العرض والطلب": "Xq9AuI7dzRk",
    "شروط العرض والطلب": "5WMJx3d2Meo",
    "قوة منطقة العرض والطلب": "BozYo0Dos-U",
    "تحديد الاتجاه": "Grw-p7rad6s",
    "انواع الاتجاه": "oJdtRl407Gw",
    "تغير الاتجاه": "IOvgSQNjtlo",
    "السيولة": "pHWSQipyZbY",
    "السيولة - ٢": "8yYNnFotGcY",
    "النماذج الفنية": "E8ZF4116Et4",
    "نموذج الكود": "8spUyGqlbfs",
    "نموذج الكود - ٢": "gdoHuv4PS9c",
    "نموذج الكي ام": "n9tp4vM37_c",
    "استراتيجية الكي ام": "PVUg_V7Bndo",
    "استراتيجية الكي ام - ٢": "MytBawz47Xs",
    "اخذ الصفقات": "UyB8Oc3dm7Q",
    "اخذ الصفقات - ٢": "WRy4Ozm3Wcw",
    "مثال": "yXGB43oAcUU",
    "مثال - ٢": "ICVGljHHyZE",
    "مثال - ٣": "fX0xadoQkhg",
    "مثال - ٤": "ZQbhIZMIMI8",
    "الاهداف والستوب": "EVVI_HV7ykI",
    "ادارة رأس المال": "B9aIiQMUInY",
    "نصائح": "yYQtTDxDLbY",
    "تطوير الاستراتيجية": "7gmLz8iFdcU",
    "ادوات مساعدة": "0OVbpGOXyz8",
    "برنامج حساب اللوت": "Z0gRh39iqPU",
    "تطبيقات عملية": "iR-AooVxXDQ",
    "تطبيقات عملية - ٢": "tVr1n0Cipys",
    "تطبيقات عملية - ٣": "i43ZJOUisv8",
    "الخاتمة": "ItZ1n7AtznE"
}

# --- 3. نظام الدخول ---
if "logged" not in st.session_state: st.session_state.logged = False

if not st.session_state.logged:
    st.markdown("<h1 style='margin-top: 100px;'>XFLOOS ACADEMY</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        with st.form("login"):
            u = st.text_input("ID")
            p = st.text_input("Password", type="password")
            if st.form_submit_button("دخول المنهج"):
                if u == "student1" and p == "12345":
                    st.session_state.logged = True
                    st.rerun()
                else: st.error("بيانات خاطئة")
else:
    # --- 4. العرض ---
    with st.sidebar:
        st.markdown("<h2 style='text-align: left;'>XFLOOS</h2>", unsafe_allow_html=True)
        st.markdown("---")
        choice = st.radio("قائمة الدروس:", list(lessons.keys()))
        if st.button("خروج"):
            st.session_state.logged = False
            st.rerun()

    st.markdown(f"<h2>{choice}</h2>", unsafe_allow_html=True)
    v_id = lessons[choice]
    
    # الكود الجديد اللي بيظبط المقاسات ويمنع القطع
    st.markdown(f"""
        <div class="video-main-container">
            <div class="responsive-iframe">
                <iframe 
                    src="https://www.youtube-nocookie.com/embed/{v_id}?rel=0&modestbranding=1&controls=1&showinfo=0" 
                    allowfullscreen>
                </iframe>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #444; margin-top: 20px;'>حصري لأكاديمية Xfloos</p>", unsafe_allow_html=True)
