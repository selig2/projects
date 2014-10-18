import random

#------------------------------------------------------------------------------
# File:    deckClass.py
# Desc:    Text based simulator for the pokemon tcg.
# Author:  Lucas A. Selig
# Copyright (c) 2014- by Lucas A. Selig.  All Rights Reserved.
#------------------------------------------------------------------------------

lookup = {'Spritzee': 'Basic', 'Aromatisse': 'Evolution', 'Xerneas': 'Basic', 'Xerneas EX': 'Basic', 'Cobalion EX': 'Basic', 'Jirachi EX': 'Basic', 'Keldeo EX': 'Basic', 'Kangaskhan EX': 'Basic', 'Mega Kangaskhan EX': 'Evolution', 'Venusaur EX': 'Basic', 'Mewtwo EX': 'Basic', 'Sigilyph': 'Basic', 'Suicune': 'Basic', 'Kyurem': 'Basic', 'N': 'Supporter', 'Professor Juniper': 'Supporter' ,'Colress': 'Supporter', 'Skyla': 'Supporter', 'Lysandre': 'Supporter', 'Ultra Ball': 'Item', 'Muscle Band': 'Item', 'Fairy Garden': 'Stadium', 'Max Potion': 'Item', 'Computer Search': 'Item', 'Mega-Phone': 'Item', 'Fairy Energy': 'Basic Energy', 'Rainbow Energy': 'Special Energy', 'Double Colorless Energy': 'Special Energy'}


class deck:

	playerHand = [] #structure that will kealep up with player's hand contents and size.
	playerPrizes = [] #structure that will keep up with player's prize contents and size.
	deckFile = open("originalDeckList.txt", 'r')
	playerDeck = deckFile.read().split('\n') # structure that will keep up with player's deck contents and size.
	deckFile.close()

	def getHandSize(self):
		return len(deck.playerHand)

	def getHandContents(self):
		return deck.playerHand

	def getPrizeSize(self):
		return len(deck.playerPrizes)

	def getPrizeContents(self):
		return deck.playerPrizes

	def getDeckContents(self):
		return deck.playerDeck

	def getDeckSize(self):
		return len(deck.playerDeck)







	def shuffle(self):
		shuffeled = [] #to copy over
		visited = [] #to keep track of what indicies we've seen 
		numCards = self.getDeckSize()

		while(len(shuffeled) != numCards):
			randIndex = random.randint(0, numCards - 1)
			
			if(randIndex in visited): #if we've already seen this index, do nothing
				pass
			else:
				shuffeled.append(deck.playerDeck[randIndex]) #choose a random element from our non-shuffeled deck and assign it a spot in the shuffeled deck.
				visited.append(randIndex) #add it to visited, so we know if we've seen it or not

		deck.playerDeck = shuffeled
		

	def resetGame(self):
		deckList  = open('originalDeckList.txt', 'r')
		deck.playerDeck = deckList.read().split('\n')
		deck.playerHand = []
		deck.playerPrizes = []



	def startingHand(self): #don't forget to shuffle the deck first.
		for i in range(7):
			deck.playerHand.append(deck.playerDeck.pop(0))#adds the first card from the shuffeled deck to my hand. Does this 7 times.

		return deck.playerHand
		#print "You have drawn your hand."


	def placePrizes(self):
		for i in range(6): #update contents of playerPrizes
			deck.playerPrizes.append(deck.playerDeck.pop(0))
		
		print "You have placed your prizes."


	def drawCards(self, amount):

		for i in range(amount): #update contents of player han
			if(len(deck.playerDeck) == 0):
				return "You have no cards left in your deck.  You lose."
			else:
				print "You drew: " + deck.playerDeck[0]
				deck.playerHand.append(deck.playerDeck.pop(0))

		print "You have drawn " + str(amount) + " cards."

	def returnHand(self):
		for i in range(len(deck.playerHand)):
			deck.playerDeck.insert(i, deck.playerHand.pop(0))#pops every card in our hand off and inserts it into the
			#deck at position i. Doesn't really matter where, because we shuffle it after.
		self.shuffle()
		self.shuffle()
		print "You have returned your hand to the deck."


