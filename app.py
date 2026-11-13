import streamlit as st

from graph import career_graph
from utils.pdf_reader import read_resume


st.title("AI Career Assistant")

st.write("Multi-Agent AI Resume Analyzer")


# Upload resume

file = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)


# Enter job description

job_description = st.text_area(
    "Enter Job Description"
)


# Analyse button

if st.button("Analyse Resume"):

    if file is None or not job_description.strip():

        st.warning("Please upload a resume and enter a job description.")

    else:

        with st.spinner("AI Agents are working..."):

            resume = read_resume(file)

            result = career_graph.invoke({
                "resume": resume,
                "job_description": job_description
            })


        st.success("Analysis completed!")


        st.header("1. Resume Analysis")
        st.write(result["analysis"])


        st.header("2. ATS Score")

        st.metric(
            "Skill Match Score",
            f'{result["ats"]["score"]}/100'
        )

        st.write("Matched Skills:", result["ats"]["matched"])
        st.write("Missing Skills:", result["ats"]["missing"])


        st.header("3. Job Recommendations")
        st.write(result["jobs"])


        st.header("4. Skill Gap Analysis")
        st.write(result["gaps"])


        st.header("5. Career Roadmap")
        st.write(result["roadmap"])


        st.header("6. Interview Preparation")
        st.write(result["interview"])