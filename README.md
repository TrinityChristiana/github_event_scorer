# Github Event Score

## Description

You are driving a pairing session with a couple of people on your team (your interviewers). During this session, we want to build out a service that allows callers to get some information about a Github user and their GitHub activity.

This work is separated into 5 objectives. You have the first one fully available to you, while the Product Manager and Scrum Master are still working on writing up the tickets for the other 4. They should be done by the time you've completed your first objective.

## Objective 1: Calculate User's Event Score

The callers of this service want to be able to pass in a username and for the response to contain passed in the user's event score using information from GitHub's Event API.

### Notes

- We will not be calling the API directly, we will be using the function `get_user_events_response`. This takes in a username and returns a list of events for that user.
- The score is calculated from the “type” property of each event, where:
  - PushEvent = 5 points
  - PullRequestReviewEvent = 4 points
  - WatchEvent = 3 points.
  - CreateEvent = 2 points.
  - Every other event = 1 point.
  - Here is what the desired output looks like:

    ```python
    {
        "user_score": None,
    }
    ```

## Objective 2: Username Validation

- Coming Soon

## Objective 3: User Information

- Coming Soon

## Objective 4: Event Impact on Score

- Coming Soon

## Objective 5: Event Information

- Coming Soon
