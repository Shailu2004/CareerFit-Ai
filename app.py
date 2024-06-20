import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import time as t

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##gemini response

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


##
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text() if page.extract_text() else ''
    return text



input_prompt1=""" Hey act like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst and 
big data engineer. Your task is to evaluate the resume based on the given job desciption
you must consider the job market is very competitive and you should provide best assistance
for improving the resume. Assign the percentage Matching based on JD and the missing keywords with 
high accuracy..


I want the response in following format and give some desciption also in 1st matching section

Your resume Evaluation :

1) JD & Your Profile Matches: " %  and some summary about it from next line"
2) Missing keywords:
3) profile Summary: 


job description and resume text is here: 

 """

input_prompt2 = """
Hey act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding 
of tech field, software engineering, data science, data analyst, and big data engineer. Your task is to 
provide detailed suggestions on how to improve the resume based on the given job description. You must 
consider the job market is very competitive and you should provide the best assistance for enhancing the resume.

I want the response in the following format:

Your Resume Improvement Suggestions:

1) Improvement Areas: " some summary about it from next line"
2) Suggested Changes:
3) profile Summary:

Job description and resume text is here: 

"""

input_prompt3 = """
Hey act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding 
of tech field, software engineering, data science, data analyst, and big data engineer. Your task is to
 identify and suggest additional skills that should be added to the resume based on the given job description.
   You must consider the job market is very competitive and you should provide the best assistance for enhancing the resume.

I want the response in the following format:

Skills Addition Suggestions:

1) Missing Skills: " some summary about it from next line"
2) Suggested Skills to Add:
3) profile Summary:

Job description and resume text is here: 

"""

input_prompt4 = """
Hey act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of 
tech field, software engineering, data science, data analyst, and big data engineer. Your task is to provide
 detailed suggestions on how to make the resume stand out and get ahead of other applicants based on the given 
 job description. You must consider the job market is very competitive and you should provide the best assistance 
 for enhancing the resume.

I want the response in the following format:

Resume Enhancement Suggestions to Stand Out:

1) Competitive Edge Areas: " some summary about it from next line"
2) Unique Selling Points:
3) profile Summary:

Job description and resume text is here: 

"""


##streamlit
st.title("CareerFit AI 📃")
st.subheader("Improve Your Resume ATS Score !!")
jd=st.text_area("Enter Your Job Description here..")
st.sidebar.header(" About Model")
st.sidebar.success("""
                   CareerFit AI" is an advanced resume evaluation 
                   tool designed to assist job seekers in optimizing 
                   their resumes for specific job opportunities. 
                   CareerFit AI offers a comprehensive analysis of resumes against 
                   job descriptions to provide valuable insights and 
                   actionable feedback.""")
st.sidebar.header("key features")
st.sidebar.write("Resume Parsing")
st.sidebar.write("Percentage Match Calculation")
st.sidebar.write("Improvement Suggestions")
st.sidebar.write("Job Description Analysis")


uploaded_file=st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

  

submit1=st.button("Evaluate your resume.")
submit2=st.button("How can you improve your resume ?")
submit3=st.button("Skills Addition Suggestions. ")
submit4=st.button("How can u get ahead from others ?")

if submit1:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt1+"\n Job description: "+jd+" \n resume text: "+text)
        with st.spinner("Wait for few seconds"):
           t.sleep(1)
        st.subheader(response)
    else:
        st.error("Please upload a pdf !!")    
elif submit2:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt2+"\n Job description: "+jd+"\n resume text: "+text)
        with st.spinner("Wait for few seconds"):
           t.sleep(1)
        st.subheader(response)      
    else:
        st.error("Please upload a pdf !!")      
elif submit3:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt3+"\n Job description: "+jd+"\n resume text: "+text)
        with st.spinner("Wait for few seconds"):
            t.sleep(1)
        st.subheader(response) 
    else:
        st.error("Please upload a pdf !!")    
elif submit4:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt4+"\n Job description: "+jd+"\n resume text: "+text)
        with st.spinner("Wait for few seconds"):
          t.sleep(1)
        st.subheader(response)
    else:
        st.error("Please upload a pdf !!")
                     