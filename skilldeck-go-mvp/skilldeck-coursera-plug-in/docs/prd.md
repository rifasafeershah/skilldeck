# Product Requirements Document (PRD)

## Document Information

**Project:** SkillDeck (SkillGraph MVP)
**Version:** 1.0
**Date:** June 2026
**Owner:** Rifa Safeer Shah
**Purpose:** Define the vision, objectives, requirements, scope, and success criteria for the SkillDeck platform.

---

# Executive Summary

SkillDeck is an AI-powered career intelligence platform that converts courses, certifications, projects, and learning experiences into measurable Skill Scores and Role Fit Scores. The platform helps users understand career readiness, identify skill gaps, and receive personalized recommendations aligned with their target career paths.

The MVP focuses on providing learners with actionable career insights through skill assessment, role alignment, and recommendation generation while establishing a foundation for future recruiter and employer-facing capabilities.

---

# Problem Statement

Professionals invest significant time and money in certifications, courses, bootcamps, and projects, yet there is no standardized way to measure how these learning experiences translate into career readiness.

Current platforms primarily track completed learning activities rather than answering critical questions:

* What skills have I developed?
* How qualified am I for my target role?
* What skills am I missing?
* What should I learn next?

SkillDeck addresses this gap by transforming learning achievements into measurable career intelligence.

---

# Product Vision

Become the standard platform for skill-based career intelligence by helping individuals measure, understand, and improve career readiness.

---

# Product Goals

## Business Goals

### Goal 1

Validate market demand for skill-based career intelligence.

### Goal 2

Develop a functional MVP demonstrating Skill Score and Role Fit Score concepts.

### Goal 3

Create a foundation for future recruiter, employer, and educational partnerships.

---

## User Goals

### Goal 1

Understand current skill strengths.

### Goal 2

Identify career skill gaps.

### Goal 3

Measure readiness for target roles.

### Goal 4

Receive actionable recommendations to improve career readiness.

---

# User Personas

## Persona: Student

### Description

Students seeking internships or entry-level opportunities.

### Pain Points

* Limited professional experience
* Unclear understanding of career readiness
* Difficulty prioritizing learning activities

### Goals

* Improve employability
* Build relevant skills
* Track progress toward career goals

---

## Persona: Career Changer

### Description

Professionals transitioning into a new field.

### Pain Points

* Uncertainty about transferable skills
* Difficulty identifying learning priorities

### Goals

* Measure readiness for a target role
* Close skill gaps efficiently

---

## Persona: Working Professional

### Description

Experienced professionals pursuing career growth.

### Pain Points

* No clear measurement of skill progression
* Difficulty evaluating training ROI

### Goals

* Identify growth opportunities
* Align learning with career advancement

---

# User Stories

## Learning Assessment

As a learner,

I want to enter my courses, certifications, and projects,

so that I can understand the skills I have developed.

---

## Career Readiness

As a learner,

I want to see a Role Fit Score,

so that I know how prepared I am for my target role.

---

## Skill Gap Analysis

As a learner,

I want to identify missing skills,

so that I know what I should learn next.

---

## Personalized Recommendations

As a learner,

I want recommendations aligned with my target role,

so that I can improve my career readiness.

---

# MVP Scope

## Included Features

### User Authentication

* User registration
* User login
* Session management

### Learning Activity Management

* Add courses
* Add certifications
* Add projects
* Store learning activity information

### Skill Scoring Engine

* Skill extraction
* Skill mapping
* Skill Score calculation

### Role Fit Engine

* Role-to-skill mapping
* Role Fit Score generation

### Recommendation Engine

* Skill gap analysis
* Personalized recommendations

### Dashboard

* Skill Scores
* Role Fit Scores
* Skill Gaps
* Recommendations

---

# Out of Scope

The following capabilities are excluded from MVP:

* LinkedIn integration
* Resume parsing
* AI chat assistant
* Recruiter dashboard
* Employer marketplace
* Learning platform integrations
* Advanced analytics
* Team collaboration features

---

# Functional Requirements

## Requirement: User Registration

### Description

Users must be able to create an account.

### Acceptance Criteria

* User enters name, email, and password
* Account is successfully created
* User is redirected to dashboard

---

## Requirement: User Login

### Description

Users must be able to authenticate using existing credentials.

### Acceptance Criteria

* User enters valid credentials
* Authentication succeeds
* Dashboard access is granted

---

## Requirement: Learning Activity Submission

### Description

Users must be able to add learning activities.

### Acceptance Criteria

* User enters title
* User selects activity type
* User provides description
* Activity is saved and displayed

---

## Requirement: Skill Score Generation

### Description

The system must generate Skill Scores based on submitted learning activities.

### Acceptance Criteria

* Skills are extracted
* Scores are calculated
* Results are displayed to user

---

## Requirement: Role Fit Calculation

### Description

The system must calculate readiness for selected roles.

### Acceptance Criteria

* User selects target role
* Role Fit Score is generated
* Results are displayed

---

## Requirement: Recommendation Generation

### Description

The system must generate recommendations based on skill gaps.

### Acceptance Criteria

* Missing skills are identified
* Recommendations are displayed
* Recommendations align with target role

---

# Non-Functional Requirements

## Security

* Authentication required
* Role-Based Access Control (RBAC)
* Secure password storage
* Session validation

---

## Performance

* Dashboard response time under 2 seconds
* Skill calculations complete within 1 second

---

## Reliability

* Platform availability target of 99% during MVP testing

---

## Privacy

* User-controlled profile visibility
* No unauthorized profile access
* Privacy-by-design principles

---

# Success Metrics

## Product Metrics

| Metric                    | Target |
| ------------------------- | ------ |
| Registered Users          | 100+   |
| Skill Score Generations   | 500+   |
| Role Fit Analyses         | 250+   |
| Recommendation Engagement | 50%    |

---

## User Metrics

| Metric               | Target |
| -------------------- | ------ |
| User Satisfaction    | 80%+   |
| Recommendation Usage | 50%+   |
| Return User Rate     | 30%+   |

---

# Risks

| Risk                    | Impact | Mitigation                                   |
| ----------------------- | ------ | -------------------------------------------- |
| Inaccurate Skill Scores | High   | Improve scoring algorithms                   |
| Low Recruiter Adoption  | High   | Validate with pilot programs                 |
| Privacy Concerns        | High   | Implement strong security controls           |
| Competitive Pressure    | High   | Focus on career intelligence differentiation |

---

# Future Roadmap

## Phase 2

* Resume parsing
* Certificate uploads
* LinkedIn integration
* AI-assisted recommendations

---

## Phase 3

* Recruiter dashboard
* Employer partnerships
* Workforce analytics

---

## Phase 4

* Skill-based hiring marketplace
* University partnerships
* Enterprise workforce intelligence

---

# Conclusion

SkillDeck aims to bridge the gap between learning and employment by providing measurable career intelligence through Skill Scores, Role Fit Scores, and personalized recommendations. The MVP focuses on validating the core value proposition while establishing the foundation for future growth into skill-based hiring and workforce intelligence.
