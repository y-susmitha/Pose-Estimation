import cv2


class Camera:

    def __init__(self, camera_id=0, width=1280, height=720):

        self.camera_id = camera_id

        self.cap = cv2.VideoCapture(camera_id)

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            width
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            height
        )

    def is_opened(self):

        return self.cap.isOpened()

    def read(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def release(self):

        self.cap.release()
