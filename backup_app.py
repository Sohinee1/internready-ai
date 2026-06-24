import streamlit as st

st.set_page_config(page_title="InternReady AI", layout="wide")

st.title("InternReady AI")
st.write("Create a personalized learning roadmap for internships, projects, and skill development.")
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
    },
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

if st.sidebar.button("Generate Roadmap"):
    st.session_state.roadmap_generated = True

if st.session_state.roadmap_generated:
    st.header(f"Roadmap for {name if name else 'Student'}")
    st.write(f"Year: {year}")
    st.write(f"Skill Level: {level}")
    st.write(f"Goal: {goal}")
    st.write(f"Duration: {duration}")
    
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


    st.subheader("Internship Readiness Score")
    st.progress(score/100)
    st.write(f"{score}/100")
    st.info(advice)


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

Week 2: Project
- Build one beginner-friendly {domain} project
- Upload your work to GitHub
- Start writing a README file

Week 3: Polish
- Improve your README
- Add screenshots
- Create a LinkedIn post
"""
    st.download_button(
    label="Download Roadmap",
    data=roadmap_text,
    file_name="internready_roadmap.txt",
    mime="text/plain"
)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Roadmap", "Project Ideas", "Resources", "GitHub Tasks", "LinkedIn Plan", "Checklist"])

    with tab1:
       st.subheader("Week 1: Foundation")
       st.write(f"Learn the basics of {domain} and study daily for {daily_time}.")
    

       st.subheader("Skills To Learn")
       for skill in selected_skills:
         st.write(f"- {skill}")

    

       st.subheader("Week 2: Project")
       st.write(f"Build one beginner-friendly {domain} project and upload it to GitHub.")

       st.subheader("Week 3: Polish")
       st.write("Improve your README, add screenshots, and create a LinkedIn post.")

    with tab2:
       st.subheader("Project Ideas")
       for project in selected_projects:
         st.write(f"- {project}")
        

    with tab3:
       st.subheader("Learning Resources")
       for resource in selected_resources:
         st.write(f"- {resource}")
    
    with tab4:
       st.subheader("GitHub Tasks")
       st.write("Create a clean GitHub repository.")
       st.write("Add a README file explaining the project.")
       st.write("Add screenshots of the app.")
       st.write("Write installation steps.")
       st.write("Mention future improvements.")

    with tab5:
       st.subheader("LinkedIn Post Idea")
       st.write(
        "I built InternReady AI, a personalized roadmap generator that helps students plan internship preparation based on their goals, skill level, and available time."
    )
       
    with tab6:
      st.subheader("Progress Checklist")
      st.checkbox("Set up GitHub profile")
      st.checkbox("Learn the basics of selected domain")
      st.checkbox("Complete one mini project")
      st.checkbox("Write a proper README")
      st.checkbox("Add screenshots to GitHub")
      st.checkbox("Create a LinkedIn project post")
       
       
    
    


    
    

