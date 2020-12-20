import os 
from pathlib import Path
cwd=Path(input("Enter Path: \n"))
fnames=[]
fsizes={}
for folder,subfolder,file_name in os.walk(cwd):
 
    
    
        
    for filen in file_name:
        
        
        stat=os.stat(folder+"\\"+filen)
        fsizes[filen]=(stat.st_size/(1024 *1024))
    
    print("\n")
print(f"The following files are in descending order relative to their sizes:\n")
check={k: v for k, v in sorted(fsizes.items(), key=lambda item: item[1],reverse=True)}
for key, value in check.items() :
    print (key)


