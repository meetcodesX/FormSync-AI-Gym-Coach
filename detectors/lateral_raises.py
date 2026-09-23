from core.base_exercise import BaseExercise

class LateralRaiseDetector(BaseExercise):
    DOWN_THRESHOLD = 30
    UP_THRESHOLD = 70
    MIN_VISIBILITY = 0.7

    LEFT_HIP = 23
    LEFT_SHOULDER = 11
    LEFT_ELBOW = 13

    RIGHT_HIP = 24
    RIGHT_SHOULDER = 12
    RIGHT_ELBOW = 14

    def __init__(self):
        super().__init__()

    def reset(self):
        self.reps = 0
        self.stage = None

    def process(self, landmarks):
        left_shoulder_angle = self.calculate_angle(
            self.get_point(landmarks, self.LEFT_HIP),
            self.get_point(landmarks, self.LEFT_SHOULDER),
            self.get_point(landmarks, self.LEFT_ELBOW)
        )

        right_shoulder_angle = self.calculate_angle(
            self.get_point(landmarks, self.RIGHT_HIP),
            self.get_point(landmarks, self.RIGHT_SHOULDER),
            self.get_point(landmarks, self.RIGHT_ELBOW)
        )

        left_vis = landmarks[self.LEFT_SHOULDER].visibility
        right_vis = landmarks[self.RIGHT_SHOULDER].visibility

        if left_vis >= right_vis:
            shoulder_angle = left_shoulder_angle
            hip_idx, shoulder_idx, elbow_idx = self.LEFT_HIP, self.LEFT_SHOULDER, self.LEFT_ELBOW
        else:
            shoulder_angle = right_shoulder_angle
            hip_idx, shoulder_idx, elbow_idx = self.RIGHT_HIP, self.RIGHT_SHOULDER, self.RIGHT_ELBOW

        key_landmark_visible = landmarks[hip_idx].visibility >= self.MIN_VISIBILITY and landmarks[shoulder_idx].visibility >= self.MIN_VISIBILITY and landmarks[elbow_idx].visibility >= self.MIN_VISIBILITY

        if key_landmark_visible:
            if shoulder_angle <= self.DOWN_THRESHOLD:
                self.stage = "down"

            if shoulder_angle >= self.UP_THRESHOLD and self.stage == "down":
                self.stage = "up"
                self.reps += 1

        if self.stage == "down":
            raise_status = "ARMS DOWN"
        elif self.stage == "up":
            raise_status = "GOOD HEIGHT" if shoulder_angle >= self.UP_THRESHOLD else "LOW"
        else:
            raise_status = "N/A"

        return {
            "reps": self.reps,
            "shoulder_angle": int(shoulder_angle),
            "raise_status": raise_status
        }