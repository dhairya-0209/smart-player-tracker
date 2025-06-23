import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import os

# File paths
video_path = r"C:\Users\ACER\Desktop\Smart-Player-Tracker\models\src\videos\15sec_input_720p.mp4"
model_path = r"C:\Users\ACER\Desktop\Smart-Player-Tracker\models\best.pt"
output_path = r"C:\Users\ACER\Desktop\Smart-Player-Tracker\output\test_writer_output.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Check file paths
print("🔍 Checking Paths:")
print("Video exists? ", os.path.exists(video_path))
print("Model exists? ", os.path.exists(model_path))
print("Output folder exists? ", os.path.exists(os.path.dirname(output_path)))

if not all([os.path.exists(video_path), os.path.exists(model_path), os.path.exists(os.path.dirname(output_path))]):
    raise FileNotFoundError("🚫 One or more paths are invalid.")

# Load model and tracker
model = YOLO(model_path)
tracker = DeepSort(max_age=30)

# Load video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError("❌ Failed to open input video.")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"🎥 Video loaded. Width: {width}, Height: {height}, FPS: {fps}")

if width == 0 or height == 0:
    raise ValueError("❌ Invalid video dimensions, check your input file.")

# Create video writer
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Video processing finished.")
        break

    # Predict
    results = model.predict(frame, verbose=False)[0]
    detections = []

    # If detections available
    if results and results.boxes is not None:
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            if int(class_id) == 0 and score > 0.5:
                detections.append([[x1, y1, x2 - x1, y2 - y1], score, 'player'])

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Annotate frame
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        x1, y1, x2, y2 = map(int, track.to_ltrb())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    frame_count += 1
    print(f"🟢 Frame {frame_count} written.")

cap.release()
