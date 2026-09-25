# ICS Risk Assessment Hub

Full-stack Django application for plant managers and OT security staff to assess Purdue-model Security Level 2 (SL2) posture.

This is Milestone Project 3 for the Code Institute Level 5 Diploma in Web Application Development.

**Live site:** TBC  
**Repository:** https://github.com/JackelineBDM/ics-risk-hub-fullstack

The earlier frontend-only site remains Milestone Project 2:  
https://jackelinebdm.github.io/ics-interactive-hub/

## Purpose

Users can create an account, add facilities, complete a saved SL2 assessment, view a threat matrix, and tick compliance controls per facility. Data is stored per user.

## Target users

- Plant and operations managers
- OT security staff
- Assessors who need a saved record

## Features

- Register, log in and log out
- Facilities: create, read, update, delete (owner only)
- Risk assessment saved to the database with score and risk level
- Threat matrix with impact filters
- SL2 checklist saved per facility
- Admin for questions, threats and controls
- Seed command to reload starter data

## Technology

- Python 3 and Django 6
- SQLite in development
- Bootstrap 5
- GitHub and GitHub Codespaces


## Data model

- User owns Facility
- Facility has Assessment and FacilityControl
- Assessment has AssessmentAnswer
- Question, Control and Threat are shared reference data

## How to run

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

Open forwarded port 8000.

## Seed data

python manage.py seed_data

## Testing

Manual checks: register, add or edit or delete a facility, owner-only data, save an assessment, filter threats, save checklist ticks.

## Security

Login required for facilities, assessments and checklist.
Queries filtered by owner.
CSRF on forms.
Before deploy: move SECRET_KEY to env, set DEBUG=False, set ALLOWED_HOSTS.

## Deployment

Not live yet. Planned: Railway or Render.

## Credits

Purdue model, NIST SP 800-82, IEC 62443, Django docs, Code Institute.
