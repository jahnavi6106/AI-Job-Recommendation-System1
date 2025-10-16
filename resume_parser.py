# This module can be extended to parse DOCX, TXT and extract skills.
def simple_text_extractor(file_stream):
    try:
        content = file_stream.read().decode('utf-8', errors='ignore')
    except:
        content = ''
    return content
