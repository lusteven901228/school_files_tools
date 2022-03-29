import PyPDF2
def rotate_pages(pdf_path,cctimes,p,q):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    pdf_writer = PyPDF2.PdfFileWriter()
    q = pdf_reader.getNumPages() if q == -1 else q
    for i in range(p,q):
        pdf_writer.addPage(pdf_reader.getPage(i).rotateCounterClockwise(90 * cctimes))
    with open(pdf_path.replace('.pdf','_rotated.pdf'),'wb') as writeFile:
        pdf_writer.write(writeFile)
if __name__ == '__main__':
    path = input('PDF_PATH:')
    if path[0] == path[-1] == '"':
        path = path[1:-1]
    a = input('start:')
    b = input('end:')
    a = int(a) if a else 0
    b = int(b) if b else -1
    rotate = int(input('Rotate_Times(counterclockwise):') or 0)
    rotate_pages(path,rotate,a,b)