# NFL-Predictor
This program creates a logistic regression model to predict a team's probability of winning a game. It can also rank teams based on the model produced.

# Necessary Packages
To run this program, you will need to install the sports-reference and the sklearn packages. Installing these packages will also install any other packages necessary.

# Steps
You will need to train the model first in order to do any other actions or you can use the provided model that has been trained using data from 1995-2019. After training, you can choose to either test the model, predict a game's result, or produce rankings.

# Training
Run the program and enter "train" when prompted. Next, specify the range of NFL seasons that will be used as training data. A logistic regression model will be generated based off a variety of stats pulled from the Sports Reference API. This may take a few minutes, or maybe even longer depending on the range of seasons used. Once this is done, you are ready to move on to either testing, predicting, or ranking.

# Testing
Run the program and enter "test" when prompted. Next, specify the range of NFL seasons that will be used as testing data. The number of correct predictions, number of total predictions, and the percentage correct will be printed to the console. Testing on prior seasons has resulted in over 70% accuracy when I've tried it.

# Predicting
Run the program and enter "predict" when prompted. Next, enter any NFL team name/abbreviation, any season, and where the game will be played in relation to this team. Now, enter another NFL team and another season. The program will output the probability that the first team has of winning against the second team.

# Ranking
Run the program and enter "rank" when prompted. Next, specify the range of NFL seasons that will be considered in the rankings. A ranking including every team in the specified range will be printed. 
