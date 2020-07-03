#  List
numbers = [1,2,3,4,5]
print(numbers)

n_data = len(numbers)
print(n_data)

numbers.append(6)
print(numbers)

# mengambil data dari index 1 sampai value 3
print(numbers[1:3])
# mengambil data dari semua sebelum dan sampai value 3
print(numbers[:3])
# mengambil data setelah index 2 
print(numbers[2:])

# Dictionary
biodata = {
	"nama" : "Budi",
	"umur" : 17,
	"tempat_tinggal" : "Bandung"
}

# ambil semua key biodata dictionary
print(biodata.keys())
# ambil semua value biodata dictionary
print(biodata.values())

# Data Frame
import pandas as pd

nama = ["Budi", "Andy", "Aldo", "Dodo"]
umur = [17, 22, 15, 18]
hobi = ["Memancing", "Traveling", "Reading", "Writing"]
asal = ["Depok", "Jakarta", "Bandung", "Jogja"]
menikah = ["yes", "no", "yes", "no"]

df = pd.DataFrame(
	{
		"nama" : nama,
		"umur" : umur,
		"hobi" : hobi,
		"asal" : asal,
		"menikah" : menikah
	}
)

print(df)

# cetak dimensi baris dan  kolom
print(df.shape)

# menampilkan deskripsi
print(df.describe())
print(df.hobi.describe())

# menambahkan kolom baru
df["new_column"] = "new value"
print(df)

# menambah kolom baru berdasarkan kolom sebelumnya (kebalikannya)
df["kebalikan status"] = df["menikah"].shift(-1)
print(df)

# mengambil beberapa row pertaana
print(df.head())
print(df.head(2))

# mengambil beberapa row terakhir
print(df.tail())
print(df.tail(2))

# mengambil secara acak
print(df.sample())

# mengambil sample dari kolom
print(df[["nama", "menikah"]])

# mengambil hanya satu kolom
print(df.nama)

# mengambil unik value dari suatu kolom
print(df.menikah.unique())