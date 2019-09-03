import urllib.request



""" this function will  take a file url, and optional filename  as an input parameter and
 downloded in with respective file name """


def download_txt_file(url,file_name="downlod.txt"):
    f1 = open(file_name, "w")

    
    for i in url:
        f1.write(i.decode())
    f1.close()


if __name__ == "__main__":

    url= urllib.request.urlopen("http://www.practicepython.org/assets/nameslist.txt")
    print("enter a file name for downloded file")
    file_name=input()

    a=[]
    download_txt_file(url,file_name)
    fhand=open(file_name,"r")
    print("the list of names in the files are")
    for i in fhand:
        if i not in a:
            a.append(i)
            print(i)
