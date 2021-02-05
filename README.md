# cloudproject1
Repo for IDS721 Cloud Project 1: Continuous Delivery of Flask Application

## Overview
The purpose of this project is to create continuous delivery of a flask application on GCP. To do so, we used GCP Cloud Shell to create a Google App Engine application, which in this case was a simple Hello World example with a few different routes. In the `main.py` file, the routes included in addition to the home page are the following:

- `name/<value>`
- `html`
- `pandas`
- `wikipedia/<company>`
- `weather`: redirects to Durham, NC weather
- `cloud`: redirects to Cloud Computing course home page

Then, after configuring Cloud Build to update when any changes are pushed to this repository, we set up continuous delivery to deploy these changes on build. This ensures that any change made to the reposity is automatically deployed when pushed.
