from PIL import Image

# imports `one.jpg` image to be manipulated
img = Image.open("one.jpg")
def crop():
    with Image.open("one.jpg") as image:
        x, y = image.size
        # width is longer
        if x > y : 
            area = (0,0,y,y)
            output = img.crop(area)
            # saves the cropped 1:1 image with the original name, replacing it
            output.save("one.jpg")
            size = [256,256]
            # resizes the image into 256px x 256px format 
            resize = output.resize(size)
            # saves the resized image with the original name, replacing it
            resize.save("one.jpg")
        # width & height are the same (1:1 ratio)
        elif x == y:
            output = img
            size = [256,256]
            resize = output.resize(size)
            resize.save("one.jpg")
        # height is longer
        else :
            print("height is large")
            area = (0,0,x,x)
            output = img.crop(area)
            output.save("one.jpg")
            size = [256,256]
            resize = output.resize(size)
            resize.save("one.jpg")
    return output

def main():
    crop()

main()


