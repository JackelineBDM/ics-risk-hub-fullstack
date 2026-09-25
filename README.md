# ICS Risk Assessment Hub

Full-stack Django application for plant managers and OT security staff to assess Purdue-model Security Level 2 (SL2) posture.

This is Milestone Project 3 for the Code Institute Level 5 Diploma in Web Application Development.

**Live site:** https://ics-risk-hub-fullstack.onrender.com  
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


## User stories

As a plant manager I can register and log in so my assessments stay private.
As a plant manager I can add and edit facilities so each site has its own record.
As a plant manager I can complete an SL2 questionnaire and see a saved score.
As an OT engineer I can filter threats by impact so I can prioritise Critical items.
As a plant manager I can tick SL2 controls for a facility and find them still ticked later.
As a staff user I can add questions, threats and controls in admin.

## UX decisions

Dark navy and yellow match the industrial Project 2 hub so users recognise the product.
Delete uses a confirm page so a facility is not removed by one mis-click.
Save messages tell the user that the database write worked.
Login-only pages stop casual visitors changing another site's data.
Forms use Bootstrap so the layout works on a phone and a desktop.

## Accessibility

Pages use heading order, labels on form controls, and button text that describes the action.
Colour is not the only way to show state: risk level is written as Low, Medium or High.
Checklist checkboxes have visible labels.

## Future features

- PostgreSQL in production
- PDF export of an assessment
- Manager versus engineer roles
- Dashboard of all facility scores

## Known limitations

SECRET_KEY is still in settings for development.
DEBUG is still True in this environment.
The live URL is not deployed yet.


## User stories

As a plant manager I can register and log in so my assessments stay private.
As a plant manager I can add and edit facilities so each site has its own record.
As a plant manager I can complete an SL2 questionnaire and see a saved score.
As an OT engineer I can filter threats by impact so I can prioritise Critical items.
As a plant manager I can tick SL2 controls for a facility and find them still ticked later.
As a staff user I can add questions, threats and controls in admin.

## UX decisions

Dark navy and yellow match the industrial Project 2 hub so users recognise the product.
Delete uses a confirm page so a facility is not removed by one mis-click.
Save messages tell the user that the database write worked.
Login-only pages stop casual visitors changing another site's data.
Forms use Bootstrap so the layout works on a phone and a desktop.

## Accessibility

Pages use heading order, labels on form controls, and button text that describes the action.
Colour is not the only way to show state: risk level is written as Low, Medium or High.
Checklist checkboxes have visible labels.

## Future features

- PostgreSQL in production
- PDF export of an assessment
- Manager versus engineer roles
- Dashboard of all facility scores

## Known limitations

SECRET_KEY is still in settings for development.
DEBUG is still True in this environment.
The live URL is not deployed yet.
