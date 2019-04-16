#import the necessary packages
import numpy as np
import cv2

def find_distance (box_width, box_height):
    width_ratio = 12; #example ratio of known width to known distance  
    height_ratio = 12; #example ratio of known height to known distance 

    calc_width_distance = box_width*width_ratio;#finding distance using the box width 
    calc_height_distance = box_height*height_ratio;#finding the distance using the box height 
    avg_distance = (calc_width_distance + calc_height_distance)/2;#averaging the two calculated distances 
    return avg_distance; 


def get_bounding_box (file_name):
    with open(filename,"r") as fin:
        for line in fin:
            #read width
            characteristics = line.split(",");
            width = float(characteristics[2]);
            height = float(characteristics[3]);
            #read height 
            #read object id and frame number 
            distance = find_distance(abs(float(width)),abs(float(height)));
            #write object id, frame number and distance into file 
            print(distance);
    fin.close();



##############################################################################################333
def find_marker(image):
  # convert the image to grayscale, blur it, and detect edges
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (5, 5), 0)
  edged = cv2.Canny(gray, 35, 125)
  
  # find the contours in the edged image and keep the largest one;
  # we'll assume that this is our piece of paper in the image
  (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  c = max(cnts, key = cv2.contourArea)
  
  # compute the bounding box of the of the paper region and return it
  return cv2.minAreaRect(c)
 
def distance_to_camera(knownWidth, focalLength, perWidth):
   # compute and return the distance from the maker to the camera
   return (knownWidth * focalLength) / perWidth
   # initialize the known distance from the camera to the object, which
   # in this case is 24 inches
   
   KNOWN_DISTANCE = 24.0
   # initialize the known object width, which in this case, the piece of
   # paper is 12 inches wide
   KNOWN_WIDTH = 11.0
   # initialize the list of images that we'll be using
   IMAGE_PATHS = ["images/1.png", "images/1.png", "images/3.png"]
   # load the furst image that contains an object that is KNOWN TO BE 2 feet
   # from our camera, then find the paper marker in the image, and initialize
   # the focal length
   image = cv2.imread(IMAGE_PATHS[0])
   marker = find_marker(image)
   focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
   # loop over the images
   for imagePath in IMAGE_PATHS:
   # load the image, find the marker in the image, then compute the
   # distance to the marker from the camera
     image = cv2.imread(imagePath)
     marker = find_marker(image)
     inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
   
   # draw a bounding box around the image and display it
   box = np.int0(cv2.cv.BoxPoints(marker))
   cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
   cv2.putText(image, "%.2fft" % (inches / 12),(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
           2.0, (0, 255, 0), 3)
   cv2.imshow("image", image)
   cv2.waitKey(0)
