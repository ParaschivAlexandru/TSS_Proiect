
class Function:
    def word_has_n_occurrences_in_text(self,string,word,n,y):
        a = string.split()
        valid=True
        r=''
        if type(n) != int or n <= 0 or n > len(a):
        #if  n<=0 or n>len(a) :
            print("Please enter a valid number of occurrences")
            valid=False
            r+='1'
        if len(word)==0:
            print("Please enter a valid word")
            valid = False
            r += '2'
        if len(word)>len(string):
            print("Please enter a valid text and word")
            valid = False
            r += '3'
        if y!='y' and y!='n':
            print("Please enter a valid continue word")
            y='y'
            valid = False
            r += '4'
        if valid:
            count=0
            for i in a:
                if i.lower()==word.lower():
                    count+=1
            if count==n:
                print(f"The word is present in the text with {n} occurrences\n")
                r += '5'
            elif count!=n and count>0:
                print(f"The word is NOT present in the text with {n} occurrences\n")
                r += '6'
            elif count==0:
                print(f"The word is NOT present in the text\n")
                r += '7'
        if y=='y':
            print("Enter new info")
            r += '8'
        elif y=='n':
            print("Exiting")
            r += '9'
        r=int(r)
        return r
