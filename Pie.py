import matplotlib.pyplot as plt

# data yang akan ditampilkan dalam pie chart
labels = ['Pensil', 'Penggaris', 'Penghapus', 'Buku', 'Pulpen']
sizes = [15, 30, 10, 20, 25]

# warna untuk setiap bagian dari pie chart
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']

# membuat pie chart
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)

# menampilkan legend dan judul
plt.legend(labels, loc="best")
plt.title("Penjualan Barang")

# menampilkan pie chart
plt.axis('equal')
plt.show()
