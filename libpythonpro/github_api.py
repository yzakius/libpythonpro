import requests


def buscar_avatar(usuario):
    """
    Busca um avatar de um usuário do Github.
    :param usuario: str com o nome do usuário do github
    :return: str com o link do avatar
    """
    requests
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('yzakius'))
