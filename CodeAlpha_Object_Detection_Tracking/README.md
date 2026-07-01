# CodeAlpha: Object Detection and Tracking

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green.svg)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-orange)

A real-time **Object Detection and Tracking application** built using Python, OpenCV, and YOLOv8. This system takes a live camera feed, detects objects frame-by-frame, and utilizes advanced multi-object tracking to assign and maintain unique persistent IDs for every object in motion. Developed as part of the **CodeAlpha Artificial Intelligence Internship**.

---

## 🚀 Features

- **Real-Time Video Processing:** Captures and feeds frames directly from an active webcam or standalone local video file.
- **State-of-the-Art Detection:** Integrates a pre-trained YOLOv8 neural network optimized for fast inference frame rates.
- **Persistent Object Tracking:** Applies advanced tracking mechanics (`BoT-SORT` / `ByteTrack`) to uniquely identify moving targets across frames.
- **Dynamic Graphical Overlays:** Automatically visualizes active bounding boxes, target class text names, confidence scoring percentages, and tracking index numbers.
- **Graceful Shutdown UI:** Robust application loop handler prevents system freezes when manually closing the GUI frame window.

---

## 📦 Installation & Quickstart

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)adityaRALPH/CodeAlpha_Object_Detection_Tracking.git
   cd CodeAlpha_Object_Detection_Tracking