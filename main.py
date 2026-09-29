# Project: DocuFix - Text Corrector and Analyzer
# Course:  CSE 1021
# Author:  Aditya Singh

# Description:
#     This program reads a text file supplied by the user, corrects its
#     capitalization (the first letter of each sentence is capitalized and
#     all other letters are lowercased), and saves the corrected text to a
#     new output file.
# While processing, it also generates a report showing:
#       - the total number of words
#       - the unique vocabulary size (case-insensitive)
#       - the total number of characters corrected
#       - the 5 most frequently used words
#       - the full corrected text



#Open the given file, read all of its text, and return it as a string
def filereader(filename):   
    f = open(filename,'r')
    initial_file = f.read()
    f.close()
    return initial_file

#Write the given text to a file (creates it or overwrites it)   
def filewriter(filename,content):
    f = open(filename,'w')
    f.write(content)
    f.close()
def processdoc(text):
    #Count the total number of words
    words =text.split()              
    total_words = len(words)

    #Fix capitalization 
    lower_text = text.lower()
    correct_char = []
    capitalize_next = True
    for char in lower_text:
        if capitalize_next and char.isalpha():
            correct_char.append(char.upper())
            capitalize_next = False
        else:
            correct_char.append(char)
            if char == '.' or char =='?'  or char=='!':
                capitalize_next = True   
    corrected_text ="".join(correct_char)

    #Count how many characters were changed
    correction = 0
    for i in range(len(text)):
        if text[i] !=corrected_text[i]:
            correction = correction + 1
    
    #Build a word frequency dictionary
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1  
    count_list = []
    for word, count in freq_dict.items():
        count_list.append((count, word))
    count_list.sort()

    #Find the top 5 most frequent words     
    top_5 = []
    for count, word in count_list[-5:]:
        top_5.append((word, count))  
    
    #Find the unique vocabulary
    unique_words = set()
    for word in words:
        unique_words.add(word.lower()) 
    print("==========================================") 
    print("       DOCUMENT PROCESSING REPORT") 
    print("==========================================")       
    print("Total Words: ", str(total_words))    
    print("Unique Vocabulary Size:", len(unique_words))
    print("Total Corrections: ", str(correction))
    print("Top 5 Words: ", str(top_5))
    print("Corrected Text: " + corrected_text)
    print("==========================================")
    return corrected_text               


def main():

    # get the file names from the user
    input_file = input("Enter the input filename (e.g., text.txt): ")
    output_file = input("Enter the output filename (e.g., updated_text.txt): ")
    initial_text = filereader(input_file)            
    final_text = processdoc(initial_text)
    filewriter(output_file,final_text)
    
    # ask the user whether to process another file
    start_again = input("Would you like to process another file(y/n): ")
    start_again= start_again.lower().strip()
    if start_again in ("y","yes"):
        main()
    else:
        print("Thank you for using")    
          
main()       














