import PyPDF2
def main():
    mergeFile = PyPDF2.PdfFileMerger()
    while True:
        p = input('File:')
        if not p or p == '0':
            break
        elif p[0] == '"':
            p = p[1:-1]
        mergeFile.append(PyPDF2.PdfFileReader(p, 'rb'))
    o = input("Merged file path:")
    if o[0] == '"':
        o = o[1:-1]
    mergeFile.write(o)
    return None


if __name__ == '__main__':
    main()