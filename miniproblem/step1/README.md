## Step 1: Organizing the Tournament
___

### Rules

* 100 players on the ladder
* Each round consist of 3 consecutive games in weach each players has to stack as much points as possible following the raking model
* At the end of each round, players are attributed a score which is the mean of the points they have obtained during the last 3 games.
* The last 10 players are out of the tournamenet. The score obtained is cumulative.
* The process is repeated until 10 players remain on the ladder.
* For the last 10 players, scores are reinitiated and 5 games are played between these players.


### Ranking model

* Impostor: 1pts per kill, 3pts per undiscovered murder, 10pts if win
* Crewmate: 3pts if the argument unmasks an imposter, 1pts if all solo tasks are made, 5ptsif win


### Data Structure and Algorithm

AVL Tree (here the database)
100 players created randomly with random score between 0 and 12 at each games and stored in the AVL Tree.
Last 10 players are deleted from the AVL Tree.
Once we have done 3*9 round (27 games) an new AVL Tree is created for the last 10 players.