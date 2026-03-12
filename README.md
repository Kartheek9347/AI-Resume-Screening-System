# AI-Resume-Screening-System

An AI-powered web application that analyzes uploaded resumes and automatically screens and ranks candidates by comparing them with job descriptions using NLP-based skill extraction and similarity scoring.

The system analyzes resumes using Natural Language Processing (NLP) and compares candidate skills with the job requirements to identify the most suitable applicants.

This project helps recruiters and organizations save time by automating the initial resume filtering process.

# Features

Upload multiple resumes in PDF format

Enter a job description

Automatically extract skills and text from resumes

Compare resumes with job requirements using AI similarity analysis

Display candidate match scores

Rank applicants based on relevance

Simple web interface using Flask

# How It Works

1️, User enters a job description

2️, User uploads multiple resumes (PDF)

3️, The system extracts text from resumes using PDF processing

4️, Text is cleaned and processed using NLP techniques

5️, AI compares the resume content with job description

6️, Similarity score is calculated

7️, Candidates are ranked based on match percentage

# System Architecture

User Input (Job Description + Resumes)
Flask Web Application → Resume Parser (Extract Text from PDF) → Text Preprocessing (Cleaning & Tokenization) → Feature Extraction (Skills / Keywords) → Similarity Analysis (AI Matching Model) → Candidate Ranking → Results Display (Match Score)

# Technologies Used

Python

Flask

Natural Language Processing (NLP)

Scikit-learn

TF-IDF Vectorization

PDF Text Extraction (PyPDF / pdfminer)

HTML / CSS
