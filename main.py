import json

# Description: We want to build out a service that allows callers to get specific information about a user from just a GitHub username.

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
class GithubEventCalculatorService:
    def get_events(self):
        print("Requesting https://api.github.com/users/%s/events" %self.username)
        # Here is where we will make the "API Call" to GitHub Events using get_user_events_response()
        # This function takes in a username
        pass

    def get_response(self):
        events = self.get_events()
        pass






def test_response_score(username, expected_score):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_score"]
    except KeyError:
        raise Exception("Failed: get_response('%s')'s response does not contain a key of user_score" %username)
    expected = expected_score
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("Failed: get_response('%s') returned a wrong score." %username)
    else:
        print("Passed: get_response('%s') returned correct score!\n" %username)

def test_invalid_username(username):
    service_instance = GithubEventCalculatorService()
    actual = service_instance.get_response(username)
    expected = "404"
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("Failed: get_response('%s') did not return a 404" %username)
    else:
        print("Passed: get_response('%s') returned a 404!\n" %username)

def test_user_id(username, expected_id):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_id"]
    except KeyError:
        raise Exception("Failed: get_response('%s')'s response does not contain a key of 'user_id'" %username)
    expected = expected_id
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("Failed:get_response('%s') returned a wrong user_id." %username)
    else:
        print("Passed: get_response('%s') returned correct user_id!\n" %username)

def test_username(username):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["username"]
    except KeyError:
        raise Exception("Failed: get_response('%s')'s response does not contain a key of 'username'" %username)
    expected = username
    if actual != expected:
        print("Expected: %s" %expected)
        print("Actual: %s" %actual)
        raise Exception("Failed:get_response('%s') returned a wrong username." %username)
    else:
        print("Passed: get_response('%s') returned correct username!\n" %username)

def test_event_impact(username, expected_output):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_events"]
    except KeyError:
        raise Exception("Failed: get_response('%s')'s response does not contain a key of 'user_events'" %username)
    impact_error = None
    for i, impact in enumerate(expected_output):
        try:
            equal = impact["event_type"] == actual[i]["event_type"] \
                and impact["score_impact"] == actual[i]["score_impact"]
        except KeyError as e:
            raise Exception("Failed: get_response('%s')'s response does not contain a key of '%s'" %(username, e))
        if not equal:
            impact_error = (impact, actual[i])


    if impact_error != None:
        print("Expected: %s" %impact_error[0])
        print("Actual: %s" %impact_error[1])
        raise Exception("Failed: get_response('%s') returned incorrect event impact object." %username)
    else:
        print("Passed: get_response('%s') returned correct event impact!\n" %username)

def test_event_info(username, expected_output):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_events"]
    except KeyError:
        raise Exception("Failed: get_response('%s')'s response does not contain a key of 'user_events'" %username)

    impact_error = None
    for i, impact in enumerate(expected_output):
        try:
            equal = impact["id"] == actual[i]["id"] \
                    and impact["repo_name"] == actual[i]["repo_name"] \
                    and impact["repo_link"] == actual[i]["repo_link"]
        except KeyError as e:
            raise Exception("Failed: get_response('%s')'s response does not contain a key of '%s'" %(username, e))
        if not equal:
            impact_error = (impact, actual[i])


    if impact_error != None:
        print("Expected: %s" %impact_error[0])
        print("Actual: %s" %impact_error[1])
        raise Exception("Failed: get_response('%s') returned incorrect event impact object." %username)
    else:
        print("Passed: get_response('%s') returned correct event impact!\n" %username)

def call_tests():
    print("**********************************")
    print("Testing Score in Response")
    print("**********************************\n")
    test_response_score("TrinityChristiana", 70)
    test_response_score("w3cj", 110)
    test_response_score("JhonDoe", 8)
    test_response_score("testuser", 0)

    # print("**********************************")
    # print("Testing User ID in Response")
    # print("**********************************\n")
    # test_user_id("TrinityChristiana", 31781724)
    # test_user_id("w3cj", 14241866)
    # test_user_id("JhonDoe", 6648398)
    # test_user_id("testuser", 19480)

    # print("**********************************")
    # print("Testing Username in Response")
    # print("**********************************\n")
    # test_username("TrinityChristiana")
    # test_username("w3cj")
    # test_username("JhonDoe")
    # test_username("testuser")

    # print("**********************************")
    # print("Testing invalid user Response")
    # print("**********************************\n")
    # test_invalid_username("InvalidUser")
    
    # print("**********************************")
    # print("Testing Event Impact Response")
    # print("**********************************\n")
    # test_event_impact("JhonDoe", [
    #     {'event_type': 'PullRequestReviewEvent', 'score_impact': 4}, {'event_type': 'WatchEvent', 'score_impact': 3}, {'event_type': 'CommitCommentEvent', 'score_impact': 1}
    #     ])
    # test_event_impact("testuser", [])


    # print("**********************************")
    # print("Testing Event Info Response")
    # print("**********************************\n")
    # test_event_info("JhonDoe", 
    #     [{'event_type': 'PullRequestReviewEvent', 'score_impact': 4, 'id': '21354028537', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}, {'event_type': 'WatchEvent', 'score_impact': 3, 'id': '21354005019', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}, {'event_type': 'CommitCommentEvent', 'score_impact': 1, 'id': '21353998726', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}])
    # test_event_info("testuser", [])

def get_user_events_response(username): 
    # Opening JSON file
    f = open('/home/coderpad/data/githubMockData.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()
    try:
        return data["events"][username]
    except KeyError:
        return {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"
        }

def get_user_info(username):
    # Opening JSON file
    f = open('/home/coderpad/data/githubMockData.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()
    try:
        return data["users"][username]
    except KeyError:
        return {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"
        }

call_tests()