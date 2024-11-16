import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)  # Initialize the SSD-MobileNet v2 model with a detection threshold
camera = jetson.utils.videoSource("/dev/video0")  # '/dev/video0'for V4L2
# image_path = "/home/nvidia/jetson-inference/python/1.jpg"
# img = jetson.utils.loadimage(image_path)
# detections = net.Detect(img)
display = jetson.utils.videoOutput("display://0")  # 'my_video.mp4'for file

# if img is not None and detections is not None:
#    # render the image with detections
#    display.Render(img)
#    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
#    for detection in detections:
#         print(f"ClassID: {detection.ClassID}")
#         print(f"Confidence: {detection.Confidence}")
#         print(f"Left: {detection.Left}")
#         print(f"Right: {detection.Right}")
#         print(f"Bottom: {detection.Bottom}")
#         print(f"Width: {detection.Width}")
#         print(f"Height: {detection.Height}")
#         print(f"Area: {detection.Area}")
#         print(f"Center: ({detection.Center[0]},{detection.Center[1]})")

# display.Close() 


while display.IsStreaming():  # main loop will go here
      img = camera.Capture()
#      print(detections)
      if img is None:  #capture timeout
              continue

      detections = net.Detect(img)
      print(detections[0])

      display.Render(img)
      display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))







