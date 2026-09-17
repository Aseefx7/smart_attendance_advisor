\# Smart Attendance Advisor



\## 1. Problem Statement



Students need to maintain a minimum attendance percentage, such as 75%.

It can be difficult to determine how many classes can be skipped safely or

how many upcoming classes must be attended when the current attendance is

below the required threshold.



The Smart Attendance Advisor is an intelligent agent that analyzes attendance

records for each subject and provides a recommendation based on the required

attendance goal.



\## 2. Objective



The objectives of this project are:



\- Calculate the current attendance percentage.

\- Analyze attendance separately for each subject.

\- Determine whether the student satisfies the required attendance goal.

\- Calculate the maximum number of classes that can be skipped while remaining

&#x20; compliant.

\- Calculate the minimum number of consecutive classes that must be attended

&#x20; when attendance is below the required threshold.

\- Handle invalid inputs and edge cases.



\## 3. Intelligent Agent Approach



The agent follows a goal-directed approach.



The main goal of the agent is:



"Maintain attendance at or above the required threshold."



The agent observes:



\- Classes attended

\- Classes conducted

\- Required attendance percentage



It then compares the current attendance with the goal.



If the attendance is at or above the threshold, the agent calculates how many

classes can safely be skipped.



If the attendance is below the threshold, the agent calculates how many

consecutive classes must be attended to reach the required percentage.



\## 4. Algorithm



1\. Read the required attendance threshold.

2\. Read the number of subjects.

3\. For each subject, read classes attended and classes conducted.

4\. Calculate current attendance percentage.

5\. Compare the percentage with the required threshold.

6\. If the goal is satisfied, calculate maximum safe skips.

7\. If the goal is not satisfied, calculate the minimum classes that must be

&#x20;  attended.

8\. Display the recommendation.

9\. Handle invalid values and edge cases.



\## 5. Project Structure



```text

smart\_attendance\_advisor/

│

├── src/

│   └── attendance\_advisor.py

│

├── tests/

│   └── test\_attendance.py

│

├── docs/

│

├── README.md

│

├── requirements.txt

│

└── .gitignore

