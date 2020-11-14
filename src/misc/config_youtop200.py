#!/usr/bin/env python
import json

""" Configuration file."""

import os
import os.path as osp

import sys
from easydict import EasyDict as edict

from enum import Enum

class phase(Enum):
    TRAIN    = 'yt_train.txt'
    VAL      = 'yt_val.txt'
    TEST  = 'yt_test.txt'
    TRAINVAL = 'yt_train.txt'

__C = edict()

# Public access to configuration settings
cfg = __C

# Number of CPU cores used to parallelize evaluation.
__C.N_JOBS = 32

# Paths to dataset folders
__C.PATH = edict()

__C.PHASE = phase.TRAIN

# Multiobject evaluation (Set to False only when evaluating DAVIS 2016)
__C.MULTIOBJECT = True

# Root folder of project
__C.PATH.ROOT = osp.abspath('../../rvos/')

# Data folder
__C.PATH.DATA = osp.abspath('/n/pfister_lab2/Lab/vcg_natural/YouTop200/release/')

# Path to input images
__C.PATH.SEQUENCES_TRAIN = osp.join(__C.PATH.DATA,"JPEGImages")
__C.PATH.SEQUENCES_VAL = osp.join(__C.PATH.DATA,"JPEGImages")
__C.PATH.SEQUENCES_TRAINVAL = osp.join(__C.PATH.DATA,"JPEGImages")
__C.PATH.SEQUENCES_TEST = osp.join(__C.PATH.DATA,"JPEGImages")

# Path to annotations
__C.PATH.ANNOTATIONS_TRAIN = osp.join(__C.PATH.DATA,"Annotations")
__C.PATH.ANNOTATIONS_VAL = osp.join(__C.PATH.DATA,"Annotations")
__C.PATH.ANNOTATIONS_TRAINVAL = osp.join(__C.PATH.DATA,"Annotations")
__C.PATH.ANNOTATIONS_TEST = osp.join(__C.PATH.DATA,"Annotations")

# Color palette
__C.PATH.PALETTE = osp.abspath(osp.join(__C.PATH.ROOT, 'src/dataloader/palette.txt'))

# Paths to files
__C.FILES = edict()

# Path to property file, holding information on evaluation sequences.
__C.FILES.DB_INFO_TRAIN = osp.abspath(osp.join(__C.PATH.DATA,"info",phase.TRAIN.value))
__C.FILES.DB_INFO_VAL = osp.abspath(osp.join(__C.PATH.DATA,"info",phase.VAL.value))
__C.FILES.DB_INFO_TRAINVAL = osp.abspath(osp.join(__C.PATH.DATA,"info",phase.TRAIN.value))
__C.FILES.DB_INFO_TEST = osp.abspath(osp.join(__C.PATH.DATA,"info",phase.TEST.value))

# Measures and Statistics
__C.EVAL = edict()

# Metrics: J: region similarity, F: contour accuracy, T: temporal stability
__C.EVAL.METRICS = ['J','F']

# Statistics computed for each of the metrics listed above
__C.EVAL.STATISTICS= ['mean','recall','decay']


def db_read_sequences_train():
  """ Read list of sequences. """

  txt_data = open(__C.FILES.DB_INFO_TRAIN)
  sequences = [line.rstrip('\n').replace('/', '_') for line in txt_data]
  
  return sequences
  
def db_read_sequences_val():
  """ Read list of sequences. """

  txt_data = open(__C.FILES.DB_INFO_VAL)
  sequences = [line.rstrip('\n').replace('/', '_') for line in txt_data]
  
  return sequences
  
def db_read_sequences_trainval():
  """ Read list of sequences. """

  txt_data = open(__C.FILES.DB_INFO_TRAINVAL)
  sequences = [line.rstrip('\n').replace('/', '_') for line in txt_data]
  
  return sequences

def db_read_sequences_test():
  """ Read list of sequences. """

  txt_data = open(__C.FILES.DB_INFO_TEST)
  sequences = [line.rstrip('\n').replace('/', '_') for line in txt_data]

  return sequences


# Load all sequences
__C.SEQUENCES_TRAIN = db_read_sequences_train()
__C.SEQUENCES_VAL = db_read_sequences_val()
__C.SEQUENCES_TRAINVAL = db_read_sequences_trainval()
__C.SEQUENCES_TEST = db_read_sequences_test()

import numpy as np
__C.palette = np.loadtxt(__C.PATH.PALETTE,dtype=np.uint8).reshape(-1,3)
