import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ["version"]

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version = version, authenticator = authenticator)

language_translator.set_service_url(url)

translation = language_translator.translate(text = 'Hello, how are you today?', model_id = 'en-es').get_result()



print(json.dumps(translation, indent = 2, ensure_ascii = False))
