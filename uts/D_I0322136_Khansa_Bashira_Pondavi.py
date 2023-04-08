harga_rumah = 550000000
uang_muka = 5000000
jangka_waktu_tahun = 20 
suku_bunga_perbulan = 5/1000

print ("report 1")

utang = harga_rumah - uang_muka
print ("besar hutang anda adalah ", utang, "Rupiah")

cicilan_pokok_bulanan = utang * suku_bunga_perbulan
print ("cicilan pokok bulanan anda adalah ", cicilan_pokok_bulanan, "Rp/bulan")

cicilan_bunga_bulanan = ((suku_bunga_perbulan * utang) * jangka_waktu_tahun) / (jangka_waktu_tahun * 12)
print ("cicilan bunga bulanan anda adalah ", cicilan_bunga_bulanan, "Rp/bulan")

total_cicilan_setiap_bulan = cicilan_bunga_bulanan + cicilan_pokok_bulanan
print ("total cicilan setiap bulan anda adalah ", total_cicilan_setiap_bulan, "Rupiah")

print ("report 2")

print ("uang muka anda ", uang_muka)

cicilan_bulanan_pertama = uang_muka + total_cicilan_setiap_bulan
print ("cicilan bulanan pertama anda adalah ", cicilan_bulanan_pertama, "Rupiah")

biaya_notaris = 2000000
biaya_provinsi = 1500000
pajak_pembelian = harga_rumah * 25/1000
PNBP = 650000
biaya_balik_nama = 1500000
total_pembayaran_pertama = cicilan_bulanan_pertama + biaya_notaris + biaya_provinsi + pajak_pembelian + PNBP + biaya_balik_nama
print("total pembayaran pertama anda adalah ", total_pembayaran_pertama, "Rupiah")