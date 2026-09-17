# Smart Attendance Advisor

## Intelligent Agent – Micro Level Project

The **Smart Attendance Advisor** is a Python-based intelligent agent that
helps students maintain the required attendance percentage for each subject.

The agent calculates the student's current attendance and provides a
goal-directed recommendation about whether classes can be skipped or how
many upcoming classes must be attended.

---

## Problem Statement

Students are required to maintain a minimum attendance percentage, such as
75%. It can be difficult to determine how many classes can be safely skipped
or how many classes must be attended when attendance is below the required
threshold.

This project solves the problem by calculating subject-wise attendance and
providing a clear recommendation based on the attendance goal.

---

## Agent Goal

The main goal of the intelligent agent is:

> Maintain attendance at or above the required threshold.

The agent observes the current attendance state and selects a recommendation
that helps the student achieve or maintain this goal.

---

## Features

- Calculates current attendance percentage.
- Supports multiple subjects.
- Uses a configurable attendance threshold.
- Calculates the maximum number of classes that can be skipped.
- Calculates the minimum number of classes that must be attended when below
  the threshold.
- Handles invalid input values.
- Handles zero classes conducted.
- Handles attendance exactly equal to the required threshold.
- Includes automated tests using `pytest`.

---

## Attendance Formula

The current attendance percentage is calculated using:

```text
Attendance Percentage =
(Classes Attended / Classes Conducted) × 100