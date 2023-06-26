from random import shuffle

NO_LANDS = 25
DECK_SIZE = 60
NO_LANDS_IN_A_ROW = 4

ITERATIONS = 100000

deck = ["L" if i <= 25 else "N" for i in range(DECK_SIZE)]

# number of land occurance for each type of scenario
data = {
	"natural": 0,
	"shuffle": 0,
	"fetch": 0
}

# true if deck has four lands in a row somewhere
def fourInARow(deck: list) -> bool:
	return "L" * NO_LANDS_IN_A_ROW in "".join(deck)

# returns index of next card after a 4 lands sequence
def nextIndex(deck: list) -> bool:
	return "".join(deck).index("L" * NO_LANDS_IN_A_ROW) + NO_LANDS_IN_A_ROW + 1

for i in range(ITERATIONS):
	print(f"iteration: {i}")

	goodDeck = False

	# make sure deck has a sequence of 4 lands and it occurs in first half of deck
	while not goodDeck:
		shuffle(deck) 

		if fourInARow(deck):
			if (nextCardIndex := nextIndex(deck)) <= DECK_SIZE // 2:
				goodDeck = True

	print(deck)
	print(f"nextCardIndex: {nextCardIndex}")
	
	# try again if the all lands sequence was last N cards of deck
	if nextCardIndex >= DECK_SIZE:
		i -= 1
		shuffle(deck)
		continue

	nextCard = deck[nextCardIndex]

	# just draw card
	data["natural"] += 1 if nextCard == "L" else 0
	print(f"nat: {nextCard == 'L'}")

	# just randomise deck
	restOfDeck = deck[nextCardIndex:]
	shuffle(restOfDeck)
	data["shuffle"] += 1 if restOfDeck[0] == "L" else 0
	print(f"nat: {restOfDeck[0] == 'L'}")

	# fecth a lands from deck if deck has land
	restOfDeck.remove("L")
	shuffle(restOfDeck)
	data["fetch"] += 1 if restOfDeck[0] == "L" else 0
	print(f"nat: {restOfDeck[0] == 'L'}")

	print(f"asdf {deck}")

for k, v in data.items():
	print(f"SCENARIO: {k} \tPROBABILITY: {v / ITERATIONS}")