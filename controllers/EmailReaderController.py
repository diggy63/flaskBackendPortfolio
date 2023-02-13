from __future__ import print_function

from flask import request, jsonify
from flask import request

import os.path


import csv
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


from extensions import db

from models.Reservation import Reservation

def getOAuth():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

def readEmails():
        # Replace "token.json" with the path to the JSON file that contains your OAuth 2.0 credentials
    creds = Credentials.from_authorized_user_file("token.json")

    # Build the Gmail API client
    service = build("gmail", "v1", credentials=creds)

    # The subject prefix of the emails to retrieve
    subject_prefix = "Reservation From Sebis"

    # Query the Gmail API to retrieve all emails with the specified subject prefix
    query = f"subject:{subject_prefix}*"
    result = service.users().messages().list(userId="me", q=query).execute()

    # Get the list of messages from the result
    messages = result.get("messages", [])

    # Create a list to hold the subject and body of each email
    email_data = []

    # Loop through the messages
    for message in messages:
        msg = service.users().messages().get(userId="me", id=message["id"]).execute()

        # Get the subject and body of the email
        for part in msg["payload"]["headers"]:
            if part["name"] == "Subject":
                email_subject = part["value"]
            if part["name"] == "From":
                email_from = part["value"]
        if "parts" not in msg["payload"]:
            if msg["payload"]["mimeType"] == "text/plain":
                email_body = base64.urlsafe_b64decode(msg["payload"]["body"]["data"].encode("UTF-8"))
        else:
            for part in msg["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    email_body = base64.urlsafe_b64decode(part["body"]["data"].encode("UTF-8"))
        
        # Add the subject and body of the email to the email_data list
        email_data.append([email_subject, email_from, email_body.decode("utf-8")])

    for email in email_data:
        info = extract_info(email)
        createReservationFromEmail(info)

    print("Emails with the subject prefix '" + subject_prefix + "' have been saved to email_data.csv.")
    return "emails have been read"



def extract_info(strings):
    name = ""
    email = ""
    phone = ""
    date_time = ""
    guests = ""
    message = ""

    for string in strings:
        if "Reservation From" in string:
            name = string.split("Reservation From Sebis -")[1].split(",")[0]
        if "From:" in string:
            email = string.split("From: ")[1].split("\r\n")[0]
        if "Number:" in string:
            prephone = re.split('Number:', string)[1]
            phone = re.split("\r\n", prephone)[0]
        if "Date and Time" in string:
            date_time = string.split("Date and Time\r\n")[1].split("\r\nGuests")[0]
        if "Guests" in string:
            guests = string.split("Guests\r\n")[1].split("\r\n")[0]
        if "Message Body" in string:
             message = string.split("Body:\r\n")[1].split("\r\n\r\n")[0]

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "date_time": date_time,
        "guests": guests,
        "message": message
    }
def createReservationFromEmail(info):
    newReservation = Reservation(
        name=info["name"],
        email=info['email'],
        number=info["phone"],
        dateAndTime=info["date_time"],
        guests=info["guests"],
        body=info["message"])
    # checks to see if this objects exsist in the table
    exists = db.session.query(db.exists().where(Reservation.name == info["name"])).scalar()

    if exists:
        print("found")
    else:
        db.session.add(newReservation)
        db.session.commit()
        print("not found")