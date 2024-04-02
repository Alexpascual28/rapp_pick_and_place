# -*- coding: utf-8 -*-
"""
Created on Mon May  1 17:23:18 2023

@title: Lab Session 7 Task 3: Implement Picking-Up Motion
@author: Alejandro Pascual San Roman (bdh532)
@organisation: School of Physics, Engineering and Technology. University of York

"""

# =============================================================================

# Now that you can place the arm over top of the targets, you can implement motion 
# to pick it up.  In most industrial robots, this motion is prescribed based on the 
# known position of the target, and you can most easily just have the arm move to a 
# pre-programmed height so that it is low enough for your gripper to grab the object, 
# and then close the gripper fingers.  You can also if needed refine the position 
# of the object as the arm is lowered.  Then, close the gripper, raise the arm, and 
# move the object using the arm to a new location, then release it.

# =============================================================================

# 1. import all the modules/libraries for Python that are needed for your code, including NumPy, SymPy, MatPlotLib 
#    (if you want to use plotting of your kinematics as before), the evasdk module, and the aravis module.
import numpy as np
import matplotlib.pyplot
from kinematics import Kinematics

from mpl_toolkits.mplot3d import Axes3D
from sympy import Matrix, Symbol, symbols, solveset, solve, simplify, S, diff, det, erf, log, sqrt, pi, sin, cos, tan, atan2, init_printing

from evasdk import Eva
from json import dumps
 
import time
import cv2
# import imutils
from aravis import Camera

# 2. Initialize your kinematics functions and variables including the constants (dimensions, etc.) for the EVA robot arm.

# Initializes main kinematics class to assist with robot movement
def initialize_kinematics():
    # Dimensions of each link of the robot in metres
    arm_dimensions = [0.187, 0.096, 0.205, 0.124, 0.167, 0.104];
    
    # Robot initial pose (in joint angles)
    initial_pose = [0, 1, -2.5, 0, -1.6, 0] # [0, 1, -2.5, 0, -1.6, 0] # or [0,0,0,0,0,0]; # or [-pi/2,-pi/4,3*pi/4,0,pi/2,0];
    simulate = True # Whether the calculations should be displayed as a graphical simulation  
    
    # Variables to control calculation speed and accuracy
    dp_threshold = 0.01 # Calculations will stop when dp is lower than the threshold
    step_size = 0.01 # In each step, the robot will move this amount
    theta_max_step = 0.5 # Each joint won't rotate more than this angle in radians
    pause = 0.0000001 # Time the plot will be displayed
    
    # Variables to control how the plot is displayed
    plot_dimensions = [[-0.5, 0.5], # x axis limits in metres (min, max)
                       [-0.5, 0.5], # y axis limits in metres (min, max)
                       [0, 0.5]]    # z axis limits in metres (min, max)
    camera_view = [30, 45] # elev, azim (camera position and rotation)
    
    # All values are written to the Kinematics class
    kn = Kinematics(arm_dimensions, initial_pose, simulate, dp_threshold, step_size, theta_max_step, pause, plot_dimensions, camera_view);
    return kn

# 3. Initialize the arm and the camera as in the previous labs and start the camera capturing frames and showing them 
#    in an OpenCV window.

# Initializes robot arm module with specified conexion details
def initialize_arm():
    print("\nInitialising EVA robot arm...")
    
    # Details to connect to the robot arm, more info here: 
    # https://wiki.york.ac.uk/display/TSS/Network+Details+and+Credentials+for+the+EVA+Arms+and+Network+Cameras 
    arm_hostname = "evatrendylimashifterpt410"
    arm_ip = "144.32.152.105"
    token = "1462980d67d58cb7eaabe8790d866609eb97fd2c"
  
    # Create an “eva” object with these parameters to connect to the arm itself on the network
    eva = Eva(arm_ip, token)
    print("Done.\n")
    return eva

