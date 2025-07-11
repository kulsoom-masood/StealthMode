import math

class PlayerTracker:
    def __init__(self, distance_threshold=50):
        self.distance_threshold = distance_threshold
        self.next_id = 0
        self.players = {}  # {player_id: (cx, cy, x1, y1, x2, y2)}

    def update(self, detections):
        updated_players = {}
        used_ids = set()

        for x1, y1, x2, y2 in detections:
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            matched_id = None
            min_dist = float('inf')

            for pid, (px, py, *_bbox) in self.players.items():
                dist = math.hypot(px - cx, py - cy)
                if dist < self.distance_threshold and pid not in used_ids and dist < min_dist:
                    matched_id = pid
                    min_dist = dist

            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1

            used_ids.add(matched_id)
            updated_players[matched_id] = (cx, cy, x1, y1, x2, y2)

        self.players = updated_players
        return {pid: (x1, y1, x2, y2) for pid, (_, _, x1, y1, x2, y2) in updated_players.items()}
