from weather_03.weather_wrapper import WeatherWrapper, FORECAST_URL

import pytest
from unittest import mock


Answers = ['Weather in London is warmer than in Moscow by 1 degrees',
           'Weather in Moscow is colder than in London by 1 degrees',
           'The weather in Moscow tomorrow will be much warmer than today',
           'The weather in Moscow tomorrow will be warmer than today',
           'The weather in Moscow tomorrow will be much colder than today',
           'The weather in Moscow tomorrow will be colder than today',
           'The weather in Moscow tomorrow will be the same than today']


def test_get_response_city_bad():
    token = '<your token>'
    wrapper = WeatherWrapper(token)

    with pytest.raises(AttributeError):
        wrapper.get_response_city('city', url=FORECAST_URL)

class Response:
    def __init__(self):
        self.status_code = 200
    def json(self):
        return {}


@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get')
def test_get_response_city(mock_get):
    responce = Response()
    token = '<your token>'
    wrapper = WeatherWrapper(token)
    wrapper.get = mock.Mock(return_value=responce)

    assert {} == wrapper.get_response_city('London', url=FORECAST_URL)

@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get')
def test_get_temperature(mock_get):
    responce = [{'main': {'temp': 7.}}]
    WeatherWrapper.get_response_city = mock.Mock(side_effect=responce)
    token = '<your token>'
    wrapper = WeatherWrapper(token)

    assert 7. == wrapper.get_temperature(city='Moscow')

@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get')
def test_get_tomorrow_temperature(mock_get):
    responce = [{'list': {7: {'main': {'temp': 7.}}}}]
    WeatherWrapper.get_response_city = mock.Mock(side_effect=responce)
    token = '<your token>'
    wrapper = WeatherWrapper(token)

    assert 7. == wrapper.get_tomorrow_temperature(city='Moscow')

def get_temperature_se(arg):
    temperature = {
        'Moscow' : 5,
        'London' : 6
    }
    return temperature.get(arg)

@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get_temperature')
def test_find_diff_two_cities(mock_get_temperature):
    token = '<your token>'
    wrapper = WeatherWrapper(token)
    wrapper.get_temperature = mock.Mock(side_effect=get_temperature_se)

    assert 1 == wrapper.find_diff_two_cities('London', 'Moscow')


@pytest.mark.parametrize(
    ['city1', 'city2',  'answer'], [
        ('London', 'Moscow', Answers[0]),
        ('Moscow', 'London', Answers[1])
    ])
@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get_temperature')
def test_get_diff_string(mock_get_temperature, city1, city2, answer):
    token = '<your token>'
    wrapper = WeatherWrapper(token)
    wrapper.get_temperature = mock.Mock(side_effect=get_temperature_se)

    assert answer == wrapper.get_diff_string(city1, city2)


@pytest.mark.parametrize(
    ['today_temp', 'tomorrow_temp',  'answer'], [
        (20, 25, Answers[2]),
        (17., 17.7, Answers[3]),
        (30, 25, Answers[4]),
        (5., 4.4, Answers[5]),
        (17, 17, Answers[6])
    ])
@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get_temperature')
@mock.patch('src.weather_03.weather_wrapper.WeatherWrapper.get_tomorrow_temperature')
def test_get_tomorrow_diff(_, __, today_temp, tomorrow_temp, answer):
    token = '<your token>'
    wrapper = WeatherWrapper(token)
    wrapper.get_temperature = mock.Mock(return_value=today_temp)
    wrapper.get_tomorrow_temperature = mock.Mock(return_value=tomorrow_temp)

    assert answer == wrapper.get_tomorrow_diff('Moscow')


def test_get():
    token = '<your token>'
    wrapper = WeatherWrapper(token)

    assert 200 == wrapper.get('city', 'https://ya.ru').status_code


