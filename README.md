# OOP_Quiz_Project
## About The Project 
This is a terminal-based trivia application built to master Object-Oriented Programming (OOP) in Python. The app fetches real-time questions from the Open Trivia Database API, manages game state through a dedicated QuizBrain class, and uses a modular architecture to separate data, modeling, and logic.

## Technical Highlights

*Object-Oriented Design*: strictly separates concerns into main (controller), QuizBrain (logic), and Question (model).

*API Integration*: Uses the requests module to fetch dynamic JSON data from the Open Trivia Database (OpenTDB).

*Data Modeling*: Converts raw JSON data into Python Objects for cleaner code and better error handling.

*Input Handling*: Includes logic for HTML entity decoding (fixing characters like &quot;) and case-insensitive user input.

## How to Run

Clone the repository.

Install dependencies: pip install requests

Run the game: python main.py
