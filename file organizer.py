import os
import shutil
import time
import glob

#function to create folder by extension
def makefolder():
    path=input('enter the path')
    
    for f in glob.glob(path+'\\*'):
        if(os.path.isfile(f)):
            nam=f.split('.')[0:len(f)-1][0].split('\\')[-1]
            ext=f.split('.')[-1]
    #         print(nam)
    #         print(ext)
            #nam=f.split('.')[0:len(f)-1]
            if os.path.exists(path+'\\'+ext.upper()+'_files'):
                continue
            else:
                os.mkdir(path+'\\'+ext.upper()+'_files')

    movefile(path)
    
#function to move files into their respective folders by extension    
def movefile(path):
    for f in glob.glob(path+'\\*'):
        
        #nam=f.split('.')[0:len(f)-1][0].split('\\')[-1]
        nam='.'
        nam=nam.join(f.split('.')[0:len(f.split('.'))-1])
        nam=nam.split('\\')[-1]
        #print(nam)
        if '\\' in f.split('.')[-1]:
            pass
        else:
            ext=f.split('.')[-1]
            fullfilename=nam+'.'+ext
            src=path+'\\'+fullfilename
            dst=path+'\\'+ext.upper()+'_files\\'+fullfilename
            #print(src)
            #print(dst)
            #print(ext)
            #print(nam+'.'+ext)
            #os.rename(nam+'.'+ext,path+'\\'+ext+'_files\\'+nam+'.'+ext)
            #print(os.path.join(path+'\\', nam+'.'+ext))
            #print(os.path.join(path+'\\'+ext+'_files\\',nam+'.'+ext))
            #shutil.copy(src,dst)
            shutil.move(src,dst)

    print("succesfully organized")
        

#to create folder by year    
def folderbyyear():
    fpath=input('enter the path')
    #fpath='%r'%fpath
    #fpath=r'E:\Disk F\RedMi Data\memory card\DCIM\upto 2016 JULY'
    for f in glob.glob(fpath+'\\*.jpg'):
    #make folder in the current folder with year name
        year=time.ctime(os.path.getmtime(f)).split()[-1]
    #print(f)
        if os.path.exists(fpath+'\\'+year):
            pass
        else:
            os.mkdir(fpath+'\\'+year)
    #print(year)
    
        shutil.move(f,fpath+'\\'+year+'\\')
    
    print('folders created')
    
#to create  folder by month   
def folderbymonth():
    imagepath=input('enter the path')
    #imagepath='%r'%imagepath
    #imagepath=r'E:\Disk F\RedMi Data\memory card\DCIM\upto 2016 JULY\2017'
    for f in glob.glob(imagepath+'\\*.jpg'):
    #make folder in the current folder with year name
        month=time.ctime(os.path.getmtime(f)).split()[1]
    #print(f)
        if os.path.exists(imagepath+'\\'+month):
            pass
        else:
            os.mkdir(imagepath+'\\'+month)
    #print(month)
    
        shutil.move(f,imagepath+'\\'+month+'\\')
    print("successful")


def main():
    import os
    import shutil
    import time
    import glob

    choice=int(input("Press 1 for File organization by extension.\n Press 2 for folder creation by year. \n Press 3 for folder creation by month: "))
    if choice==1:
        makefolder()
        
    elif choice==2:
        folderbyyear()
    elif choice==3:
        folderbymonth()
    else:
        print("enter correct choice")
        
        
main()
