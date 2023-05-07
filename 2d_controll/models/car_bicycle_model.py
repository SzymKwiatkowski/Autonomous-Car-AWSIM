import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import minimize, differential_evolution

from models.state import State

class Model:
    def __init__(self, dt=0.1, L=3, steer_angle=0, accelartion=0):
        self.L = L
        self.dt = dt
        
        self.steer_angle = steer_angle
        self.accelartion = accelartion
        
        self.state = State()
        

    def update_states(self, inputs, init_state, coff):

        next_state = self.state.calculate_next_state(inputs, init_state, coff, self.dt, self.L)

        return next_state