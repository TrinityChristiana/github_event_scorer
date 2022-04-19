# Github Event Score
API Endpoint: https://api.github.com/users/:username/events

[Documentation](https://docs.github.com/en/rest/reference/activity#list-events-for-the-authenticated-user)

## Acceptence Criteria:
1. There is an input on the page for a user to type their github username
1. When the user has typed their username in the input and clicks a button for the form, their username is used to get thir girhub events
1. A score for their events have been calculated given the following criteria:
   - The score is calculated from the "type" property, where
     - PushEvent = 5 points
     - PullRequestReviewEvent = 4 points
     - WatchEvent = 3 points.
     - CreateEvent = 2 points.
     - Every other event = 1 point.
1. The calculated score are printed on the DOM using a preexisting Components
1. Above the user's score, text that reads "{username}'s Score" shows up on the DOM