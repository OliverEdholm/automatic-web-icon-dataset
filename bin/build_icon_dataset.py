import sys
import json
from uuid import uuid4
from urllib.parse import urljoin
from multiprocessing import Pool

import cv2

from src.scraping import get_second_degree_urls
from src.image_downloading import get_all_images
from src.alexa_ranking import get_top_n_alexa_domains
from src.classifiers import IconBinaryClassifier


def get_image_hash(image, hash_size=8):
	resized = cv2.resize(image, (hash_size + 1, hash_size))
 
	diff = resized[:, 1:] > resized[:, :-1]
 
	return sum([2 ** i 
                for (i, v) in enumerate(diff.flatten())
                if v])


def download_domain(info):
    idx, domain, dataset_dir_path = info

    domain = f'http://{domain}'
    print(f'starting {idx + 1}, {domain}')

    saved_image_hashes = set()

    icon_binary_classifier = IconBinaryClassifier()

    all_urls = get_second_degree_urls(domain)
    all_urls.add(domain)
    for url in all_urls:
        for image, attributes in get_all_images(url):
            image_hash = get_image_hash(image)
            if icon_binary_classifier.is_icon(image) and \
                    image_hash not in saved_image_hashes:
                identifier = uuid4()

                cv2.imwrite(
                    f'{dataset_dir_path}/{identifier}.jpg',
                    image
                )

                with open(f'{dataset_dir_path}/{identifier}.json', 'w') as f:
                    json.dump({'attributes': attributes}, f)

                saved_image_hashes.add(image_hash)

    print(f'finished {idx + 1}, {domain}')


def main():
    top_n_alexa, dataset_dir_path, n_processes = sys.argv[1:]

    top_n_alexa = int(top_n_alexa)
    n_processes = int(n_processes)

    alexa_domains = get_top_n_alexa_domains(top_n_alexa)

    pool = Pool(n_processes)
    pool.map(
        download_domain, 
        [(idx, domain, dataset_dir_path)
         for idx, domain in enumerate(alexa_domains)]
    )


if __name__ == '__main__':
    main()
