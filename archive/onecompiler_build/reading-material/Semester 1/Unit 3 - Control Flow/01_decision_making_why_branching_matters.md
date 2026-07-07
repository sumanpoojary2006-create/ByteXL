## Introduction

Asha taps her PIN into her phone's lock screen without even thinking about it. In a heartbeat the phone decides between two completely different outcomes: either her home screen springs open full of apps, or the screen shakes and flashes "Wrong PIN, try again." Every program she has met so far in this course has only run straight ahead, performing each instruction in order and reaching the end having done every line exactly once. That works fine for a calculator that always adds two numbers, but her phone clearly does more than that.

Should the phone unlock? Only if the PIN is correct. Should an app show "Welcome back"? Only if she is already logged in. Each of these is a fork in the road, a point where the program looks at a situation and chooses what to do next. Without that fork, the phone would have to do the same thing every single time it is touched, which is clearly not how any real device behaves. Teaching a program to make those choices is what this unit, control flow, is all about.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8h2g6c/01_branching_two_paths.png)

## Programs That Only Go Straight

Picture the kind of program you can already write:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2RlY2lzaW9uX21ha2luZ193aHlfYnJhbmNoaW5nX21hdHRlcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InByaWNlID0gaW50KGlucHV0KFwiUHJpY2U6IFwiKSlcbnF0eSA9IGludChpbnB1dChcIlF1YW50aXR5OiBcIikpXG5wcmludChcIlRvdGFsOlwiLCBwcmljZSAqIHF0eSkifQ"
 width="100%"
></iframe>

It reads, it calculates, it prints, and every line runs no matter what. There is no choice here. Whether the total is 10 rupees or 10 lakh, the program behaves identically. Useful, but limited. A program that cannot decide cannot react, and a phone that cannot decide could never tell Asha's correct PIN apart from a stranger's guess; it would have to treat both exactly the same way, which is obviously not acceptable.

## Life Is Full of Forks

Now think about how often a small decision changes what should happen:

- A login either greets you or rejects you.
- A shopping cart either applies a discount or charges full price.
- A traffic signal either says go or says stop.
- A game either adds to your score or ends your turn.

In every case there is a **condition**, a yes or no question, and the answer decides the path. "Is the PIN correct?" "Is the cart total above 500?" "Is the light green?" The program checks the condition, then branches one way or the other.

## Forks at a Glance

| Scenario | Condition | If True | If False |
|---|---|---|---|
| Login screen | Is the PIN correct? | Show home screen | Show error |
| Shopping cart | Is the total above 500? | Apply discount | Charge full price |
| Traffic signal | Is the light green? | Go | Stop |
| Game | Did you score? | Add to score | End turn |

## A Condition Is Just a Yes or No Question

You already know how to ask these questions. In the last unit you built booleans using comparison and logical operators, and a condition is exactly that: an expression that comes out as `True` or `False`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2RlY2lzaW9uX21ha2luZ193aHlfYnJhbmNoaW5nX21hdHRlcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImFnZSA9IDIwXG5wcmludChhZ2UgPj0gMTgpICAgICMgVHJ1ZSJ9"
 width="100%"
></iframe>

That single `True` is the seed of a decision. In the rest of this unit you will attach actions to these answers: do this when the condition is true, do that when it is false, and handle the many-option cases in between. By the end you will be able to express, in code, almost any rule you can state in a sentence.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8h2g6c/01_condition_question_gate.png)


## Conclusion

So far your programs have run top to bottom with no choices, but real problems constantly branch based on a situation. The key idea of control flow is simple: a program asks a condition, a yes or no question that evaluates to a boolean, and then chooses what to do based on the answer. Everything that follows, the `if`, the `else`, the `elif`, and more, is just different ways of acting on those answers. Learn to spot the forks in a problem, and you are already thinking in control flow. The very next lesson starts with the simplest fork of all, a single condition that decides whether one extra action happens at all.
