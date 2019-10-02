import cv2

from src.image_downloading import get_all_images


def test_get_all_images():
    all_images = get_all_images('http://nooooooooooooooo.com')

    assert len(all_images) == 1, 'Should only contain Darth Vader image'

    assert (all_images[0][0] == cv2.imread('data/test_images/vader.jpg')).all(), \
        'Should download Darth Vader image'
    assert all_images[0][1] == {'alt': 'Darth Vader FML', 'src': 'vader.jpg'}, \
        'Should return Darth Vader alt text'
