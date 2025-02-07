class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]):
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car):
        washing_price = (car.comfort_class
                         * (self.clean_power
                             - car.clean_mark)
                         * (self.average_rating
                             / self.distance_from_city_center))
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power >= car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def rate_service(self, mark: int):
        future_average_rating = (((self.average_rating
                                  * self.count_of_ratings)
                                 + mark)
                                 / (self.count_of_ratings
                                    + 1))
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(future_average_rating, 1)
