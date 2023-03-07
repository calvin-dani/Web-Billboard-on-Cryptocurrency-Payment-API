# Cryptocurrency-Payment

# About
A one page website that is an internet billboard. On this billboard anyone who pays maximum money will have his message written on the billboard. When next person pays more money the previous message is removed and his message is now live. The payment is done in cryptocurrencies using Blockonomics API (Here in BTC).

![Application Screenshots](/SS1.png)

![Application Screenshots](/SS2.png)

# System Design

Using blockonomics api, The user fills the form and pays to designated address.

The blockonomics api has a webhook which then forwards the status of the transaction.

Theres two servers that handle : CRUD and analytics responsibilty as done in microservices pattern

The webhook is connected to the CRUD server which on a succesful payment triggers 'GET' operation.

The 'GET' operation fetches all the details of the transaction including the form details filled.

This then is written to MongoDB after parsing and some transformations.

The Web App polls the analytic server regularly. Which it fetchs the latest message with the highest donation and displays it.




# Technology Stack
## Frontend Application
ReactJS & ScaleText
## Backend Server & Deployment
Python, Flask, ngRok, Blockonomics Crypto API
## Database
MongoDB