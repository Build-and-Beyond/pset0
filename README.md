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

Some string methods you'll need (like `.lower()`, `.strip()`, `.count()`) are not taught in lecture. You'll discover them through the "Useful String Methods" tables in each problem. This is by design — syntax is best learned by doing, not by memorizing.

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

# Problem 1 — NAMASTE

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

This single word carries over 5,000 years of continuous use. Archaeologists have found gestures resembling Namaste in Harappan seals dating back to 2000 BCE. The gesture appears in temple sculptures across India, Buddhist traditions spanning from Sri Lanka to Japan, and ancient meditation practices that prewritten almost every major religion.

What makes Namaste remarkable is not just its age, but its adaptability. Through centuries of empires rising and falling — the Mauryas, the Guptas, the Mughals, the British — this one gesture persisted. It survived Sanskrit evolving into Hindi, Bengali, Tamil, and dozens of other languages. It survived the introduction of Islam, Christianity, and every other faith that reached the subcontinent.

In 2020, when the COVID-19 pandemic forced the world to reconsider the handshake — a practice that originated as a way to show you weren't carrying a weapon — Namaste became a global phenomenon. World leaders from France's Emmanuel Macron to Israel's Benjamin Netanyahu were photographed using it. The WHO indirectly promoted it as a "contactless greeting." Newspapers from The New York Times to The Guardian ran stories about this ancient Indian practice.

A gesture that survived 5,000 years of human history became, in a moment of crisis, the world's most practical piece of cultural technology.

And the very first thing most programmers learn to build? A program that greets someone. The tradition continues — just in a new medium.

Your phone says "Hello" when you unlock it. Chat applications greet you when you open them. Voice assistants introduce themselves. Even websites say "Welcome back." The greeting is, and has always been, humanity's first protocol — the first message any system sends when a connection is established.

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
- `print` can display multiple pieces of information together. An f-string like `f"Namaste, {name}"` lets you embed variables directly.

### What This Problem Quietly Teaches

```
Input → Store → Output
```

The user gives information to the program. The program stores that information in memory. Then the program uses it to generate output. This is the fundamental pattern of all computing — and, as it turns out, also the fundamental pattern of greeting someone: you hear their name, you remember it, and you respond.

---

# Problem 2 — NAMASTE+

> "Humans are flexible with language. Computers are not."

India has 22 officially recognized languages and over 19,500 dialects. A single country — smaller in area than the United States — contains more linguistic diversity than all of Europe combined.

Walk east from Gujarat and you'll hear Gujarati. Cross the border into Maharashtra and it becomes Marathi. Keep walking through Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, West Bengal, Punjab — each state, each region, each community has its own way of saying the same thing: *I acknowledge you. I see you. You are welcome here.*

| Language / Region | Greeting      |
| ----------------- | -------------- |
| Hindi / Sanskrit  | Namaste        |
| Bengali           | Nomoshkar      |
| Tamil             | Vanakkam       |
| Punjabi           | Sat Sri Akal   |
| Gujarati          | Kem Cho        |
| Kannada           | Namaskara      |
| Malayalam         | Namaskaram     |
| Odia              | Namaskar       |
| Telugu            | Namaskaram      |
| Assamese          | Namaskar       |

These aren't just different words for the same idea. Each greeting carries the weight of its culture. *Vanakkam* in Tamil isn't just "hello" — it comes from the root word *vanakkam*, meaning "respect" or "reverence." *Sat Sri Akal* in Punjabi translates to "Truth is the Eternal One" — it's a theological statement disguised as a greeting. *Nomoshkar* in Bengali carries the same Sanskrit root as Namaste, but through centuries of Bengali pronunciation, the sound itself has shifted, the way a river slowly carves a new path through stone.

Real-world software rarely receives perfectly formatted input. A user might type:

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

Every single one of these is the same word. But to a computer, they're completely different strings. `"TAMIL" == "tamil"` is `False`. This is not a bug — it's a fundamental truth about how computers process information. They are precise. They don't assume. They don't interpret. They do exactly what you tell them, nothing more.

The programs that feel "smart" — Google search, autocorrect, voice assistants — are all built on top of this reality. They work because someone, at some point, wrote code that says: "Before you do anything else, clean the input. Strip the spaces. Convert everything to the same case. Then decide what to do with it."

This is not just a programming technique. It's a way of thinking: **normalize first, then process.** It applies to data, to communication, to arguments, to relationships. Before you react to what someone said, make sure you understood what they meant.

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

You don't need all of these. Read the problem carefully, think about what could go wrong with user input, and choose the right tool.

### What This Problem Quietly Teaches

```
Programs can make decisions.
```

This problem introduces:

- conditions (`if` / `elif` / `else`)
- input normalization (cleaning data before processing)
- string formatting
- branching logic

The deeper lesson: **information never arrives perfectly.** It arrives messy, inconsistent, and partial. The question is not whether you'll encounter this — you always will — but whether your code can handle it gracefully.

---

# Problem 3 — PARITY

> "In 1962, a missing hyphen destroyed a $18.5 million spacecraft."

