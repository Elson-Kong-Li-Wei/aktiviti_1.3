pi = 3.142
jejari = float(input("Sila masukkan jejari tangki air:")
tinggi = float(input("Sila masukkan tinggi tangki air:")
isipadu = pi * (jejari)**2 * tinggi
luaspermukaan1 = 2 * pi * (jejari)**2
luaspermukaan2 = 2 * pi * jejari * tinggi
luaspermukaan = luaspermukaan1 + luaspermukaan2
print("Isipadu tangki air ialah",round(isipadu,2))
print("Jumlah luas permukaan tangki air ialah",round(luaspermukaan,2))
