<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/robot.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">Robotic Arm Pick and Place</h1>
</p>
<p align="center">
    <em><code>RAPP (Robot Arm Pick & Place) - Pick and place algorithm using OpenCV and the Armbot kinematics class, as a demo project. Using the algorithm, the EVA arm can detect an object, pick it up with an implemented custom gripper, and place it elsewhere. Using Python.</code></em>
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Running the Code](#-running-the-code)
- [ Key Components](#key-components)
  - [ Kinematics: Mathematical Foundations](#kinematics-mathematical-foundations)
  - [ ArmBot](#armbot)
  - [ Pick-and-Place Algorithm](#pick-and-place-algorithm)
- [ Contributing](#-contributing)
</details>
<hr>

##  Overview

<code>This project provides a comprehensive framework for controlling a robotic arm to perform a pick-and-place operation. It leverages computer vision to identify objects, calculate their positions, and manipulate them accurately. The project is structured into three main components: kinematics calculations (**kinematics.py**), the robotic arm control (**armbot.py**), and the pick-and-place algorithm implementation (**pick-and-place.py**). This guide details the setup process, key functionalities, and the mathematical foundations behind the robotic operations.</code>

---

##  Repository Structure

```sh
└── rapp_pick_and_place/
    ├── README.md
    ├── aravis.py
    ├── armbot.py
    ├── evasdk
    │   ├── Eva.py
    │   ├── EvaDiscoverer.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── eva_errors.py
    │   ├── eva_http_client.py
    │   ├── eva_locker.py
    │   ├── eva_ws.py
    │   ├── helpers.py
    │   ├── robot_state.py
    │   └── version.py
    ├── kinematics.py
    └── pick-and-place.py
```

---

##  Modules

<details open><summary>.</summary>

| File                                                                                                        | Summary                         |
| ---                                                                                                         | ---                             |
| [pick-and-place.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/pick-and-place.py) | <code>► Main pick and place algorithm </code> |
| [armbot.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/armbot.py)                 | <code>► Armbot class </code> |
| [kinematics.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/kinematics.py)         | <code>► Kinematics class </code> |
| [aravis.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/aravis.py)                 | <code>► Aravis class for camera control </code> |

</details>

<details closed><summary>evasdk</summary>

| File                                                                                                                 | Summary                         |
| ---                                                                                                                  | ---                             |
| [eva_http_client.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/eva_http_client.py) | <code>► INSERT-TEXT-HERE</code> |
| [eva_ws.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/eva_ws.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [EvaDiscoverer.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/EvaDiscoverer.py)     | <code>► INSERT-TEXT-HERE</code> |
| [eva_locker.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/eva_locker.py)           | <code>► INSERT-TEXT-HERE</code> |
| [eva_errors.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/eva_errors.py)           | <code>► INSERT-TEXT-HERE</code> |
| [version.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/version.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [Eva.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/Eva.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [helpers.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/helpers.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [robot_state.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/evasdk/robot_state.py)         | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**Prerequisites:**

To run this project, you need Python installed on your system (Python 3.6 or newer is recommended). Additionally, you must install the following libraries:

* **Python**: `version 3.6.0++`
* **NumPy**: `For numerical calculations`
* **Matplotlib**: `For plotting and visualization of the robot's movements`
* **SymPy**: `For symbolic mathematics and kinematics calculations`
* **OpenCV (cv2)**: `For image processing and computer vision tasks`
* **Threading**: `For parallel execution of image acquisition and processing`
* **evasdk (specific to the EVA robotic arm, included in evasdk folder)**: `For eva robot arm control`
* **aravis**: `For camera control`

You can install these packages using pip:

> ```console
> $ pip install numpy matplotlib sympy opencv-python aravis
> ```

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the rapp_pick_and_place repository:
>
> ```console
> $ git clone https://github.com/Alexpascual28/rapp_pick_and_place.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd rapp_pick_and_place
> ```
>
> 3. Install the dependencies.

###  Running the Code

To start the pick-and-place operation, run the pick-and-place.py script in your terminal:

<h4>From <code>source</code></h4>

> Run rapp_pick_and_place using the command below:
> ```console
> $ python pick-and-place.py
> ```

Ensure that kinematics.py and armbot.py are in the same directory as pick-and-place.py, as they are imported by the main script.

---

## Key Components

### Kinematics: Mathematical Foundations

`kinematics.py` defines the **Kinematics** class responsible for calculating the robot arm's movements. It uses mathematical models to determine how the arm should move its joints to reach a specific position.

**Inverse Kinematics and the Jacobian Matrix**

Inverse kinematics is the process of determining the joint parameters that provide a desired position of the robot's end effector. The Jacobian matrix is a critical tool in solving inverse kinematics problems because it relates the change in joint angles to the resulting movement of the end effector in space.

In the Kinematics class, we calculate the Jacobian matrix as follows:

> ```console
> # Calculate the numerical value of J (jacobian) at each point,
> # you can produce the Jacobian as follows
> J = p.jacobian(theta)
> J_i = J.subs({theta1:theta_i[0], theta2:theta_i[1], theta3:theta_i[2],
>             theta4:theta_i[3], theta5:theta_i[4], theta6:theta_i[5]}).evalf()
> ```

Where `p` is the position vector of the end effector, and `theta` represents the joint angles.

To move the end effector towards a target, we adjust the joint angles based on the calculated differential movement `dp`. The Jacobian inverse is used to find the necessary change in joint angles `dtheta` to achieve `dp`:

> ```console
> J_inv = J_i.pinv()
> dtheta = J_inv * dp_step
> ```

`dp_step` is the desired small step towards the target position. The pseudoinverse (`pinv()`) of the Jacobian is used when the matrix is not square, ensuring a solution exists.

### ArmBot

The **ArmBot** class, defined in `armbot.py`, using the kinematics class to control the robotic arm and integrates computer vision for object detection. Key functions include:

**Main Functions of ArmBot Class**

* **initialize_kinematics()**: Sets up the kinematics for the robotic arm.
* **move_end_efector(absolute_position)**: Moves the end effector to an absolute position.
* **shift_end_efector(relative_position)**: Adjusts the end effector's position relative to its current location.
* **open_gripper()** and **close_gripper()**: Controls the gripper to pick up or release objects.
* **start_image_acquisition()**: Starts continuous image acquisition and processing.
* **detect_colour(image, colour_name)**: Identifies objects in the image based on their color.
* **detect_shapes(mask, shape_name)**: Detects geometric shapes within a masked image.

### Pick-and-Place Algorithm

The pick-and-place algorithm integrates kinematics, robotic arm control, and computer vision to identify objects, calculate their positions, and manipulate them. The process involves:

* Moving the arm to a starting position and opening the gripper.
* Continuously capturing images to detect a target object based on color and shape.
* Calculating the object's position in the camera frame and adjusting the arm's position to align the gripper above the object.
* Lowering the gripper, closing it to grasp the object, lifting, and moving the object to a new location for release.

> ```console
> # From pick-and-place.py, aligning and picking up an object
> if is_gripper_over_object:
>    arm.open_gripper()
>    pick_up_position = [0, 0, -0.05] 
>    arm.shift_end_efector(pick_up_position)
>    arm.close_gripper()
>    pick_up_position = [0, 0, 0.3] 
>    arm.shift_end_efector(pick_up_position)
>    ...
>
> ```

This snippet shows how the script aligns the gripper above the object, adjusts the gripper's height to pick up the object, and then moves the object to a predefined location.

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Alexpascual28/rapp_pick_and_place.git/issues)**: Submit bugs found or log feature requests for the `rapp_pick_and_place` project.
- **[Submit Pull Requests](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Alexpascual28/rapp_pick_and_place.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Alexpascual28/rapp_pick_and_place.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/Alexpascual28/rapp_pick_and_place.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Alexpascual28/rapp_pick_and_place.git">
   </a>
</p>
</details>

---
