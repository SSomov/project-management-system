# PROJECT MANAGEMENT SYSTEM

**Built with Python and Django.**

## Install and run development mode no docker

`poetry install`

`set -o allexport; source .env.dev; set +o allexport`

`poetry run python manage.py migrate`

`poetry run python manage.py livereload > /dev/null | poetry run hypercorn manager.asgi:app --reload --debug --log-file -`

## Internationalization and localization¶

`django-admin makemessages -l ru`
`django-admin compilemessages`

## Features

- Interface to create your Company and Users
- Create Projects, tasks, update infos
- Views by Users, by Tasks and Projects
- Login and Logout, Create your Profile, update Profile picture
- Interact with other users sending friendly requests, add and remove friends
- Hosted at: http://gui-projects.herokuapp.com/
- Integration with Amazon AWS S3 for static files

## Built With:

- Python 3.10
- Django Framework 3.0.10
- CoreUI templates

## Contributing

If you want to contribute, just open an issue and tell me where I can improve.
Fork the repository and change whatever you'd like.
Pull requests are always welcome.

---
