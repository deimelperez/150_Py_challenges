rain = str.lower(input("Is it raining?(yes or no): "))
if rain == 'yes':
    wind = str.lower(input("Is it windy?(yes or no): "))
    if wind == 'yes':
        print('“It is too windy for an umbrella”')
    else:
        print('“Take an umbrella”')
else:
    print('“Enjoy your day!”')
