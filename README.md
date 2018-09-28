
# Chess AI
### Run it
` python3 GameMaster.py Player01 Player01` 

### Summary
Welcome to _Chess AI_, this project was created by Ben and Kostya. We took an introductory artificial intelligence class and decided it would be fun to use some of the new skills we had learned and apply them to a personal project.  

### Skills learned
* Alpha Beta Pruning
* State Space Search
* AI , automation, move prediction
* Python

### Game Assumptions
* No special moves
* Regular 8 by 8 chess board

### What you're seeing
As the game runs you will see two bots that are looking two to three moves ahead during each turn to determine what their next best move is. While exploring future moves we assume the opposing bot will choose the best possible move they can, and we use a technique called Alpha Beta pruning that cuts off unhelpful branches before exploring them in order to save time.

The game is built in Python3 and relies on the concept of State Space Search, that is every move is a separate state. This makes it easier to explore options, hold on to small bits of information that are dependent on the current state, and makes it easier to pass on moves between functions.
