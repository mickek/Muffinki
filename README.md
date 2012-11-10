heroku-django-pipeline
======================

  First [install the Heroku Toolbelt on your local workstation.](https://devcenter.heroku.com/articles/python)
  
  Create and activate virtual environment.
  
    virtualenv --no-site-packages my-project-name
    source my-project-name/bin/activate
    cd my-project-name

  Clone heroku-django-pipeline template from github.
  
    git clone git@github.com:10clouds/heroku-django-pipeline.git app
    cd app

  Install all requirements.
  
    pip install -r requirements.txt
    
  Change settings file:

  - you need to set proper AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME
  - also rememeber to create the AWS s3 storage bucket
  
  Create heroku app and deploy it.
  
    heroku create
    heroku config:add BUILDPACK_URL=git://github.com/galuszkak/heroku-buildpack-django.git
    git push heroku master

  Go to a kitchen, make some coffee and start coding.
