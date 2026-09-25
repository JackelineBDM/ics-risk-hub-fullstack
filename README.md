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

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

## Testing

See TESTING.md.
Automated: python manage.py test facilities
Expected: 2 tests OK.

## Security

Login required for private pages.
Querysets filtered by owner.
CSRF on forms.
SECRET_KEY and DEBUG come from environment variables on Render.
DEBUG is False in production.

## Deployment

Host: Render
Build: ./build.sh
Start: gunicorn config.wsgi:application
Live URL: https://ics-risk-hub-fullstack.onrender.com

Free Render instances sleep after idle time. The first load can take about a minute.

## Credits

Purdue model, NIST SP 800-82, IEC 62443, Django docs, Code Institute.
