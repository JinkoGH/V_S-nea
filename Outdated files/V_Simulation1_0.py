#imports
import numpy as np
import math

#from Login_system1_2 import *

#points representing the trees
class Tree1():
    def __init__(self, x, y):
        self.x = x
        self.y = y

#nodes
class Node():
    #implementing dimensions
    def __init__(self, centre,width,height):
        self.height = height
        self.width = width
        self.centre = centre
        self.west = centre.x -width
        self.east = centre.x +width
        self.north = centre.y +height
        self.south = centre.y -height
    #functions of node
    def containsPoint(self,point):
        return (self.west <= point.x < self.east and self.north <= point.y < self.south)
    #visualisation function
    def draw(self, ax, c = 'k', lw=1, **kwargs):
        x1,y1 = self.west, self.north
        x2,y2= self.east, self.south
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)

#quadtree
class Quadtree:
    def __init__(self, boundary, capacity = 4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False
    #inserting functions
    def insert(self,point):
        # when tree is not in range of the quadtree
        if not self.boundary.containsPoint(point):
            return False
        # if node is not preoccupied by a tree
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.divide()
        #recursive function to call itself
        if self.ne.insert(point):
            return True
        elif self.nw.insert(point):
            return True
        elif self.se.insert(point):
            return True
        elif self.sw.insert(point):
            return True
    def divide(self):
        centre_x = self.boundary.centre.x
        centre_y = self.boundary.centre.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2
        #centre points
        #northeast point
        ne = Node(Tree1(centre_x + new_width, centre_y + new_height), new_width, new_height)
        self.ne = Quadtree(ne)
        #northwest point
        nw = Node(Tree1(centre_x - new_width, centre_y + new_height), new_width, new_height)
        self.nw = Quadtree(nw)
        #southeast point
        se = Node(Tree1(centre_x + new_width, centre_y - new_height), new_width, new_height)
        self.se = Quadtree(se)
        #southwest point
        sw = Node(Tree1(centre_x - new_width, centre_y - new_height), new_width, new_height)
        self.sw = Quadtree(sw)
        self.divided = True

    def draw(self, ax):
        self.boundary.draw(ax)
        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)
        else:
            print("point draw fail")









