#!/bin/bash

# Create the web_dynamic directory if it doesn't exist
mkdir -p web_dynamic

# Copy static and templates directories
cp -r web_flask/static web_dynamic/
cp -r web_flask/templates web_dynamic/

# Copy individual files
cp web_flask/100-hbnb.html web_dynamic/
cp web_flask/__init__.py web_dynamic/
cp web_flask/100-hbnb.py web_dynamic/

# Change to the web_dynamic directory
cd web_dynamic

# Run the Flask web application
python 100-hbnb.py

