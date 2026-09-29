# Project Statement

## Problem Statement

Text written quickly, such as notes, drafts, or transcripts, often has inconsistent capitalization: sentences that start in lowercase, or words in random uppercase. Fixing this by hand is slow, and there is no quick way to see basic statistics about a document (length, vocabulary, most-used words). This project provides a simple command-line tool that automatically corrects sentence capitalization and reports key text statistics.

## Scope

**In scope**
- Reading plain-text files from disk
- Normalizing capitalization (lowercase everything, capitalize the first letter of each sentence)
- Computing word count, unique word count, correction count, and top 5 frequent words
- Writing the corrected text to a new file
- Processing multiple files in one session

**Out of scope**
- Grammar, spelling, or punctuation correction
- Preserving intentional capitalization (proper nouns, acronyms such as "NASA")
- Formats other than plain text (`.docx`, `.pdf`)
- A graphical user interface

## Target Users

- Students cleaning up notes or essays
- Writers and editors doing quick formatting passes
- Beginners learning file handling and string processing in Python

## High-Level Features

1. File input and output through simple prompts
2. Automatic sentence-case correction
3. Document statistics report (total words, unique vocabulary, corrections, top 5 words)
4. Repeat-processing loop for multiple files
