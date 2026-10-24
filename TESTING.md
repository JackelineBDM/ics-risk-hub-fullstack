# Testing

## Automated tests

Command:
~~~
python manage.py test facilities assessments compliance
~~~

Result (21 Oct 2026): 9 tests OK.

Coverage includes:
- Login required for facility list, assessment form and checklist
- User sees only their own facilities
- Facility create
- Other user cannot edit a facility they do not own
- Missing assessment answers do not save
- Yes answer saves assessment with correct score
- Checklist page loads when logged in
- Checklist tick is persisted

## Manual tests

| Test | Steps | Expected | Actual | Date |
| --- | --- | --- | --- | --- |
| Register | Open live site, register new user | Account created, redirected | Pass | 21 Oct 2026 |
| Log in | Log in with new user | Home page shows logged-in state | Pass | 21 Oct 2026 |
| Add facility | My Facilities → Add → save | Facility appears in list | Pass | 21 Oct 2026 |
| Edit facility | Edit name and save | Name updates | Pass | 21 Oct 2026 |
| Assessment | Open Assess, answer all Yes, save | Score and risk level shown | Pass | 21 Oct 2026 |
| Threat filter | Open Threats, click Critical | Only critical threats listed | Pass | 21 Oct 2026 |
| Checklist | Open Checklist, tick one, save, reload | Tick still present | Pass | 21 Oct 2026 |
| Cross-user | Log in as second user | First user’s facility not visible | Pass | 21 Oct 2026 |

## Bugs found and fixed

- Owner-list test matched the single letter “B” in unrelated markup. Fixed by asserting full facility names and the queryset.
- Assessment and checklist saves could leave partial data on error. Wrapped both in transaction.atomic().
- Historical SECRET_KEY present in early commits. Key rotated on Render and history cleaned with git-filter-repo.

## Remaining limitations

The risk score is a project-defined indicator based on the weighted yes/no questions. It is not a certified SL2 compliance result under IEC 62443 or NIST SP 800-82.

## Accessibility notes

- Assessment radio buttons are grouped by question.
- Colour contrast uses navy (#001427) and yellow (#ffcb05).
- Keyboard navigation works for forms and links.
- Layout tested on mobile and tablet widths via browser tools.

## Live authenticated check

On the deployed site a test user registered, created a facility, saved an assessment and saved checklist ticks. All records remained after logout and login.

## HTML validation

W3C Nu HTML Checker on the live registration page (https://ics-risk-hub-fullstack.onrender.com/accounts/register/) completed with no errors or warnings on 24 October 2026. Password help text is rendered in a block container outside paragraphs. The page uses an h1 heading.
