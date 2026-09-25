# Testing

## Automated

python manage.py test facilities

Expected: 2 tests OK.

## Manual

| Test | Steps | Expected |
|---|---|---|
| Register | Open register, create user | Account created, can log in |
| Login | Log in with that user | Hello, username in nav |
| Add facility | My Facilities, Add, save | Card appears |
| Edit facility | Edit, change name, save | New name shows |
| Delete facility | Delete, confirm | Card gone |
| Owner only | Second user logs in | Cannot see first user's plants |
| Assessment | Assess, answer all, save | Score and risk saved |
| Threat filter | Threats, click Critical | Only critical cards |
| Checklist | Tick items, save, refresh | Ticks remain |
| Logout | Log out | Login button returns |
