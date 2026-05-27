# image-manipulation-pipeline

### General information
This is a simple image manipulation tool currently only useable through a limited set of doable tasks with a exact sequence of image modification steps involved. Currently the script only checks for the dimensions of a image and converts it to a 1:1 ratio if not already after which it resizes that image to the proportion of 256px x 256px and saves it.

### steps involved
- a image named `one.jpg` must be with the same directory as the `main.py` file for it to be able to access and modify it.
- then the script is to be run simply and the result is to be viewed.

### internal process
- First the scripts searches and opens a image file named `one.jpg`.
- Then it checks for the image's dimensions.
    - If the image is already in a 1:1 ratio in dimension, it moves on to the resizing process.
    - If the width of the image is longer than its height, it decreases the width size to the exact value of the height. Effectively converting it to a image with 1:1 proportions.
    - Likewise for when its width is longer than its height the process is flipped to make a 1:1 image.
- Then it takes the output image from any of the scenario's and resizes the image to a 256px x 256px dimensional format which then is saved as the original image.

### Note
    provided image in the directory is a sample image to be used as testing for the project. It can be tested with any other image as long as the name remains the same!