Thank you for using Image Invert! This is a program which allows you to only invert specific pixels of an image.
Use your web browser to find a url to set as the image. You can also use locally saved images by doing the following:

1. Make a copy of the image.
2. Move the copy to this folder (ImageInvert)
3. Rename the image to 'image.png'
4. Run the script and type 'local' for the url

You can also invert the whole image by not specifying a color.

How it works:

1. User inputs image url/local
2. Use the requests module to open contents as an image.
3. User inputs color choice or leaves it blank.
4. Create regex pattern to see if user typed a color name or RGB value (r'\d+, \d+, \d+|\(\d+, \d+, \d+\))
5. Map list into tuple.
6. If color is left blank, invert image, save it as 'result.png' and display
7. If color is not blank, create an inverted copy of the image and save as 'invert.png'.
8. Use NumPy to create arrays of both the original image, and the inverted copy.
9. Use Numpy.where() to check if each pixel matches the target color, if it does replace said pixel with a pixel from the inverted copy.
10. Use Image.fromarray() to create an image from the result array. Save as 'result.png'.