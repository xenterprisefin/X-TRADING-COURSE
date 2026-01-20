import streamlit as st
import google.generativeai as genai

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="منصة الكورس", layout="wide")

# إخفاء العلامات الافتراضية
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# إعداد الذكاء الاصطناعي
if "GENAI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GENAI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. قائمة الدروس (بالعناوين الأصلية من صورك بالترتيب) ---
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
    st.title("🔐 تسجيل الدخول")
    u = st.text_input("ID")
    p = st.text_input("Password", type="password")
    if st.button("دخول"):
        if u == "student1" and p == "12345":
            st.session_state.logged = True
            st.rerun()
        else: st.error("بيانات خاطئة")
else:
    # --- 4. المنصة ---
    with st.sidebar:
        st.title("قائمة الدروس")
        choice = st.radio("", list(lessons.keys()))
        if st.button("خروج"):
            st.session_state.logged = False
            st.rerun()

    c1, c2 = st.columns([2, 1])
    with c1:
        st.header(choice)
        v_id = lessons[choice]
        st.components.v1.html(f"""
            <iframe width="100%" height="400" 
            src="https://www.youtube.com/embed/{v_id}?rel=0" 
            frameborder="0" allowfullscreen></iframe>
        """, height=410)
    
    with c2:
        st.subheader("🤖 مساعد AI")
        if "msgs" not in st.session_state: st.session_state.msgs = []
        for m in st.session_state.msgs:
            with st.chat_message(m["role"]): st.markdown(m["content"])
        
        if prompt := st.chat_input("اسأل المساعد..."):
            st.session_state.msgs.append({"role":"user","content":prompt})
            with st.chat_message("user"): st.markdown(prompt)
            try:
                res = model.generate_content(f"جاوب الطالب عن: {prompt}")
                with st.chat_message("assistant"): st.markdown(res.text)
                st.session_state.msgs.append({"role":"assistant","content":res.text})
            except: st.error("تأكد من الـ API Key")
