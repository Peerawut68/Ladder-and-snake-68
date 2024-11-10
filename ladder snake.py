import pygame
import random
import math

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake And Ladder')

class board:
	def __init__(self):
		# board List
		self.boardarr = []
		count = 1 

		#Board size  15 X 15
		for i in range(0,15):
			temp = []
			for j in range(0,15):
				x = j*60
				y =	i*60
				temp.append((x,y,count))
				count+=1
			self.boardarr.append(temp)

class dice:
	 def roll():
        return random.randint(1, 6)

class player:
	def win(self):
       
        return self.position == 225
