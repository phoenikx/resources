import os

TOKEN_PICKLE_FILE_LOCATION = os.path.expanduser('~/resources/tokens/token.pickle')
CREDENTIALS_FILE_LOCATION = os.path.expanduser('~/resources/credentials/credentials.json')
CREDENTIALS_JSON_DOWNLOAD_PATH = 'https://developers.google.com/docs/api/quickstart/js'

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# The ID of resources document (should be a google docs file).
DOCUMENT_ID_FILE = os.path.expanduser('~/resources/')
