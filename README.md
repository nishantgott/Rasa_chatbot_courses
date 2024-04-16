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



   
