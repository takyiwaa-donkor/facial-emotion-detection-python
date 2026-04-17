"""
Configuration module for the Habit Tracking Application.

This module initializes the global logging settings used across the
application. It configures:
    - The log file location (`habit_tracker.log`)
    - The logging level (INFO)
    - The log message format, including timestamp, severity, and message

All modules in the application can import this configuration to ensure
consistent logging behavior for debugging, auditing, and tracking user
actions.
"""
import logging

logging.basicConfig(
    filename="habit_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)