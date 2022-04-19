import json

# Description: We want to build out a service that allows callers to get specific information about a user from just a GitHub username.

# Objective 2: We want the response to return the string "404" when the passed in username does not exist

class GithubEventCalculatorService:
    def __init__(self):
        self.score_map = {
            "PushEvent": 5,
            "PullRequestReviewEvent": 4,
            "WatchEvent": 3,
            "CreateEvent": 2,
            "Other": 1
        }

    def get_events(self):
        print("Requesting https://api.github.com/users/%s/events" %self.username)
        response = get_user_events_response(self.username)
        return response

    def calculate_score(self, events):
        user_score = 0
        for event in events:
            try:
                user_score += self.score_map[event["type"]]
            except KeyError:
                user_score += self.score_map["Other"]

        return user_score
        
    def get_response(self, username):
        self.username = username
        user_events = self.get_events()
        if "error" in user_events:
            return "404"
        user_score = self.calculate_score(user_events)
        return {
            "user_score": user_score
        }

def test_response_score(username, expected_score):
    service_instance = GithubEventCalculatorService()
    actual = service_instance.get_response(username)
    expected = {
        "user_score": expected_score,
    }
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("get_response('%s') returned a wrong score." %username)
    else:
        print("get_response('%s') returned correct the score!\n" %username)

def test_invalid_username(username):
    service_instance = GithubEventCalculatorService()
    actual = service_instance.get_response(username)
    expected = "404"
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("get_response('%s') returned wrong result." %username)
    else:
        print("get_response('%s') returned correct result!\n" %username)

def call_tests():
    test_response_score("TrinityChristiana", 70)
    test_response_score("w3cj", 110)
    test_response_score("JhonDoe", 8)
    test_response_score("testuser", 0)
    test_invalid_username("InvalidUser")

def get_user_events_response(username): 
    # Opening JSON file
    f = open('/home/coderpad/data/githubEvents.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()
    try:
        return data[username]
    except KeyError:
        return {"error": "404: User not found"}
    
call_tests()

# Objective 1: Event score
# We want the response to contain an event score for the passed in user.
# The score is calculated from the “type” property, where:
# - PushEvent = 5 points
# - PullRequestReviewEvent = 4 points
# - WatchEvent = 3 points.
# - CreateEvent = 2 points.
# - Every other event = 1 point.
    # Dict defining the desired output:

    # return {
    #     "user_score": None,
    # }

# Objective 2: We want the response to return the string "404" when the passed in username does not exist

# Objective 3: User Information
# Along with the score we want the response to contain some user information.
# Without makibng any additional calls to the API, we want the response to contain both the Username and the User Id for the passed in user
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

