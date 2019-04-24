#  Distance_Lu_VIP_2019
python -c 'import distance; distance.get_bounding_box("gt.txt","example1.txt")'

Two functions are present in this implementation of finding the distance of the object from the camera. One of the function is reading the ground truth or object tracking file which has the object frame, the object id, the width, the height of the bounding boxes present in the video. Then the function calls the second function and passes the height and the width of the bounding boxes. This function then calculates the distance of the object being passed in that particular frame. 

find_distance

get_bounding_box
This function does multiple things 



