print(' *** Wind classification ***')
Speed = float(input('Enter wind speed (km/h) : '))

if Speed >= 0 and Speed < 52:
    print("Wind classification is Breeze.")
elif Speed >= 52 and Speed < 56:
    print("Wind classification is Depression.")
elif Speed >= 56 and Speed < 102:
    print("Wind classification is Tropical Storm.")
elif Speed >= 102 and Speed < 209:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")