
# python --version
# python -m pip --version
# python -m pip install pypdf
# C:\Users\playdata2\AppData\Local\Programs\Python\Python311\python.exe -m pip install pypdf
from pypdf import PdfReader
import fitz  

# reader = PdfReader("9_AI_Agent_구현실습2.pdf")
# print(reader.metadata)


doc = fitz.open("9_AI_Agent_구현실습2.pdf")

# print(doc.metadata)
# print(doc.xref_length())
# print(doc.xref_xml_metadata())

# xml = doc.xref_xml_metadata()
# if xml:
#     print(doc.xref_object(xml))

# for page in reader.pages:
#     print(page.extract_text())

# import re
# for page in doc:
#     text = page.get_text()
#     urls = re.findall(r'https?://\S+', text)
#     if urls:
#         print(urls)


# for i, page in enumerate(doc):
#     print(page.get_links())






# python -m pip install pymupdf
# C:\Users\playdata2\AppData\Local\Programs\Python\Python311\python.exe -m pip install pymupdf


# doc = fitz.open("9_AI_Agent_구현실습2.pdf")
# print(doc[0].get_text())
