# User Stories & Acceptance Criteria

## Epic 1: User Authentication

### User Story 1.1: User Registration

As a new user,

I want to create an account,

so that I can access SkillDeck features and save my career data.

#### Acceptance Criteria

* User can enter name, email, and password
* Email must be unique
* Password is securely stored
* Account is created successfully
* User is automatically logged in after registration
* User is redirected to the dashboard

---

### User Story 1.2: User Login

As a returning user,

I want to log into my account,

so that I can access my saved career profile.

#### Acceptance Criteria

* User can enter email and password
* System validates credentials
* Invalid credentials generate an error message
* Successful login creates a valid session
* User is redirected to dashboard

---

### User Story 1.3: User Logout

As a logged-in user,

I want to log out,

so that my account remains secure.

#### Acceptance Criteria

* User can click logout
* Session is terminated
* Authentication token is removed
* User is redirected to landing page

---

# Epic 2: Learning Activity Management

### User Story 2.1: Add Learning Activity

As a user,

I want to add courses, certifications, and projects,

so that SkillDeck can evaluate my skills.

#### Acceptance Criteria

* User can enter title
* User can select activity type
* User can provide description
* Activity is successfully saved
* Activity appears in dashboard

---

### User Story 2.2: Delete Learning Activity

As a user,

I want to remove incorrect activities,

so that my profile remains accurate.

#### Acceptance Criteria

* User can delete an activity
* Activity is removed from dashboard
* Future score calculations exclude deleted activity

---

### User Story 2.3: View Learning Activities

As a user,

I want to see all submitted learning activities,

so that I can verify my profile information.

#### Acceptance Criteria

* All activities are displayed
* Activity type is visible
* Activity title is visible
* Activity list updates after additions or deletions

---

# Epic 3: Skill Score Generation

### User Story 3.1: Generate Skill Scores

As a user,

I want SkillDeck to calculate Skill Scores,

so that I can understand my strongest skills.

#### Acceptance Criteria

* Skills are extracted from learning activities
* Scores are calculated automatically
* Scores are displayed visually
* Scores range from 0 to 100
* Duplicate skills are aggregated

---

### User Story 3.2: View Skill Breakdown

As a user,

I want to understand how my score was calculated,

so that I trust the results.

#### Acceptance Criteria

* Skill names are displayed
* Associated scores are displayed
* Scoring logic is explainable
* Skills are sorted by score

---

# Epic 4: Role Fit Analysis

### User Story 4.1: Select Target Role

As a user,

I want to select a target role,

so that SkillDeck can evaluate my readiness.

#### Acceptance Criteria

* User can select Product Manager
* User can select Data Analyst
* User can select Cybersecurity Analyst
* Role selection is saved for analysis

---

### User Story 4.2: Generate Role Fit Score

As a user,

I want to see how well my skills align with a target role,

so that I understand my career readiness.

#### Acceptance Criteria

* Role Fit Score is calculated
* Score ranges from 0 to 100
* Score appears immediately after analysis
* Highest matching role is displayed

---

### User Story 4.3: Compare Multiple Roles

As a user,

I want to compare my fit across roles,

so that I can evaluate career options.

#### Acceptance Criteria

* System displays all supported roles
* Role Fit Scores are shown side-by-side
* Roles are ranked by score

---

# Epic 5: Skill Gap Analysis

### User Story 5.1: Identify Skill Gaps

As a user,

I want to see missing skills,

so that I know where to improve.

#### Acceptance Criteria

* Missing skills are identified
* Gap analysis is role-specific
* Skill gaps are clearly displayed

---

### User Story 5.2: Receive Recommendations

As a user,

I want personalized recommendations,

so that I know what actions to take next.

#### Acceptance Criteria

* Recommendations align with skill gaps
* Recommendations are displayed after analysis
* Recommendations are actionable
* Recommendations support selected target role

---

# Epic 6: Dashboard Experience

### User Story 6.1: View Dashboard Results

As a user,

I want all career insights in one location,

so that I can easily understand my readiness.

#### Acceptance Criteria

* Dashboard displays Skill Scores
* Dashboard displays Role Fit Scores
* Dashboard displays Skill Gaps
* Dashboard displays Recommendations

---

### User Story 6.2: Generate Updated Analysis

As a user,

I want to refresh my analysis after adding new activities,

so that my scores remain accurate.

#### Acceptance Criteria

* User can rerun analysis
* Updated scores are generated
* Dashboard reflects new results
* Previous scores are replaced
