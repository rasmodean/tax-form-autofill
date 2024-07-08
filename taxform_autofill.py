import csv
import pandas as pd
import os
import fitz
import re
import operator

# Constants:
COUNTY_LIST = list()
CLINET_LIST = list()

LOCAL_WH_CSV_PATH = ''
PDF_DIR_PATH = ''
OUTPUT_DIR_PATH = ''

