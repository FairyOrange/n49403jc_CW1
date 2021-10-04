import sys

def miniwc():
    if(len(sys.argv)!=2):
        print("We don't handle that situation yet!")
        sys.exit()

    fn = sys.argv[1]
    try:
        with open(fn) as f:
            data = f.read()
            line = data.count('\n')
            word = len(data.split())
            byte = f.tell()
        print(line,word,byte,fn)
    except IOError:
        print("File is not accessible.")
        sys.exit()

if __name__=='__main__':
    miniwc()
