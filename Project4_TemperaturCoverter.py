print('---TEMPERTURE CONVERTER---')

units = {
    1: 'Celcius',
    2: 'Fahrenheit',
    3: 'Kelvin',
    4: 'Reamur'
}

for i in range(1, 5):
    print(f"{i} - {units[i]}")
before = float(input('PICK WHICH TEMPERATURE YOU WANT: '))

for i in range(1, 5):
    print(f"{i} - {units[i]}")
after = float(input('WHAT DO YOU WANT TO CONVERT TO: '))


if before in [1, 2, 3, 4]:
    tempnow = float(input('INPUT THE DEGREE NUMBER: '))
    if before == 1:
        if after == 2:
            result = ((9/5)*(tempnow))+32
        elif after == 3:
            result = (tempnow+273.15)
        elif after == 4:
            result = ((4/5)*tempnow)
        else:
            result = tempnow
    elif before == 2:
        if after == 1:
            result = (5/9)(tempnow-32)
        elif after == 3:
            result = ((tempnow-32)/1.8)+273.15
        elif after == 4:
            result = 4/9(tempnow-32)
        else:
            result = tempnow
    elif before == 3:
        if after == 1:
            result = tempnow-273.15
        elif after == 2:
            result = (1.8(tempnow-273.15))+32
        elif after == 4:
            result = 4/5(tempnow-273.15)
        else:
            result = tempnow
    else:
        if after == 1:
            result = (5/4)*tempnow
        elif after == 2:
            result = ((9/4)*tempnow)+32
        elif after == 3:
            result = ((5/4)*tempnow)+273
        else:
            result = tempnow
else:
    print('INVALID')

print(f"{tempnow} degree {units[before]} to {units[after]} is {result} degree")
    