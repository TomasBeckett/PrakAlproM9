def nilai_terbaik(nilai):
    if isinstance(nilai, list):
        nilai.sort()
        nilai.reverse()
        tertinggi = nilai[0:3]
        return tertinggi
    else:
        return None

print(nilai_terbaik([91, 82, 95, 73, 85, 40, 0]))
print(nilai_terbaik([43, 53, 12, 19, 0, 98]))
print(nilai_terbaik("OKE"))

