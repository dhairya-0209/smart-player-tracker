# ⚽ Smart Player Tracker 🧠🎯
Player re-identification using YOLOv11 and Deep SORT

---

## 📌 Project Overview

**Smart Player Tracker** is an AI-powered sports analytics tool that detects and re-identifies players across frames in a **single video feed** using:

- ✅ YOLOv8 (custom trained model)
- ✅ Deep SORT for object tracking
- ✅ OpenCV for video processing

The project tracks players (class: `person`), assigns unique IDs, and renders the **real-time annotated output** to a `.mp4` file with bounding boxes and player IDs.

---


## 🛠️ Features

-  Accurate Player Detection via YOLOv8 (custom `best.pt` model)
-  Real-Time Tracking using Deep SORT
-  Video Output with Tracked Player IDs
-  Tested across various frame resolutions
-  Efficient processing with frame-by-frame control

---


## 🛠️ Tech Stack

| Tool          | Description |
|---------------|-------------|
| [YOLOv8](https://github.com/ultralytics/ultralytics) | For object detection of players, ball, and referees |
| [Deep SORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch) | Multi-object tracking algorithm |
| OpenCV        | Video I/O and drawing utilities |
| Python        | Programming language (v3.13.5 used) |

---

## 🚀 How to Run This Project
🛠️ Make sure you have:

- Python 3.10+

- best.pt YOLOv8 trained model

- Your input video placed correctly

- (Optional) A virtual environment setup

## 1️⃣ Clone the Repository

Copy
Edit
git clone https://github.com/dhairya-0209/Smart-Player-Tracker.git
cd Smart-Player-Tracker

## 2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate  # For Windows

 OR
 
source venv/bin/activate  # For Mac/Linux

## 3️⃣ Install the Required Libraries

pip install -r requirements.txt

🔄 If requirements.txt is missing, run:

pip install opencv-python ultralytics deep_sort_realtime numpy

## 4️⃣ Add Your YOLOv8 Model

Place your trained YOLO model (best.pt) inside the models/ folder

Smart-Player-Tracker/
└── models/
    └── best.pt
    
## 5️⃣ Add Input Video

- Place your input video in:

Smart-Player-Tracker/src/videos/

- Default video name: 15sec_input_720p.mp4

You can edit the video path in src/main.py if needed.

## 6️⃣ Run the Project

cd src
python main.py

## ✅ Output

Processed video will be saved in:


Smart-Player-Tracker/output/result.mp4

 It will display real-time player tracking with bounding boxes and IDs.

 ---

## 🪓🪓 The Grind Behind It
This wasn’t just about writing code — it was about not giving up.

🕛 Started at 12 PM with just an idea and a .pt model.
Faced everything from:

Faced:

❌ DLL & path errors

❌ YOLO model loading failures

❌ 0-byte .mp4 videos

❌ Frame read errors

❌ Deep SORT mismatches

❌ NoneType object failures

🧠 Spent hours investigating:

- Why is the output video empty?

- Why is nothing displaying on screen?

- Why is YOLO not detecting anything?

🛠️ I even wrote dummy video scripts to test OpenCV's VideoWriter manually.

🔄 Moved files across folders, used VS Code drag-and-drop, checked paths line-by-line.

⚙️ Ran yolo predict to verify model behavior.

And finally...

🎉 The video played successfully at 11:57 PM — 12 hours of complete hustle.

## 🔗 Downloads

| File | Link |
|------|------|
| 🧠 YOLOv8 Model (`best.pt`) | [Download Here](https://drive.google.com/file/d/1X85lL8_jYiaBjclZW6XRk2xczE2gBtPO/view?usp=sharing) |


  
## ❤️ A Note from Me

More than a project — this was a 12-hour sprint of frustration, learning, and triumph.

From broken frames to full-frame tracking...
This build taught me patience, precision, and perseverance.

🧑‍💻 Built with focus, curiosity, and zero breaks.
– Dhairya Bhatia



