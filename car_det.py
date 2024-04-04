from object_detector import ObjectDetector


ojb = ObjectDetector(
    weights ="cars.weights"
    cfg = "yolov4-custom.cfg"
)

img = ojb.object_detector("")