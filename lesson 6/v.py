import random
from random import randint,choice

emotion=random.choice(["хорошее","плохое","среднее"])
weather=random.choice(["дождливо","облачно","ясно"])

if emotion=="хорошее":
    print("настроение было",emotion,"на улице было" , weather,"пойду гулять")

elif emotion=="среднее" and weather!="дождливо":
    print("настроение было",emotion,"на улице было" , weather,"пойду гулять")

else:
    print("настроение было",emotion,"на улице было" , weather,"не пойду гулять")
