#!/bin/sh
gunicorn --bind 0.0.0.0:8080 run:app --chdir /opt/webapp2