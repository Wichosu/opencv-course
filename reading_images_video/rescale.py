import cv2 as cv

#img = cv.imread('photos/cat.jpeg')
#cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(capture, width, height):
  #Live video
    capture.set(3, width)
    capture.set(4, height)

#img_rescale = rescaleFrame(img)
#cv.imshow('Photo rescale', img_rescale)

#cv.waitKey(0)

#capture = cv.VideoCapture('videos/video.webm')

#while True:
#    isTrue, frame = capture.read()
#
 #   frame_resized = rescaleFrame(frame, scale=0.5)
#
 #   cv.imshow('Video', frame)
  #  cv.imshow('Video Rescaled', frame_resized)

#    if cv.waitKey(20) & 0xFF==ord('d'):
 #       break

#capture.release()
#cv.destroyAllWindows()