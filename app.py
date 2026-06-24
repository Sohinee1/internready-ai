import streamlit as st

st.set_page_config(
    page_title="InternReady AI",
    page_icon="🎯",
    layout="wide"
)

st.title("InternReady AI")
st.subheader("Personalized internship preparation for engineering students")

st.write(
    "InternReady AI helps students plan what to learn, what projects to build, "
    "and how to present their work for internships and LinkedIn."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pages", "3")

with col2:
    st.metric("Focus", "Internships")

with col3:
    st.metric("Built With", "Streamlit")

st.header("How To Use")

st.markdown("""
1. Open **Roadmap Generator** from the sidebar.
2. Enter your year, skill level, domain, daily time, goal, and duration.
3. Generate your roadmap and download it.
4. Open **Student Toolkit** to track progress and create resume or LinkedIn content.
""")

st.header("Features")

st.markdown("""
- Domain-specific learning roadmap
- Skills and project suggestions
- Learning resources
- Internship readiness score
- Personalized advice
- Downloadable roadmap
- Progress checklist
- Resume and LinkedIn helper
""")

st.header("Why This Project Is Useful")

st.write(
    "Many students want internships but do not know how to plan their learning, "
    "choose projects, or present their work. This app gives them a simple, structured starting point."
)