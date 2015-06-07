#####################################################################################################################################################
#  																																					#
# An Esperanto to English translator thingy... 																										#
# It outputs a sentence to be translated, then the user must input their translation, after which the user will be notified on their correctness! 	#
# 																																					#
# Takes a word list with given rules - which can be changed and updated... 																			#
# 																																					#
# Thank you for using my program! 																													#
# 																																					#
# Started work on 06/06/2015 (DD/MM/YYYY) 																											#
# 																																					#
#####################################################################################################################################################
#  																																					#
#																																					#
#																																					#
# 											------ Todo is attached at end of the 'Main' function! ------- 											#
#  																																					#
# 	~ William James Angus, 2015 																													#
# 	~ Version: 0.0.1 																																#
#####################################################################################################################################################



#####################################################################################################################################################
#  																																					#
# 																------ Changelog ------																#
#  																																					#
#####################################################################################################################################################
#  																																					#
#  																------ Version 0.0.1 ------															#
#===================================================================================================================================================#
#																																					#
# 																		07/06/2015																	#
#																																					#
#	~ Added basic functionality - working algorithm! 																								#
# 	~ Added automatic updater! 																														#
#  																																					#
#####################################################################################################################################################


import sys
import inspect
import shutil
import urllib.request
import os
import random

def Main():

	# Version of the program! 
	version 			= '0.0.1'

	# Performs a function to check if it needs to be updatesated, and if so, it updates itself!
	checkUpdate(version)

	# The list of languages to be tested.
	languages 			= ["English", "Esperanto"]

	# Define the lists of words.
	prepositionsEO 		= ["lia",	"mia",	"via",	"la"	]
	prepositionsEN 		= ["his",	"my",	"your",	"the"	]
	subjectsEO			= ["kato",	"domo"					]
	subjectsEN			= ["cat",	"house"					]
	verbsEO 			= ["amas",	"falas"					]
	verbsEN 			= ["loves",	"falls"					]
	objectsEO 			= ["min",	"vin"					]
	objectsEN 			= ["me",	"you"					]

	# Obtain the language to be defined.
	language 			= random.choice(languages)

	# Convert lists into numbers.
	prepositionsLen		= len(prepositionsEO) - 1
	subjectsLen 		= len(subjectsEO) - 1
	verbsLen 			= len(verbsEO) - 1
	objectsLen 			= len(objectsEO) - 1

	# Generate the sentence as a list.
	sentence			= generateSentence(prepositionsLen, subjectsLen, verbsLen, objectsLen)

	# Values of the index variables.
	prepositionIndex	= sentence[0]
	subjectIndex 		= sentence[1]
	verbIndex 			= sentence[2]
	objectIndex 		= sentence[3]

	# Assigns variables to the indexes of the words to be translated to and from.
	questionPreposition, questionSubject, questionVerb, questionObject, answerPreposition, answerSubject, answerVerb, answerObject = generateSentenceValuesFromIndex(language, prepositionIndex, subjectIndex, verbIndex, objectIndex, prepositionsEO, prepositionsEN, subjectsEO, subjectsEN, verbsEO, verbsEN, objectsEO, objectsEN)

	# Create a binary list dictating if each sentence part should be used.
	binaryList 			= createList()

	# Prints the sentence to be translated.
	print("Translate: " + formSentence(binaryList, questionPreposition, questionSubject, questionVerb, questionObject))
	


#####################################################################################################################################################
#  																																					#
#																																					#
#																																					#
# 																	------ Todo ------- 															#
#  																																					#
#																																					#
# 	~ Add file support. 																															#
# 	~ Add self-updater. - Accomplished																												#
#  																																					#
#																																					#
#####################################################################################################################################################


def generateSentence(prepositionL, subjectL, verbL, objectL):

	return random.randint(0, prepositionL), random.randint(0, subjectL), random.randint(0, verbL), random.randint(0, objectL)


def generateSentenceValuesFromIndex(language, prepositionIndex, subjectIndex, verbIndex, objectIndex, prepositionsEO, prepositionsEN, subjectsEO, subjectsEN, verbsEO, verbsEN, objectsEO, objectsEN):

	if language == "English":
		questionPreposition = prepositionsEN[prepositionIndex]
		questionSubject		= subjectsEN[subjectIndex]
		questionVerb 		= verbsEN[verbIndex]
		questionObject 		= objectsEN[objectIndex]
		answerPreposition 	= prepositionsEO[prepositionIndex]
		answerSubject 		= subjectsEO[subjectIndex]
		answerVerb 			= verbsEO[verbIndex]
		answerObject 		= objectsEO[objectIndex]
	else:
		questionPreposition = prepositionsEO[prepositionIndex]
		questionSubject 	= subjectsEO[subjectIndex]
		questionVerb 		= verbsEO[verbIndex]
		questionObject 		= objectsEO[objectIndex]
		answerPreposition 	= prepositionsEN[prepositionIndex]
		answerSubject 		= subjectsEN[subjectIndex]
		answerVerb 			= verbsEN[verbIndex]
		answerObject 		= objectsEN[objectIndex]

	return questionPreposition, questionSubject, questionVerb, questionObject, answerPreposition, answerSubject, answerVerb, answerObject


def createList():

	count = 0

	while count < 3:
		a 		= random.randint(0, 1)
		b 		= random.randint(0, 1)
		c 		= random.randint(0, 1)
		d 		= random.randint(0, 1)
		count 	= a + b + c + d

	return [a, b, c, d]


def formSentence(binaryList, prep, sub, verb, obj):

	sentence = ""

	if binaryList[0] == 1:
		sentence = sentence + " " + prep
	if binaryList[1] == 1:
		sentence = sentence + " " + sub
	if binaryList[2] == 1:
		sentence = sentence + " " + verb
	if binaryList[3] == 1:
		sentence = sentence + " " + obj

	return sentence


def checkUpdate(version):

	versionString = "~ Version: " + str(version)
	thisFileAddress = inspect.getsourcefile(sys.modules[__name__])
	url = "https://raw.githubusercontent.com/aniboy10/EsperantoTester/master/EsperantoTester.py"
	response = urllib.request.urlopen(url)
	print(str(response.read()).find(str(versionString)))
	if str(response.read()).find(str(versionString)) < 0:
		with urllib.request.urlopen(url) as response, open(thisFileAddress, 'wb') as out_file:
			print(response)
			shutil.copyfileobj(response, out_file)
		python = sys.executable
		os.execl(python, python, * sys.argv)


if __name__ == '__main__':
	Main()