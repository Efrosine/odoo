from odoo import models, fields

class Identity(models.Model):  # Nama kelas diawali huruf kapital
    _name = 'tracer.identity'
    _description = 'Data Identitas Mahasiswa'

    name = fields.Char(string='Nama', required=True)
    nim = fields.Char(string='NIM', required=True)
    tahunlulus = fields.Date(string='Tahun Lulus', required=True)
    nomor_telepon = fields.Char(string='Nomor Telepon/HP (WA aktif)', required=True)
    email = fields.Char(string='Alamat Email (Email aktif)', required=True)
    alamat_rumah = fields.Text(string='Alamat Rumah', required=True)
    
    fakultas = fields.Many2one('tracer.fakultas', string='Fakultas', required=True)  # Fakultas
    prodi = fields.Many2one('tracer.prodi', string='Program Studi', required=True)  # Program Studi
    status_saat_ini = fields.Selection([
        ('bekerja', 'Bekerja (full time/part time)'),
        ('wiraswasta', 'Wiraswasta'),
        ('melanjutkan_pendidikan', 'Melanjutkan Pendidikan'),
        ('tidak_bekerja', 'Tidak bekerja tetapi sedang mencari kerja')
    ], string='Jelaskan Status Anda Saat Ini', required=True)  # Status Saat Ini
