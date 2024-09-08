import cv2
import numpy as np
import streamlit as st

# Webcamera or video file
cap = cv2.VideoCapture('video.mp4')
in_line_position = 450  # Y-coordinate of the "in" line
out_line_position = 550  # Y-coordinate of the "out" line
min_width_react = 80  # Minimum width of vehicle detection box
min_hight_react = 80  # Minimum height of vehicle detection box
fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
# Real-world distance between two points on the video (in meters)
distance_between_lines_m = 10  # Adjust according to your setup

# Initialize background subtractor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
in_counter = 0
out_counter = 0
previous_frame_positions = {}


while True:
    ret, frame1 = cap.read()
    if not ret:
        break

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    
    # Applying background subtraction in each frame
    img_sub = algo.apply(blur)
    dillt = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    diltada = cv2.morphologyEx(dillt, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(diltada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the "in" and "out" lines
    cv2.line(frame1, (25, in_line_position), (1200, in_line_position), (0, 255, 0), 3)  # Green "in" line
    cv2.line(frame1, (25, out_line_position), (1200, out_line_position), (0, 0, 255), 3)  # Red "out" line
     
    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_hight_react)
        if not validate_counter:
            continue
     
        # Draw bounding box and vehicle text
        cv2.putText(frame1, "Vehicle", (x, y-20), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 3)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = center_handle(x, y, w, h)

        # Calculate speed
        if i in previous_frame_positions:
            previous_position = previous_frame_positions[i]
            distance_px = np.linalg.norm(np.array(center) - np.array(previous_position))
            distance_m = (distance_px / frame1.shape[1]) * distance_between_lines_m  # Convert pixels to meters
            speed_m_s = distance_m * fps  # Speed in meters per second
            speed_kmh = speed_m_s * 3.6  # Convert to km/h

            # Display speed above the vehicle
            cv2.putText(frame1, f"Speed: {speed_kmh:.2f} km/h", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)

        # Store the current position as the previous one for the next frame
        previous_frame_positions[i] = center
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 225), -1)

        # Check if the vehicle is crossing the "in" or "out" line
        if center[1] < (out_line_position + offset) and center[1] > (out_line_position - offset):
            out_counter += 1
            cv2.line(frame1, (25, out_line_position), (1200, out_line_position), (255, 0, 0), 3)
            detect.remove(center)
            print("Vehicle out count: " + str(out_counter))

        elif center[1] < (in_line_position + offset) and center[1] > (in_line_position - offset):
            in_counter += 1
            cv2.line(frame1, (25, in_line_position), (1200, in_line_position), (255, 0, 0), 3)
            detect.remove(center)
            print("Vehicle in count: " + str(in_counter))

    # Display the total vehicle count for both "in" and "out"
    cv2.putText(frame1, f"In: {in_counter}", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
    cv2.putText(frame1, f"Out: {out_counter}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    # Calculate the total vehicle count
    total_vehicles = in_counter + out_counter

    # Display the vehicle counts for "in", "out", and total
    cv2.putText(frame1, f"In: {in_counter}", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
    cv2.putText(frame1, f"Out: {out_counter}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.putText(frame1, f"Total: {total_vehicles}", (50, 230), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)

    cv2.imshow('Vehicle Detection', frame1)

    if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
        break

cv2.destroyAllWindows()
cap.release()
