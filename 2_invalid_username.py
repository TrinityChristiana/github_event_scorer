#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import json

# Objective 2: Username Validation

# We want the caller of this service to be notified if a username they passed in does not exist.

# So, when a username does not exist, we want the response to be the string "404".


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
        print("Requesting https://api.github.com/users/%s/events" % self.username)
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
        if "message" in user_events and user_events["message"] == "Not Found":
            return "404"
        user_score = self.calculate_score(user_events)
        return {
            "user_score": user_score
        }


def test_response_score(username, expected_score):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_score"]
    except KeyError:
        raise Exception(
            "Failed: get_response('%s')'s response does not contain a key of user_score" % username)
    expected = expected_score
    if actual != expected:
        print("Expected: %s" % expected)
        print("Actual: %s" % actual)
        raise Exception(
            "Failed: get_response('%s') returned a wrong score." % username)
    else:
        print("Passed: get_response('%s') returned correct score!\n" % username)


def test_invalid_username(username):
    service_instance = GithubEventCalculatorService()
    actual = service_instance.get_response(username)
    expected = "404"
    if actual != expected:
        print("Expected: %s" % expected)
        print("Actual: %s" % actual)
        raise Exception(
            "Failed: get_response('%s') did not return a 404" % username)
    else:
        print("Passed: get_response('%s') returned a 404!\n" % username)


def test_user_id(username, expected_id):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_id"]
    except KeyError:
        raise Exception(
            "Failed: get_response('%s')'s response does not contain a key of 'user_id'" % username)
    expected = expected_id
    if actual != expected:
        print("Expected: %s" % expected)
        print("Actual: %s" % actual)
        raise Exception(
            "Failed:get_response('%s') returned a wrong user_id." % username)
    else:
        print("Passed: get_response('%s') returned correct user_id!\n" % username)


def test_username(username):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["username"]
    except KeyError:
        raise Exception(
            "Failed: get_response('%s')'s response does not contain a key of 'username'" % username)
    expected = username
    if actual != expected:
        print("Expected: %s" % expected)
        print("Actual: %s" % actual)
        raise Exception(
            "Failed:get_response('%s') returned a wrong username." % username)
    else:
        print("Passed: get_response('%s') returned correct username!\n" % username)


def test_event_impact(username, expected_output):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_events"]
    except KeyError:
        raise Exception(
            "Failed: get_response('%s')'s response does not contain a key of 'user_events'" % username)
    impact_error = None
    for i, impact in enumerate(expected_output):
        try:
            equal = impact["event_type"] == actual[i]["event_type"] \
                and impact["score_impact"] == actual[i]["score_impact"]
        except KeyError as e:
            raise Exception(
                "Failed: get_response('%s')'s response does not contain a key of '%s'" % (username, e))
        if not equal:
            impact_error = (impact, actual[i])

    if impact_error != None:
        print("Expected: %s" % impact_error[0])
        print("Actual: %s" % impact_error[1])
        raise Exception(
            "Failed: get_response('%s') returned incorrect event impact object." % username)
    else:
        print("Passed: get_response('%s') returned correct event impact!\n" % username)


def test_event_info(username, expected_output):
    service_instance = GithubEventCalculatorService()
    try:
        actual = service_instance.get_response(username)["user_events"]
    except KeyError:
        raise Exception(
            "Failed: get_response('%s')'s response does not contain a key of 'user_events'" % username)

    impact_error = None
    for i, impact in enumerate(expected_output):
        try:
            equal = impact["id"] == actual[i]["id"] \
                and impact["repo_name"] == actual[i]["repo_name"] \
                and impact["repo_link"] == actual[i]["repo_link"]
        except KeyError as e:
            raise Exception(
                "Failed: get_response('%s')'s response does not contain a key of '%s'" % (username, e))
        if not equal:
            impact_error = (impact, actual[i])

    if impact_error != None:
        print("Expected: %s" % impact_error[0])
        print("Actual: %s" % impact_error[1])
        raise Exception(
            "Failed: get_response('%s') returned incorrect event impact object." % username)
    else:
        print("Passed: get_response('%s') returned correct event impact!\n" % username)


def call_tests():
    print("**********************************")
    print("Obj 1: Testing Score in Response")
    print("**********************************\n")
    test_response_score("TrinityChristiana", 70)
    test_response_score("w3cj", 110)
    test_response_score("JhonDoe", 8)
    test_response_score("testuser", 0)

    print("**********************************")
    print("Obj 2: Testing invalid user Response")
    print("**********************************\n")
    test_invalid_username("InvalidUser")

    # print("**********************************")
    # print("Obj 3: Testing User ID in Response")
    # print("**********************************\n")
    # test_user_id("TrinityChristiana", 31781724)
    # test_user_id("w3cj", 14241866)
    # test_user_id("JhonDoe", 6648398)
    # test_user_id("testuser", 19480)

    # print("**********************************")
    # print("Obj 3: Testing Username in Response")
    # print("**********************************\n")
    # test_username("TrinityChristiana")
    # test_username("w3cj")
    # test_username("JhonDoe")
    # test_username("testuser")

    # print("**********************************")
    # print("Obj 4: Testing Event Impact Response")
    # print("**********************************\n")
    # test_event_impact("JhonDoe", [
    #     {'event_type': 'PullRequestReviewEvent', 'score_impact': 4}, {'event_type': 'WatchEvent', 'score_impact': 3}, {'event_type': 'CommitCommentEvent', 'score_impact': 1}
    #     ])
    # test_event_impact("testuser", [])

    # print("**********************************")
    # print("Obj 5: Testing Event Info Response")
    # print("**********************************\n")
    # test_event_info("JhonDoe",
    #     [{'event_type': 'PullRequestReviewEvent', 'score_impact': 4, 'id': '21354028537', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}, {'event_type': 'WatchEvent', 'score_impact': 3, 'id': '21354005019', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}, {'event_type': 'CommitCommentEvent', 'score_impact': 1, 'id': '21353998726', 'repo_name': 'codetracker-learning/LAB-pet-adoption', 'repo_link': 'https://github.com/codetracker-learning/LAB-pet-adoption'}])
    # test_event_info("testuser", [])


def get_user_events_response(username):
    """
    Returns a list of events for the passed in username.

        Parameters:
            username (str): A string

        Returns:
            event_data (list): A list of events for the username
    """
    # Opening JSON file
    # f = open('/home/coderpad/data/githubMockData.json') # for Coderpad
    f = open('./githubMockData.json')

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
    """
    Returns a dictionary with user information for the passed in username.

        Parameters:
            username (str): A string

        Returns:
            user_info (dict): A dictionary containing user information
    """
    # Opening JSON file
    # f = open('/home/coderpad/data/githubMockData.json') # for Coderpad
    f = open('./githubMockData.json')

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
