

A Python console-based Habit Tracker that allows users to record daily habits, track streaks, and analyse habit performance using reports and visual progress indicators.

The application stores habit records in a SQLite database, enabling users to maintain long-term habit data and generate meaningful analytics.

## Project Overview

Developing good habits requires consistency and feedback.
Many people struggle to maintain habits because they cannot easily track progress or identify behaviour patterns.

This Habit Tracker solves this problem by providing a simple but powerful habit monitoring system with:

persistent data storage

performance analytics

visual progress indicators

The application demonstrates Python programming, modular design, and database integration.

## Features
Habit Management

Users can:

View predefined habits

Record daily habit values

Select measurement units

Store records with dates

## Example habits:

Habit	Example Units
Water Intake	gallons / liters
Exercise	km / miles
Sleep	hours / minutes
Reading	hours / minutes
Meditation	minutes / hours
Habit Streak Analytics

The system calculates habit consistency using:

Longest streak

Current streak

Streak statistics

maximum

minimum

average

Example output:

Longest streak: 12 days
Current streak: 5 days
Average streak: 6.3 days
Habit Reports

Users can generate reports to analyse their behaviour.

Daily Report

Shows which habits were completed today.

Weekly Report

Displays completion frequency during the last 7 days.

Example:

Weekly Report
-------------
Water Intake   5/7 days
Exercise       4/7 days
Sleep          7/7 days
Reading        3/7 days
Meditation     2/7 days
Monthly Report

Shows habit consistency across the last 30 days.

Visual Progress Bars

Reports include ASCII progress bars with colour indicators.

Example:

Exercise      ███████████░░░░░░░░ 55%
Sleep         ███████████████████ 100%
Reading       ███░░░░░░░░░░░░░░░░ 20%

Performance colours:

Colour	Meaning
Green	Excellent consistency
Yellow	Moderate consistency
Red	Needs improvement
Habit Leaderboard 🏆

The leaderboard ranks habits based on completion percentage over the last 30 days.

Example:

Habit Leaderboard
-----------------

1. Sleep        ███████████████████ 95%
2. Water Intake ██████████████░░░░░ 70%
3. Exercise     █████████░░░░░░░░░░ 45%
4. Reading      █████░░░░░░░░░░░░░░ 25%
5. Meditation   ████░░░░░░░░░░░░░░░ 20%
System Architecture

The application follows a modular design architecture.

+-------------------+
|       USER        |
|  (Console Menu)   |
+---------+---------+
          |
          v
+-------------------+
|      main.py      |
| Application Logic |
+---------+---------+
          |
          v
+-------------------+
|    database.py    |
| Database Queries  |
+---------+---------+
          |
          v
+-------------------+
|     SQLite DB     |
|      habit.db     |
+-------------------+

Benefits:

modular structure

easier debugging

scalable architecture

Technologies Used
Technology	Purpose
Python	Core programming language
SQLite	Persistent data storage
PyCharm	Development environment
GitHub	Version control
Colorama	Coloured console output
Installation

Clone the repository:

git clone https://github.com/yourusername/habit-tracker.git

Navigate to the project directory:

cd habit-tracker

Install required dependency:

pip install colorama or pip3

Run the application:

python main.py or python3

Example Console Menu
===============================
        HABIT TRACKER
===============================

1 View Habits
2 Record Habit
3 Longest Streak
4 Current Streak
5 Streak Statistics
6 View Records
7 Daily Report
8 Weekly Report
9 Monthly Report
10 Habit Leaderboard
11 Exit
Project Structure
habit-tracker
│
├── main.py
├── database.py
├── habit.db
│
├── tests
│   └── test_tracker.py
│
├── screenshots
│   ├── menu.png
│   ├── record_habit.png
│   ├── weekly_report.png
│   └── leaderboard.png
│
└── README.md

## Screenshots

Example screenshots to include in the repository:

Feature	Screenshot
Main Menu	screenshots/menu.png
Recording Habit	screenshots/record_habit.png
Weekly Report	screenshots/weekly_report.png
Habit Leaderboard	screenshots/leaderboard.png
Development Approach

The application was developed using a modular Python architecture.

main.py

Handles:

console menu

habit logic

analytics functions

report generation

database.py

Handles:

database connection

table creation

saving habit records

retrieving historical data

This separation improves code maintainability and readability.

Challenges and Solutions
Habit Streak Calculations

Calculating streaks required comparing dates using the Python datetime module.

Persistent Storage

Habit records needed to remain available between sessions.

Solution:

Implemented SQLite database storage.

User Experience

The console interface was enhanced using:

structured menus

progress indicators

coloured outputs

Future Improvements

## Possible extensions include:

Custom user-defined habits

Graphical user interface (GUI)

Data visualisation using charts

Exporting reports to CSV or PDF

Mobile or web-based version

## License

This project was created for educational purposes.(MIT)

Author: Takyiwaa Donkor

Developed as part of a Python programming project demonstrating habit tracking, analytics, and database integration.