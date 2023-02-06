import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ["version"]

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version = version, authenticator = authenticator)

language_translator.set_service_url(url)

# Function that takes a text in English
#  and returns its translation into French.
def englishToFrench(englishText):
    """
    This function takes an English string as an argument 
    and translates it into French using the IBM Watson AI 
    translation service. 
    """
    
    englishText = englishText.lower()
    
    translation = language_translator.translate(text = englishText, 
    model_id = "en-fr").get_result()

    frenchText = translation["translations"][0]["translation"]

    return frenchText

# Function that takes a text in French
#  and returns its translation into English.
def frenchToEnglish(frenchText):
    """
    This function takes an French string as an argument 
    and translates it into English using the IBM Watson AI 
    translation service.
    """
   
    frenchText = frenchText.lower()

    translation = language_translator.translate(text = frenchText, 
    model_id = "fr-en").get_result()

    englishText = translation["translations"][0]["translation"]

    return englishText

en_message = ""

fr_message = ""

print(englishToFrench(en_message))

print(frenchToEnglish(fr_message))