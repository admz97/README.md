import translator
	

	def unit_test():
	    test_case = [
	        "Hello, My name is Ahmed",  # correct input
	        "i love football",  # correct input
	        "have a nice day",  # correct input
	        "'Hello",  # test for the translation of the world 'Hello
	        "",  # test for null input
	        "1234"]  # number input
	

	    for case in test_case:
	        french_text = translator.Translation().englishtofrench(case)
	        print(french_text)
	

	if __name__ == '__main__':
	    unit_test()
