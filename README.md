# shouldifetch
Testing a hypothesis about not fetching in order NOT draw the 5th land in a row

## Premise
Recently I came acorss and arugument on wether or not if you draw 4 lands in a row you should fetch before potentialy drawing another lands.
The intuition is that you should not fetch since it's very unlikley that there are 5 lands in a row on top of your deck, and shuffling it will "break" that unlikley scenario.
To me this seems totaly wrong since intuitively i think MTG decks are memoryless.

### Memorylessness
From [wikipedia](https://en.wikipedia.org/wiki/Memorylessness): In probability and statistics, memorylessness is a property of certain probability distributions. It usually refers to the cases when the distribution of a "waiting time" until a certain event does not depend on how much time has elapsed already. To model memoryless situations accurately, we must constantly 'forget' which state the system is in: the probabilities would not be influenced by the history of the process.

A nice example is if you were to toss N coins and all are tails the N+1st coin will still have only a 50% chance of being tails since the tosses are independant. (Although it seems unlikely to get 5 tails in a row (in fact it, kinda is $(\frac{1}{2})^5 = 0.03125$))

### Setup
To me this seems like a simple problem of proving wether or not MTG decks are memoryless.
Card decks follow a discrete distribution and [here](https://math.stackexchange.com/questions/2600145/prove-that-memorylessness-of-a-discrete-distribution-defines-geometric-distribut#2600168) I found that a discrete distribution is memolyless $\textbf{iff}$ it's gemetric.
I believe, since we are modeling a deck as lands of non lands and looking at a number of lands before a nonlands we can say this model follows a geometric distribution $\rightarrow$ is memoryless.

### Experiment
In the code provided i have some varibales with deck size and what not and am testing 3 scenerions, one where one does not fetch, one where one only shuffles, and one where the player fetches.
I rand 100000 iterations and found the following probabilities of drawing the 5th land in a row in a 60 card deck conating 25 lands:
| Scenario    | Probability     |
|--------------|-----------|
| natural | 0.4053      |
| shuffle      | 0.40588  |
| fetch      | 0.39246  |

### Results
The experiement seems to have prooven that MTG decks are memoryless and even that you should fetch to thin your deck in this spot. Thanks for coming to my Ted Talk!