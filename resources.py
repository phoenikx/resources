from __future__ import print_function

import logging
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from constants import constants as const
from utils import log_util


class Resources:
    def __init__(self):
        self.logger = log_util.get_logger()
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

    def create_empty_table(self):
        requests = [{
            'insertTable': {
                'rows': 3,
                'columns': 3,
                'endOfSegmentLocation': {
                    'segmentId': ''
                }
            },
        }
        ]

        result = self.service.documents().batchUpdate(documentId=const.DOCUMENT_ID_FILE,
                                                      body={'requests': requests}).execute()
        return result

    def reset(self):
        if os.path.exists(const.TOKEN_PICKLE_FILE_LOCATION):
            os.remove(const.TOKEN_PICKLE_FILE_LOCATION)
            self.logger.info("Successfully reset")
        self.logger.error("Have you performed the setup?")

    def setup(self):
        if os.path.exists(const.TOKEN_PICKLE_FILE_LOCATION):
            self.logger.error("You have already performed the setup before. You can reset and setup again.")
            return
        self.logger.info("Please visit: %s and click on %s, download the JSON file and place it in %s" %
                         (const.CREDENTIALS_JSON_DOWNLOAD_PATH, 'ENABLE THE GOOGLE DOCS API',
                          '~/resources/credentials/credentials.json'))


if __name__ == '__main__':
    resources = Resources()
    resources.setup()
    # print(resources.create_empty_table())
