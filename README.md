# Moto Madness
Battleship is a single-player python version of the classic turn-based guess game.</br >
</br > 

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/am-i-responsive.png?raw=true)</br >
</br >
Image created using [Am I responsive](https://ui.dev/amiresponsive)</br >
</br >

### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://moto-madness.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/cmikedev/ecommerce).


____



## 1. Design

### 1.1 Structure

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/battleship-flowchart.png?raw=true)</br >
</br>

1. The user inputs their desired difficulty level.
2. The gameboard's grid, enemy ships and the number of missiles are determined by the difficulty level selected.
3. An enemy and guess (user) gameboards of grid N x N are generated.
4. The ships are generated and placed on the enemy gameboard.
5. When the user enters their row and column guess, the guess gameboard stores these coordinates - this is not visible to the user.
6. If the coordinates on the user guess gameboard matches those of the visible enemy one, the gameboard reprints showing an "X" within the grid to denote a hit.
7. If the coordinates don't match, the gameboard reprints showing a "-" to denote a miss.
8. If the number of ships hit equals the number of ships generated and the number of missiles remaining is not equal to 0, then the user wins.
9. If the number of ships hit is less than the number generated and the number of missiles is equal to 0, the user loses.</br >
</br >

### 1.2 Modules Used
* The __sleep__ function is imported from Python's [time](https://docs.python.org/3/library/time.html) module in order to stagger displayed text (see section 2.1) and create a delay before the running of selected loops.
* The __randint__ function is imported from Python's [random](https://docs.python.org/3/library/random.html) module in order to randomly generate the position of the enemy ships on the game board.</br >
</br >

## 2. Features

### 2.1 The Introduction Screen
When the page loads the user is presented with an introduction providing a brief background story. The purpose of this is to provide a sense of immersion in the game.
* The text loading is staggered in order to make it look like the user is awaiting receipt of a message from fleet Command. This is done to create a further sense of immersion by linking the user with an imaginery third party, a Fleet Command.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/introduction.png?raw=true)</br >
</br >

* The user is then provided with a prompt move on to the next screen allowing them as much time as is required to read the introduction screen.</br >
</br >

### 2.2 The Instructions Screen
* The game instructions are laid out for the user. Again, they will be provided with a prompt to move onto the next screen in their own time.
* The user will not need to come back to this screen as simplified instructions will be provided on the game screen.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/instructions.png?raw=true)</br >
</br >

### 2.3 The Difficulty Screen
* The Difficulty Screen provides the user the opportunity to provide input into the game. The four difficuly levels are explained and the user is prompted to choose.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/difficulty.png?raw=true)</br >
</br >

* Depending on the difficulty level chosen, from 'Easy' to 'Insane', the board size will increase as will the number of enemy vessels. The number of missiles, while increasing in number, will either decrease proprotionately to the board size or remain the same (in the case of 'Medium' and 'Hard').</br >
</br >

### 2.4 The Game Board
When the user has selected their desired difficulty level, the game board will be generated with its size corresponding to the diffficulty chosen.
* The user is once again provided with instructions on how to play.
* The game board grids are visualised (the image below shows a 9x9 grid as per 'Insane' difficulty level).
* The number of enemy ships and the number destroyed will be displayed (again, based on difficulty level chosen).
* The missiles (turns).</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/gameboard.png?raw=true)</br >
</br >

* The user is asked to input their guess by way of selected the numerical row and aphabetical column. These coordinates represent a place on the grid.
* An enemy ship occupies one grid space. If the user's guess corresponds to the coordinates of the enemy ship, the enemy ship is destroyed.
* The board will then be reprinted displaying an "X" in the grid where a ship was destroyed or a "-" to denote a miss.
* The number of enemy ships and missiles remaining displays are then updated as the board reprints.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/ships-missiles-remaining.png?raw=true)</br >
</br >

* If the user has failed to destroy all ships by the time their missiles remaining reaches 5, the missiles remaining message will update to warn the user that they are running low on ammo.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/low-ammo-warning.png?raw=true)</br >
</br >

