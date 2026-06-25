import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

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
        with st.spinner("Generating resume bullet..."):
            prompt = f"""
Write 2 to 3 professional resume bullet points for a B.Tech CSE AIML student's project.

Project name: {project_name}
Domain: {domain}
Tech stack: {tech_stack}
Main feature: {main_feature}

Use strong action verbs, keep each bullet under 25 words, and make it suitable for an internship resume.
"""
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                resume_bullet = response.text
            except Exception as error:
                resume_bullet = f"Something went wrong: {error}"

        st.success(resume_bullet)

with tab3:
    st.header("LinkedIn Helper")

    post_project_name = st.text_input("Project name for LinkedIn", value="InternReady AI")
    post_feature = st.text_input("Key feature", value="personalized roadmap generation")
    post_stack = st.text_input("Tech stack used", value="Python and Streamlit")

    if st.button("Generate LinkedIn Caption"):
        with st.spinner("Generating LinkedIn caption..."):
            prompt = f"""
Write a LinkedIn post for a B.Tech CSE AIML student announcing a project they built.

Project name: {post_project_name}
Key feature: {post_feature}
Tech stack: {post_stack}

Make it sound genuine, beginner-friendly, slightly excited, include relevant hashtags at the end, and keep it under 150 words.
"""
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                caption = response.text
            except Exception as error:
                caption = f"Something went wrong: {error}"

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
    