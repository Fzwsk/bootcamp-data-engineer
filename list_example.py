#cek value dalam list
fruits = ['Pisang','Apple','Mangga']
#menambah value dalamlist diakhir
fruits.append(30)
#menambah value dalam list dibarus manapun
fruits.insert(1,2.4)
#menambah/gabung value dalam list
database = ['postgres','mysql']
fruits.extend(database)
#hapus value dalam list
fruits.remove("Mangga") #hapus berdasarkan nama value dalam list
fruits.pop(0) #hapus berdasarkan ururtan value dalam list
del fruits[1] #hapus berdasarkan ururtan value dalam list
print(fruits)