import streamlit as st

st.set_page_config(
    page_title="Student Toolkit",
    page_icon="🧰",
    layout="wide"
)

st.title("Student Toolkit")
st.write("Track your preparation and create project presentation content.")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Checklist", "Resume Helper", "LinkedIn Helper", "GitHub Tips"]
)

with tab1:
    st.header("Progress Checklist")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Setup")
        st.checkbox("Install Python, VS Code, and Git")
        st.checkbox("Create a GitHub account")
        st.checkbox("Create a LinkedIn account")
        st.checkbox("Create your first project folder")

    with col2:
        st.subheader("Learning")
        st.checkbox("Learn Python basics")
        st.checkbox("Learn Git and GitHub basics")
        st.checkbox("Understand selected domain fundamentals")
        st.checkbox("Complete at least one mini project")

    with col3:
        st.subheader("Presentation")
        st.checkbox("Write a clean README file")
        st.checkbox("Add screenshots to GitHub")
        st.checkbox("Create a demo video")
        st.checkbox("Write a LinkedIn project post")
        st.checkbox("Add project to resume")

with tab2:
    st.header("Resume Helper")

    project_name = st.text_input("Project name", value="InternReady AI")
    domain = st.selectbox(
        "Project domain",
        ["AI/ML", "Data Science", "Web Development", "Cybersecurity", "App Development"]
    )
    tech_stack = st.text_input("Tech stack", value="Python, Streamlit")
    main_feature = st.text_input("Main feature", value="personalized roadmap generation")

    if st.button("Generate Resume Bullet"):
        resume_bullet = (
            f"Built {project_name}, a {domain} project using {tech_stack}, "
            f"featuring {main_feature} for student internship preparation."
        )
        st.success(resume_bullet)

with tab3:
    st.header("LinkedIn Helper")

    post_project_name = st.text_input("Project name for LinkedIn", value="InternReady AI")
    post_feature = st.text_input("Key feature", value="personalized roadmap generation")
    post_stack = st.text_input("Tech stack used", value="Python and Streamlit")

    if st.button("Generate LinkedIn Caption"):
        caption = f"""
I built {post_project_name}, a student-focused project that helps with internship preparation.

The project includes {post_feature} and was built using {post_stack}.

This project helped me learn app development, user input handling, project structuring, and practical problem-solving.
"""
        st.info(caption)

with tab4:
    st.header("GitHub Tips")

    st.markdown("""
- Use a clear repository name
- Add a proper README file
- Include screenshots
- Mention features clearly
- Add installation steps
- Add future scope
- Keep your code clean and readable
""")
    