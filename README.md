#TASK
1. Write an application, which will perform the following tasks. 1

Parse the HTML for the “Top Playstation 3 Games (By Metascore)” on Metacritic’s PS3 page:

http://www.metacritic.com/game/playstation-3.

* Expose a method, which will return the parsed information as an array of JSON elements. 1a
  E x a m p le output:

[

{

"title": "XCOM: Enemy Within",

“score”: 88

},

{

"title": "Assasin’s Creed IV: Black Flag",

“score”: 88

}

... etc ...

]

2. Expose a REST API for retrieving top PS3 games. 2

There should be 2 exposed methods:

* An HTTP “GET” request a “/games” returns all top PS3 games on metacritic page 2a
* An HTTP “GET” request at “/games/TITLE_OF_GAME_GOES_HERE” returns JSON for a
specific game that matches the corresponding game title. For example, an HTTP GET at /games/Gran%20Turismo%206 should return an individual JSON object for Gran
Turismo 6 2b

Example output:

{

"title": "Gran Turismo 6",

“score”: 81

}

##Deliverables:

1. Provide the source-code, which satisfies 1 and 2 described above. 1
2. Provide “Readme” style documentation on how to run your code. 2
3. Provide unittests to prove the correctness of your code. 3



Requirements:
pyquery (pip install puquery)
