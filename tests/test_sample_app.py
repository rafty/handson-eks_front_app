from samples import sample_app


def test_ok_sample():
    result = sample_app.add_calc(1, 2)
    assert 3 == result


# def test_string_sample():
#     result = sample.add_calc(1, 2)
#     assert '3' == result
#
#
# def test_str_param_sample():
#     result = sample.add_calc(1, '2')
#     assert 3 == result


def test_str_param_2_sample():
    result = sample_app.add_calc('1', '2')
    assert result is False


def test_ok_0_sample():
    result = sample_app.add_calc(0, 1000000000)
    assert 1000000000 == result


def test_ok_minas_sample():
    result = sample_app.add_calc(-1, 1)
    assert 0 == result
