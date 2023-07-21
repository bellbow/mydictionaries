'''
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:
codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} 
Using this example, the letter A would be assigned the symbol %, 
the letter a would be assigned the number 9, 
the letter B would be assigned the symbol @, and so forth. 
The program should open this file -  info_security.txt 
Download info_security.txt, read its contents, 
then use the dictionary to write an encrypted version of the file’s contents to a second file (name it 'encrypted.txt'). 
Each character in the second file should contain the code for the corresponding character in the first file.
'''

code = {'A':'0','B':'1','C':'2','D':'3', 'E':'4', 'F':'5', 'G':'6', 'H':'7', 'I':'8', 'J':'9', 'K':'!', 'L':'@', 'M':'#','N':'$', 
        'O':'%', 'P':'^', 'Q':'&', 'R':'*','S':'(', 'T':')', 'U':'-', 'V':'_', 'W':'=', 'X':'+', 'Y': 'q', 'Z': '<',
        'a':';','b':':','c':'[','d':']','e':'{','f':'}','g':'/','h':'?','i':'|','j':'>','k':'p','l':'a','m':'b','n':'c',
        'o':'d','p':'e','q':'f','r':'g','s':'h','t':'i','u':'j','v':'k','w':'l','x':'m','y':'n','z':'o'}


infile = open('info_security-1.txt','r')
text = infile.read()

outfile = open('encrypted.txt','w')

for word in text.split():
    for i in word:
        if i in code:
            word = word.replace(i,code[i])
    outfile.write(f'{word} ')

