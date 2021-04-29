store=95
base=store*1000
instrument=900
nail=80

new_instruments=base//instrument
stuff1=base%instrument
new_nails=stuff1//nail
stuff2=stuff1%nail
stuff3=stuff2/1000
print("На инструменты уходит",instrument/1000,"кг железа")
print("На гвозди уходит",nail/1000,"кг железа")
print("У вас было",store,"кг железа")
print("Сделали",new_instruments,"инструментов")
print("Сделали",new_nails,"гвоздей")
print("Не использовали",stuff3,"кг железа ")
