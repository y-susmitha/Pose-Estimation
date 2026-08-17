\# RehabRanger



RehabRanger is a Python-based real-time rehabilitation exercise monitoring system.



The system uses camera-based pose estimation to detect body landmarks, calculate joint angles, identify exercise states, count repetitions, detect compensatory movements, provide exercise feedback, and store session information.



\---



\## 1. Project Overview



The main objective of RehabRanger is to provide a modular framework for monitoring rehabilitation exercises using computer vision and human pose estimation.



The system processes live camera frames and follows this general pipeline:



Camera

&#x20;  ↓

Pose Detection

&#x20;  ↓

Body Landmarks

&#x20;  ↓

Joint Angle Calculation

&#x20;  ↓

Exercise State Detection

&#x20;  ↓

Repetition Counting

&#x20;  ↓

Compensation Detection

&#x20;  ↓

Feedback

&#x20;  ↓

Session Logging



\---



\## 2. Project Structure



```text

RehabRanger/

│

├── main.py

├── camera.py

├── pose\_detector.py

├── session\_engine.py

├── state\_machine.py

├── exercise\_loader.py

├── feedback.py

├── calibration.py

├── repetition\_counter.py

├── compensation.py

├── logger.py

├── config.yaml

├── requirements.txt

├── README.md

│

├── exercises/

│   ├── side\_arm\_raise.yaml

│   ├── lunges.yaml

│   └── seated\_dorsiflexion.yaml

│

├── output/

│   ├── keypoints.json

│   └── events.json

│

├── models/

│   └── pose\_landmarker.task

│

└── utils/

&#x20;   ├── \_\_init\_\_.py

&#x20;   └── geometry.py



3\. Main Files

main.py



The main entry point of the RehabRanger application.



It initializes the required components and starts the exercise monitoring session.



camera.py



Responsible for:



Opening the webcam

Capturing video frames

Providing frames to the pose detector

Releasing the camera

pose\_detector.py



Responsible for:



Loading the pose estimation model

Processing camera frames

Detecting human body landmarks

Returning landmark coordinates

session\_engine.py



Controls the overall rehabilitation exercise session.



It coordinates:



Pose detection

Exercise state

Repetition counting

Feedback

Compensation detection

Logging

state\_machine.py



Determines the current exercise state from joint-angle measurements.



For example:



DOWN → UP → DOWN



State transitions are used by the repetition counter.



exercise\_loader.py



Loads exercise-specific configuration files from the exercises directory.



feedback.py



Generates exercise feedback based on the current state and detected movement.



Examples:



Excellent

Slow Down

Lift Smoothly

Lower Completely

calibration.py



Provides the calibration stage required before or during an exercise session.



repetition\_counter.py



Counts completed exercise repetitions based on the state transitions.



compensation.py



Detects undesirable or compensatory body movements.



Examples include:



Excessive trunk leaning

Incorrect knee alignment

Unwanted joint movement

logger.py



Stores session information, pose keypoints, repetitions, feedback, and compensation events.



4\. Exercise Configurations



Exercise-specific information is stored in YAML files.



Side Arm Raise



File:



exercises/side\_arm\_raise.yaml



The configuration contains:



Exercise name

Exercise type

Joint

MediaPipe landmarks

Angle thresholds

Exercise states

Repetition definition

Feedback

Compensation rules



Example:



name: Side Arm Raise





exercise\_type: upper\_body





joint: shoulder





side: right





landmarks:

&#x20; shoulder: 12

&#x20; elbow: 14

&#x20; wrist: 16

Lunges



File:



exercises/lunges.yaml



The primary joint being monitored is the knee.



Example:



name: Lunges





exercise\_type: lower\_body





joint: knee





side: right





landmarks:

&#x20; hip: 24

&#x20; knee: 26

&#x20; ankle: 28

Seated Dorsiflexion



File:



exercises/seated\_dorsiflexion.yaml



The primary joint being monitored is the ankle.



Example:



name: Seated Dorsiflexion





exercise\_type: lower\_body





joint: ankle





side: right





landmarks:

&#x20; knee: 26

&#x20; ankle: 28

&#x20; foot: 32

5\. Geometry Module



The file:



utils/geometry.py



contains mathematical functions used by the pose-processing system.



Important functions include:



calculate\_angle()

calculate\_distance()

midpoint()

normalize\_point()

pixel\_point()

angle\_from\_landmarks()



The calculate\_angle() function is particularly important because rehabilitation exercises can be analyzed using joint angles.



For example:



Shoulder

&#x20;   |

&#x20;   |

&#x20; Elbow

&#x20;   |

&#x20;   |

&#x20; Wrist



The angle formed by three landmarks can be calculated and passed to the exercise state machine.



6\. Pose Model



The pose model is stored under:



models/pose\_landmarker.task



This is a binary model file used by the pose detection component.



It is NOT a Python source-code file.



The model is loaded by:



pose\_detector.py



The model file must contain the actual compatible pose-estimation model. An empty .task file will not perform pose estimation.



7\. Output Files

keypoints.json



Location:



output/keypoints.json



This file stores pose landmark information obtained from the pose detector.



Typical information includes:



Frame number

Landmark ID

X coordinate

Y coordinate

Z coordinate

Timestamp



Example:



\[

&#x20;   {

&#x20;       "frame\_number": 1,

&#x20;       "landmarks": \[

&#x20;           {

&#x20;               "id": 12,

&#x20;               "x": 0.45,

&#x20;               "y": 0.30,

&#x20;               "z": -0.10

&#x20;           }

&#x20;       ]

&#x20;   }

]

events.json



Location:



output/events.json



This file stores important exercise events.



Examples include:



SESSION\_START

REPETITION

FEEDBACK

COMPENSATION

SESSION\_END



Example:



\[

&#x20;   {

&#x20;       "event\_type": "SESSION\_START",

&#x20;       "exercise": "Side Arm Raise"

&#x20;   },

&#x20;   {

&#x20;       "event\_type": "REPETITION",

&#x20;       "exercise": "Side Arm Raise",

&#x20;       "repetitions": 1

&#x20;   },

&#x20;   {

&#x20;       "event\_type": "FEEDBACK",

&#x20;       "exercise": "Side Arm Raise",

&#x20;       "message": "Excellent arm raise"

&#x20;   }

]

8\. Configuration



The general application configuration is stored in:



config.yaml



Exercise-specific configurations are stored separately under:



exercises/



This separation allows the same Python processing modules to support multiple exercises.



9\. Requirements



The project uses Python and the following packages:



opencv-python

numpy

PyYAML



The exact versions used in the current environment are specified in:



requirements.txt

10\. Python Version



The current development environment uses:



Python 3.7.6



Python executable:



C:\\Python376\\python.exe



Check the Python version using PowerShell:



C:\\Python376\\python.exe --version

11\. Installation



Open PowerShell and navigate to the project:



cd C:\\Users\\sushm\\Downloads\\NEW



Install the required packages:



C:\\Python376\\python.exe -m pip install -r requirements.txt

12\. Verify Installation



Check OpenCV:



C:\\Python376\\python.exe -c "import cv2; print(cv2.\_\_version\_\_)"



Check NumPy:



C:\\Python376\\python.exe -c "import numpy; print(numpy.\_\_version\_\_)"



Check PyYAML:



C:\\Python376\\python.exe -c "import yaml; print(yaml.\_\_version\_\_)"

13\. Running the Application



From the project directory:



cd C:\\Users\\sushm\\Downloads\\NEW



Run:



C:\\Python376\\python.exe main.py



The application should initialize the camera and pose-processing pipeline.



14\. Testing Individual Components



Individual modules can be tested before running the complete application.



For example:



C:\\Python376\\python.exe test\_geometry.py



Pose detection can be tested using:



C:\\Python376\\python.exe test\_pose.py

15\. Repetition Counting



The repetition counter uses exercise states.



For example:



DOWN

&#x20; ↓

UP

&#x20; ↓

Repetition + 1

&#x20; ↓

DOWN



A valid transition between exercise states represents a completed repetition according to the exercise configuration.



16\. Feedback System



The feedback system uses the exercise configuration to provide instructions to the user.



Examples:



Lower Completely

Excellent Curl

Slow Down

Lift Smoothly



Feedback can be generated according to:



Current exercise state

Movement speed

Joint angle

Detected compensation

17\. Compensation Detection



Compensation detection is used to identify movements that may indicate incorrect exercise technique.



For example:



Side Arm Raise

&#x20;   ↓

Arm movement detected

&#x20;   ↓

Trunk movement checked

&#x20;   ↓

Excessive trunk leaning?

&#x20;   ↓

Yes → "Avoid leaning your trunk"



Compensation thresholds are defined in the exercise YAML configuration.



18\. Logging



The logger records information from the exercise session.



Examples include:



Session started

Joint angle

Repetition

Feedback

Compensation

Pose keypoints

Session ended



The information is stored under:



output/

19\. Complete Processing Pipeline

&#x20;                   CAMERA

&#x20;                      │

&#x20;                      ▼

&#x20;               ┌─────────────┐

&#x20;               │ camera.py   │

&#x20;               └──────┬──────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ pose\_detector.py│

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;               POSE LANDMARKS

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ geometry.py     │

&#x20;             │ Angle Calculation│

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;                JOINT ANGLE

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ state\_machine.py│

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;                EXERCISE STATE

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌──────────────────┐

&#x20;             │ repetition\_counter│

&#x20;             └────────┬─────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;               REPETITION COUNT

&#x20;                      │

&#x20;            ┌─────────┴─────────┐

&#x20;            ▼                   ▼

&#x20;     compensation.py       feedback.py

&#x20;            │                   │

&#x20;            └─────────┬─────────┘

&#x20;                      ▼

&#x20;                  logger.py

&#x20;                      │

&#x20;             ┌────────┴────────┐

&#x20;             ▼                 ▼

&#x20;      keypoints.json      events.json

20\. Important Notes

pose\_landmarker.task is a binary model file and should not contain Python code.

Exercise thresholds in YAML files are configurable parameters.

keypoints.json stores pose landmark information.

events.json stores exercise/session events.

The utils directory contains reusable geometry functions.

The same processing framework can be used for multiple exercises.

The current project is intended as a software/engineering framework for exercise monitoring. The exercise thresholds should not be considered clinically validated rehabilitation criteria.

21\. Future Improvements



Possible future extensions include:



More rehabilitation exercises

Left/right side selection

Improved calibration

More robust compensation detection

Real-time graphical feedback

Voice feedback

Exercise performance scoring

Session history

Database integration

Patient progress visualization

Multi-camera pose estimation

Improved pose tracking

Automatic exercise selection





```powershell

cd C:\\Users\\sushm\\Downloads\\NEW

Get-Content README.md





