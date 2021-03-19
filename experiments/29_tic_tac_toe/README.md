**Tic tac toe game**

    Can be played with another person or with the computer.
    
    Rules:
        The game is played on a grid that's <5> squares by <5> squares.
        User can choose to play X (makes first move) or 0. Players take turns putting their marks in empty squares.
        The first player to get 5 of their marks in a row (up, down, across, or diagonally) is the winner.
        When all <25> squares are full, the game is over. If no player has 5 marks in a row, the game ends in a tie.
					

**board.py**

    Creates grid board <5> by <5>.
    Fills the chosen cell with the User (or computer) symbol.
    After each step checks if the last step makes the win.


**user.py**
    
    Class User contains information about User: username, password, websocket connection info. 
    Processes messages for user connection, choice (to play X or 0), move, restart button click, disconnect.
        Initiate start and processing (while connected) websocket channel for User.
        Adds a new connected user to the users list if there are less than two of them.
        Gives the option to play X or 0.
        If one of two players made a choice to play X or 0, the game started (creates board).
        The first step made by the User who plays X. When User made their move, the move goes to another player.
        In the end of the round any player can choose to restart the game.


**main_logic.py**

     If the game wasn't started yet and there are fewer than 2 players, a new player (not in the users list) can be added.
        User name and generated password added to the users list.
    Initiate starts and processes websocket channel for the added user.
    Exchanges massages (pressed buttons, moves) between users (server, web browser).
    Starts the game, processes each move, restarts the game.


**start_servers.py**

    Starts http server at port <8080>, websoket at port 6789.
    Class HttpHandler to exchange messages between two different users (possible on different machines) by one central server.
        From main HTML page which contains register form redirect user to a game field, updates board and score.
    Processes websocket connection: check if user connected (in users list) - starts connection (message exchange), else prints 'logged off'.
