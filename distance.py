#import the necessary packages
import numpy as np
import cv2

def find_distance (box_width, box_height, first_width, first_height,first_dist):
    #width_ratio = float(180*15); #example ratio of known width to known distance  
    #height_ratio = float(490*15); #example ratio of known height to known distance 
    
    #area remains constant 
    #calculating the area of the triangle formed by height and distance to the object as well as width and distance 
    width_ratio = float(first_width*first_dist);
    height_ratio = float(first_height*first_dist);

    #distance will be constant area / height (or width)
    calc_width_distance = width_ratio/box_width;#finding distance using the box width 
    calc_height_distance = height_ratio/box_height;#finding the distance using the box height 
    avg_distance = (calc_width_distance + calc_height_distance)/2;#averaging the two calculated distances 
    return avg_distance; 


def get_bounding_box (file_name_in, file_name_out):
    fout = open(file_name_out,"w");#oepning output file to write in 
    count = 1; #keepiung count of how many lines have been read 
    with open(file_name_in,"r") as fin: #reading ground truth file line by line 
        for line in fin:
            if(line == '\n'): #in case of blank lines 
                continue;
            chars = [0]*10;
            chars = line.split(",",9); #reading the file lines per number 

            width = float(chars[4]); 
            height = float(chars[5]);
            frame = int(chars[0]);
            id_track = int(chars[1]);
            
            scale_factor = 1; # example scale factor for changing pixel distance to actual distance 
            width *= scale_factor; 
            height *= scale_factor;

            #if the first line is being read, store the height and width to calculate ratio and pass with every run
            if(count == 1):
                first_height = height;
                first_width = width;
            
            #calling function to calculate distance
            distance = find_distance(abs(float(width)),abs(float(height)),abs(float(first_width)), abs(float(first_height)),15); #the contant 15 will have to be replaced by the physical distance in ft distance of the person in the first frame with id 1
            
            #writing into file: frame, id, distance
            fout.write("%d,%d,%lf\n" %(frame, id_track,distance));
            count = count+1;
            #print(distance);
    fin.close();
    fout.close();


