apel = 12000
mangga = 10000
jeruk = 15000
uang_dimiliki = 150000


jumlah_apel = int(input("Masukkan jumlah apel yang ingin dibeli: "))
jumlah_mangga = int(input("Masukkan jumlah mangga yang ingin dibeli: "))
jumlah_jeruk = int(input("Masukkan jumlah jeruk yang ingin dibeli: "))

sisa_uang = uang_dimiliki - (jumlah_apel * apel + jumlah_mangga * mangga + jumlah_jeruk * jeruk)

print("Sisa uang setelah membeli buah: Rp", sisa_uang)


