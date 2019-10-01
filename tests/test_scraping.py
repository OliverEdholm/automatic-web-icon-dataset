import cv2

from src.scraping import get_second_degree_urls


def test_get_second_degree_domain_urls():
    second_degree_urls = get_second_degree_urls('https://craigslist.org/contact')

    assert 'https://www.craigslist.org/about/help/' in second_degree_urls, 'Should contain help link'
    assert 'https://www.craigslist.org/about/' in second_degree_urls, 'Should contain about link'

    assert '#' not in second_degree_urls, 'Should only return valid links'
    