# Interview Guide

Possible Solution: <https://replit.com/@trinitychristia/GitHub-Event-Scorer?v=1#README.md>

## Description

This Coding challange will test the following

1. Ability to take in external data and manipulate it for an expected outcome
1. Ability to turn requirements into code well.

## Canidate Help

### Keying of Event Kinds

Part of the interview that is interesting is how they handle the keying of event kinds. If they do something like:

```python
if event.type === 'PushEvent':
  score = 5
elif event.type === 'WatchEvent':
  score = 3
```

Try to push them towards a look up table by asking how they could reduce the cyclomatic complexity of their answer. Here's an example of a lookup table:

```python
scoreLookup = {
  'PushEvent': 5,
  'PullRequestReviewCommentEvent': 4,
  'WatchEvent': 3,
  'CreateEvent': 2,
}
```

You can drill into what happens if you access an undefined property of a dictionaty in python (you get undefined).

### Bonus Questions

```python
# Objective 2: We want the response to return the string "404" when the passed in username does not exist

# Objective 3: User Information
# Along with the score we want the response to contain some user information.
# Without making any additional calls to the API, we want the response to contain both the Username and the User Id for the passed in user
    # Dict defining the desired output:

    # return {
    #     "username": None,
    #     "user_id": None,
    #     "user_score": None,
    # }

# Objective 4: Event Impact on score
# The callers of this service want to show the end user's how their events impacted their score. So, the response should contain a list of each of the user events types, along with how many points it contributed to the score. They do not want the events to be joined together by type.
    # Dict defining the desired output:

    # return {
    #     "username": None,
    #     "user_id": None,
    #     "user_score": None,
    #     "user_events": [
    #         {
    #             "event_type": None,
    #             "score_impact": None,
    #         },
    #         {...}
    #     ],
    # }

# Objective 5: Event Information
# Now the callers want some more information about the events. Within the list of events and the impact each event had on the score, we want the folloinw information to be in the response
    # 1. The Event's ID
    # 2. Event Repo name
    # 3. Event Repo Link
        # Dict defining the desired output:

        # return {
        #     "username": None,
        #     "user_id": None,
        #     "user_score": None,
        #     "user_events": [
        #         {
        #             "event_type": None,
        #             "score_impact": None,
        #             "id": None,
        #             "repo_name": None,
        #             "repo_link": None
        #         },
        #         {...}
        #     ],
        # }
```

### If they finish

1. Ask them: What if every event with the event type with the word "Comment" in it counts for -2 points.
1. You can ask them how they would go about being able to calculate the score of multiple users and order them by score.
