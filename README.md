# Vehicle Detection and Counting System

## Overview

This project is a vehicle detection and counting system using OpenCV and Python. It processes a video file to detect vehicles, count how many vehicles enter and exit a specified region, and calculate their speed. The system displays the counts of vehicles that have entered and exited the region, as well as the total number of vehicles.

## Features

- Detects vehicles using background subtraction and contour detection.
- Counts vehicles entering and exiting a defined line.
- Calculates the speed of vehicles in kilometers per hour (km/h).
- Resizes the video display to fit a specified window size.
- Supports counting and tracking for multiple types of vehicles (car, bike, truck).

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required Python packages using pip:

```bash
pip install opencv-python-headless numpy
