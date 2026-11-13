from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from llm import llm

from agents.resume_agent import resume_analyzer
from agents.ats_agent import ats_analyzer
from agents.job_agent import job_recommender
from agents.skill_gap_agent import skill_gap_analyzer
from agents.roadmap_agent import career_roadmap
from agents.interview_agent import interview_preparation


# Shared information

class CareerState(TypedDict, total=False):

    resume: str
    job_description: str
    analysis: str
    ats: dict
    jobs: str
    gaps: str
    roadmap: str
    interview: str


# Resume Agent

def resume_node(state):

    result = resume_analyzer(llm, state["resume"])

    return {"analysis": result}


# ATS Agent

def ats_node(state):

    result = ats_analyzer(
        state["resume"],
        state["job_description"]
    )

    return {"ats": result}


# Job Agent

def job_node(state):

    result = job_recommender(llm, state["analysis"])

    return {"jobs": result}


# Skill Gap Agent

def skill_node(state):

    result = skill_gap_analyzer(
        llm,
        state["resume"],
        state["job_description"]
    )

    return {"gaps": result}


# Roadmap Agent

def roadmap_node(state):

    result = career_roadmap(llm, state["gaps"])

    return {"roadmap": result}


# Interview Agent

def interview_node(state):

    result = interview_preparation(llm, state["resume"])

    return {"interview": result}


# Create workflow

workflow = StateGraph(CareerState)

workflow.add_node("resume", resume_node)
workflow.add_node("ats", ats_node)
workflow.add_node("jobs", job_node)
workflow.add_node("skills", skill_node)
workflow.add_node("roadmap", roadmap_node)
workflow.add_node("interview", interview_node)


# Connect agents

workflow.add_edge(START, "resume")
workflow.add_edge("resume", "ats")
workflow.add_edge("ats", "jobs")
workflow.add_edge("jobs", "skills")
workflow.add_edge("skills", "roadmap")
workflow.add_edge("roadmap", "interview")
workflow.add_edge("interview", END)


# Compile workflow

career_graph = workflow.compile()