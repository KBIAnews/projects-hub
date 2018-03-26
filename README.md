# KBIA Projects Hub
A hub for all aspects of KBIIA special project and podcast builds.

This project is built on [Django Bakery](https://github.com/datadesk/django-bakery), a project pioneered by the LA Times Data Desk that takes complex Django sites and bakes them out as flat files.

## To Work on This Project
Be sure you have the `kbia_bakery` environment variables set on your computer, you've made a [virtual environment](https://open.nytimes.com/set-up-your-mac-like-an-interactive-news-developer-bb8d2c4097e5?mcubz=1) and run `pip install requirements.txt` on the main folder.

Then, while in that virtual environment, you can easily run `python manage.py runserver` and get a functional version of the site running locally on your computer, ready for development or data input.

One more note: There's a good chance you'll run across Markdown while working on this project. It's an alternative, super easy way to write text that compiles to HTML, and if you're ever confused, you can just ask [this Markdown learning tool](http://mdcheatsheet.com/) for advice.

## To Deploy This Project
Again, making sure you've got the KBIA settings inside your AWS CLI, run `python manage.py build` (no output means things went well), then quickly test everything still works on this flat-file version of the site by running `python manage.py buildserver` and looking around.

At that point, you can deploy your project using Fabric by running `fab deploy`.

__Unless you've otherwise been instructed, avoid using the Django Bakery's `publish` command, since that's really designed to publish to a TLD, and this is probably headed to [apps.kbia.org](http://apps.kbia.org/).__

## Available Django Commands
You can access these commands by using `python manage.py [command_here]`. It's an incomplete list, but it covers most of what you could want.

|Command|Origin App|What It Does|
|-------|----------|------------|
|`runserver`|`django.contrib.staticfiles`|Creates a local WSGI server on your computer running the site.|
|`collectstatic`|`django.contrib.staticfiles`|Collects and organizes the project's static files so they can be run and accessed by a server instance.|
|`makemigrations`|Django System|Makes automated SQL migrations (written in Python) to update model tables.|
|`migrate`|Django System|Runs SQL migrations (written in Python) to update model tables.|
|`build`|`django-bakery`|Runs `collectstatic`, then builds a static site based on static views listed in `settings.py`.|
|`buildserver`|`django-bakery`|Creates a Python SimpleHTTPServer of Django Bakery's build directory so you can check things out.|
