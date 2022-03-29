import PyPDF2
import os

def quad_crop(file_path, target_file_path = ''):
    path = file_path[:file_path.rfind('\\')]
    with open(file_path, 'rb') as pdf_file:
        r = PyPDF2.PdfFileReader(pdf_file)
        n = r.getNumPages()
        p = r.getPage(0)
        x_max, y_max = p.cropBox.upperRight
        x_max /= 2
        y_max /= 2
    if path: os.chdir(path)
    count = 0
    for j in range(2):
        for k in range(2):
            writer = PyPDF2.PdfFileWriter()
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                for i in range(n):
                    page = reader.getPage(i)
                    page.cropBox.lowerLeft = (j*x_max, k*y_max)
                    page.cropBox.upperRight = ((j+1)*x_max, (k+1)*y_max)
                    writer.addPage(page)
                writer.write(open(file_path[:-4] + '_' + str(count) + '.pdf','wb'))
            count += 1
    
    final_writer = PyPDF2.PdfFileWriter()
    readers = []
    for i in range(4):
        readers.append(PyPDF2.PdfFileReader(file_path[:-4] + '_' + str(i) + '.pdf'))
    
    for i in range(n):
        for j in range(4):
            final_writer.addPage(readers[j].getPage(i))
    
    final_writer.write(open(target_file_path if target_file_path else file_path[:-4] + '_quad.pdf','wb'))
    del readers, final_writer
    
    for i in range(4):
        os.system('del ' + file_path[:-4] + '_' + str(i) + '.pdf')
    
if __name__ == '__main__':
    while file_path := input("crop_PDF_path: "):
        if file_path[0] == '"':
            file_path = file_path[1:-1]
        target_path = input("target_PDF_path: ")
        quad_crop(file_path, target_path)