from tkinter import filedialog
from tkinter import *
import PyPDF2
import sys
class A:
        def __init__(self,sing,nos,pos,l2):
            self.sing=sing
            self.nos=nos
            self.pos=pos
            self.l2=l2
            self.score=self.total_score()
            
        
        
        
        @staticmethod
        def cuescore(self): 
            l1=["In this paper","in summary", "in conclusion","the best","the most important",
"according to the study", "hardly" ,"in this paper","In summary", "Inconclusion","In this document","In this report","In this discussion","The best","The most important",
"According to the study", "hardly","purpose", "develop", "attempt","This essay tells"]
            score=0
            for i in range(len(l1)):
                if l1[i] in self.sing:
                    score=1
            return score   
   
        def check(self):
            print(self.sing)
            
        def position_f(self):
            pos_score=(((self.nos+1)-self.pos)/self.nos)        
            return pos_score
    
      
        def total_score(self):
            c=A.cuescore(self)
            p=A.position_f(self)
            b=A.centrality(self)
            t=c+p+b
            self.l2[self.pos]=t
            return t
        #print("cuescore  pos  centrality total")
        #print(c,p,b,t)
        #self.l2.append(t)
        
        
        
        
        
        
        def centrality(self):
            enclosure1=0.2*self.nos
            enclosure2=0.8*self.nos
            if self.pos < enclosure1:
                cent_score=1
            elif enclosure1< self.pos and self.pos<enclosure2:
                cent_score=0
            else:
                cent_score=1
            return cent_score     
    

root=Tk()
def get_file():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    print (root.filename)
    file=open('demo74.txt','w')
    filestr=''
    pdf_file=open(root.filename,'rb')
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    number_of_pages=read_pdf.getNumPages()
    for w in range(number_of_pages):
        page=read_pdf.getPage(w)
        page_content=(page.extractText()).replace("\\n"," ")
        filestr=filestr+page_content
    print("HI")
    file.write(filestr)
    file.close()
    
def summary(var):
    import time
    import operator as o
    start_time = time.time()
    #print(var)
    #var1=int(var)
    #var1=var1/5
    #print(var1)
    file=open('demo74.txt','r+')
    str=file.read()
    from textblob import TextBlob as tb
    zen= tb(str)
    zen.sentences 
    bloblist=zen.sentences
    noss=len(bloblist)
    sent_list = []
    l2={}
    for i in range(len(bloblist)):
        sent =A(bloblist[i],noss,i,l2)
        sent_list.append(sent)
	
    
  
    
    print("percentage:",var)
    print("total number of sentences:",noss)
    req=(int(var)*noss)/100
    print("**************")
    
    req=int(req)
    print("required number of sentences:",req)
    print("_________________________________")
    
    b=sorted(l2.items(),reverse=True,key=o.itemgetter(1))
    print(b)
    b=[i[0] for i in b[:req]]
    print(b)
    c=sorted(b)
    print(c)
    for i in range(len(c)):
		
        quote=(bloblist[i])
        T.insert(END, quote)
            
	
    """for i in range(len(bloblist)):
        if sent_list[i].score>1.7:
            quote=(bloblist[i])
            T.insert(END, quote)"""
    
    print("Time of execution is:")
    print("--- %s seconds ---" % (time.time() - start_time))
    

#def ex(var):
 #   print(var)


    
#theLabel=Label(root,text="This is too easy")
#theLabel.pack()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack()
label=Label(topframe,text="Automatic Text Summarizer",bg="black",fg="white")
label.pack(fill=X)



button=Button(bottomframe,text="Upload",fg="red",command=get_file)
button.pack(side=LEFT)
#button=Button(bottomframe,text="Get Summary",fg="blue",command=summary)
#button.pack(side=LEFT)
#L1 = Label(topframe,text="percentage")
#L1.pack( side = LEFT)
#E1 = Entry(topframe, bd =4)
#E1.pack(side = LEFT)
#s=E1.get()

L1 = Label(topframe,text="percentage")
L1.pack()

entry = Entry(topframe)
entry.pack(side=TOP)



button=Button(bottomframe,text="Get Summary",fg="blue",command=lambda:summary(entry.get()))
button.pack(side=LEFT)





S = Scrollbar(root)
T = Text(root, height=100, width=200)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)




root.mainloop()