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

- 🎯 Accurate Player Detection via YOLOv8 (custom `best.pt` model)
- 🧠 Real-Time Tracking using Deep SORT
- 🎥 Video Output with Tracked Player IDs
- 🧪 Tested across various frame resolutions
- 💾 Efficient processing with frame-by-frame control

---


## 🛠️ Tech Stack

| Tool          | Description |
|---------------|-------------|
| [YOLOv8](https://github.com/ultralytics/ultralytics) | For object detection of players, ball, and referees |
| [Deep SORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch) | Multi-object tracking algorithm |
| OpenCV        | Video I/O and drawing utilities |
| Python        | Programming language (v3.13.5 used) |

---


🪓 The Grind Behind It
Let me be real here.

This project wasn’t just about code. It was about resilience.

Started at 🕛 12 PM sharp, just an idea and a .pt file.

Faced:

DLL errors

Path errors

YOLO loading issues

0-byte video generation

Frame failures

Deep SORT mismatches

Non-playable .mp4 files

🧠 Spent hours figuring out: Why video isn’t saving? Why is model not loading?

🔧 Even wrote dummy video generators to test OpenCV

📼 Used VS Code extensions, system drag-and-drop, and file system checkers

💪 From frustration to solution, the video finally ran at 11:57 PM — 12 hours later.

💡 This wasn’t just a project. This was a one-day bootcamp on computer vision + debugging.


---


❤️ A Special Note
This project represents a full day of relentless problem-solving. From path bugs, corrupt videos, black screen outputs, NoneType errors, and YOLO quirks — each issue was solved with patience and resolve.

🧑‍💻 From 12 PM to 12 AM, this became more than a submission — it became a testament of never giving up.


---




