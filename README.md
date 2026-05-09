# Logic101 — PSET 0

> "Programming is not about memorizing syntax. It is about learning how humans, systems, and information interact."

Welcome to the very first problem set of Logic101.

These problems are designed not merely to teach Python syntax, but to help you think computationally.

Each problem introduces:

- a real-world system
- cultural or historical context
- computational thinking
- logical precision
- and the idea that software is ultimately about transforming information

Unlike traditional programming exercises, these problems intentionally connect code with:

- human behavior
- language
- communication
- technology
- and systems used in everyday life

---

## Getting Started

### In a Codespace

1. Click [this link](https://codespaces.new/Build-and-Beyond/pset0?quickstart=1) to open a Codespace
2. Wait for the environment to set up (about 1-2 minutes)
3. Run `l101 login` to authenticate with GitHub
4. You're ready to code!

### Locally

```bash
pip install l101
l101 login
l101 pull pset0
cd ~/logic101/pset0
```

### Available Commands

| Command | What it does |
|---------|-------------|
| `l101 pull pset0` | Download the starter code |
| `l101 test namaste.py` | Run visible tests locally |
| `l101 submit pset0` | Submit for grading (max 5 attempts) |
| `l101 status` | Check submission history |

---

## Problem 1 — NAMASTE

> "A greeting is one of the oldest technologies humans ever invented."

Long before smartphones, social media, or even modern nations existed, humans used greetings to signal peace, trust, and respect.

The word *Namaste* comes from Sanskrit:

```
namas + te
```

roughly meaning:

```
I bow to you
```

What makes this especially fascinating is that gestures similar to Namaste appear across many ancient cultures. Historians have found comparable greeting postures in:

- ancient Indian sculptures
- Buddhist traditions across Asia
- old temple carvings
- early meditation practices

Even more interestingly, during the COVID-19 pandemic, many world leaders and media outlets discussed Namaste as a contactless alternative to handshakes.

A simple greeting carried thousands of years of cultural history into the modern digital world.

Today, modern software systems also begin interactions with greetings:

- chat applications
- voice assistants
- customer support bots
- games
- websites

One of the very first things many programmers learn to build is a tiny program that greets a user.

---

### Specification

In a file called `namaste.py`, implement a program that prompts the user for their name and then greets them.

For example, if the user's name is `Aarav`, your program should output:

```
Namaste, Aarav
```

### Demo

```
What is your name? Aarav
Namaste, Aarav
```

```
What is your name? Tanishka
Namaste, Tanishka
```

### Hints

- Remember that `input` allows programs to receive information from users.
- Think carefully about how to store the user's name so you can use it later.
- `print` can display multiple pieces of information together.

### What This Problem Quietly Teaches

```
Input → Store → Output
```

The user gives information to the program. The program stores that information in memory. Then the program uses it to generate output.

---

## Problem 2 — NAMASTE+

> "Humans are flexible with language. Computers are not."

Across India, greetings often change depending on language and region.

Some examples include:

| Language / Region | Greeting      |
| ----------------- | -------------- |
| Hindi / Sanskrit  | Namaste        |
| Bengali           | Nomoshkar      |
| Tamil             | Vanakkam       |
| Punjabi           | Sat Sri Akal   |
| Gujarati          | Kem Cho        |
| Kannada           | Namaskara      |

Real-world software rarely receives perfectly formatted input.

A user might type:

```
tamil
```

or:

```
TAMIL
```

or even:

```
   TaMiL
```

Modern software systems often clean and format user input before processing or displaying it.

---

### Specification

In a file called `namasteplus.py`, implement a program that asks the user for:

- their name
- their preferred language or region

and then greets them appropriately.

For example:

```
What is your name? Ravi
Preferred language: Tamil
Vanakkam, Ravi
```

or:

```
What is your name? Ananya
Preferred language: Bengali
Nomoshkar, Ananya
```

Your program should behave correctly regardless of capitalization or accidental spaces. If the user enters a language not in the table, your program should fall back to `Namaste`.

### Useful String Methods

| Method          | Example                    | Result        |
| --------------- | -------------------------- | ------------- |
| `.lower()`      | `"HELLO".lower()`          | `"hello"`     |
| `.upper()`      | `"hello".upper()`          | `"HELLO"`     |
| `.capitalize()` | `"tanishka".capitalize()`  | `"Tanishka"`  |
| `.title()`      | `"logic 101".title()`      | `"Logic 101"` |
| `.strip()`      | `"   hello   ".strip()`    | `"hello"`     |

### What This Problem Quietly Teaches

```
Programs can make decisions.
```

This problem introduces:

- conditions
- input normalization
- string formatting
- branching logic

Many real-world systems depend heavily on handling messy human input correctly.

---

## Problem 3 — TRANSLATOR

> "Technology doesn't just change how humans communicate. It changes language itself."

Before smartphones became smart, typing on phones was frustratingly slow.

Early mobile phones used numeric keypads instead of full keyboards. To type even a simple message, users often had to press the same button multiple times.

At the same time, SMS messages originally had strict character limits. Twitter, when first launched in 2006, limited posts to only 140 characters.

As a result, internet users began inventing shortcuts and abbreviations:

```
brb  → be right back
lol  → laughing out loud
idk  → I don't know
gr8  → great
u    → you
r    → are
```

Over time, internet language evolved even further. Modern social media platforms introduced entirely new slang:

```
sus
mid
slay
rizz
no cap
```

Modern software systems constantly process messy human language. Examples include:

- autocorrect systems
- chat applications
- subtitles
- moderation systems
- translators
- AI chatbots

---

### Specification

In a file called `translator.py`, implement a program that converts Gen Z slang into more traditional English.

Your program should prompt the user for a sentence and then replace known slang words with their corresponding meanings.

| Slang    | Meaning        |
| -------- | -------------- |
| `fr`     | `for real`     |
| `idk`    | `I don't know` |
| `sus`    | `suspicious`   |
| `mid`    | `average`      |
| `no cap` | `not lying`    |
| `rizz`   | `charisma`     |

For example:

```
Input: fr bro that movie was mid
Output: for real bro that movie was average
```

### Useful String Methods

| Method       | Example                                 | Result          |
| ------------ | --------------------------------------- | --------------- |
| `.lower()`   | `"HELLO".lower()`                      | `"hello"`       |
| `.strip()`   | `"   hello   ".strip()`                | `"hello"`       |
| `.replace()` | `"sus".replace("sus", "suspicious")`   | `"suspicious"`  |

### What This Problem Quietly Teaches

```
Human language is inconsistent.
```

Modern systems constantly:

- clean text
- normalize inputs
- replace patterns
- process human communication

At their core, many systems are simply:

```
Input → Process → Output
```

---

## Problem 4 — MORSE

> "Long before the internet, humans were already transmitting messages across continents using nothing but electricity, timing, and sound."

In the early 1800s, sending information across long distances was painfully slow. A message from one city to another could take:

- days
- weeks
- or even months

That changed with the invention of the **telegraph** — one of the world's first major electrical communication systems.

Instead of physically carrying messages, telegraphs transmitted electrical signals through long wires stretched across cities and countries.

But there was a problem. How could words be sent using only `ON` or `OFF` signals?

To solve this, Samuel Morse and Alfred Vail helped develop a system now known as **Morse Code** — a communication system where letters are represented using combinations of:

- short signals (`.`)
- long signals (`-`)

One of the most famous Morse signals in history is **SOS**, represented as:

```
... --- ...
```

Even today, Morse code still appears in:

- emergency communication
- aviation
- military systems
- amateur radio
- navigation beacons

---

### Specification

In a file called `morse.py`, implement a program that converts text into Morse code.

Your program should prompt the user for a word or sentence and then output the corresponding Morse representation.

For example:

```
Input: SOS
Output: ... --- ...
```

```
Input: HELLO
Output: .... . .-.. .-.. ---
```

Your program should:

- Handle both uppercase and lowercase input
- Include numbers 0-9
- Separate letters with spaces
- Separate words with ` / `

### MORSE Code Dictionary

| Letter | Code  | Letter | Code  | Number | Code   |
| ------ | ----- | ------ | ----- | ------ | ------ |
| A      | `.-`  | N      | `-.`  | 0      | `-----`|
| B      | `-...`| O      | `---` | 1      | `.----`|
| C      | `-.-.`| P      | `.--.`| 2      | `..---`|
| D      | `-..` | Q      | `--.-`| 3      | `...--`|
| E      | `.`   | R      | `.-.` | 4      | `....-`|
| F      | `..-.`| S      | `...` | 5      | `.....`|
| G      | `--.` | T      | `-`   | 6      | `-....`|
| H      | `....`| U      | `..-` | 7      | `--...`|
| I      | `..`  | V      | `...-`| 8      | `---..`|
| J      | `.---`| W      | `.--` | 9      | `----.`|
| K      | `-.-` | X      | `-..-`|        |        |
| L      | `.-..`| Y      | `-.--`|        |        |
| M      | `--`  | Z      | `--..`|        |        |

### Hints

- Use a dictionary to map each character to its Morse code representation.
- Don't forget to handle spaces between words.
- Remember to convert input to uppercase before looking up characters.
- Numbers are encoded differently from letters.

### What This Problem Quietly Teaches

```
Information can be encoded.
```

Computers constantly convert information between different representations:

- text
- binary
- audio
- images
- network signals
- compressed files

At their core, many systems are simply:

```
Input → Encode → Output
```

Long before modern computers existed, Morse code showed that human language itself could be transformed into machine-readable signals.

---

## How to Submit

When you're ready to submit, run:

```
l101 submit pset0
```

You have a maximum of **5 submission attempts**. Your best score will be kept.

Each hidden test is worth 1 point. To get full marks, pass all 14 hidden tests.

Good luck!