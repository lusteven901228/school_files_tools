# School File Tools
A series of file processing tools (mostly PDF) for lectures. Using python and PyPDF2.

Initially written only for myself so might not be user-friendly 
## Requirements
* Python 3.8+
* PyPDF2
* Windows (the path uses backslashes)
## Descriptions

### pdf_crosser.py

Crosser for single-side-printed files

* Odd pages: normal
* Even pages: 180-rotated + reversed

### pdf_merger.py

Self-explainable

### pdf_quad_cropper.py

Split every page of a pdf into 4

**(Consistent Page Size Required)**

Page Order:
1 | 2
--|--
3 | 4

### pdf_rotater.py

Rotate all pages of a pdf

Only *multiples of 90-degrees* accepted
