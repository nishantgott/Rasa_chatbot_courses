from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient

def connect_to_mongodb(mongo_url):
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        # Accessing a database
        dbb = client.get_database()
        print("Connected to MongoDB successfully!")
        return dbb
    except Exception as e:
        print("Error connecting to MongoDB:", str(e))
        return None

mongo_url = "mongodb+srv://nishantgk2004:heBmoS6edFGkPTBr@cluster0.jr4xu3z.mongodb.net/ecommerce"
db = connect_to_mongodb(mongo_url)


class ActionGiveCourses(Action):

    def name(self) -> Text:
        return "action_give_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Access the "courses" collection in the "ecommerce" database
            courses_collection = db["courses"]
            # Retrieve data from the collection
            courses_data = courses_collection.find()
            # Print the retrieved data
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveCategories(Action):

    def name(self) -> Text:
        return "action_give_categories"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="DS and Algorithms \nPlacement and Test Series \nProgramming Languages \nWeb Development \nMachine Learning and Data Science \nSchool \nGATE")

        return []


class ActionGiveDsaCourses(Action):

    def name(self) -> Text:
        return "action_give_dsa_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'DS and Algorithms':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGivePtsCourses(Action):

    def name(self) -> Text:
        return "action_give_pts_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'Placement and Test Series':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGivePlCourses(Action):

    def name(self) -> Text:
        return "action_give_pl_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'Programming Languages':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveWdCourses(Action):

    def name(self) -> Text:
        return "action_give_wd_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'Web Development':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveMlCourses(Action):

    def name(self) -> Text:
        return "action_give_ml_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'Machine Learning and Data Science':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveSchoolCourses(Action):

    def name(self) -> Text:
        return "action_give_school_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'School':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveGateCourses(Action):

    def name(self) -> Text:
        return "action_give_gate_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here are the available courses:\n"
            for course in courses_data:
                if course['category'] == 'GATE':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []
