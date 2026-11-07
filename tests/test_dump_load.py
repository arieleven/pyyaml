import pytest
import yaml


def test_dump():
    assert yaml.dump(['foo'])


def test_load_no_loader():
    with pytest.raises(TypeError):
        yaml.load("- foo\n")


def test_load_safeloader():
    assert yaml.load("- foo\n", Loader=yaml.SafeLoader)


@pytest.mark.parametrize("text", ["a\t b", "a\x07 b", "a\t  b"])
def test_double_quoted_wrap_past_width_round_trips(text):
    # Nested deep enough that the indentation alone is wider than `width`.
    data = [[[text]]]
    dumped = yaml.dump(data, Dumper=yaml.Dumper, width=5, indent=2,
                       default_style='"')
    assert yaml.load(dumped, Loader=yaml.SafeLoader) == data
