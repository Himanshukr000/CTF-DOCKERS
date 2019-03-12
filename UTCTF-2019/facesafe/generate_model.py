from locker.constants import MODELS_DIRECTORY, MODEL_PREFIX, RANDOM_PREFIX
from locker.trainer.train import train_model
import numpy as np
from scipy.misc import imsave
import os

while True:
	print("Training model")
	model_path = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX)
	random_image_path = os.path.join(MODELS_DIRECTORY, RANDOM_PREFIX)

	# Generate our random image
	random_image = np.random.rand(32, 32, 3)
	imsave(random_image_path, random_image)

	# Train our model
	result = train_model(model_path, random_image_path, epochs=5)
	if not result:
		print("Model isn't accurate enough! Retrying...")

		# Clean up
		os.remove(random_image_path)
	else:
		break