from speech_to_text import text
from fpdf import FPDF

# Tạo một class kế thừa từ lớp FPDF để tạo báo cáo
class BaoCaoSiemAm(FPDF):
    def __init__(pdf,ten, msba, bung, chan_doan, noi_dung):
        super().__init__()
        pdf.ten = ten
        pdf.msba = msba
        pdf.bung = bung
        pdf.chan_doan = chan_doan
        pdf.noi_dung = noi_dung

    # Tạo header
    def header(pdf):
        # Thêm logo và tên bệnh viện        
        pdf.image('logo.png', 10, 8, 33)
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'ABC HOSPITAL', 0, 1, 'C')
    
    # Tạo footer
    def footer(pdf):
        # Thêm số trang
        pdf.set_y(-15)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 10, 'Trang ' + str(pdf.page_no()) + '/{nb}', 0, 0, 'C')

    # Tạo content
    def bao_cao(pdf):
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'BAO CAO SIEU AM BUNG', 0, 1, 'C')
        pdf.cell(0, 10, '', 0, 1)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Thong tin benh nhan:', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, '- Ho ten: ' + pdf.ten, 0, 1)
        pdf.cell(0, 10, '- MSBA: ' + pdf.msba, 0, 1)
        pdf.cell(0, 10, '- Bung: ' + pdf.bung, 0, 1)
        pdf.cell(0, 10, '- Chan doan: ' + pdf.chan_doan, 0, 1)
        pdf.cell(0, 10, '', 0, 1)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Ket qua sieu am:', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, pdf.noi_dung)

# Tạo đối tượng báo cáo và thực thi tạo báo cáo
bao_cao = BaoCaoSiemAm(
    'ABC',
    'AB1231',
    'Bung thuong',
    text,
    'Phat hien khoi u xcm ben phai abc'
)
bao_cao.bao_cao()
bao_cao.output('BaoCaoSiemAm.pdf', 'F')