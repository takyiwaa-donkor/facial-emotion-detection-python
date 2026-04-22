**Facial Emotion Detection System – Python, DeepFace and OpenCV**

A modular, Python‑based emotion recognition system designed to automatically detect emotional states from facial images.
The system supports both single‑image detection and batch processing, producing structured outputs, confidence scores, categorized folders, and persistent CSV logs.
It was developed across three phases — Conception → Development → Finalisation — with a strong focus on architecture, testing, and real‑world applicability.

**Overview**
This project addresses a key challenge in marketing and user‑experience research:
How can we understand emotional reactions quickly, objectively, and at scale?

Traditional surveys and interviews often fail to capture spontaneous emotional responses.
This system provides a data‑driven, automated alternative, using computer vision and deep learning to classify emotions such as:

- Angry

- Happy

- Sad

- Neutral

- Surprise

- Fear

- Disgust

The system outputs:

- Predicted emotion

- Confidence score

- Visual display

- CSV log entry

- Categorized image copy

**Key Features**

Emotion Detection
- Detect emotion from a single image

- Detect emotions from an entire folder

- Confidence score for each prediction

- Visual output using Matplotlib

Structured Output
- CSV logging of all detections

- Categorized folders for each emotion

- Timestamped and confidence‑tagged filenames

CLI Interface
- Simple 4‑option menu

- User‑friendly workflow

- No technical expertise required

Performance
- Average processing time: ~0.23 seconds per image

- Stable predictions across lighting, angles, and expression variations

**System Architecture**
The system follows a modular, layered architecture:

User
  ↓
CLI Interface (main.py)
  ↓
Emotion Detection Service (services/emotion_detector.py)
  ↓
Preprocessing & Utilities (utils/)
  ↓
Persistence Layer (persistence/)
  ↓
CSV Logging + Categorized Output Folders
  ↓
DeepFace Model (TensorFlow backend)

Why this architecture works
- Clear separation of concerns

- Easy to maintain and extend

- Supports future GUI or web integration

- Enables independent testing of each layer

**Frameworks and Tools**
Deep Learning and Emotion Recognition
- DeepFace (TensorFlow backend)
- Pretrained CNN models for emotion classification

Image Processing
- OpenCV for image loading, preprocessing, and color conversion
- Matplotlib for visual output

Data Handling & File Management
- CSV for persistent logging
- OS and Shutil for folder creation and categorized storage

**Repository Structure**

emotion-detection-system/
│
├── application/
│   └── cli.py                     # Command-line interface
│
├── services/
│   └── emotion_detector.py        # DeepFace model inference
│
├── domain/
│   └── models.py                  # Domain entities (if applicable)
│
├── persistence/
│   └── csv_logger.py              # CSV logging utilities
│
├── utils/
│   ├── image_loader.py            # OpenCV loading + preprocessing
│   └── file_utils.py              # Path handling, folder creation
│
├── categorized_results/           # Output folders (angry, happy, etc.)
│
├── test_images/                   # Input dataset for testing
│
├── tests/
│   ├── test_emotion_detector.py
│   ├── test_batch_detection.py
│   ├── test_performance.py
│   └── test_preprocessing.py
│
├── docs/
│   ├── FacialEmotionDetection_Abstract.pdf
│   ├── FacialEmotionDetection_ConceptionPhase.pdf
│   ├── FacialEmotionDetection_DevelopmentPhase.pdf
│   ├── FacialEmotionDetection_FinalisationPhase.pdf
│   └── FacialEmotionDetection_UserManual.pdf
│
├── Screenshots/                   # CLI and output screenshots
│
├── main.py                        # Application entry point
├── results.csv                    # Logged detections
├── requirements.txt               # Dependencies
├── pytest.ini                     # Pytest configuration
└── README.md                      # Project documentation

**Detection Pipeline**

1. Load image with OpenCV

2. Convert BGR → RGB

3. Run DeepFace emotion model

4. Extract emotion + confidence

5. Display result with Matplotlib

6. Log to CSV

7. Copy image to categorized folder

This pipeline is lightweight, efficient, and easy to extend.

**Testing Strategy**

Manual Testing
- Single image detection

- Batch folder detection

- Error handling (invalid paths, missing files)

Automated Testing (pytest)
- Performance tests

- Preprocessing validation

- Emotion detection accuracy

- CSV logging

- Batch processing

Performance Results
- ~0.23 seconds per image

- All tests passed

- Stable predictions across multiple runs

**Progress vs Original Plan**
Planned (Phase 1)
- Basic emotion detection

- Single image input

- Simple console output

Achieved (Final Version)
- Full CLI menu

- Single + batch processing

- Categorized output folders

- CSV logging

- Image visualization

- Performance testing

- Modular architecture

- Extensive documentation

The system evolved from a simple detector into a multi‑feature emotion analysis platform.

**Future Improvements**
- Real‑time webcam detection

- GUI (Tkinter/PyQt)

- Web interface (Flask/FastAPI)

- Database storage

- Multi‑face detection

- Advanced models (Vision Transformers)
