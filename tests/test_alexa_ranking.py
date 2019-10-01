import pytest

from src.alexa_ranking import get_top_n_alexa_domains


@pytest.mark.parametrize('top_n, expected', [
    (1,
    [
        'google.com'
    ]),
    (5, 
    [
        'google.com',
        'youtube.com',
        'baidu.com',
        'tmall.com',
        'qq.com'
    ])
])
def test_get_top_n_alexa_domains(top_n, expected):
    assert get_top_n_alexa_domains(top_n) == expected
