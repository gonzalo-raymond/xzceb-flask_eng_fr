"""
Module for traduct english to french and french to english
"""
import os
#import json
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
# Function that takes a text in English
#  and returns its translation into French.
def english_to_french(english_text):
    """
    This function takes an English string as an argument 
    and translates it into French using the IBM Watson AI 
    translation service. 
    """
    french_text = None
    if english_text is not None and english_text != "":
        english_text = english_text.lower()
        translation = language_translator.translate(
            text = english_text, model_id = "en-fr").get_result()
        french_text = translation["translations"][0]["translation"]
    return french_text
# Function that takes a text in French
#  and returns its translation into English.
def french_to_english(french_text):
    """
    This function takes an French string as an argument 
    and translates it into English using the IBM Watson AI 
    translation service.
    """
    english_text = None
    if french_text is not None and french_text != "":
        french_text = french_text.lower()
        translation = language_translator.translate(
            text = french_text, model_id = "fr-en").get_result()
        english_text = translation["translations"][0]["translation"]
    return english_text
