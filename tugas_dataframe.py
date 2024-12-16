import pandas as pd
import numpy as np

print('no. 1')
df_jabar = pd.read_csv('jabar_df.csv')
print(df_jabar)
print("\n")

print('no. 2')
total_2015 = 0
for i, j in df_jabar.iterrows():
    if j['tahun'] == 2015:
        total_2015 += j['jumlah_produksi_sampah']
print(f"Total sampah di seluruh kabupaten/kota pada tahun 2015: {total_2015:.2f} ton perhari")
print("\n")

print('no. 3')
total_pertahun = {}
for i, j in df_jabar.iterrows():
    tahun = j['tahun']
    jumlah_sampah = j['jumlah_produksi_sampah']
    if tahun in total_pertahun:
        total_pertahun[tahun] += jumlah_sampah
    else:
        total_pertahun[tahun] = jumlah_sampah
for i, j in total_pertahun.items():
    print(f"Tahun {i}: {j:.2f} ton perhari")
print("\n")

print("no. 4")
total_perkota = df_jabar.groupby('nama_kabupaten_kota')['jumlah_produksi_sampah'].sum().reset_index()
for i, j in total_perkota.iterrows():
    kota = j['nama_kabupaten_kota']
    total = j['jumlah_produksi_sampah']
    print(f"Kota: {kota} || Total sampah dari 2015-2023: {total:.2f} ton")