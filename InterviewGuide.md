# Interview Guide

Possible Solution: <https://github.com/TrinityChristiana/github_event_scorer>

## Description

This Coding challenge will test the following abilities:

1. Ability to take in external data and manipulate it for an expected outcome.
1. Ability to turn requirements into code.
1. Ability to build on top of previous work.

## Candidate Help

### Keying of Event Kinds

Part of the interview that is interesting is how they handle the keying of event kinds. If they do something like:

```python
if event.type === 'PushEvent':
  score = 5
elif event.type === 'WatchEvent':
  score = 3
```

Try to push them towards a look-up table by asking how they could reduce the cyclomatic complexity of their answer. Here's an example of a lookup table:

```python
scoreLookup = {
  'PushEvent': 5,
  'PullRequestReviewCommentEvent': 4,
  'WatchEvent': 3,
  'CreateEvent': 2,
}
```

You can drill into what happens if you access an undefined property of a dictionary in python (you get undefined).

## Objectives

These are the "Tickets that the PM and Scrum Master are working on". So add these to the IDE instructions as they complete the tasks.

There are commented out tests for these objectives. They are labeled with the corresponding number, so make sore to comment those back in before you work on that.

The objectives are commented out in python syntax for you to be able to quickly copy and paste this into the interviewees' coding IDE.

```python
# Objective 1: Calculate User's Event Score

## The callers of this service want to be able to pass in a username and for the response to contain passed in the user's event score using information from GitHub's Event API.


## We will not be calling the API directly, we will be using the function `get_user_events_response`. This takes in a username and returns a list of events for that user.

## The score is calculated from the “type” property of each event, where:

  ##  PushEvent = 5 points
  ##  PullRequestReviewEvent = 4 points
  ##  WatchEvent = 3 points.
  ##  CreateEvent = 2 points.
  ##  Every other event = 1 point.

## Dictionary defining the desired output:

  ##  {
  ##    "user_score": None,
  ##  }
```

```python
# Objective 2: Username Validation

## We want the caller of this service to be notified if a username they passed in does not exist.

## So, when a username does not exist, we want the response to be the string "404".
```

```python
# Objective 3: User Information

## The callers of the service have decided to make a front-end of this application for their end-users. 

## They want to show the user some information about the username they are getting the score to. They want the passed-in username,and the user_id to be added to the current response.

## Dictionary defining the desired output:

    ##  {
    ##    "username": None,
    ##    "user_id": None,
    ##    user_score": None,
    ##  }
```

```python
# Objective 4: Event Impact on Score

## The callers of this service want to show their users how each event impacts their score.

## Within the current response, we need to add a list of each event with the event type and how many points it contributed to the score.

## Dictionary defining the desired output:

    ##  {
    ##    "username": None,
    ##    "user_id": None,
    ##    "user_score": None,
    ##    "user_events": [
    ##      {
    ##        "event_type": None,
    ##        "score_impact": None,
    ##      },
    ##      {...}
    ##      ],
    ##  }
```

```python
# Objective 5: Event Information

## The front-end users are enjoying their application and are asking for more information about their events.

## So the service callers are asking for more information to be added to the response. Within the list of events information, we want the following to be in the response

    ## 1. The Event's ID
    ## 2. Event Repo name
    ## 3. Event Repo Link (ex: https://github.com/username/repo_name)

## Dictionary defining the desired output:

    # {
    #   "username": None,
    #   "user_id": None,
    #   "user_score": None,
    #   "user_events": [
    #     {
    #       "event_type": None,
    #       "score_impact": None,
    #       "id": None,
    #       "repo_name": None,
    #       "repo_link": None
    #     },
    #     {...}
    #   ],
    # }
```

### Bonus Questions

1. Ask them: What if every event with the event type with the word "Comment" in it counts for -2 points.
1. You can ask them how they would go about being able to calculate the score of multiple users and order them by score.
