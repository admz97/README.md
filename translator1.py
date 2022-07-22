class ahmed_translation:
def __init__ (self):
""" input(english) >>>> print(french)"""
authenticator = IAMAuthenticator('yh3FZLY_WgCVgtIDnS0G6e1fG-OJK0d08DtZ4utRQ0vr')
self. language_translator = LanguageTranslatorV3(
version='2021-03-16°,
authenticator=authenticator
)
                               
self. language_translator.set_service_url(
'https://api.us-south.Language-translator.watson.cloud.ibm.com/instances/1b2ac512-fc0e-4960-bf35-ffe5380de3011')


def englishtofrench(self, english-text):
""" input(engLish) -> return(french) """
translation_result = self.Language_translator,translate(
  text=english_text,
  model_id='en-fr').get_result()

french text = translation_ result['translations'][0]['translation']
return french_text


if __name__ == '__main__'

english_text = "HelLo, My name is Ahmed
french_text = ahmed_translation().engLishtofrench(engLish_text)
print (french_text)

