# AI Powered Career Growth & Skill Intelligence Platform
Transform learning achievements into measurable career readiness through Skill Scores, Role Fit Scores, and Personalized Skill Gap Analysis.
# Overview
Professionals complete certifications, courses, bootcamps, and training programs every day, but there is no standardized way to measure how those learning experiences translate into career readiness.

SkillGraph addresses this challenge by converting learning activities into quantifiable skill intelligence.

Instead of simply displaying certificates, SkillGraph:
- Calculates Skill Scores
- Measures Role Fit Scores
- Identifies Skill Gaps
- Recommends Career Development Actions
- Helps users understand their readiness for target roles

This project was developed as part of a Product Vision initiative focused on creating measurable skill-based career development.
# Problem Statement
Current career development platforms suffer from several limitations:
- Certifications provide static proof of completion
- Learning platforms focus on content consumption rather than career outcomes
- Resumes fail to accurately represent current skill levels
- Recruiters struggle to assess actual candidate readiness
- Users lack visibility into skills needed for desired career paths

SkillGraph bridges the gap between: Learning -> Skills -> Career Readiness
# Solution
SkillGraph creates a dynamic skill profile by analyzing:
- Certifications
- Courses
- Professional Learning Activities
- Skill Keywords
- Career Interests

The platform generates:
## Skill Scores
Quantified measurements of skill proficiency.
<img width="1546" height="563" alt="image" src="https://github.com/user-attachments/assets/74af6d69-baed-4bd9-b4a0-c7aa6e327ea3" />

### Skill Score Calculation
#### Step 1: User Adds Learning Experiences
<img width="558" height="247" alt="image" src="https://github.com/user-attachments/assets/1b95318d-1804-4274-9642-70f565e9404d" />

#### Step 2: Extract Skills
Each learning experience maps to one or more skills.

<img width="418" height="465" alt="image" src="https://github.com/user-attachments/assets/f7a526b2-a3a3-4337-9b43-c16c1a4d2a35" />

#### Step 3: Assign Learning Points
<img width="444" height="137" alt="image" src="https://github.com/user-attachments/assets/c917b301-148f-4302-9b6b-050ee8d9567f" />

Example:

<img width="371" height="295" alt="image" src="https://github.com/user-attachments/assets/e4548785-1da0-48c4-bf4e-305a0e95bb11" />

#### Step 4: Generate Skill Scores
<img width="469" height="96" alt="image" src="https://github.com/user-attachments/assets/1623e1cf-28ab-4e66-866d-bb15fcf80598" />

Example:

<img width="350" height="222" alt="image" src="https://github.com/user-attachments/assets/3dedc9cd-6645-4c2b-a293-218f091c3d94" />
<img width="485" height="213" alt="image" src="https://github.com/user-attachments/assets/b8955da4-3417-40a3-8688-c882cce96512" />

## Role Fit Scores
Measures alignment with target career paths.
<img width="1240" height="342" alt="image" src="https://github.com/user-attachments/assets/a7e0071d-6730-46da-922b-9fee2686a5b1" />

### Role Fit Score Calculation
#### Step 1: Define Required Skills
Example Role:

<img width="218" height="56" alt="image" src="https://github.com/user-attachments/assets/cccd9107-dfd7-424f-b40d-4a67ecb1cd52" />

Required Skills:

<img width="333" height="282" alt="image" src="https://github.com/user-attachments/assets/d9fa43c6-dc77-42ac-8670-b77a6d04c340" />

#### Step 2: Match User Skill Scores
<img width="387" height="218" alt="image" src="https://github.com/user-attachments/assets/589d5250-de4c-4a7b-afa6-bbb03227b25c" />

Total User Score:

<img width="398" height="49" alt="image" src="https://github.com/user-attachments/assets/75fd0c22-c9cd-4e16-9a83-8ef28571cd60" />

Maximun Possible Score:

<img width="300" height="51" alt="image" src="https://github.com/user-attachments/assets/bba0456f-1ab3-450e-9566-386a2f216acf" />

#### Step 3: Calculate Role Fit %
<img width="782" height="97" alt="image" src="https://github.com/user-attachments/assets/d890d672-058f-45e3-b2d8-85e686f6b99f" />
<img width="298" height="177" alt="image" src="https://github.com/user-attachments/assets/164368c2-15e9-4628-8e8e-ddbe7d57c28a" />

## Skill Gap Analysis
Identifies missing skills and growth opportunities.
<img width="1177" height="241" alt="image" src="https://github.com/user-attachments/assets/ffcf106c-a7a2-47ff-857d-0071b6a15c05" />

### Skill Gap Detection
The system identifies missing or low-scoring skills.
Example:

<img width="368" height="138" alt="image" src="https://github.com/user-attachments/assets/506ee320-bd2d-4337-9fe1-cb4fa3f3772e" />

Missing Skills:

<img width="264" height="100" alt="image" src="https://github.com/user-attachments/assets/db972add-1742-4802-b7fc-a25b88d17cd6" />

Low Confidence Skills:

<img width="410" height="94" alt="image" src="https://github.com/user-attachments/assets/1a20fc50-5699-4c25-98a3-e80f8b260d55" />

### Receommendation Engine
Based on identified gaps, SkillGraph recommends actions.

<img width="502" height="470" alt="image" src="https://github.com/user-attachments/assets/88bcf242-7383-49b9-b446-1d00074df639" />

# Tech Stack
## Backend
- Python 3.11+
- FastAPI
- Uvicorn
## Frontend
- HTML5
- CSS3
- Vanilla JavaScript
## Data Processing
- Python Dictionaries
- JSON Data Models

# Project Structure
<img width="338" height="769" alt="image" src="https://github.com/user-attachments/assets/4dce6055-5e36-455e-a972-03493e6e0157" />

# Example Workflow
## Step 1
Add completed learning experiences:
<img width="1557" height="601" alt="image" src="https://github.com/user-attachments/assets/847be892-b2e7-4c8c-bee1-1b9ccffd9888" />
## Step 2
Choose target role:
<img width="1571" height="389" alt="image" src="https://github.com/user-attachments/assets/f93eff69-6305-4535-bb9e-06a62332b051" />

## Step 3
Generate SkillGraph and view results:
<img width="1554" height="1303" alt="image" src="https://github.com/user-attachments/assets/6d97f62d-eddf-4935-96a2-b2181ff08167" />

# Future Enhancements
## Phase 2
- Resume Parsing
- LinkedIn Profile Import
- PDF Certificate Upload
- Skill Verification Links
## Phase 3
- AI-Powered Skill Extraction
- LLM-Based Career Recommendations
- Personalized Learning Paths
- Industry Benchmarking
# Phase 4
- Recruiter Dashboard
- Candidate Matching Engine
- Hiring Analytics
- Employer Partnerships

# Product Vision
SkillGraph aims to become the standard platform for skill readiness and career intelligence by transforming learning achievements into measurable, actionable career insights. Rather than focusing solely on completed courses, SkillGraph focuses on what truly matters: Can a person perform in the role they aspire to achieve?

# Author
Rifa Safeer Shah
LinkedIn: https://www.linkedin.com/in/rifasafeershah/
