# SkillDeck Risk Analysis

## Document Information

**Project:** SkillDeck (SkillGraph MVP)
**Version:** 1.0
**Date:** June 2026
**Owner:** Rifa Safeer Shah
**Purpose:** Identify and evaluate business, product, technical, security, and operational risks associated with the SkillDeck platform.

---

# Executive Summary

SkillDeck is an AI-powered career intelligence platform that converts certifications, courses, projects, and learning experiences into measurable Skill Scores and Role Fit Scores. The platform helps users identify strengths, skill gaps, and career readiness while supporting the transition toward skills-based hiring.

This document outlines key risks that could impact product adoption, user trust, security, scalability, and business success.

---

# Risk Assessment Methodology

Risks are evaluated using:

| Rating | Description                                                |
| ------ | ---------------------------------------------------------- |
| Low    | Limited impact on users or business                        |
| Medium | Moderate impact requiring mitigation                       |
| High   | Significant impact on users, trust, revenue, or operations |

---

# Product Risks

## Risk: Inaccurate Skill Assessment

### Description

Users may possess skills that are not reflected through certifications, courses, or projects, causing Skill Scores to underestimate actual capability.

### Impact

High

### Likelihood

High

### Mitigation

* Weight hands-on projects higher than passive learning
* Allow users to submit portfolio evidence
* Continuously refine scoring algorithms
* Provide transparent scoring explanations

---

## Risk: Misleading Role Fit Scores

### Description

Role Fit Scores may be interpreted as guarantees of employability rather than indicators of readiness.

### Impact

High

### Likelihood

Medium

### Mitigation

* Clearly communicate scoring limitations
* Position scores as guidance, not predictions
* Provide skill gap explanations alongside scores

---

# Business Risks

## Risk: Low Recruiter Adoption

### Description

Recruiters may continue relying on resumes, degrees, and traditional credentials.

### Impact

High

### Likelihood

Medium

### Mitigation

* Conduct pilot programs with hiring teams
* Demonstrate correlation between scores and performance
* Publish transparent scoring methodology

---

## Risk: Competition

### Description

Established platforms such as LinkedIn Learning, Coursera, Indeed, and credentialing providers may introduce similar features.

### Impact

High

### Likelihood

High

### Mitigation

* Focus on career intelligence rather than content delivery
* Develop proprietary scoring models
* Build network effects through user skill profiles

---

# Security Risks

## Risk: Unauthorized Data Access

### Description

User profiles may contain sensitive educational, career, and professional information.

### Impact

High

### Likelihood

Medium

### Mitigation

* Authentication and authorization controls
* Role-Based Access Control (RBAC)
* Encryption of sensitive data
* Security logging and monitoring

---

## Risk: API Abuse

### Description

Attackers may attempt to automate requests, scrape data, or overload platform resources.

### Impact

Medium

### Likelihood

Medium

### Mitigation

* API rate limiting
* Input validation
* Authentication tokens
* Monitoring and anomaly detection

---

# Privacy Risks

## Risk: User Trust and Data Sharing

### Description

Users may be concerned about how their learning records and career data are stored and shared.

### Impact

High

### Likelihood

Medium

### Mitigation

* Explicit user consent
* Privacy controls
* User-managed profile visibility
* Data minimization principles

---

# Technical Risks

## Risk: Poor Skill Extraction Accuracy

### Description

Keyword-based extraction may fail to accurately identify user skills.

### Impact

Medium

### Likelihood

Medium

### Mitigation

* Expand skill taxonomy
* Introduce AI-assisted classification
* User feedback mechanisms
* Continuous model improvement

---

## Risk: Scalability Constraints

### Description

As user adoption increases, scoring and analytics workloads may exceed infrastructure capacity.

### Impact

Medium

### Likelihood

Medium

### Mitigation

* Cloud-native architecture
* Horizontal scaling
* Caching frequently accessed data
* Database optimization

---

# Operational Risks

## Risk: User Retention

### Description

Users may generate a score once and never return.

### Impact

Medium

### Likelihood

High

### Mitigation

* Career progression tracking
* Personalized recommendations
* Goal setting
* Progress dashboards

---

# Top Risks Summary

| Risk                        | Impact | Likelihood | Priority |
| --------------------------- | ------ | ---------- | -------- |
| Inaccurate Skill Assessment | High   | High       | Critical |
| Recruiter Adoption          | High   | Medium     | High     |
| Unauthorized Data Access    | High   | Medium     | High     |
| Competition                 | High   | High       | Critical |
| User Trust & Privacy        | High   | Medium     | High     |
| User Retention              | Medium | High       | Medium   |

---

# Conclusion

The primary risks facing SkillDeck are score credibility, recruiter adoption, competitive differentiation, and protection of user data. The platform mitigates these risks through transparent scoring, strong security controls, user privacy protections, and continuous improvement of the skill intelligence model. Long-term success depends on establishing trust among both job seekers and employers while demonstrating measurable value in skills-based hiring decisions.
