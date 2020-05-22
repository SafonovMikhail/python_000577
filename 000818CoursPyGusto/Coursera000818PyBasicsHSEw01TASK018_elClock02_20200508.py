sec = int(input())
hour = (sec // 3600) % 24  #
min = (sec % 3600) // 60
sec1 = (sec % 3600) % 60
print(hour, ':', min // 10, min % 10, ':', sec1 // 10, sec % 10, sep='')
