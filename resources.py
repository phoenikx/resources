from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from constants import constants as const


class Resources:
    def __init__(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(const.TOKEN_PICKLE_FILE_LOCATION):
            with open(const.TOKEN_PICKLE_FILE_LOCATION, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(const.CREDENTIALS_FILE_LOCATION, const.SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open(const.TOKEN_PICKLE_FILE_LOCATION, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('docs', 'v1', credentials=creds)
        self.document = self.service.documents().get(documentId=const.DOCUMENT_ID).execute()

    def get_current_resources(self):
        print(self.document)


if __name__ == '__main__':
    resources = Resources()
    print(resources.get_current_resources())
