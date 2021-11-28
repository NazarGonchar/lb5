import csv

x = 1
filename = "mydata.txt"
while x!=0:
    print("Виберіть опцію: \n [1] - читання з файла \n [2] - запис у файл \n ")
    x=int(input(""))
    if x == 1:
        fd = open(filename, "r")
        reader = csv.reader(fd, delimiter="\t")
        for row in reader:
            print(row)
        fd.close()
        print("зчитування файлу виконано")
    elif x==2:
        fd = open(filename, "w")
        for i in range(9):
            A = i*15
            fd.write("%i\t%.1f\n" % (i, A))
        fd.close()
        print("запис файлу виконано")
    else:
        print("Немає такого варіанту")