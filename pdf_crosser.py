import PyPDF2
def cross_pages(path1, path2, target_path):
    reader1 = PyPDF2.PdfFileReader(path1,strict=False)
    reader2 = PyPDF2.PdfFileReader(path2,strict=False)
    b = False
    n1 = reader1.getNumPages()
    n2 = reader2.getNumPages()
    if n1 == n2:
        b = False
    elif n1 == n2+1:
        b = True
    else:
        raise Exception('The pages of two pdfs are not the same!')
    writer = PyPDF2.PdfFileWriter()
    for i in n2:
        writer.addPage(reader1.getPage(i))
        writer.addPage(reader2.getPage(n2-1-i))
    if b:
        writer.addPage(reader1.getPage(n1-1))
    writer.write(open(target_path,'wb'))

if __name__ == '__main__':
    while path1 := input('PDF_PATH1:'):
        path2 = input('PDF_PATH2:')
        target_path = input('TARGET_PATH:')
        if path1[0] == path1[-1] == '"':
            path1 = path1[1:-1]
        if path2[0] == path2[-1] == '"':
            path2 = path2[1:-1]
        if target_path[0] == target_path[-1] == '"':
            target_path = target_path[1:-1]
        cross_pages(path1,path2,target_path)
    