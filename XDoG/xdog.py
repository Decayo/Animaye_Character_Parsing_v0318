import argparse
import numpy as np
from pathlib import Path
from PIL import Image
from scipy.ndimage import gaussian_filter
import sys 

from util import load_img, save_img

class XDoG:
    def __init__(self, input, gamma, phi, eps, k, sigma, thresh=False):
        self.input_arr = load_img(input)
        self.set_params(gamma, phi, eps, k, sigma)
        self.thresh = thresh
        self.output_arr = None

    def set_params(self, gamma, phi, eps, k, sigma):
        self.gamma = gamma
        self.phi = phi 
        self.eps = eps 
        self.k = k 
        self.sigma = sigma

    def apply(self):
        g_filtered_1 = gaussian_filter(self.input_arr, self.sigma)
        g_filtered_2 = gaussian_filter(self.input_arr, self.sigma * self.k)

        z = g_filtered_1 - self.gamma * g_filtered_2

        z[z < self.eps] = 1.

        mask = z >= self.eps
        z[mask] =  1. + np.tanh(self.phi * z[mask])

        if self.thresh:
            mean = z.mean()
            z[z < mean] = 0.
            z[z >= mean] = 1.

        self.output_arr = z
