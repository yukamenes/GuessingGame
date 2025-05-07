# Number Guessing Game 🎲✨

Welcome to the **Number Guessing Game**! 🕹️ This fun Python console game challenges you to guess a secret number between 1 and 100. With cool ASCII art, two difficulty levels, and clear feedback, it’s a great way to test your guessing skills! 🚀

Inspired by the demo at [appbrewery.github.io/python-day12-demo/](https://appbrewery.github.io/python-day12-demo/).

## 🎮 Features
- 🔢 Randomly generated number between 1 and 100.
- 🥳 Two difficulty modes:
  - **Easy**: 10 attempts to guess the number.
  - **Hard**: 5 attempts for a real challenge!
- ✅ Input validation ensures guesses are integers between 1 and 100.
- 📢 Helpful feedback: "Too high" or "Too low" to guide your guesses.
- 🎨 Eye-catching ASCII art logo to set the mood.
- 🏆 Win with a celebratory message or learn the answer if you run out of guesses.

## 🛠️ Requirements
- 🐍 Python 3.6 or higher
- 📦 No external libraries needed (just the standard `random` module)

## 🚀 Get Started
1. Clone or download this repository to your computer. 📥
2. Make sure Python 3 is installed. Check with:
   ```bash
   python --version
   ```
3. Ensure the following files are in the same directory:
   - `main.py`: The heart of the game logic. 💻
   - `art.py`: The awesome ASCII art logo. 🎨

## 🎉 How to Play
1. Open your terminal and navigate to the project folder.
2. Launch the game with:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts:
   - Choose a difficulty by typing `easy` or `hard`. ⚖️
   - Guess the number by entering integers between 1 and 100. 🔍
4. The game will tell you if your guess is **too high**, **too low**, or **correct**! 🎯
5. Win by guessing the number, or find out the answer if you run out of attempts. 🥳

## 📂 Project Structure
- `main.py`: Contains the game logic, input validation, and game loop.
- `art.py`: Stores the stylish ASCII art logo displayed at startup.

## 🖥️ Example Gameplay
Below is an example of how the game looks when you play it:

```
(                          )   )        ( /(                 )            
 )\ )     (    (         ( /(( /(   (    )\())  (     )    ( /(    (  (    
(()/(    ))\  ))\(  (    )\())\()) ))\  ((_)\  ))\   (     )\())  ))\ )(   
 /(_))_ /((_)/((_)\ )\  (_))((_)\ /((_)  _((_)/((_)  )\  '((_)\  /((_|()\  
(_)) __(_))((_))((_|(_) | |_| |(_|_))   | \| (_))( _((_)) | |(_)(_))  ((_) 
  | (_ | || / -_|_-<_-< |  _| ' \/ -_)  | .` | || | '  \()| '_ \/ -_)| '_| 
   \___|\_,_\___/__/__/  \__|_||_\___|  |_|\_|\_,_|_|_|_| |_.__/\___||_|   

Welcome to the Number Guessing Game!
I'm thinking about a number between 1 and 100
Choose a difficulty. Type 'easy' or 'hard': 12
You should write 'easy' or 'hard'
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 remaining to guess the number
Make a guess: 60
Too low
Guess again
You have 9 remaining to guess the number
Make a guess: 80
Too low
Guess again
You have 8 remaining to guess the number
Make a guess: 90
Too high
Guess again
You have 7 remaining to guess the number
Make a guess: 85
Too high
Guess again
You have 6 remaining to guess the number
Make a guess: 84
Too high
Guess again
You have 5 remaining to guess the number
Make a guess: 92
Too high
Guess again
You have 4 remaining to guess the number
Make a guess: 82
You got it! The answer was 82
```

## 🌟 Why It's Fun
- Simple yet engaging gameplay that keeps you guessing! 🤔
- Perfect for beginners learning Python or anyone who loves a quick challenge. 💡
- The ASCII art makes every game session visually exciting! 🎨

## 🙌 Credits
- ASCII art created using [patorjk.com/software/taag/](https://patorjk.com/software/taag/). 🖌️
- Inspired by the awesome Python course demo from App Brewery. 📚

## 📜 License
This project is licensed under the **CC0 1.0 Universal (CC0 1.0) Public Domain Dedication**.  
The code and assets are dedicated to the public domain, meaning you can use, modify, distribute, and share them freely without any restrictions. No attribution is required, but it’s always appreciated! 😊  
For full details, see the [CC0 1.0 Universal license](https://creativecommons.org/publicdomain/zero/1.0/).

---

**Ready to guess the number? Dive in and have fun!** 🎉
