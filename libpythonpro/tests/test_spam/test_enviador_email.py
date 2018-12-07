import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com', 'isaac@isaac.com'],
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,  # remetente
        'destion@foo.bar',  # destinatário
        'Assunto',
        'Conteúdo',
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'isaac'],
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,  # remetente
            'destion@foo.bar',  # destinatário
            'Assunto',
            'Conteúdo',
        )
