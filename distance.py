#import the necessary packages
import numpy as np
import cv2

def find_distance (box_height, first_height,first_dist):
    #width_ratio = float(180*15); #example ratio of known width to known distance  
    #height_ratio = float(490*15); #example ratio of known height to known distance 
    
    #area remains constant 
    #calculating the area of the triangle formed by height and distance to the object as well as width and distance 
    #width_ratio = float(first_width*first_dist);
    height_ratio = float(first_height*first_dist);

    #distance will be constant area / height (or width)
    #calc_width_distance = width_ratio/box_width;#finding distance using the box width 
    calc_height_distance = height_ratio/box_height;#finding the distance using the box height 
    avg_distance = (calc_height_distance);# + calc_width_distance)/2;#averaging the two calculated distances 
    return avg_distance; 


def get_bounding_box (file_name_in, file_name_out): #,calib_file):
    fout = open(file_name_out,"w");#oepning output file to write in 
    count = 1; #keepiung count of how many lines have been read 
    with open(file_name_in,"r") as fin: #reading ground truth file line by line 
        for line in fin:
            if(line == '\n'): #in case of blank lines 
                continue;
            chars = [0]*10;
            chars = line.split(",",9); #reading the file lines per number 

            #width = float(chars[4]); 
            height = float(chars[5]);
            frame = int(chars[0]);
            id_track = int(chars[1]);
            #scale factor will have to be determined by taking the size of a bounding box around one person 
            #finding the distance of the person from the camera, and then moving the persona nd finding the same two 
            # paramters and relation between them will give scale factor 
            #scale factor will vary for every scenario and every camera 
            
            
            #scale_factor = calib_cam(calib_file);
            
            scale_factor = 1.25; # example scale factor for changing pixel distance to actual distance 
            #width *= scale_factor; 
            #height *= scale_factor;

            #if the first line is being read, store the height and width to calculate ratio and pass with every run
            if(count == 1):
                first_height = height;
                #first_width = width;
            
            #calling function to calculate distance
            distance = find_distance(abs(float(height)), abs(float(first_height)),15); #the contant 15 will have to be replaced by the physical distance in ft distance of the person in the first frame with id 1
            #distance = distance * scale_factor;
            #writing into file: frame, id, distance
            fout.write("%d,%d,%lf\n" %(frame, id_track,distance));
            count = count+1;
            #print(distance);
    fin.close();
    fout.close();

def calib_cam (filename_in):
    count = 1;
    i = 0;
    with open(filename_in,"r") as calib_file: #reading ground truth file line by line
             for line in calib_file:
                if(line == '\n'): #in case of blank lines
                    continue;

                if(count == 1):
                    chars = line.split(",",2); #reading the file lines per number                
                    height1 = float(chars[0]); 
                    distance1 = int(chars[1]);
                    area1 = height1*distance1;
                    count = 2;
                else: 
                    chars = line.split(",",2); #reading the file lines per number
                    height2 = float(chars[0]);
                    distance2 = int(chars[1]);
                    calc_dist = height1*distance1/height2;
                    factor = factor + (distance2/calc_dist);
                    count = 1;

    factor = factor / i; #taking an average of the factors 
    calib_file.close();
    return factor; 
                
                


