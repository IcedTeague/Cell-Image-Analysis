# Cell-Image-Analysis

This is a simple python script that takes in an image of cells on a black background and extracts the boundary of the largest cell.

There are several phases to this process. The image is first converted to greyscale to make the image manipulation easier. It is then converted into a binary image with grey levels lower then 10 being converted to 0 and all other grey levels being converted to 1. Once in this form, a process called connected components is used to identify the number and size of all the cells in the image. Once the largest cell is identified, we remove all other cells so that only the largest is visible. Finally, we dialate the image and subtract the origianl cell from the dialated cell to get our largest cell boundary. This new image is then saved to a jpg.
