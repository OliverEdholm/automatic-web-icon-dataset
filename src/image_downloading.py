import os
from uuid import uuid4
from urllib.parse import urljoin

import cv2
import requests
from lxml import html


def _clean_url(url):
    if url[:2] == '//':
        url = url[2:]
    elif url[:1] == '/':
        url = url[1:]

    if 'http' not in url:
        url = f'http://{url}'

    return url


def _download_image(url):
    if 'data:image' in url:
        return

    url = _clean_url(url)

    try:
        r = requests.get(url, stream=True, timeout=10)
        if r.status_code == 200:
            path = f'/tmp/{uuid4()}'

            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)

            image = cv2.imread(path)
            
            os.remove(path)

            return image
    except Exception as e:
        print(e)


def get_all_images(url, max_n_images=100):
    page = requests.get(url).content

    tree = html.fromstring(page)

    all_images = []
    for image_tag in tree.xpath('//img'):
        if image_tag.attrib.get('src'):
            url = urljoin(url, image_tag.attrib['src'])
            image = _download_image(url)
            
            if image is not None:
                all_images.append((image, dict(image_tag.attrib)))
        
        if len(all_images) == max_n_images:
            break
    
    return all_images
        

