from flask import Flask, render_template, request, redirect, url_for
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

app = Flask(__name__)

# Google Calendar API scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar.events']

@app.route('/')
def index():
    return render_template('index.html')

# CLIENT_SECRET_PATH = os.path.join(os.path.dirname(__file__), 'client_secret.json')

@app.route('/set_reminder', methods=['POST'])
def set_reminder():
    client_config = {
    "installed": {
        "client_id": "1086598195682-9iq0lf94s5p1fnlbgsnjivlk6d38hmu6.apps.googleusercontent.com",
        "client_secret": "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",
        "redirect_uris": ["http://localhost"]
    }
}
    flow = InstalledAppFlow.from_client_config(client_config, scopes=['https://www.googleapis.com/auth/calendar.events'])
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(client_config, scopes=['https://www.googleapis.com/auth/calendar.events'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Create a Google Calendar event
    service = build('calendar', 'v3', credentials=creds)
    note = request.form.get('note')
    event = {
        'summary': 'Reminder',
        'description': f'Set from Post-it Notes Program: {note}',
        'start': {
            'dateTime': '2022-01-01T12:00:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2022-01-01T13:00:00',
            'timeZone': 'America/Los_Angeles',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
