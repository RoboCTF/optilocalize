#!/usr/bin/env python
#
# A test script to ensure that the kinematics work.

import time, math
from pmw3901 import PAA5100

L = 0.1778 # Length from back axle to front axle

class OptiFlo():
  def __init__(self, glbl_x=0, glbl_y=0, glbl_theta=0):
    self.flo = PAA5100(spi_port=0, spi_cs=1, spi_cs_gpio=7)
    self.flo.set_rotation(0)
    self.world_pos = (glbl_x, glbl_y, glbl_theta)
  
  def update_pos(self):
    dx, dy = self.flo.get_motion()
    # d_phi = math.atan(dy / dx)
    d_theta = dx * math.tan(dy/dx) / L
    
    # Assume dt = 100ms or 0.1s
    dt = 0.1
    glbl_theta = self.world_pos[2] + d_theta * dt
    glbl_dx = dx * math.cos(glbl_theta)
    glbl_dy = dx * math.sin(glbl_theta)
    
    glbl_x = self.world_pos[0] + glbl_dx * dt
    glbl_y = self.world_pos[1] + glbl_dy * dt
    
    self.world_pos = (glbl_x, glbl_y, glbl_theta)
    
if __name__ == "__main__":
  optiflow = OptiFlow()
  while True:
    try:
      optiflow.update_pos()
      print(optiflow.world_pos)
    except RuntimeError:
      break
  # Close SPI connection
    
