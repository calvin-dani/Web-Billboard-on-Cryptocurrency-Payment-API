# README

This folder contains the crud server. Which can be scaled to add furthur crud queries to the DB.

Currently it queries to insert the message of the donor.

# Prerequisites

Python 3.1.0 ^
ngRok 

Both of the dependecies should already be installed.

# Installation

Run the command below in the same order to install necessary dependencies for the flask server,

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

python3 crud_server.py

ngrok http 5003
