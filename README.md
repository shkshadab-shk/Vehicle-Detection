# Vehicle Detection and Counting System

## Overview

This project is a vehicle detection and counting system using OpenCV and Python. It processes a video file to detect vehicles, count how many vehicles enter and exit a specified region, and calculate their speed. The system displays the counts of vehicles that have entered and exited the region, as well as the total number of vehicles.

## Features

- Detects vehicles using background subtraction and contour detection.
- Counts vehicles entering and exiting a defined line.
- Calculates the speed of vehicles in kilometers per hour (km/h).


## Requirements

- Python 3.x
- OpenCV
- NumPy


Certainly! Here’s how you might customize the README to better fit your project details and preferences:

Vehicle Detection and Counting System
Overview
This project is a vehicle detection and counting system designed to analyze video footage and track vehicle movement. It utilizes OpenCV and Python to detect vehicles, count how many vehicles enter and exit specific regions, and calculate their speeds. The processed video will display vehicle counts and speeds in real time.

Features
Vehicle Detection: Uses background subtraction and contour detection to identify vehicles.
Vehicle Counting: Tracks vehicles entering and exiting predefined lines.
Speed Calculation: Computes the speed of each vehicle in kilometers per hour (km/h).
Resizable Display: Adjusts the video display size to fit different screens.
Vehicle Type Tracking: Counts different types of vehicles (e.g., cars, bikes, trucks).
Requirements
To run this project, you'll need Python 3.x and the following Python packages:

OpenCV
NumPy
Install the necessary packages using pip:

bash
Copy code
pip install opencv-python-headless numpy
Usage
Prepare Your Video File: Place your video file in the project directory and name it traffic.mp4, or update the code to reference your file name.

Run the Script: Execute the script using Python:

bash
Copy code
python vehicle_detection.py
View the Results: The video will display with overlaid lines showing the entry and exit points. Vehicle counts and speeds will be displayed on the video. Press Enter to exit the program and close the video window.
Code Details
Video Capture: cv2.VideoCapture('traffic.mp4') initializes video capture from the file.
Background Subtractor: cv2.bgsegm.createBackgroundSubtractorMOG() for vehicle detection.
Center Calculation: center_handle(x, y, w, h) calculates the center of detected vehicles.
Frame Resizing: cv2.resize(frame1, (display_width, display_height)) scales the video frame to fit the display window.
Vehicle Tracking: Monitors vehicles crossing defined lines for entry and exit counts.
Speed Calculation: Computes vehicle speeds and displays them on the video

You can install the required Python packages using pip:

```bash
pip install opencv-python-headless numpy
python vehicle_detection.py




