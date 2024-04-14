from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
from rasa_sdk.events import SlotSet

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
            courses_message = "Here are the available courses for Data structures and algorithms:\n"
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
            courses_message = "Here are the available courses for placement and tests:\n"
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
            courses_message = "Here is a list of courses to help you learn programming languages\n"
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
            courses_message = "These are all the available web development courses:\n"
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
            courses_message = "Here are the available courses for Machine Learning and Data Science:\n"
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
            courses_message = "Here is a list of courses to help you crack GATE!\n"
            for course in courses_data:
                if course['category'] == 'GATE':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveFreeCourses(Action):

    def name(self) -> Text:
        return "action_give_free_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here is a list of free courses:\n"
            for course in courses_data:
                if course['price'] == 0:
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGivePaidCourses(Action):

    def name(self) -> Text:
        return "action_give_paid_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here is a list of paid courses:\n"
            for course in courses_data:
                if course['price'] != 0:
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []



class ActionGivePacedCourses(Action):

    def name(self) -> Text:
        return "action_give_paced_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here is a list of self paced courses:\n"
            for course in courses_data:
                if course['pace'] == 'Self-paced':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionGiveLiveCourses(Action):

    def name(self) -> Text:
        return "action_give_live_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            courses_collection = db["courses"]
            courses_data = courses_collection.find()
            courses_message = "Here is a list of live courses:\n"
            for course in courses_data:
                if course['pace'] != 'Self-paced':
                    courses_message += f"{course['course_no']}: {course['course_name']}\n"
            dispatcher.utter_message(text=courses_message)
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))
        dispatcher.utter_message(text="PLEASE CHOOSE THE COURSE NUMBER")

        return []


class ActionSelectCourses(Action):

    def name(self) -> Text:
        return "action_select_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the course number entity from the latest user message
        course_no = next(tracker.get_latest_entity_values("course_no"), None)

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        # Convert course_no to integer
        try:
            course_no = int(course_no)
        except ValueError:
            dispatcher.utter_message(text="Invalid course number. Please provide a valid course number.")
            return []

        # Check if the course number is within a valid range (e.g., 1 to 40)
        if course_no <= 0 or course_no > 40:
            dispatcher.utter_message(text="Course number not available. Please choose another course.")
            return [SlotSet("course_no", None)]

        try:
            courses_collection = db["courses"]
            course = courses_collection.find_one({"course_no": course_no})
            courses_message = course['course_name']
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))

        # Set the course_no slot with the valid course number
        dispatcher.utter_message(text="You have selected the course "+str(course_no) + " - " + courses_message)
        return [SlotSet("course_no", course_no)]