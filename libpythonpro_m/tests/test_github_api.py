from unittest.mock import Mock

from libpythonpro_m import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'mateuslourenco', 'id': 19513199,
        "avatar_url": "https://avatars.githubusercontent.com/u/19513199?v=4"
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('mateuslourenco')
    assert 'https://avatars.githubusercontent.com/u/19513199?v=4' == url
