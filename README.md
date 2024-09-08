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


## Usage
Prepare Your Video File: Place your video file in the project directory and name it <b>video.mp4</b>, or update the code to reference your file name.
Run the Script: Execute the script using Python:


## Result
View the Results: The video will display with overlaid lines showing the entry and exit points. Vehicle counts and speeds will be displayed on the video. Press Enter to exit the program and close the video window

## Code Details
Video Capture: <b>cv2.VideoCapture('video.mp4') </b> initializes video capture from the file.
Background Subtractor: <b>cv2.bgsegm.createBackgroundSubtractorMOG()</b> for vehicle detection.
Center Calculation: center_handle(x, y, w, h) calculates the center of detected vehicles.
Frame Resizing: <b>cv2.resize(frame1, (display_width, display_height))</b> scales the video frame to fit the display window.
Vehicle Tracking: Monitors vehicles crossing defined lines for entry and exit counts.
Speed Calculation: Computes vehicle speeds and displays them on the video.

## Configuration

Line Positions: Adjust in_line_position and out_line_position to set entry and exit lines based on your video.
Detection Sensitivity: Modify min_width_react and min_hight_react to fine-tune vehicle detection.
Display Size: Set display_width and display_height to match your screen resolution for optimal display.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.


```bash
pip install opencv-python-headless numpy
python vehicle_detection.py







    


