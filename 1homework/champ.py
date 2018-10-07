#!/usr/bin/env python

from random import randint
import car as c
import weather as w

CAR_SPECS = {
    'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
    'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
    'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
    'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
    'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
}


def start(competitors, distance, wind_speed):
    cars = {}
    weather=w.Weather(wind_speed)
    for competitor_name in competitors:
        competitor_time = 0
        competitor_speed = 0
        car = c.Car(competitor_name, CAR_SPECS[competitor_name])
        cars[competitor_name] = car

        for distance in range(distance):
            _wind_speed = randint(0, weather.get_wind_speed())

            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / car.specs["time_to_max"]) * car.specs['max_speed']
                if _speed > _wind_speed:
                    _speed -= (car.specs["drag_coef"] * _wind_speed)

            competitor_time += float(1) / _speed

        print("Car <%s> result: %f" % (competitor_name, competitor_time))


if __name__ == '__main__':
    competitors = ('ferrary', 'bugatti', 'toyota', 'lada', 'sx4')
    start(competitors, distance=10000, wind_speed=20)
