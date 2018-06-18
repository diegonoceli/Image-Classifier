from keras.models import load_model
classifier = load_model('models/model.h5')

import numpy as np
from keras.preprocessing import image
x=raw_input("Digite 0 para sair, ou o nome da imagem para classificar ");
while(x!='0'):
	test_image = image.load_img(x, target_size = (150, 150))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)
	if result[0][0] == 1:
		prediction = 'dog'
	else:
	    prediction = 'cat'
	print(prediction)
	x=raw_input("\nDigite 0 para sair, e o nome da imagem para classificar ");