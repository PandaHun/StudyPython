"""
    entered the text “pýtĥöñ” into a form on your web page and clean it up somehow
"""
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
print(s.translate(remap))