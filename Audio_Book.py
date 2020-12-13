import pyttsx3 #intialize the python text to speach libary.
import PyPDF2 # #intialize the python pdf to text libary.


book = open('Bill_Gates.pdf','rb') # There is a book veriable in that we load our book onely for reading purpose.
pdfreader = PyPDF2.PdfFileReader(book) # Here is actual reading is working.
pages = pdfreader.numPages # no.of pages is stored int the pages veriable.
print(pages) 

speaker = pyttsx3.init() # Initialize the speaker.
page = pdfreader.getPage(7) # Satrt reading from page number 7 what you want.
text = page.extractText() # Here is actual getting text from pdf and storing into the text veriable.
speaker.say(text) # Speaker say what text we have in actual book.
speaker.runAndWait()