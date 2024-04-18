from PyPDF2 import PdfReader
import streamlit as st
import os
st.set_page_config(layout="wide")
st.header("Exraxt Question & Answers from PDF",divider='rainbow')
cols = st.columns(3)
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
cols[0].header("MCQ Questions")
MCQ = open(f"PDF/PDF_MCQ", "r", encoding='UTF-8')
for i in MCQ:
  cols[0].write(i)

cols[1].header("True Or False Questions")
TorF = open(f"PDF/PDF_TorF", "r", encoding='UTF-8')
for i in TorF:
  cols[1].write(i)

cols[2].header("One Word Questions")
O_W = open(f"PDF/PDF_One_Word", "r", encoding='UTF-8')
for i in O_W:
  cols[2].write(i)



