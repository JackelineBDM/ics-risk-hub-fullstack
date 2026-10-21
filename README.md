# ICS Risk Assessment Hub

Full-stack Django app for plant managers and OT staff to assess Purdue-model SL2 posture.

Milestone Project 3, Code Institute Level 5 Diploma in Web Application Development.

**Live site:** https://ics-risk-hub-fullstack.onrender.com  
**Repository:** https://github.com/JackelineBDM/ics-risk-hub-fullstack

Project 2 frontend: https://jackelinebdm.github.io/ics-interactive-hub/

## Purpose

A logged-in user can add facilities, save an SL2 assessment, view threats by impact, and tick compliance controls. Records belong to that user only.

## User stories

- As a plant manager I can register and log in so my data stays private.
- As a plant manager I can add, edit and delete facilities.
- As a plant manager I can complete an 8-question assessment and see a saved score.
- As an OT engineer I can filter threats by impact.
- As a plant manager I can save SL2 checklist ticks per facility.
- As staff I can add questions, threats and controls in admin.

## Features

- Register, log in, log out
- Facility CRUD, owner only
- Saved assessment with score, percentage and risk level
- Threat matrix with Medium / High / Critical filters
- SL2 checklist saved per facility
- Seed command for starter data
- Deployed on Render

## UX decisions

Dark navy and yellow match the Project 2 hub.
Delete uses a confirm page.
Success messages confirm a database save.
Login is required for facilities, assessments and the checklist.
Bootstrap keeps the layout usable on phone and desktop.

## Data model

User owns Facility.
Facility has Assessment and FacilityControl.
Assessment has AssessmentAnswer.
Question, Control and Threat are shared reference tables.

## How to run

~~~
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
~~~

## Testing

See TESTING.md.

Automated command:

~~~
python manage.py test assessments threats facilities
~~~

Result 25 Sep 2026: 4 tests OK.

Manual checks on the live site all passed: register, add facility, save assessment, threat matrix, checklist. Evidence is in docs/.

Known limits: the free Render app sleeps after idle time. The free PostgreSQL database expires on 25 Oct 2026. A bad address shows the custom 404 page.

## Security
An earlier commit contained a secret key. The key was rotated and the history was cleaned with git-filter-repo.


Login required for private pages.
Querysets filtered by owner.
CSRF on forms.
SECRET_KEY and DEBUG come from environment variables on Render.
DEBUG is False in production.

## Deployment

Host: Render
Database: Render PostgreSQL (ics-risk-hub-db)

Build: ./build.sh
Start: gunicorn config.wsgi:application
Live URL: https://ics-risk-hub-fullstack.onrender.com

Free Render instances sleep after idle time. The first load can take about a minute.

## Accessibility

Pages use one main heading, labelled form controls, and button text that names the action. Risk level is written as words, not colour alone. The layout uses Bootstrap so it works on a phone and a desktop.

## Credits

Purdue model, NIST SP 800-82, IEC 62443, Django docs, Bootstrap, PostgreSQL, Render, Code Institute.


## Entity relationship diagram

~~~mermaid
erDiagram
    User ||--o{ Facility : owns
    User ||--o{ Assessment : created_by
    Facility ||--o{ Assessment : has
    Facility ||--o{ FacilityControl : has
    Assessment ||--o{ AssessmentAnswer : has
    Question ||--o{ AssessmentAnswer : answers
    Control ||--o{ FacilityControl : tracks
    Threat
~~~


## Screenshots

- [Homepage](docs/live-home.png)
- [Facilities](docs/facility.png)
- [Assessment result](docs/assessment.png)
- [Threat matrix](docs/threats.png)
- [SL2 checklist](docs/checklist.png)
\n
## Data model – field tables

### Facility
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| owner | ForeignKey(User) | required | CASCADE |
| name | CharField | max_length=200 | — |
| sector | CharField | choices | — |
| description | TextField | blank=True | — |

### Assessment
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| facility | ForeignKey(Facility) | required | CASCADE |
| created_by | ForeignKey(User) | required | CASCADE |
| score | PositiveIntegerField | default=0 | — |
| max_score | PositiveIntegerField | default=0 | — |
| percentage | PositiveIntegerField | default=0 | — |
| risk_level | CharField | choices: low/medium/high | — |
| recommendation | TextField | blank=True | — |
| created_at | DateTimeField | auto_now_add | — |

### AssessmentAnswer
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| assessment | ForeignKey(Assessment) | required | CASCADE |
| question | ForeignKey(Question) | required | CASCADE |
| answer | CharField | choices: yes/no | — |

### Question
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| text | CharField | max_length=300 | — |
| points | PositiveIntegerField | default=10 | — |
| order | PositiveIntegerField | default=1 | — |

### Control
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| title | CharField | max_length=250 | — |
| order | PositiveIntegerField | default=1 | — |

### FacilityControl
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| facility | ForeignKey(Facility) | required | CASCADE |
| control | ForeignKey(Control) | required | CASCADE |
| is_implemented | BooleanField | default=False | — |
| notes | TextField | blank=True | — |
| updated_at | DateTimeField | auto_now | — |

### Threat
| Field | Type | Constraints | On delete |
| --- | --- | --- | --- |
| name | CharField | required | — |
| description | TextField | — | — |
| impact | CharField | choices | — |
| purdue_level | CharField | — | — |

User owns Facility. Facility has Assessment and FacilityControl. Assessment has AssessmentAnswer. Question, Control and Threat are shared reference data.
\n
## How to run and deploy

### Local
~~~
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
~~~
Python 3.12 or 3.14. Environment variables: SECRET_KEY, DEBUG, DATABASE_URL, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS.

### Render
1. Create a Web Service from this GitHub repo.
2. Build command: ./build.sh
3. Start command: gunicorn config.wsgi:application
4. Add a PostgreSQL database and link DATABASE_URL.
5. Set environment variables: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS.
6. Deploy. The build script runs migrations, collects static files and loads seed data.
7. Verify the live URL loads, register works, and a facility can be saved.

## Code style
flake8 reports mostly E501 (line length > 79). These are left as-is for readability of model fields, URLs and test data. Unused imports and missing newlines were cleaned. Assessment radio buttons use fieldset and legend for grouping.
