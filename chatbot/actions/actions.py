from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
from rasa_sdk.events import SlotSet
import csv

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


def get_data(course_no, col, dispatcher):
    try:
        course_no = int(course_no)
    except ValueError:
        dispatcher.utter_message(text="Invalid course number. Please provide a valid course number.")
        return []

    try:
        courses_collection = db["courses"]
        course = courses_collection.find_one({"course_no": course_no})
        courses_message = course[col]
    except Exception as e:
        print("Error retrieving data from MongoDB:", str(e))

    return courses_message

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


class ActionAskPace(Action):

    def name(self) -> Text:
        return "action_ask_pace"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        # Convert course_no to integer
        try:
            course_no = int(course_no)
        except ValueError:
            dispatcher.utter_message(text="Invalid course number. Please provide a valid course number.")
            return []

        try:
            courses_collection = db["courses"]
            course = courses_collection.find_one({"course_no": course_no})
            courses_message = course['pace']
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))

        # Set the course_no slot with the valid course number
        if courses_message == "Self-paced":
            dispatcher.utter_message(text = "It is a self paced course. You can join the course anytime. All of the content will be available once you get enrolled. You can finish it at your own decided speed.")
        else:
            dispatcher.utter_message(text = "It is a live course. The schedule can be viewed in the course page")

        return [SlotSet("course_no", course_no)]


class ActionAskPrice(Action):

    def name(self) -> Text:
        return "action_ask_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        try:
            course_no = int(course_no)
        except ValueError:
            dispatcher.utter_message(text="Invalid course number. Please provide a valid course number.")
            return []

        try:
            courses_collection = db["courses"]
            course = courses_collection.find_one({"course_no": course_no})
            courses_message = course['price']
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))

        if courses_message == 0:
            dispatcher.utter_message(text = "It is a free course")
        else:
            dispatcher.utter_message(text = "The price of this course is "+ str(courses_message))

        return [SlotSet("course_no", course_no)]


class ActionAskDuration(Action):

    def name(self) -> Text:
        return "action_ask_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        try:
            course_no = int(course_no)
        except ValueError:
            dispatcher.utter_message(text="Invalid course number. Please provide a valid course number.")
            return []

        try:
            courses_collection = db["courses"]
            course = courses_collection.find_one({"course_no": course_no})
            courses_message = course['duration']
        except Exception as e:
            print("Error retrieving data from MongoDB:", str(e))

        dispatcher.utter_message(text = courses_message)

        return []


class ActionAskMentor(Action):

    def name(self) -> Text:
        return "action_ask_mentor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'mentor', dispatcher)

        dispatcher.utter_message(text = courses_message)

        return []


class ActionAskOverview(Action):

    def name(self) -> Text:
        return "action_ask_overview"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'overview', dispatcher)

        dispatcher.utter_message(text = "This course is updated to stay relevant and stands out from other courses in the market.\n")
        dispatcher.utter_message(text = courses_message)

        return []


class ActionAskDoubtSupport(Action):

    def name(self) -> Text:
        return "action_ask_doubt_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'doubt_support', dispatcher)

        dispatcher.utter_message(text = courses_message)

        return []


class ActionAskRating(Action):

    def name(self) -> Text:
        return "action_ask_rating"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'rating', dispatcher)

        dispatcher.utter_message(text = "The rating of this course is " + str(courses_message))

        return []


class ActionAskTestimonials(Action):

    def name(self) -> Text:
        return "action_ask_testimonials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'testimonials', dispatcher)

        dispatcher.utter_message(text = "Here are a few testimonials from people who have taken this course")
        dispatcher.utter_message(text = courses_message)

        return []


class ActionKind(Action):

    def name(self) -> Text:
        return "action_ask_kind"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message1 = get_data(course_no, 'pace', dispatcher)
        courses_message2 = get_data(course_no, 'category', dispatcher)

        dispatcher.utter_message(text = "This is a " + courses_message1 + " course for "+courses_message2)

        return []


class ActionDescription(Action):

    def name(self) -> Text:
        return "action_ask_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'description', dispatcher)

        dispatcher.utter_message(text = courses_message)

        return []


class ActionDifficulty(Action):

    def name(self) -> Text:
        return "action_ask_difficulty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'difficulty', dispatcher)

        dispatcher.utter_message(text = "The difficulty rating of this course is " + courses_message)

        return []


class ActionAskAid(Action):

    def name(self) -> Text:
        return "action_ask_aid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'price', dispatcher)

        if courses_message == 0:
            dispatcher.utter_message(text="This is a free course.")
        else:
            courses_price = float(courses_message)  # Convert price to float
            refund = courses_price * 0.9  # Calculate refund amount
            dispatcher.utter_message(text=f"This course has a 90 day challenge, where 90% refund is given if you complete the course in 90 days!\n"
                                           f"You pay {courses_price} now and get back {refund:.2f} after successfully finishing the challenge.")
        return []


class ActionAskPre(Action):

    def name(self) -> Text:
        return "action_ask_pre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'prereq', dispatcher)
        dsa = get_data(course_no, 'dsa_prerequisite', dispatcher)
        if dsa=="yes":
            courses_message += ". But having a basic understanding of Data Structures and Algorithms will make it easier"

        dispatcher.utter_message(text = courses_message)

        return []


class ActionAskLink(Action):

    def name(self) -> Text:
        return "action_ask_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_no = tracker.get_slot("course_no")

        if course_no is None:
            dispatcher.utter_message(text="Course number not provided. Please provide a course number.")
            return []

        courses_message = get_data(course_no, 'link', dispatcher)

        dispatcher.utter_message(text = "Course link: "+courses_message)

        return []



class ActionExportChatData(Action):
    def name(self) -> Text:
        return "action_export_chat_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract user data and chat transcripts
        user_id = tracker.sender_id
        user_name = tracker.get_slot("user_name")
        chat_transcripts = []
        for event in tracker.events:
            if event.get("event") == "user":
                chat_transcripts.append(event.get("text"))
        file_path = "chat_data.csv"
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["User ID", "User Name", "Chat Transcript"])
            writer.writerow([user_id, user_name, "\n".join(chat_transcripts)])
        dispatcher.utter_message(text="Chat data has been exported.")
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry, I didn't understand that. Can you please rephrase?")
        return []



