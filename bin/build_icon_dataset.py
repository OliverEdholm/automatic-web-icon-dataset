import sys
import json
from uuid import uuid4
from urllib.parse import urljoin

import cv2

from src.scraping import get_second_degree_urls
from src.image_downloading import get_all_images
from src.alexa_ranking import get_top_n_alexa_domains
from src.classifiers import IconBinaryClassifier


def get_image_hash(image, hashSize=8):
	resized = cv2.resize(image, (hashSize + 1, hashSize))
 
	diff = resized[:, 1:] > resized[:, :-1]
 
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def main():
    top_n_alexa, dataset_dir_path = sys.argv[1:]

    top_n_alexa = int(top_n_alexa)

    icon_binary_classifier = IconBinaryClassifier()

    saved_image_hashes = set()
    for domain in get_top_n_alexa_domains(top_n_alexa):
        domain = f'http://{domain}'
        print(domain)

        all_urls = get_second_degree_urls(domain)
        all_urls.add(domain)

        for url in all_urls:
            for image, alt_text in get_all_images(url):
                image_hash = get_image_hash(image)
                if icon_binary_classifier.is_icon(image) and \
                     image_hash not in saved_image_hashes:
                    identifier = uuid4()

                    cv2.imwrite(
                        f'{dataset_dir_path}/{identifier}.jpg',
                        image
                    )

                    with open(f'{dataset_dir_path}/{identifier}.json', 'w') as f:
                        json.dump({'altText': alt_text}, f)

                    saved_image_hashes.add(image_hash)

                    



if __name__ == '__main__':
    main()
