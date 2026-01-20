import streamlit as st

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="Xfloos Academy", layout="wide", page_icon="💰")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* حاوية الفيديو لمنع التسريب */
    .premium-video-box {
        position: relative;
        width: 100%;
        max-width: 850px;
        margin: auto;
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid #d4af37;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
        background: #000;
    }

    /* طبقة شفافة تمنع الضغط على أزرار يوتيوب الجانبية في النهاية */
    .video-guard {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 100%;
        height: 50px;
        z-index: 5;
        background: transparent;
    }
    
    h1, h2 { color: #d4af37 !important; text-align: center; }
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

# --- 3. الدخول ---
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
    
    # الكود السحري لتقليل الترشيحات
    st.markdown(f"""
        <div class="premium-video-box">
            <div class="video-guard"></div>
            <iframe width="100%" height="480" 
            src="https://www.youtube.com/embed/{v_id}?rel=0&modestbranding=1&controls=1&showinfo=0&iv_load_policy=3&fs=1&color=white" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #444; margin-top: 30px;'>جميع الفيديوهات ملك لأكاديمية Xfloos</p>", unsafe_allow_html=True)
