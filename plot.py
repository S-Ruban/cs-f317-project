import matplotlib.pyplot as plt  # matplotlib library to plot graphs
import csv
import os
from numpy.lib.function_base import average  # idk why I imported this

red_wins = []  # cumulative games red won whenever it starts first
black_wins = []  # cumulative games black won whenever it starts first
rw = []  # individual result of every game that red plays first
bw = []  # individual result of every game that black plays first
rwp = []  # red win percentage vs games
bwp = []  # black win percentage vs games
moves = []  # moves vs games
avmoves = []  # average number of moves vs games
i = 0
with open(
    os.getcwd() + "/stats/stats_log_1.csv", "r"
) as csvfile:  # modify this part to open whichever .csv file required
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        if i > 0 and i % 2 == 0:  # skip every alternate blank line
            black_wins.append(int(row[1]))
            red_wins.append(int(row[0]))
            moves.append(int(float(row[3]) * 42))
        i += 1
*red_wins, _ = red_wins  # remove last game
rw.append(red_wins[0])
bw.append(black_wins[1] - black_wins[0])
for i in range(len(red_wins)):
    if i % 2 == 0:
        if i > 0:
            rw.append(red_wins[i] - red_wins[i - 1])
    else:
        if i > 1:
            bw.append(black_wins[i] - black_wins[i - 1])
rwp.append(rw[0] * 100)
bwp.append(bw[0] * 100)
for i in range(1, len(rw)):
    rwp.append(((rwp[i - 1] / 100) * i + rw[i]) * 100 / (i + 1))
    bwp.append(((bwp[i - 1] / 100) * i + bw[i]) * 100 / (i + 1))
x1 = range(1, len(rwp) + 1)  # x ticks
x2 = range(1, len(moves) + 1)  # x ticks
print(average(moves))
avmoves.append(moves[0])
for i in range(1, len(moves)):
    avmoves.append((avmoves[i - 1] * i + moves[i]) / (i + 1))
print(rwp[-1], bwp[-1])
plt.plot(x1, rwp, color="red")
plt.plot(x1, bwp, color="black")
plt.xlabel("Number of games")
plt.ylabel("% win rate when playing first")
plt.show()
# plt.plot(x2, moves)
plt.plot(x2, avmoves)
plt.xlabel("Number of games")
plt.ylabel("Number of moves")
plt.show()
