import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')
import re

df = pd.read_csv('tennis_articles.csv')

df.head(5)