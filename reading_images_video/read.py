import cv2 as cv

#img = cv.imread('photos/cat.jpeg')

#cv.imshow('Cat', img)

#Reading videos
#Todo Add a video to videos folder
capture = cv.VideoCapture('videos/video.webm')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)