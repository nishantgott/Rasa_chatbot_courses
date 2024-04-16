# GalaBot - Chatbot for selling courses

This is a chatbot designed to help students purchase courses on geeksforgeeks. They can choose a course and ask any questions they have in mind regarding the course  


## Try the deployed chatbot now!

Head over to [https://polite-gelato-17df59.netlify.app/](https://polite-gelato-17df59.netlify.app/) to try the chatbot


## Install dependencies

Run:
```bash
pip install -r requirements.txt
```


## Run the bot

Use `rasa train` to train a model. (Use "cd chatbot" first if not in chatbot directory")

Then, to run, first set up your action server in one terminal window: (Use "cd chatbot" first if not in chatbot directory")
```bash
rasa run actions

```

In another window, to talk to the bot, run: (Use "cd chatbot" first if not in chatbot directory")
```
rasa shell

```


## Overview of the files

`data/nlu/nlu.yml` - contains NLU training data

`data/nlu/rules.yml` - contains rules training data

`data/stories/stories*.yml` - contains stories training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble



## Things you can ask the bot

1. Show all the available courses
2. Show different categories of courses
3. Show the available courses by category like - 
     - DSA
     - Machine Learning
     - Data Science
     - Web Development
     - School
     - GATE
     - Programming
     - Free
     - Paid
     - Self-paced
     - Live
4. Select a course you want to enquire about by specifying the course number
5. Ask questions about the selected course like -
     - Description
     - Pace
     - Price
     - Rating
     - Testimonials
     - Course Link
     - Financial aid
     - Pre-requisites
     - Overview
     - Certification
     - Doubt support
     - Instructor/mentor details
     - Duration
  

  ## Database
  I created a MongoDB database containing course details from GeeksforGeeks, categorized by subject, pace, and difficulty. The data was sourced from the website, course brochures, and mentor LinkedIn profiles. I then integrated this database with my chatbot for easy access. You can view the database in the CSV file given above.
  
  The database currently consists of 40 courses, each with 15 columns.The database is dynamic and can be modified in MongoDB, allowing for the addition of more data. This enhances the chatbot's capabilities, making it even more powerful.


  ## Steps

1. Improved Intent Classification: Enhanced the intent model to accurately identify user queries about available courses. Expanded the training data with diverse examples, enabling the chatbot to understand variations in user input. By enriching the training dataset, the DIETClassifier can better generalize and classify user intents, reducing misclassification errors.

2. Added Course Category Listing: Implemented functionality to list all available course categories, alongside their respective course numbers. This enables users to easily explore different course categories and make informed selections by specifying the course number.

3. Filtered Course Listings by Category: Added intents and actions to filter courses based on specific categories. Utilized separate intents for each course category, providing users with options based on their preferences.

4. Course Type Filtering: Introduced intents and actions to filter courses by their type, including paid, free, self-paced, and live courses. This enhances user experience by offering options that match their specific requirements.

5. Course Selection Capability: Implemented functionality for users to select a course of interest. Utilized a slot named "course_no" to remember the selected course number. Additionally, added logic to handle out-of-range course numbers, ensuring that errors don't occur

6. Integration with Database: Integrated the chatbot with a database to retrieve course information and respond to user queries dynamically. This allows the chatbot to provide accurate and up-to-date course details directly from the database.

7. Fallback Mechanism: Created a fallback action to handle instances where the confidence of intent classification falls below a predefined threshold of 0.3. This ensures that the chatbot can  handle user queries that may not match any defined intents with sufficient confidence.

8. Chat Transcript Logging: Implemented an action to save the chat transcript of user interactions in a CSV file. This action is triggered when the user says thanks to end the conversation, providing a record of the chat session for future reference or analysis.



   
