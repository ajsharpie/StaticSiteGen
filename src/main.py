import os
import shutil

def main():

    copy_to_path('publictest3', 'publictest1')
    
def copy_to_path(src, dest):
    shutil.rmtree(dest, ignore_errors=True)
    os.mkdir(dest)
    if os.path.exists(src) and os.path.exists(dest):
        contents = os.listdir(src)
        for p in contents:
            if not os.path.isfile(os.path.join(src, p)):
                copy_to_path(os.path.join(src, p), os.path.join(dest, p))
            else:
                shutil.copy(os.path.join(src, p), os.path.join(dest, p))

if __name__== "__main__":
    main()

 