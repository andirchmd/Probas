# -*- coding: utf-8 -*-
"""Probabilitas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nTsjx6PovOVDyolwPjD1GM8-4lZijGzo

# Tugas Individu 2 Probabilitas dan Statistika
oleh [Andi Rachmad Triandika Rusli](https://github.com/andirchmd) (2109106132)

---

Import Library yang dibutuhkan
"""

import pandas as pd  # untuk baca dan processing dataset
import matplotlib.pyplot as plt # untuk visualisasi dataset
import seaborn as sns # visualisasi tingkat lanjut

"""## Soal 1
Baca file excelnya
"""

data = pd.read_csv("https://raw.githubusercontent.com/andirchmd/Probas/main/StudentsPerformance.csv")

"""## Soal 2
Tampilkan dan jelaskan tipe tiap-tiap kolom data
"""

data

"""## Soal 3
Lakukan pengolahan data tunggal terhadap kolom data numerik math_score,reading_score, dan writing_score dengan membuat ringkasan data (summary). Summary data adalah informasi yang berisi informasi antara lain N jumlah data, Mean Rata-rata, dan Standar deviasi
"""

# Mendapatkan jumlah data
N = data['math_score'].count()  # Karena semua kolom mempunyai jumlah data yang sama, kita bisa gunakan salah satu kolom untuk mendapatkan jumlahnya

# Mendapatkan rata-rata untuk setiap kolom
mean_math = data['math_score'].mean()
mean_reading = data['reading_score'].mean()
mean_writing = data['writing_score'].mean()

# Mendapatkan standar deviasi untuk setiap kolom
std_math = data['math_score'].std()
std_reading = data['reading_score'].std()
std_writing = data['writing_score'].std()

# Menampilkan ringkasan data
print("Summary untuk kolom math_score:")
print(f"N: {N}")
print(f"Mean: {mean_math}")
print(f"Standar Deviasi: {std_math}")
print("\nSummary untuk kolom reading_score:")
print(f"N: {N}")
print(f"Mean: {mean_reading}")
print(f"Standar Deviasi: {std_reading}")
print("\nSummary untuk kolom writing_score:")
print(f"N: {N}")
print(f"Mean: {mean_writing}")
print(f"Standar Deviasi: {std_writing}")

"""## Soal 4
Dengan pengolahan data tunggal, buat grafik BOX PLOT ketiga variabel score berdasarkan kategori gender, race/ethnicity dan parental level of education
"""

# Mengatur ukuran gambar
plt.figure(figsize=(15, 5))

# Box plot berdasarkan gender
plt.subplot(1, 3, 1)
sns.boxplot(data=data, x="gender", y="math_score")
plt.title("Box Plot of Math Score by Gender")
plt.subplot(1, 3, 2)
sns.boxplot(data=data, x="gender", y="reading_score")
plt.title("Box Plot of Reading Score by Gender")
plt.subplot(1, 3, 3)
sns.boxplot(data=data, x="gender", y="writing_score")
plt.title("Box Plot of Writing Score by Gender")

# Menampilkan grafik
plt.tight_layout()
plt.show()

# Box plot berdasarkan race/ethnicity
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.boxplot(data=data, x="race/ethnicity", y="math_score")
plt.title("Box Plot of Math Score by Race/Ethnicity")
plt.subplot(1, 3, 2)
sns.boxplot(data=data, x="race/ethnicity", y="reading_score")
plt.title("Box Plot of Reading Score by Race/Ethnicity")
plt.subplot(1, 3, 3)
sns.boxplot(data=data, x="race/ethnicity", y="writing_score")
plt.title("Box Plot of Writing Score by Race/Ethnicity")

# Menampilkan grafik
plt.tight_layout()
plt.show()

# Box plot berdasarkan parental level of education
plt.figure(figsize=(20, 5))
plt.subplot(1, 3, 1)
sns.boxplot(data=data, x="parental level of education", y="math_score")
plt.title("Box Plot of Math Score by Parental Level of Education")
plt.xticks(rotation=45)
plt.subplot(1, 3, 2)
sns.boxplot(data=data, x="parental level of education", y="reading_score")
plt.title("Box Plot of Reading Score by Parental Level of Education")
plt.xticks(rotation=45)
plt.subplot(1, 3, 3)
sns.boxplot(data=data, x="parental level of education", y="writing_score")
plt.title("Box Plot of Writing Score by Parental Level of Education")
plt.xticks(rotation=45)

# Menampilkan grafik
plt.tight_layout()
plt.show()

"""## Soal 5
Buat table cross: gender versus race/ethnicity, gender versus parental level of education dan race/ethnicity versus parental level of education

"""

# Cross tabulation untuk gender versus race/ethnicity
ct_gender_race = pd.crosstab(data['gender'], data['race/ethnicity'])
print("Table Cross: Gender vs Race/Ethnicity\n")
print(ct_gender_race)
print("\n" + "="*50 + "\n")

# Cross tabulation untuk gender versus parental level of education
ct_gender_education = pd.crosstab(data['gender'], data['parental level of education'])
print("Table Cross: Gender vs Parental Level of Education\n")
print(ct_gender_education)
print("\n" + "="*50 + "\n")

# Cross tabulation untuk race/ethnicity versus parental level of education
ct_race_education = pd.crosstab(data['race/ethnicity'], data['parental level of education'])
print("Table Cross: Race/Ethnicity vs Parental Level of Education\n")
print(ct_race_education)

