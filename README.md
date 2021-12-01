# About

This project is an implementation of a research paper in the field of reinforcement learning

**Reinforcement Learning for Connect Four: https://web.stanford.edu/class/aa228/reports/2019/final106.pdf**

We have employed Deep Q Learning in our agent to play against itself and learn with each move. The agent takes turns as player 1 (red) and player 2 (black), where each player plays the starting move every alternate game.

## Tools and Frameworks

Keras framework is used for the Deep Q Network. `matplotlib` library is used to plot the graphs of the results. The project contains four python files, viz, `c4.py`, `c4_game.py`, `c4_model.py` and `plot.py`.

`c4.py` is the main program and is to be executed to either train the agent, play against the agent as a human player, or play with another human player. This program controls the flow of the game and collects statistics of the game during training of the agent.

` c4_game.py` is the game environment that contains the rules of the game and ensures that the rules are not violated. Unlike typical environments in reinforcement learning that are imported from OpenAI Gym or other sources, this environment was coded from scratch in python.

`c4_model.py` is the code for the Deep Q Network and the Q Learning algorithm using the convolutional neural network (CNN). Here the CNN is implemented using the Keras framework. Adam optimizer is used in the CNN.

`plot.py` is the code to read the `.csv` file containing the statistics of each game played and plot the results using `matplotlib`.

`plots` folder contains graphs for win rate vs games, number of moves vs games and average number of moves vs games

`snapshots` folder contains agent's snapshot of training

`stats` folder contains the `.csv` files

`order.txt` contains order of hyperparameters during testing

# Running the Code

Training is done in AI vs AI mode:
`python c4.py ava`

You can play against the agent in Human vs AI mode:
`python c4.py hva --weights-file=snapshots/current_best.h5`

Play against another player (enter column number to move and `q` to quit):
`python c4.py hvh`

Edit the `plot.py` file to read the specific `.csv` file that has the information for training of one set of hyperparameters.

# Team Members

1. 2019A7PS0097H - Ruban S
2. 2018B5A71056H - Tanmay Chowhan
3. 2019AAPS1489H - Neerukonda Harsha
4. 2019AAPS0248H - Indrashis Das
5. 2019A7PS0111H - Bharadwaz Rushi
