from testPhrasesGenerator import *
from os import listdir
from os.path import isfile, join
import timeit

def noMutationTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

	dirFunction = "NoMutated"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 
def mutateUttTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


	dirFunction = "MutateChar"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 

def mutateWithDistanceUttTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "MutateCharWithDistance"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 

def deleteCharsTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "deleteChars"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)	
	return 

def traductionChained(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "traductionChained"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def randomTraductionChained(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	dirFunction = "randomTraductionChained"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def changeNumberToWord(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "changeNumberToWord"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def changeWordToNumber(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "changeWordToNumber"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return

def convertAdjectivesToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

	dirFunction = "convertAdjectivesToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertAdjectivesToAntonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

	dirFunction = "convertAdjectivesToAntonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertObjectsToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
	dirFunction = "convertObjectsToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return

	return

def convertAdverbsToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

	dirFunction = "convertAdverbsToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertAdverbsToAntonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]

	dirFunction = "convertAdverbsToAntonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def mixedTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0.05, 0.05, 0.05, 0.25, 0.25, 0.05, 0.05, 0, 0.05, 0.05, 0.05, 0.05, 0.05, 0]

	dirFunction = "distributed"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return



def sturdinessTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0.3, 0.3, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "sturdinessTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def intentTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0, 0, 0.3, 0.45, 0, 0, 0, 0.05, 0.05, 0.05, 0.05, 0.05, 0]

	dirFunction = "intentTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def coherenceTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

	dirFunction = "coherenceTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def gridTest():

	#chatbots = ([f for f in listdir("../convosGen")])
	chatbots = ["Miso-Test", "viberSampleNutrition", "RoomReservation"]
	startExec = timeit.timeit()
	for chatbot in chatbots:

		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/mutateUtteranceStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)
		
		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/mutateUtteranceWithDistancesStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)

		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/deleteCharsStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)

		sturdinessTest(chatbot)
		intentTest(chatbot)
		coherenceTest(chatbot)

	endExec = timeit.timeit()
	print("\n total exec time: ", chatbot, ": ",(endExec - startExec))

if __name__ == "__main__":

	gridTest()



	