"""## Soal 6
Buat table pivot gender versus race/ethnicity terhadap masing-masing data numerik math_score, reading_score, dan writing_score
"""

# Pivot table untuk math_score
pivot_math_score = data.pivot_table(values='math_score', index='gender', columns='race/ethnicity', aggfunc='mean')

# Pivot table untuk reading_score
pivot_reading_score = data.pivot_table(values='reading_score', index='gender', columns='race/ethnicity', aggfunc='mean')

# Pivot table untuk writing_score
pivot_writing_score = data.pivot_table(values='writing_score', index='gender', columns='race/ethnicity', aggfunc='mean')

print("Pivot Table: Gender vs Race/Ethnicity for Math Score\n")
print(pivot_math_score)
print("\nPivot Table: Gender vs Race/Ethnicity for Reading Score\n")
print(pivot_reading_score)
print("\nPivot Table: Gender vs Race/Ethnicity for Writing Score\n")
print(pivot_writing_score)

"""## Soal 7
Buat table distribusi frekuensi (pengolahan berkelompok) terhadap masing-masing data numerik math_score, reading_score, dan writing_score dengan jumlah dan lebar kelas sebesar 10
"""

# Membuat batas kelas
max_math = data['math_score'].max()
max_reading = data['reading_score'].max()
max_writing = data['writing_score'].max()

bins_math = range(0, max_math + 10, 10)
bins_reading = range(0, max_reading + 10, 10)
bins_writing = range(0, max_writing + 10, 10)

# Mengelompokkan data ke dalam kelas
data['math_group'] = pd.cut(data['math_score'], bins=bins_math, right=False)
data['reading_group'] = pd.cut(data['reading_score'], bins=bins_reading, right=False)
data['writing_group'] = pd.cut(data['writing_score'], bins=bins_writing, right=False)

# Menghitung frekuensi distribusi
math_freq = data['math_group'].value_counts().sort_index()
reading_freq = data['reading_group'].value_counts().sort_index()
writing_freq = data['writing_group'].value_counts().sort_index()

print("Tabel distribusi frekuensi untuk Math Score:\n")
print(math_freq)
print("\nTabel distribusi frekuensi untuk Reading Score:\n")
print(reading_freq)
print("\nTabel distribusi frekuensi untuk Writing Score:\n")
print(writing_freq)

"""## Soal 8
Buat grafik histogram untuk table distribusi frekuensi [soal no.6](https://colab.research.google.com/drive/1nTsjx6PovOVDyolwPjD1GM8-4lZijGzo?authuser=2#scrollTo=mzkFvHVzYq8d&line=1&uniqifier=1)

"""

# Membuat batas kelas seperti sebelumnya
bins = range(0, 110, 10)  # 110 as a cap to ensure all scores up to 100 are included

# Mengelompokkan data ke dalam kelas
data['math_group'] = pd.cut(data['math_score'], bins=bins, right=False)
data['reading_group'] = pd.cut(data['reading_score'], bins=bins, right=False)
data['writing_group'] = pd.cut(data['writing_score'], bins=bins, right=False)

# Buat tabel pivot
pivot_math = data.pivot_table(index='math_group', columns=['gender', 'race/ethnicity'], values='math_score', aggfunc='count').fillna(0)
pivot_reading = data.pivot_table(index='reading_group', columns=['gender', 'race/ethnicity'], values='reading_score', aggfunc='count').fillna(0)
pivot_writing = data.pivot_table(index='writing_group', columns=['gender', 'race/ethnicity'], values='writing_score', aggfunc='count').fillna(0)

# Menggambar histogram dari tabel pivot
def draw_histogram(pivot, title):
    pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(title)
    plt.ylabel("Frequency")
    plt.show()

draw_histogram(pivot_math, "Histogram of Math Score by Gender and Race/Ethnicity")
draw_histogram(pivot_reading, "Histogram of Reading Score by Gender and Race/Ethnicity")
draw_histogram(pivot_writing, "Histogram of Writing Score by Gender and Race/Ethnicity")

"""## Soal 9
Dengan table distribusi frekuensi di [nomor 7](https://colab.research.google.com/drive/1nTsjx6PovOVDyolwPjD1GM8-4lZijGzo?authuser=2#scrollTo=oNPjFs5vZOsm&line=1&uniqifier=1), hitung K1, D3 dan P35 kolom math_score

"""

# Membuat batas kelas dan tabel distribusi frekuensi
bins = range(0, 110, 10)
data['math_group'] = pd.cut(data['math_score'], bins=bins, right=False)
freq_table = data['math_group'].value_counts().sort_index()
cumulative_freq = freq_table.cumsum()

N = data['math_score'].count()

def find_statistic_value(p):
    target = N * p / 100
    relevant_class = cumulative_freq[cumulative_freq >= target].index[0]
    L = relevant_class.left
    F = cumulative_freq[cumulative_freq < target].iloc[-1] if p != 0 else 0
    f = freq_table[relevant_class]
    w = 10  # lebar kelas
    X_p = L + ((target - F) / f) * w
    return X_p

K1 = find_statistic_value(25)
D3 = find_statistic_value(30)
P35 = find_statistic_value(35)

print(f"K1  (Kuartil Pertama): {K1}")
print(f"D3  (Desil Ketiga)   : {D3}")
print(f"P35 (Persentil ke-35): {P35}")