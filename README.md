# Django Celery Progress

Django Celery Progress is an app which provides a reusable way to track the progress of Celery tasks, and render a live progress bar on any page. This fork fixed the compatibility issue with Django >= 1.8 

For Django <= 1.7, please refer to the original git repo [link](https://github.com/robgolding/django-celery-progress.git)

## Requirements

* Django >= 1.8
* Celery

## Installation

Clone this package from github
```
    git clone https://github.com/theblackcat102/django-celery-progress.git
```

Install using setup.py
```
    cd django-celery-progress
    python setup.py install
```

Add package to INSTALLED_APPS in settings.py
```
    INSTALLED_APPS = (
        ...
        'celery_progress',
        ...
    )
```

Setup your celery task: tasks.py
```
import random, time
from celery_progress import backend
from celery import Celery

app = Celery('background_task')

@app.task(bind=True)
def test_task(app_instance):
	for i in range(100):
		time.sleep(random.uniform(0, 1))
		backend.set_progress(app_instance.request.id, i)
	return 'done'

```

In your target template:
```
{% load static celery_progress_tags %}

<script type="text/javascript" src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js'></script>
<script type="text/javascript" src='{% static "celery_progress/js/update.js" %}'></script>

{% progress_bar 'test_task' task_id %}

<script type='text/javascript'>
    trackProgress('test_task', function taskDone(result) {
        alert('Done! Result: ' + result);
    });
</script>
```

Due to some unresolved issue templates, templates path of this packeg are not included by Django 1.11. Hence you may need to create the progress_bar.html template by creating a new folder name "celery_progress" under any templates path and add the file
celery_progress/templates/celery_progress/progress_bar.html to the newly created folder

Static files for this package may need to transfer to your static sources as well.

## TODO:
1. test package for django 1.8 1.9 1.10 version (please post an issue if you tested the package in any of the newer django version)

### shout out to [Rob](https://github.com/robgolding) for creating this package.