On July 22, 1962, NASA launched Mariner 1 — America's first attempt to send a spacecraft toward Venus. The Atlas-Agena rocket lifted off from Cape Canaveral at 9:21 AM. Everything looked normal.

Then, 293 seconds into the flight, the rocket began to veer off course. The guidance system, which was supposed to keep the vehicle on a smooth trajectory toward space, had received an incorrect command. The rocket's steering went haywire. Range Safety Officer Robert E. Grey watched the data, made a decision no one wants to make, and pressed the destruct button.

The rocket exploded over the Atlantic Ocean. $18.5 million (equivalent to roughly $180 million today) vanished in a ball of fire.

The investigation revealed an almost unbearably simple cause: **a single missing hyphen in the guidance code**. One character. A bar (`-`) that should have been overbar (`‾`). The programmer who transcribed the mathematical equations from paper to punch cards missed this one symbol. The computer, doing exactly what it was told — nothing more, nothing less — interpreted the equation correctly, but for the wrong formula.

Mariner 1 was not the first system destroyed by a small data error, and it would not be the last. In 1996, the European Space Agency's Ariane 5 rocket self-destructed 37 seconds after launch because of an integer overflow — trying to store a 64-bit number in a 16-bit space. The rocket was worth $500 million. In 1999, NASA's Mars Climate Orbiter was lost because one team used metric units and another used imperial. The spacecraft approached Mars at the wrong altitude and disintegrated in the atmosphere. Cost: $327 million.

These are not programming errors in the way most people think of them. They are not bugs in algorithms. They are **data integrity errors** — the wrong data, the wrong format, the wrong unit, the wrong symbol. And they are devastating precisely because computers are so precise: they process exactly what they receive, with no common sense to catch obvious mistakes.

How do you protect against this?

The answer has been known since 1947, when a mathematician named Richard Hamming was working on the same problem at Bell Labs. Hamming was using a relay computer — a room-sized machine that processed data by physically opening and closing electrical switches. The computer ran on weekends, and if an error occurred, the entire calculation would stop. Hamming's programs would have to wait until Monday to be re-run, wasting days.

Frustrated, Hamming asked a question that would change computing forever: **Can we detect errors automatically, without human intervention?**

He discovered that by adding just a few extra bits — called **parity bits** — to any piece of data, you could detect whether an error had occurred during transmission or storage. A single bit of redundant information, calculated from the data itself, could tell you whether something had gone wrong.

Parity works like this: you count the number of 1s in a binary string. If the count is even, the parity is even. If the count is odd, the parity is odd. By storing one extra bit — the parity bit — you create a simple checksum. If a single bit flips during transmission, the parity changes, and the receiver knows something went wrong.

This idea — that a small amount of redundant information can catch errors — is now used everywhere:

- Every byte of RAM in your computer can have a parity bit that detects memory corruption
- Spacecraft like Voyager 1 and Voyager 2 use parity and more advanced error-correcting codes to communicate across billions of kilometers of space
- QR codes use parity-based error correction, which is why they still work even when partially covered
- Every WiFi packet, every Bluetooth transmission, every USB data transfer uses parity or its descendants
- The very concept of "checksums" on downloaded files is a direct descendant of Hamming's idea

The Mariner 1 disaster cost $18.5 million and delayed America's Venus exploration by years. Richard Hamming's parity system costs almost nothing — a single bit — and catches errors that would otherwise go undetected.

In this problem, you'll implement the simplest form of error detection: counting 1s in a binary string and determining whether it has even or odd parity.

---

### Specification

In a file called `parity.py`, implement a program that:

1. Prompts the user for a binary string (containing only 0s and 1s)
2. Counts the number of 1s in the string
3. Prints the count of 1s
4. Reports whether the string has **even** or **odd** parity

For example:

```
Enter a binary string: 10101
1s: 3
Error detected — odd parity
```

```
Enter a binary string: 10100
1s: 2
Valid — even parity
```

```
Enter a binary string: 00000
1s: 0
Valid — even parity
```

### Hints

- You can count the occurrences of a character in a string using `.count()`. For example: `"10101".count("1")` returns `3`.
- To check if a number is even or odd, use the modulo operator `%`. For example: `3 % 2 == 1` (odd), `2 % 2 == 0` (even).
- Think about edge cases: what if the string has zero 1s? What if it's all 1s?

### What This Problem Quietly Teaches

```
Information can be checked.
```

In 1962, a missing hyphen destroyed a spacecraft worth $18.5 million. In 1999, a unit mismatch destroyed the Mars Climate Orbiter. In 1947, Richard Hamming proved that a single extra bit — a parity bit — can detect that something went wrong.

Every byte of RAM in your computer uses this idea. Every spacecraft transmission uses this idea. Every QR code uses this idea.

At their core, many systems are simply:

```
Input → Count → Decide
```

The lesson is not just about binary. It's about a deeper truth: **small checks prevent large failures.** A parity bit costs almost nothing. Not having one can cost everything.

---

## How to Submit

When you're ready to submit, run:

```
l101 submit pset0
```

You have a maximum of **5 submission attempts**. Your best score will be kept.

Each hidden test is worth 1 point. To get full marks, pass all 10 hidden tests.

Good luck!