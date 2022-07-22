from ibm_watson import LanguageTranslatorV3
	from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
	

	class Translation:
	    """ Main Class """
	    def __init__(self):
	        """ input(english) >>> print(french) """
	        authenticator = IAMAuthenticator('yh3FZLY_WgCVgtIDnS0G6e1fG-OJK0d08DtZ4utRQ0vr')
	        self.language_translator = LanguageTranslatorV3(
	            version='2022-07-22',
	            authenticator=authenticator
	        )
	        self.language_translator.set_service_url(
	            'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/68838cb3-b18b-4011-8a7e-56d7a2ef6158')
	

	    def englishtofrench(self, english_input):
	        """ input(english) >>> return(french) """
	        translation_result = self.language_translator.translate(
	            text=english_input,
	            model_id='en-fr').get_result()
	        french_output = translation_result['translations'][0]['translation']
	        return french_output
	
	
	def frenchtoenglish(self, french_input):
	        """ input(frensh) >>> return(english) """
	        translation_result = self.language_translator.translate(
	            text=french_input,
	            model_id='fr-en').get_result()
	        english_output = translation_result['translations'][0]['translation']
	        return english_output
	
	
	
	

	    def englishtogerman(self, english_input):
	        """ input(english) >>> return(german) """
	        if english_input == "" or english_input is None:
	            return ""
	        translation_result = self.language_translator.translate(
	            text=english_input,
	            model_id='en-de').get_result()
	        german_output = translation_result['translations'][0]['translation']
	        return german_output
	

	if __name__ == '__main__':
	    """ This is Main function """
	    ENGLISH = "Hello, My name is Ahmed"
	    german = Translation().englishtogerman(ENGLISH)
	    print(german)


