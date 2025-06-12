import os
import boto3
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

translate_client = boto3.client(
    "translate",
    aws_access_key_id=os.environ.get('TRANS_AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('TRANS_AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('TRANS_AWS_REGION_NAME')
)


response = translate_client.translate_text(
    Text="क्या कर रहा है भाई तू?",
    SourceLanguageCode="hi",
    TargetLanguageCode='en',
)

print(type(response))
pprint(response)

print("\n"*2)
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Translation successful:")
    print('\t', response['TranslatedText'])
else:
    print("Translation failed")

"""
{
    'TranslatedText': 'What are you doing brother?', 
    'SourceLanguageCode': 'hi', 
    'TargetLanguageCode': 'en', 
    'ResponseMetadata': 
    {
        'RequestId': '09bfbe3...f8d', 
        'HTTPStatusCode': 200, 
        'HTTPHeaders': 
        {
            'x-amzn-requestid': '09b...f8d', 
            'cache-control': 'no-cache', 
            'content-type': 'application/x-amz-json-1.1', 
            'content-length': '100', 
            'date': 'Tue, 19 Nov 2024 18:44:24 GMT'
        }, 
    'RetryAttempts': 0
    }
}
<class 'dict'>
"""
