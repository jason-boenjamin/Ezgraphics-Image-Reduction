# Jason Boenjamin
# Professor Ashraf
# Lab 7 Chapter 5
# February 15th, 2023
from ezgraphics import GraphicsImage

# creates a negative version of the image
def createNegative(image):
  width = image.width()
  height = image.height()

  newImage = GraphicsImage(width, height)
  for row in range(height) :
    for col in range(width) :
      red = image.getRed(row,col)
      green = image.getGreen(row,col)
      blue = image.getBlue(row,col)

      newRed = 255- red
      newGreen = 255 - green
      newBlue = 255 - blue
      
      newImage.setPixel(row,col,newRed,newGreen,newBlue)

  return newImage

#from p37,creates a border
def createBorder(window, image, colorname) :
  width = image.width()
  height = image.height()

  newImage = GraphicsImage(width, height)

  newCan = window.canvas()
  newCan.setLineWidth(5)
  newCan.setOutline(colorname)
  newCan.drawRectangle(0,0, width, height)
  return newImage

  #reduces the image in half
def reduceHalf(window,image) :
  
  width = image.width()
  height = image.height()

  newImage = GraphicsImage(width, height)
  #count = 1
  for row in range(height) :

    for col in range(width) :
      if row % 2 != 1 or col % 2 != 1:
        #newImage.setPixel(row, col, image.getPixel(row * 2, col * 2))
        newImage.setPixel(row//2, col//2, image.getRed(row,col),image.getGreen(row,col),image.getBlue(row,col))
    
  return newImage
      