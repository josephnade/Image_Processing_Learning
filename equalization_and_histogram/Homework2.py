'''
171805020
Yusuf AKIN
Image Processing - Homework2
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

class image_graphs:
    def __init__ (self, image,histogram):
        self.image = image
        self.histogram = histogram
    
    def histogram_grapher(self,path_name,graph_name):
        for k in range(self.image.shape[0]):
            for l in range(self.image.shape[1]):
                pixel_value = self.image[k,l]
                self.histogram[pixel_value]+=1
        plt.title(graph_name)
        plt.bar(np.arange(len(self.histogram)),self.histogram)
        plt.xlabel("Gray Level")
        plt.ylabel("Number of Pixel")
        plt.savefig(path_name)
        equal_image = cv2.imread(path_name)
        cv2.imshow(graph_name,equal_image)
        return self.histogram
    
    
    def histogram_equalization(self,path_name,graph_name):
        GL=255
        equal_histogram=np.zeros_like(self.histogram)
        equal_image=np.zeros_like(self.image)
        for i in range(len(self.histogram)):
            equal_histogram[i]=int(GL*np.sum(self.histogram[0:i]))
        
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                px_vl=self.image[x, y]
                equal_image[x, y]=equal_histogram[px_vl]
        
        plt.title(graph_name)
        plt.bar(np.arange(len(equal_histogram)),equal_histogram)
        plt.xlabel("Gray Level")
        plt.ylabel("Number of Pixel")
        plt.savefig(path_name)
        equal_image = cv2.imread(path_name)
        cv2.imshow(graph_name,equal_image)
        return self.histogram
       
    def specification(self,image2,path_name,graph_name):
        image_list=[self.image, image2]
        for i in range(2):
            GL=255
            equal_histogram=np.zeros_like(self.histogram)
            equal_image=np.zeros_like(image_list[i])
            for k in range(len(self.histogram)):
                equal_histogram[k]=int((GL*np.sum(self.histogram[0:k]))/(image_list[i].shape[0]*image_list[i].shape[1]))
            
            for x in range(image_list[i].shape[0]):
                for y in range(image_list[i].shape[1]):
                    pixel_value=image_list[i][x, y]
                    equal_image[x, y]=equal_histogram[pixel_value]
                

        plt.title(graph_name)
        plt.bar(np.arange(len(equal_histogram)),equal_histogram)
        plt.xlabel("Gray Level")
        plt.ylabel("Number of Pixel")
        plt.savefig(path_name)
        img = cv2.imread(path_name)
        cv2.imshow("Specification",img)
        
    def image_joiner(self,path_name1, path_name2):
        image_1=cv2.imread(path_name1)
        image_2=cv2.imread(path_name2)
        joined_img=cv2.add(image_1,image_2)
        cv2.imwrite("Joined_img.png",joined_img)
        cv2.imshow("Joined Image",joined_img)
    
    
image = cv2.imread("image.png")   
image2 = cv2.imread("image2.png")
hist_zeros = np.zeros([256])


first_hist = image_graphs(image, hist_zeros)
histogram = first_hist.histogram_grapher("first_histogram.png","First Histogram")

second_hist = image_graphs(image2, hist_zeros)
histogram = second_hist.histogram_grapher("second_histogram.png","Second Histogram")



first_equal = image_graphs(image, histogram)
first_equalization = first_equal.histogram_equalization("first_equalization.png","First Equalization")
second_equal = image_graphs(image,first_equalization)
second_equalization = second_equal.histogram_equalization("second_equalization.png", "Second Equalization")


specification = image_graphs(image, histogram)
specification.specification(image2,"specification.png","Specification")
specification.image_joiner("image.png","image2.png")

"""
Questions - Answers :
    ------------------------------------------------------------------------------------
    + Two images have same histogram or Histogram is a unique representation of an image.
    
    - Two image can have same histogram for example vertical half white and half white
    square and horizontal the same square have same histogram if pixel number is same.
    Histogram graphic just says which tone we mostly have but do not say where they are.
    ------------------------------------------------------------------------------------
    + Can we reconstruct image from histogram?
    
    - As I said above histogram does not says location of pixels and histogram is not unique
    representation of an image
    ------------------------------------------------------------------------------------
    + Second pass of Histogram Equalization will produce exactly the same result as the first pass

    - As we saw on the code part first and second equalization is exactly same results.
    ------------------------------------------------------------------------------------
    + By seeing histogram can we guess nature of the image
    - We can estimate nature of the image by seeing histogram. 
    X label tells us color tone and Y label tells the intensity.
    On the graph, there are mostly left side pixel (close to 0) data you can estimate this image darker. 
    When you get close the right side (255) there are bright one.
    ------------------------------------------------------------------------------------
"""