### 2.5 End Game
The game can end one of two ways:
* If the user destroys all of the enemy vessels before they run out of missiles they win the game. The game will end a new screen will load informing them of their victory.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/game-won.png?raw=true)</br >
</br >

* If the user runs out of missiles and there are still enemy vessels remaining, the lose the game. The game will end a new screen will load informing them of their defeat.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/game-lost.png?raw=true)</br >
</br >


## 3. Testing

### 3.1 General Testing
During the development of the project, much of the functions were initially written using the [Replit Python Online Compiler](https://replit.com/lm/python3). This allowed for testing and editing of smaller sctions of code before they were added to the main file. Individual functions were tested in the main file through the GitPod terminal by adding them to a main function.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/main.png?raw=true)</br >
</br >

This allowed for the entirety of the game running order to be tested or just individual functions. The majority of the errors returned during the testing stage related to items being out of range or handling the input of blank/incorrect data. An example of two of the latter errors is shown below:
* The first, where a user is asked to please enter a ship row, allowed for the return key to be pressed.
* The second, where a user is asked to enter a ship column throws up a <mark style="background-color: grey">ValueError</mark> when a return key is pressed.
In both instances a message informing the user that their input was incorrect and prompting them to enter the correct input should have been returned.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/errors.png?raw=true)</br >
</br >

### 3.2 PEP8 Testing
The [PEP8 Online](http://pep8online.com/) validator provided visibility for any errors within the code. The initial validation run flagged numerous amber and red errors relating to whitespace, no lines after functions, missing parentheses and lines of code that were too long. Over the course of several more validation runs, these errors were eliminated and the code as it is shows no errors.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/pep8-result.png?raw=true)</br >
</br >

### 3.3 Bugs
All identified bugs have been fixed including the example shown in section 3.1 above.</br >
</br >


## 4. Deployment

### 4.1 Deploying the repository via Heroku
* The app was created using Heroku via the following steps:
    * On the https://dashboard.heroku.com/apps page, click <mark style="background-color: grey">New</mark> and then select <mark style="background-color: grey">Create New App</mark> from the drop-down menu.
    * When the next page loads insert the <mark style="background-color: grey">App name</mark> and <mark style="background-color: grey">Choose a region</mark>. The click <mark style="background-color: grey">Create app</mark>
    * In the settings tab click on <mark style="background-color: grey">Reveal Config Vars</mark> and add the key <mark style="background-color: grey">Port</mark> and the value <mark style="background-color: grey">8000</mark>. The other credentials 
    </br >
* To deploy the Heroku app:
    * Click on the <mark style="background-color: grey">Deploy</mark> tab and select <mark style="background-color: grey">Github-Connect to Github</mark>.
    * Enter the repository name and click <mark style="background-color: grey">Search</mark>.
    * Choose the repository that holds the correct files and click <mark style="background-color: grey">Connect</mark>.
    * A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub. For this app automatic was selected.
    * Once the deployment method has been chosen the app will be built and can be launched by clicking the <mark style="background-color: grey">Open app</mark> button at the top of the page.<br />
    <br />

### 4.2 GitHub
#### Forking the repository
* The GitHub repository can be forked to make a copy of the original. This copy can then be viewed or changed without affecting the original repository via the following steps:
    * In the Respository section, select the [ecommerce](https://github.com/cmikedev/ecommerce) repository
    * At the top right of the page select <mark style="background-color: grey">fork</mark> from the menu below your profile
    * A copy of the repository will now be created in your account

#### Creating a local clone
* To create a local clone via GitHub:
    * In the Respository section, select the [ecommerce](https://github.com/cmikedev/ecommerce) repository
    * From the horizontal menu above the repository contents select <mark style="background-color: grey">Code</mark>
    * __Copy__ the link that that is shown
    * Within __Gitpod__ change the directory to where you would like the location of the cloned directory to be
    * Type __git clone__ and paste the link that you copied
    * Press <mark style="background-color: grey">Enter</mark> and the local clone will be created<br />
    <br />




## 5. Credits



----

## 6. Acknowledgements
I would like to thank my course mentor Harry Dhillon for providing guidance on this project.