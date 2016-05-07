TASK
1
Write an application, which will perform the following tasks.
1 ) Parse the HTML for the “Top Playstation 3 Games (By Metascore)” on Metacritic’s PS3 page:
http://www.metacritic.com/game/playstation-3.
a ) Expose a method, which will return the parsed information as an array of JSON
elements.
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
2) Expose a REST API for retrieving top PS3 games.
There should be 2 exposed methods:
a) An HTTP “GET” request a “/games” returns all top PS3 games on metacritic page
b) An HTTP “GET” request at “/games/TITLE_OF_GAME_GOES_HERE” returns JSON for a
specific game that matches the corresponding game title. For example, an HTTP GET at
/games/Gran%20Turismo%206 should return an individual JSON object for Gran
Turismo 6
Example output:
{
"title": "Gran Turismo 6",
“score”: 81
}
Deliverables:
A. Provide the source-code, which satisfies 1 and 2 described above.
B. Provide “Readme” style documentation on how to run your code.
C. P r o v i d e u n i t t e s t s t o p r o v e t h e c o r r e c t n e s s o f y o u r c o d e .
