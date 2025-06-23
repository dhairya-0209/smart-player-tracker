# ⚽ Smart Player Tracker 🧠🎯
Player re-identification using YOLOv11 and Deep SORT

---

## 🚀 Project Summary

This project is built to **detect, identify, and track players and referees** in a football match using a pre-trained YOLOv8 model combined with Deep SORT tracking. It processes video input frame-by-frame, draws bounding boxes, and assigns consistent IDs to each individual — all saved into a resulting video.

This wasn't just a project, it was a **marathon of determination, learning, debugging, and never giving up**. From 12 PM to 12 AM, this tracker was brought to life with sheer passion.

---

## 📽️ Demo Preview

> *Video Coming Soon (check `output/result.mp4`)*

⚠️ If you'd like to see this system live in action — [clone this repo](#-clone-this-repository), install dependencies, and test with your own video files!

---

## 🛠️ Tech Stack

| Tool          | Description |
|---------------|-------------|
| [YOLOv8](https://github.com/ultralytics/ultralytics) | For object detection of players, ball, and referees |
| [Deep SORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch) | Multi-object tracking algorithm |
| OpenCV        | Video I/O and drawing utilities |
| Python        | Programming language (v3.13.5 used) |

---

## 📂 Folder Structure


A cutting-edge sports analytics project that combines the power of **YOLOv8** and **Deep SORT** to re-identify and track football players in a single video feed, frame by frame.


Smart-Player-Tracker/
├── models/
│ ├── best.pt # Trained YOLOv8 model
│ └── src/
│ ├── main.py # Main execution script
│ └── videos/ # Input video folder
├── output/
│ └── result.mp4 # Output with tracking annotations
├── requirements/
│ └── requirements.txt # Python dependencies
├── report.md # Report (optional)
└── read.md # This file 📄


---

## 🔧 How to Run

### 1️⃣ Clone This Repository


git clone https://github.com/<dhairya-0209>/Smart-Player-Tracker.git
cd Smart-Player-Tracker 
---







