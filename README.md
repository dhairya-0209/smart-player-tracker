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


## 🪓 The Grind Behind It
Let me be real here.

This project wasn’t just about code. It was about resilience.

🕛 Started at 12 PM sharp, with just an idea and a .pt file.

Faced:

❌ DLL errors

❌ Path errors

❌ YOLO model loading failures

❌ 0-byte .mp4 videos

❌ Frame read errors

❌ Deep SORT mismatches

❌ NoneType object failures

❌ Files not refreshing in VS Code

🧠 Spent hours investigating:

- Why is the output video empty?

- Why is nothing displaying on screen?

- Why is YOLO not detecting anything?

🛠️ I even wrote dummy video scripts to test OpenCV's VideoWriter manually.

🔄 Moved files across folders, used VS Code drag-and-drop, checked paths line-by-line.

⚙️ Ran yolo predict to verify model behavior.

And finally...

🎉 The video played successfully at 11:57 PM — 12 hours of complete hustle.


  
## ❤️ A Special Note

This wasn’t just a project.
This was a one-day bootcamp in Computer Vision, Debugging, and Determination.

From broken paths and corrupt videos
To finally watching the player tracking happen live on screen,
This became more than a submission —
It became a personal milestone.

🧑‍💻 Built by Dhairya Bhatia — fueled by coffee, curiosity, and commitment.





