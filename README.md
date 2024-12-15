# traffic-light-detection
This repository contains a traffic light detection system that uses YOLO and TensorFlow along with ONNX for color detection. The project aims to detect traffic lights in images or video streams and classify their state (go(green) stop (red, yellow) and unknown) to assist in automated driving or monitoring systems.

## Features
Object Detection: Uses YOLO to detect traffic lights in real-time.

Color Classification: Leverages TensorFlow and ONNX to classify the detected traffic light's color.

Flexible Deployment: Supports processing images, videos, or live streams.
## Requirements

To set up and run the project, ensure you have the following:

- Python 3.8+
- Required Python packages (see `requirements.txt`):
  - ultralytics
  - tensorflow
  - onnxruntime
  - numpy
  - opencv-python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vusallyv/traffic-light-detection.git
   cd traffic-light-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


