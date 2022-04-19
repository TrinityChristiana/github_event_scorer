Possible Solution: https://codesandbox.io/s/unruffled-grass-vrksno?file=/src/index.js
# Interview Guide

## Description

This Coding challange will test the following

1. Ability to call an API
1. Ability to take in data and manipulate it for the frontend application
1. Present the manipulated data with react
   1. Using State
   1. Using Props
   1. Using Lifecycle Hooks
1. Ability to pass data between sibling components
1. Ability to use and update pre-existing components
1. Ability to turn requirements into code well.

## Pad Setup

To show this coding challange in three files follow these steps:
  - Create a pad using this question
  - Change language to anu other language (like Javascript)
  - Change the langiage back to HTML/JS/CSS
  - Then remove everything frm the new index.js file
  - Remove everything form the index.css file
  - Copy the code within the script tag in the index.html and paste it into the index.js file
  - Run the code to make sure there are no errors and that the DOM reads "Happy Coding!"

## Canidate Help

### Code to fetch the events if they need that

```javascript
fetch('https://api.github.com/users/sophiebits/events')
  .then(res => res.json())
  .catch(err => console.error('Encountered a problem fetching events', err))
```

If they forget to add error handling to the call, ask them how they could improve their data fetching logic to see if they realize they should

### Keying of Event Kinds

Part of the interview that is interesting is how they handle the keying of event kinds. If they do something like:

```javascript
if (event.type === 'PushEvent') {
  score = 5
} else if (event.type === 'WatchEvent') {
  score = 3
}
```

Try to push them towards a look up table by asking how they could reduce the cyclomatic complexity of their answer. Here's an example of a lookup table:

```javascript
let scoreLookup = {
  'PushEvent': 5,
  'PullRequestReviewCommentEvent': 4,
  'WatchEvent': 3,
  'CreateEvent': 2,
}
```

You can drill into what happens if you access an undefined property of an object in js (you get undefined). 

### Bonus Questions

```js
6. Using an existing component, render a list of the user's events and how each event impacted the user's score. Example:
   - PushEvent +5
   - CreateEvent +2
7. In the list of the user's events, render the event's id, type, repo name, and add a link to the repo
```

### If they finish

1. Ask them: What if every event with the event type with the word "Comment" in it counts for -2 points.
1. You can ask them how they would go about being able to calculate the score of multiple users and order them by score.