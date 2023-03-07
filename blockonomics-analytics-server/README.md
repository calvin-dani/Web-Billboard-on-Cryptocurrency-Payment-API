# README

This folder contains the analytics server. Which can be scaled to add furthur analytics queries to the DB.

Currently it queries for the message of the largest value donated.

# Prerequisites

Python 3.1.0 ^
ngRok 

Both of the dependecies should already be installed.

# Installation

Run the command below in the same order to install necessary dependencies for the flask server,

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

python3 analytics_server.py


