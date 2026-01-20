import streamlit as st
import google.generativeai as genai

# إعداد الذكاء الاصطناعي
if "GENAI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GENAI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- نظام تسجيل الدخول ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 دخول منصة الكورسات")
    user_id = st.text_input("ID الطالب")
    password = st.text_input("كلمة السر", type="password")
    if st.button("تسجيل الدخول"):
        if user_id == "student1" and password == "12345": # تقدر تغيرهم من هنا
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("البيانات غلط يا بطل!")
else:
    # --- محتوى المنصة بعد الدخول ---
    st.sidebar.title("📚 دروس الكورس")
    choice = st.sidebar.radio("اختر الدرس:", ["مقدمة", "الدرس الأول", "اسأل مساعد AI"])

    if choice == "مقدمة":
        st.title("مرحباً بك في الكورس")
        st.write("هنا تضع مقدمة عن الكورس ومحتوياته.")
    
    elif choice == "الدرس الأول":
        st.title("الدرس الأول: البداية")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # حط لينك فيديوهاتك هنا
        st.write("وصف للدرس ومرفقات التحميل.")

    elif choice == "اسأل مساعد AI":
        st.title("🤖 مساعدك الذكي")
        user_q = st.chat_input("اسأل أي سؤال عن الدرس...")
        if user_q:
            response = model.generate_content(user_q)
            st.chat_message("assistant").write(response.text)