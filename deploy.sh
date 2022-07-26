#!/bin/bash

echo "web: gunicorn server:app" > Procfile
git init
git add .
git commit -m "UAS 0416 0434 Jago Banget"

heroku create uas-pemweb-0416-0434
git push heroku master

heroku addons:create cleardb:ignite

dbURL=heroku config | grep CLEARDB_DATABASE_URL
heroku config:set DATABASE_URL=$dbURL

echo $dbURL
