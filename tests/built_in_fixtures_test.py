import pathlib
import pytest

from src.hex_converter import (  # noqa: F401
    main,
    print_hexadecimal_to_decimal,
    write_hexadecimal_to_decimal,
)

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


def test_monkeypatch(monkeypatch):
    def mock_main(_):
        return "a"

    monkeypatch.setattr("builtins.input", mock_main)
    output = main()

    assert output == 10


def test_capsys(capsys):
    print_hexadecimal_to_decimal("a")
    captured = capsys.readouterr()
    assert captured.out == "10\n"
    assert captured.err == ""


def test_tmp_path(tmp_path):
    dir = tmp_path / "output.txt"
    write_hexadecimal_to_decimal("a", dir)
    assert pathlib.Path(dir).read_text() == "10"
