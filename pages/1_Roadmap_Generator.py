import streamlit as st

st.set_page_config(
    page_title="Roadmap Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("Roadmap Generator")
st.write("Create a personalized internship preparation roadmap based on your goals, domain, and available time.")

domain_data = {
    "AI/ML": {
        "skills": ["Python", "NumPy", "Pandas", "Matplotlib", "Scikit-learn"],
        "projects": ["Student performance predictor", "Resume screening tool", "Study habit analyzer"],
        "resources": ["Python basics", "Kaggle Learn", "Scikit-learn tutorials"]
    },
    "Data Science": {
        "skills": ["Python", "Excel", "SQL", "Pandas", "Data visualization"],
        "projects": ["College expense dashboard", "Student marks analysis", "Placement data analysis"],
        "resources": ["Kaggle Learn", "W3Schools SQL", "Pandas documentation"]
    },
    "Web Development": {
        "skills": ["HTML", "CSS", "JavaScript", "React", "Firebase"],
        "projects": ["Portfolio website", "Lost and found app", "Student task manager"],
        "resources": ["MDN Web Docs", "freeCodeCamp", "React documentation"]
    },
    "Cybersecurity": {
        "skills": ["Networking basics", "Linux", "Python scripting", "Web security basics", "OSINT"],
        "projects": ["Password strength checker", "Phishing link detector", "Basic port scanner"],
        "resources": ["TryHackMe beginner paths", "OWASP Top 10", "Linux Journey"]
    },
    "App Development": {
        "skills": ["Dart", "Flutter", "Firebase", "UI design basics", "API integration"],
        "projects": ["Habit tracker app", "Attendance tracker app", "Study planner app"],
        "resources": ["Flutter documentation", "Firebase documentation", "Dart language tour"]
    }
}

if "roadmap_generated" not in st.session_state:
    st.session_state.roadmap_generated = False

st.sidebar.header("Student Profile")

name = st.sidebar.text_input("Your name")

year = st.sidebar.selectbox(
    "Current year",
    ["First Year", "Second Year", "Third Year", "Final Year"]
)

level = st.sidebar.selectbox(
    "Current skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

domain = st.sidebar.selectbox(
    "Interested domain",
    ["AI/ML", "Data Science", "Web Development", "Cybersecurity", "App Development"]
)

daily_time = st.sidebar.selectbox(
    "Daily time available",
    ["1 hour", "2 hours", "3 hours", "4+ hours"]
)

goal = st.sidebar.selectbox(
    "Main goal",
    ["Build projects", "Get internship-ready", "Prepare for hackathons", "Improve resume"]
)

duration = st.sidebar.selectbox(
    "Roadmap duration",
    ["30 days", "50 days", "90 days"]
)

generate_clicked = st.sidebar.button("Generate Roadmap")
reset_clicked = st.sidebar.button("Reset Roadmap")

if generate_clicked:
    st.session_state.roadmap_generated = True

if reset_clicked:
    st.session_state.roadmap_generated = False

if st.session_state.roadmap_generated:
    selected_skills = domain_data[domain]["skills"]
    selected_projects = domain_data[domain]["projects"]
    selected_resources = domain_data[domain]["resources"]

    score = 40

    if level == "Intermediate":
        score += 15
    elif level == "Advanced":
        score += 25

    if daily_time == "2 hours":
        score += 10
    elif daily_time == "3 hours":
        score += 15
    elif daily_time == "4+ hours":
        score += 20

    if goal == "Get internship-ready":
        score += 10
    elif goal == "Build projects":
        score += 8
    elif goal == "Prepare for hackathons":
        score += 7

    if duration == "50 days":
        score += 5
    elif duration == "90 days":
        score += 10

    if score > 100:
        score = 100

    if score < 60:
        advice = "Focus on basics first. Build one small project and study consistently for the next few weeks."
    elif score < 80:
        advice = "You are on a good path. Strengthen your skills by completing one portfolio-ready project."
    else:
        advice = "You are close to internship-ready. Polish your GitHub, improve your resume, and start applying."

    roadmap_text = f"""
InternReady AI Roadmap

Name: {name if name else 'Student'}
Year: {year}
Skill Level: {level}
Domain: {domain}
Daily Time: {daily_time}
Goal: {goal}
Duration: {duration}
Internship Readiness Score: {score}/100
Personalized Advice: {advice}

Skills To Learn:
{chr(10).join("- " + skill for skill in selected_skills)}

Project Ideas:
{chr(10).join("- " + project for project in selected_projects)}

Learning Resources:
{chr(10).join("- " + resource for resource in selected_resources)}

Week 1: Foundation
- Learn the basics of {domain}
- Study daily for {daily_time}
- Set up GitHub and LinkedIn

Week 2: Project Building
- Build one beginner-friendly {domain} project
- Upload your work to GitHub
- Start writing a README file

Week 3: Polish And Present
- Improve your README
- Add screenshots
- Create a LinkedIn post
"""

    st.header(f"Roadmap for {name if name else 'Student'}")

    summary_col, score_col = st.columns([2, 1])

    with summary_col:
        st.subheader("Profile Summary")

        row1_col1, row1_col2, row1_col3 = st.columns(3)

        with row1_col1:
            st.metric("Year", year)

        with row1_col2:
            st.metric("Domain", domain)

        with row1_col3:
            st.metric("Daily Time", daily_time)

        row2_col1, row2_col2, row2_col3 = st.columns(3)

        with row2_col1:
            st.metric("Skill Level", level)

        with row2_col2:
            st.write("Goal")
            st.write(goal)

        with row2_col3:
            st.metric("Duration", duration)

    with score_col:
        st.subheader("Readiness")
        st.metric("Score", f"{score}/100")
        st.progress(score / 100)

    st.info(advice)

    st.download_button(
        label="Download Roadmap",
        data=roadmap_text,
        file_name="internready_roadmap.txt",
        mime="text/plain"
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Roadmap", "Project Ideas", "Resources", "GitHub Tasks", "LinkedIn Plan"]
    )

    with tab1:
        st.subheader("Week 1: Foundation")
        st.write(f"Learn the basics of {domain} and study daily for {daily_time}.")

        st.subheader("Skills To Learn")
        st.markdown("\n".join(f"- {skill}" for skill in selected_skills))

        st.subheader("Week 2: Project Building")
        st.write(f"Build one beginner-friendly {domain} project and upload it to GitHub.")

        st.subheader("Week 3: Polish And Present")
        st.write("Improve your README, add screenshots, and create a LinkedIn post.")

    with tab2:
        st.subheader("Project Ideas")
        st.markdown("\n".join(f"- {project}" for project in selected_projects))

    with tab3:
        st.subheader("Learning Resources")
        st.markdown("\n".join(f"- {resource}" for resource in selected_resources))

    with tab4:
        st.markdown("""
       - Create a clean GitHub repository
       - Add a README file explaining the project
       - Add screenshots of the app
       - Write installation steps
       - Mention future improvements
       """)

    with tab5:
        st.subheader("LinkedIn Post Idea")
        st.write(
            "I built InternReady AI, a personalized roadmap generator that helps students plan internship preparation based on their goals, skill level, and available time."
        )

else:
    st.info("Fill your details in the sidebar and click Generate Roadmap.")

