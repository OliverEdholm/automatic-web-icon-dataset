import cv2
import numpy as np


# focus on high precision, since the web is so big, you still get lots of icons
class IconBinaryClassifier:
    def __init__(
        self,
        n_unique_threshold=50, 
        bilinear_resize_shape=(20, 20), 
        max_non_square_offset=6,
        max_area=int(6e4)
    ):
        self._n_unique_threshold = n_unique_threshold
        self._bilinear_resize_shape = bilinear_resize_shape
        self._max_non_square_offset = max_non_square_offset
        self._max_area = max_area

    def _preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return cv2.resize(
            gray, self._bilinear_resize_shape, interpolation=cv2.INTER_LINEAR)
    
    def _get_n_unique_colors(self, image):
        assert image.shape[-1] == 1 or len(image.shape) == 2, 'Must be grayscale'
        
        flattened = image.flatten()
        
        return len(np.unique(flattened))
        
    def _get_non_square_offset(self, image):
        if image.shape[0] > image.shape[1]:
            return image.shape[0] / image.shape[1]
        else:
            return image.shape[1] / image.shape[0]
    
    def _get_area(self, image):
        return image.shape[0] * image.shape[1]
    
    def is_icon(self, image):
        preprocessed = self._preprocess_image(image)
        n_unique_colors = self._get_n_unique_colors(preprocessed)

        non_square_offset = self._get_non_square_offset(image)

        area = self._get_area(image)

        return (
            n_unique_colors <= self._n_unique_threshold and \
            non_square_offset <= self._max_non_square_offset and \
            area <= self._max_area
        )
