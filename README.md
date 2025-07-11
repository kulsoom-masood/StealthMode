# StealthMode
# Player Re-Identification – Internship Assignment Submission

This project is a submission for the AI Internship assignment focused on solving the player re-identification problem in a short soccer video.

---

## Objective

The goal was to detect players in a 15-second video and assign unique IDs to them. These IDs should remain consistent across the video, even if players temporarily leave the frame and return later.

---

## My Approach

1. I used the provided YOLOv11 model to detect players in each frame of the video.
2. I implemented a custom tracking system that assigns and maintains player IDs.
3. This tracking is based on comparing player positions (centroids) between frames.
4. The logic ensures that if a player leaves the frame and comes back, they are re-identified using distance-based matching.

---

## How It Works

- The YOLO model runs on each frame and outputs bounding boxes for detected objects.
- I filter these results to only include players.
- For each player, I compute the center point of their bounding box.
- The tracking system compares current detections to previously tracked players.
- If a detected player is close to a previously seen one, the same ID is assigned.
- If it’s a new player (or someone who re-enters after a while), a new ID is given.

This logic is simple but works well in controlled clips like the one provided.

---

## What I Built

- A complete working pipeline to read the input video, detect players, assign IDs, and save an output video with the player IDs annotated on screen.
- The tracking system is fully custom and does not rely on prebuilt libraries like DeepSORT.
- It can be easily extended or replaced with a more advanced method later.

---

## Challenges

- Tracking based only on position is not always reliable, especially when players are close to each other.
- Without using jersey numbers or appearance-based features, it’s hard to be sure if a player is the same when re-entering.
- Players who leave the frame for too long may be treated as new, depending on the threshold set.

---

## What Could Be Improved

- Incorporate jersey number recognition to help with re-identification.
- Use appearance features or embeddings to compare players beyond just their position.
- Integrate a more advanced tracker like DeepSORT for better performance in longer or more complex videos.

---

## Summary

This solution demonstrates a simple but effective way to detect and re-identify players using the provided model. It focuses on logic building, custom tracking, and creating a working pipeline rather than relying on heavy external tools. It’s built with clarity and extendability in mind.

Thank you for reviewing my work.
