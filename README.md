### This repo is the one-day-build of my professional portfolio website (www.findram.dev)

---

# Features

- Django
- Wagtail CMS
  - Richtext capability for blog section
  - Streamfields and Orderedfields for adding new items (e.g. portfolio snippets & testimonials)
- HTML/CSS3
- Gunicorn / Nginx deployment on DigitalOcean

---

# Docker instructions

- Build

```
$ docker-compose build

# Run manage.py commands
$ docker-compose run app manage migrate
```

- Run

```
$ docker-compose up app
```
