from skimage import io,color,filters,morphology,measure
import matplotlib.pyplot as plt
import numpy as np

#Calculates the largest cell and returns it's boundary
def cell_processing(image):
    #Converts image to greyscale
    grey_image = color.rgb2gray(image)

    grey_image = (grey_image * 255).astype(np.uint8)

    plt.imshow(grey_image, cmap="gray")
    plt.show()

    #Thresholds image, any value over 10 is turned white (which marks a cell)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if grey_image[x,y] < 10:
                grey_image[x,y] = 0
            elif grey_image[x,y] >= 10:
                grey_image[x,y] = 255
    
    plt.imshow(grey_image, cmap="gray")
    plt.show()

    #passes binary cell image through connected components function
    #each pixel value is now labeld with the object index that the pixel is a part of
    labeled_cells = measure.label(grey_image)
    cell_label = 1
    largest_cell_label = 0
    largest_cell = 0
    largest_cell_size = 0

    #prints cell sizes and selects the largest cell
    #a threshold of 500 is used to remove noise from connected components
    for prop in measure.regionprops(labeled_cells):
        if prop.area >=500:
            print("Cell: "+str(cell_label)+"-("+str(prop.area)+")")
            if largest_cell_size == 0 or prop.area > largest_cell_size:
                largest_cell_label = cell_label
                largest_cell = prop.label
                largest_cell_size = prop.area
            cell_label += 1
    
    print("\nLargest Cell: "+str(largest_cell_label)+"-("+str(largest_cell_size)+")")

    #creates a new binary image of the largest cell
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if labeled_cells[x,y] == largest_cell:
                labeled_cells[x,y] = 255
            else:
                labeled_cells[x,y] = 0

    plt.imshow(labeled_cells, cmap="gray")
    plt.show()

    #creates a dialated image of the cells and subtracts the original from the dialation
    #to get the boundary of the cell
    cell_dilation = morphology.binary_dilation(labeled_cells,morphology.disk(1))

    plt.imshow(cell_dilation, cmap="gray")
    plt.show()

    boundary_image = np.clip(cell_dilation - labeled_cells,0,255)
    
    return boundary_image
            

cell_image_raw = "cell_image.jpg"
cell_image = io.imread(cell_image_raw)
plt.imshow(cell_image, cmap="gray")
plt.imsave('cell_image.jpg', cell_image, cmap='gray')
plt.show()

largest_cell = cell_processing(cell_image)
plt.imshow(largest_cell, cmap="gray")
plt.imsave('largest_cell.jpg', largest_cell, cmap='gray')
plt.show()