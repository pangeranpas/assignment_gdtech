1. Pembuatan Module Odoo
a) Buat module baru dengan nama siswa
b) Buat empat model:
i. Model Siswa
Field: - name, type char
- date_of_birth, type date
- kelas, type Many2one model Kelas
- guru, type Many2one model Guru
- mata_pelajaran, type Many2one related ke Model Guru.Mata Pelajaran
ii. Model Guru
Field: - name, type char
- mapel, type Many2one model Mata Pelajaran
iii. Model Mata Pelajaran
Field: - name, type char
iv. Model Kelas
Field: - name, type char
c) Buatkan masing-masing model view untuk form input dan tree viewnya
d) Buatkan print report pdf di mo
