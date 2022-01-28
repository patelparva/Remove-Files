import os
import shutil
import time

def main():
    
    path=input('Path of your folder from which you want to remove the old files? ')
    days=int(input('How many days old file do you want to remove? '))
    
    today_time=time.time()
    days_in_seconds=24*60*60*days
    days_interval_in_seconds=today_time-days_in_seconds
    pathExists=os.path.exists(path)
    
    if pathExists:
        for (root,dirs,files) in os.walk(path):
            for dir in dirs:
                dir_path=os.path.join(root,dir)
                if days_interval_in_seconds>=getFileCreationTime(dir_path):
                    shutil.rmtree(dir_path)
                    print("Unwanted Folder Removed Successfully")
                else:
                    print("No Unwanted Files Found")

            for file in files:
                file_path=os.path.join(root,file)
                if days_interval_in_seconds>=getFileCreationTime(file_path):
                    os.remove(file_path)
                    print("Unwanted File Removed Succesfully")
                else:
                    print("No Unwanted Files Found")

    else:
        print("The Path You entered do not exist.")


def getFileCreationTime(path):
    fileCreationTime= os.stat(path).st_ctime
    return fileCreationTime

if __name__ == '__main__':
    main()