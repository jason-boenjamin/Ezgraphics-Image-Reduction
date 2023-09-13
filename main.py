# Jason Boenjamin
# Professor Ashraf
# Lab 7 Chapter 5
# February 15th, 2023

from ezgraphics import GraphicsWindow, GraphicsImage
import processimg

def main() :
  win = GraphicsWindow(1000,1000)
  can = win.canvas()
  win.setTitle("APPA")
  image = GraphicsImage("appastanding.png")
  print("reduces image in half")
  can.drawImage(processimg.reduceHalf(win, image))


    
if __name__ == "__main__" :
  main()