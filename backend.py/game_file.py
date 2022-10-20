'''
Name: Agar.io-Clone
Main function for the agar.io clone
Authors: DaviZCodes and HenryMal
'''
import random
import math
import pygame as pyg
import os

# Display dimensions
WIDTH = 1920
HEIGHT = 1080 
DISPLAY_TUPLE = (WIDTH, HEIGHT)

# Basic ball dimensions
START_PLAYER_RADIUS = 30
START_PELLET_RADIUS = 3

# data sets for players, bots, and pellets
players = {} # dictionary
bots = {}
pellets = {}

# class for map
class Background:
  def __init__(self,)

# class for camera
class CameraPOV:
  def __init__(self):
    # base values for x, y components
    self.x_component = 0
    self.y_component = 0
    self.zoom = 0.6
  
  # function to find the centre of player so camera can allocate itself
  def centre(self, player):
    self.x_component = player.position
    self.y_component = player.position 

# class for pellets
class Pellet:
  def __init__(self, game):
    self.game = game
    self.radius = START_PELLET_RADIUS
    self.color = (240,248,255) #aliceblue rgb
    
  def draw(self):
  def consumed(self)
  def spawn(self):
  
# class for player
class MainCell:
  def __init__(self, game, cell_name, cell_size = 500, cell_color):
    self.cell_name = cell_name
    self.cell_size = cell_size
    self.cell_color = cell_color
  def consume(self, pellets):
  def draw(self):
  def mass_decay(self):
  def position(self):

#class for bots (ATM THE BOTS CANNOT SPLIT OR GO AFTER MASS, THEY JUST HOVER AROUND RANDOMLY)

class Bot:
  def __init__(self):
    self.cell_name = "Bot"
    self.cell_color = (0, 0, 0)
  def consume(self, pellets):
  def draw(self):
  def mass_decay(self)
 
# class for virus

class NormalVirus:
  def __init__(self):
  def draw(self):
  
# special virus

class DecayVirus:
 def __init__(self):
 def draw(self):

# special virus 2

class Moving Virus:
  
  
  
# final class for game
class AgarClone():
  def __init__(self):
    self.display = pyg.display.set_mode(DISPLAY_TUPLE)
               
