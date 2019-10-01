import cv2
import pytest

from src.classifiers import IconBinaryClassifier


@pytest.mark.parametrize('path, expected', [
    ('data/test_images/icon1.jpeg', True),
    ('data/test_images/natural1.jpeg', False),
    ('data/test_images/natural2.jpeg', False),
    ('data/test_images/natural3.jpeg', False)
])
def test_icon_binary_classifier(path, expected):
    image = cv2.imread(path)

    icon_binary_classifier = IconBinaryClassifier()
    
    assert icon_binary_classifier.is_icon(image) is expected, 'Should classify correctly'
    