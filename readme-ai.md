<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
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
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>This project provides a comprehensive framework for controlling a robotic arm to perform a pick-and-place operation. It leverages computer vision to identify objects, calculate their positions, and manipulate them accurately. The project is structured into three main components: kinematics calculations (kinematics.py), the robotic arm control (armbot.py), and the pick-and-place algorithm implementation (pick-and-place.py). This guide details the setup process, key functionalities, and the mathematical foundations behind the robotic operations.</code>

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
| [pick-and-place.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/pick-and-place.py) | <code>► INSERT-TEXT-HERE</code> |
| [armbot.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/armbot.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [kinematics.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/kinematics.py)         | <code>► INSERT-TEXT-HERE</code> |
| [aravis.py](https://github.com/Alexpascual28/rapp_pick_and_place.git/blob/master/aravis.py)                 | <code>► INSERT-TEXT-HERE</code> |

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

**System Requirements:**

* **Python**: `version x.y.z`

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
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run rapp_pick_and_place using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