# Initializes camera module by connecting using the specified details
def initialize_camera():
    print("\nInitialising camera...")
    
    # Conexion details for the camera
    camera_hostname = "evacctv01"
    camera_ip = "144.32.152.102"
    camera_id = 'S1188411'

    # You can initialize a Camera object and set its parameters with:
    cam = Camera(camera_id)
    cam.set_feature("Width", 1936)
    cam.set_feature("Height", 1216)
    cam.set_frame_rate(10)
    cam.set_exposure_time(100000)
    cam.set_pixel_format_from_string('BayerRG8')

    # Print out the camera parameters in use
    print("\nCamera model: ", cam.get_model_name())
    print("Vendor Name: ", cam.get_vendor_name())
    print("Device id: ", cam.get_device_id())
    print("Region: ", cam.get_region(), end="")
    print("\n")
    
    return cam

def main():
    # Connect to the arm, camera and kinematics modules
    kn = initialize_kinematics();
    eva = initialize_arm();
    cam = initialize_camera();
    
    # Start camera acquisition block
    try:
        # Start the camera
        cam.start_acquisition_continuous()
        print("Camera On")
        
        # Open an OpenCV window to view the image
        cv2.namedWindow('capture', flags=0)
        
        # Capture an individual frame
        frame = cam.pop_frame()
        print("[", time.time(), "] initial frame. ""Shape: ", frame.shape)
        
        if not 0 in frame.shape:
            # Convert to standard RGB format
            image = cv2.cvtColor(frame, cv2.COLOR_BayerRG2RGB)
    
            # Show the image and wait a short time with:
            cv2.imshow("capture", image)
            cv2.waitKey(1)
            
        # 4. Move the arm to a starting position, ideally near where your target is located so that your camera can see it, 
        #    and initialize the state of the robot arm to have no object in its gripper and to move to pick up.
        target_position = [0, -0.2, 0.3];
        current_pose = kn.calculate_joint_angles(target_position, position_type = "absolute")
        
        with eva.lock():
          eva.control_wait_for_ready()
          eva.control_go_to(current_pose)
        
        # Open the gripper (to get rid of whatever is being gripped and test the gripper)
        with eva.lock():
           eva.control_wait_for_ready()
           eva.gpio_set('ee_d0', False)
           eva.gpio_set('ee_d1', True)
           
        time.sleep(0.2)
        
        # Close your gripper (or open it, depending on the design you have made), 
        # you need to set ee_d1 to a low logic state and ee_d2 to a high logic state
        with eva.lock():
           eva.control_wait_for_ready()
           eva.gpio_set('ee_d1', False)
           eva.gpio_set('ee_d0', True)
           
        # 5. Start your main program loop, in which you will probably need to:
        t = 0
        t_timeout = 50000 
        
        # Start main loop
        while t < t_timeout:
            i = 0
            maximum_i = 1000
            is_gripper_over_object = False
            is_aligned_x = False;
            is_aligned_y = False;
            is_aligned_z = False;
            
            # Start loop to detect if gripper is directly over the target
            while i < maximum_i and is_gripper_over_object == False:
                i += 1
            
                # a. Capture a frame from the camera and convert it to OpenCV format.
                frame = cam.pop_frame()
                print("[", time.time(), "] frame nb: ", i, " shape: ", frame.shape)
                
                # If a frame is taken (frame.shape is not empty)
                if not 0 in frame.shape:
                    # Convert to standard RGB format
                    cv_image = cv2.cvtColor(frame, cv2.COLOR_BayerRG2RGB)
                    
                    # Convert to bgr
                    #cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
                    
                    # b. Perform shape detection or blob detection using OpenCV to identify the target object to pick up.
                    
                    # Convert rgb image into hsv image
                    # hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV) # BGR to HSV
                    hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2HSV)
                    
                    # Initialise sensitivity colour detection value (10 should be enough)
                    red_sensitivity = 10
                    yellow_sensitivity = 12
                    cyan_sensitivity = 16
                    magenta_sensitivity = 16
                    
                    # Identify hue for different colours
                    red_hue = 0
                    yellow_hue = 30
                    cyan_hue = 90
                    magenta_hue = 150
                    
                    # Set upper and lower bounds for HSV colours
                    # Red = 0
                    hsv_red_lower = np.array([red_hue - red_sensitivity, 100, 100])
                    hsv_red_upper = np.array([red_hue + red_sensitivity, 255, 255])
                    
                    # Filter out colours separately using cv2.inRange() method
                    red_mask = cv2.inRange(hsv_image, hsv_red_lower, hsv_red_upper)
                    
                    # Generalize mask by using morphology
                    kernel_open = np.ones((15,15), np.uint8)
                    kernel_close = np.ones((30,30), np.uint8)
                    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel_close)
                    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel_open)
                    
                    # Apply mask to original image using cv2.bitwise_and() method
                    mask_image = cv2.bitwise_and(cv_image, cv_image, mask=red_mask)
                    
                    # Detect contours within image
                    contours = cv2.findContours(red_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    
                    # If there is any:
                    if len(contours[0]) > 0:
                        # Select the largest one
                        max_contour = max(contours[0], key = cv2.contourArea)
                        
                        # Calculate minimum rectangle parameters
                        rectangle = cv2.minAreaRect(max_contour)
                        [[center_x, center_y], [contour_width, contour_height], angle_of_rotation] = rectangle
                        
                        # Get corner points of the rectangle
                        box = cv2.boxPoints(rectangle)
                        box = np.int0(box)
                        
                        # c. Show the frame in the OpenCV window with detection annotations.
                        
                        # Draw and label the contours
                        cv2.putText(mask_image, "target", (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
                        cv2.drawContours(mask_image, [box], -1, (0, 255, 0), 2)
                        
                        cv2.putText(cv_image, "target", (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
                        cv2.drawContours(cv_image, [box], -1, (0, 255, 0), 2)
            
                        # Show the image and wait a short time with:
                        cv2.imshow("capture", cv_image)
                        cv2.waitKey(1)
                        
                        # d. Identify the location of the target object or the target drop location and convert this target location
                        #    into the coordinate system that you are using for kinematics.
                        
                        image_height, image_width, image_channels = cv_image.shape # Image dimesions (width, height) in pixels
                        
                        pixel_size = 0.00000586 # Pixel size in metres (4.8 micrometers)
                        sensor_width_m = pixel_size * image_width # Width of the camera sensor in metres
                        focal_length_m = 0.016 # Camera focal length in metres (16 milimetres).
                        
                        focal_length_p = focal_length_m * image_width / sensor_width_m # Rough estimate of focal length in px. Must be in pixels! Can be calibrated to find out more accurately.
                        known_width = 0.02 # Known width of object in metres (2 centimetres).
                        
                        # Calculate position of center point of contour in 3D space (from the camera)
                        center_z = (known_width * focal_length_p) / contour_width # Distance to the object in metres
                        # point_xyz = [center_x, center_y, center_z] # point is in Camera Optical frame, i.e. point[0] x-right (px),  point[1] y-down (px), point[2] z-forward (m)
    
                        # e. Calculate inverse kinematics for the robot arm to move to the next step in direction towards the target 
                        #    location - it is usually better to move as a series of small steps rather than a single large motion 
                        #    but it depends on how your inverse kinematics are implemented.
                        
                        # Robot movement step size and target distance
                        robot_step_size = 0.01 # in metres (e.g 1 cm -> 0.01 m)
                        target_distance_to_object = 0.15 # Target distance to the object (e.g 15 cm -> 0.15 m)
                        margin = 0.01 # Margin of alignment to the object
                        
                        # Adjust x axis
                        if (center_x > (image_width / 2) + margin): # If the object is too much to the left
                            target_position_x = robot_step_size; # Move to the right
                            is_aligned_x = False;
                            
                        elif (center_x < (image_width / 2) - margin): # If the object is too much to the right
                            target_position_x = -robot_step_size; # Move to the left
                            is_aligned_x = False;
                            
                        else: # If the object is in the centre (within the margin)
                            is_aligned_x = True;
                            target_position_x = 0; # Stop
                            
                        # Adjust y axis
                        if (center_y > (image_height / 2) + margin): # If the object is too up in the image
                            target_position_y = robot_step_size; # Move down
                            is_aligned_y = False;
                            
                        elif (center_y < (image_height / 2) - margin): # If the object is too down in the image
                            target_position_y = -robot_step_size; # Move up
                            is_aligned_y = False;
                            
                        else: # If the object is in the centre (within the margin)
                            is_aligned_y = True;
                            target_position_y = 0; # Stop
                              
                        # Adjust z axis
                        if (center_z > target_distance_to_object + margin): # If the object is too far away
                            target_position_z = -robot_step_size; # Move forward
                            is_aligned_z = False;
                            
                        elif (center_z < target_distance_to_object - margin): # If the object is too near
                            target_position_z = robot_step_size; # Move backwards
                            is_aligned_z = False;
                            
                        else: # If the object at the correct distance (within the margin)
                            is_aligned_z = True;
                            target_position_z = 0; # Stop
                            
                        # Add all movements together (along the three axis)
                        target_position = [target_position_x, target_position_y, target_position_z];
        
                        # Move the robot
                        current_pose = kn.calculate_joint_angles(target_position, position_type = "relative")
                        with eva.lock():
                          eva.control_wait_for_ready()
                          eva.control_go_to(current_pose)
                          
                        # If the gripper is aligned right on top of the object (on the three axis), break the loop (see beginning of while statement)
                        is_gripper_over_object = is_aligned_x and is_aligned_y and is_aligned_z;
                        
            # f. Detect when the gripper on the robot arm is located around the target object, and close the gripper, 
            #    or else detect that the arm has reached the drop location and open the gripper.
            if is_gripper_over_object:
                # Open gripper
                with eva.lock():
                   eva.control_wait_for_ready()
                   eva.gpio_set('ee_d0', False)
                   eva.gpio_set('ee_d1', True)
                
                # Move towards the object
                pick_up_position = [0, 0, -0.05] # Object pick up distance, relative to the camera
                
                current_pose = kn.calculate_joint_angles(pick_up_position, position_type = "relative")
                with eva.lock():
                  eva.control_wait_for_ready()
                  eva.control_go_to(current_pose)
                  
                # Close gripper
                with eva.lock():
                   eva.control_wait_for_ready()
                   eva.gpio_set('ee_d1', False)
                   eva.gpio_set('ee_d0', True)
                   
                # Move up
                pick_up_position = [0, 0, 0.3] # Object pick up distance, relative to the camera
                
                current_pose = kn.calculate_joint_angles(pick_up_position, position_type = "relative")
                with eva.lock():
                  eva.control_wait_for_ready()
                  eva.control_go_to(current_pose)
                   
                # Move to target drop location
                target_drop_location = [0.2, 0.3, 0.1]
                
                current_pose = kn.calculate_joint_angles(target_drop_location, position_type = "absolute")
                with eva.lock():
                  eva.control_wait_for_ready()
                  eva.control_go_to(current_pose)
                  
                # Drop object
                with eva.lock():
                   eva.control_wait_for_ready()
                   eva.gpio_set('ee_d0', False)
                   eva.gpio_set('ee_d1', True)
        
                # g. Repeat and change the current status of the arm if it has completed picking up or dropping an object.
                is_gripper_over_object = False
                
            else:
                print("\nTimeout. No object was detected, or the robot arm failed to align itself with the object. Retrying.\n")

        # 6. Complete the main program loop and return the arm to home position.
        print("\nProcess ended. Returning to home location.")
        
        target_position = [0, -0.2, 0.3];
        current_pose = kn.calculate_joint_angles(target_position, position_type = "absolute")
        with eva.lock():
            eva.control_wait_for_ready()
            eva.control_go_to(current_pose)
        
    # 7. Handle exceptions with “except KeyboardInterrupt:'' and “finally:” so that if problems occur the camera is shut down 
    #    and the arm stopped safely.  It is possible to use a “try” and “except” block to automatically reset the arm with 
    #    eva.control_reset_errors() if collisions occur, but this is rarely done in practice because for safety a human operator 
    #    should inspect the arm after an error before restarting automated motion.
    except KeyboardInterrupt:
       print("Exiting...")
       
    finally:
        # To automatically reset the arm. A human operator should inspect the arm after an error before restarting automated motion.
        # eva.control_reset_errors()
        
        # Stop acquisition and shut down the camera with:
        cam.stop_acquisition()
        cam.shutdown()
        print("Camera Off")

if __name__ == "__main__":
    main();




