import cv2
from ultralytics import YOLO
from tracker import PlayerTracker

# Load YOLO model
model = YOLO("model/best.pt")

# Initialize the tracker
tracker = PlayerTracker(distance_threshold=60)

# Open video
cap = cv2.VideoCapture("input/15sec_input_720p.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output/output_with_ids.mp4", fourcc, fps, (width, height))

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        cls = int(cls)
        if cls == 2:  # Only track players
            x1, y1, x2, y2 = map(int, box)
            detections.append((x1, y1, x2, y2))

    tracked_players = tracker.update(detections)

    for player_id, (x1, y1, x2, y2) in tracked_players.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {player_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
