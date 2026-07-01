import cv2
from ultralytics import YOLO

def main():
    print("Loading pre-trained YOLOv8 model...")
    model = YOLO("yolov8n.pt")  

    # Set up real-time video input
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam or video source.")
        return

    window_name = "CodeAlpha - Object Detection & Tracking"
    # Create a named window so we can track its status explicitly
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    print("Press 'q' or click the 'X' button to exit the application safely.")

    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            print("Video stream ended or frame failed to read.")
            break

        # Apply Object Detection AND Tracking
        results = model.track(frame, persist=True, verbose=False)

        # Render visual bounding boxes
        annotated_frame = results[0].plot()

        # Display the output
        cv2.imshow(window_name, annotated_frame)

        # --- FIXES THE GLITCH HERE ---
        # 1. Check if 'q' is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
            
        # 2. Check if the user clicked the window's close 'X' button
        # WND_PROP_VISIBLE returns 0.0 if the window has been closed manually
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    # Clean up and completely release system resources
    print("Releasing camera and closing windows...")
    cap.release()
    cv2.destroyAllWindows()
    print("Application closed safely.")

if __name__ == "__main__":
    main()