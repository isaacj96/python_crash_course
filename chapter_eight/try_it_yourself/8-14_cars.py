def store_car_name(model, year, **car_info):
    car_info['model'] = model
    car_info['year'] = year
    return car_info


print(store_car_name('Sonata', 2007, maker='Hyundai', miles=180000))
