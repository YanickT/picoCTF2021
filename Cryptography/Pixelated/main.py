from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


first = np.asarray(Image.open("scrambled1.png"))
sec = np.asarray(Image.open("scrambled2.png"))

plt.imshow(first + sec, interpolation='nearest')
plt.show()