import os

TOKEN_PICKLE_FILE_LOCATION = os.path.expanduser('~/resources/tokens/token.pickle')
CREDENTIALS_FILE_LOCATION = os.path.expanduser('~/resources/credentials/credentials.json')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of resources document (should be a google docs file).
DOCUMENT_ID = '1GS9pkr5l3K3zqXAVwoKyks12xHtPl8CkGhhOAoVGBLY'
