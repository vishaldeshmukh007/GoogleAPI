# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
#from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']





def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
 #  printLabels(service.users().labels())
    printMessage(service.users().messages())


def printLabels(labels):
    results = labels.list(userId='me').execute()
    labels = results.get('labels', [])
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


def isSubject(self):
    if self.get('name').lower() == 'from' and 'magnemit'.lower() in self.get('value').lower():
        return True
    else:
        return False



def printMessage(param):
    results = param.list(userId='me').execute()
    messages = results.get('messages',[])
    getParticularMessages(messages, param)


def showMessageInfo(messageId, content):
    content.get('payload')


def getParticularMessages(messages, param):
    expediaMessages = []
    if not messages:
        print("No messages found")
    else:
        for i in range(len(messages)):
            message = messages[i]
            messageId = message.get('id')
            content = param.get(userId='me', id=messageId).execute()
            headers = content.get('payload').get('headers')
            countS = list(filter(isSubject, headers)).__len__()
            result = countS
            if result == 1:
                expediaMessages.append(messageId)
                showMessageInfo(messageId,content)

    for messageId in expediaMessages:
        print(messageId)


if __name__ == '__main__':
    main()
# [END gmail_quickstart]
