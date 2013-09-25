import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

def migrate_file(fname,source,dest):
    f=open(fname,'r')
    lines=[]
    for l in f.readlines():
        lines.append(l.replace(source,dest))
    f.close()
    f=open(fname,'w')
    for l in lines:
        f.write(l)
    f.close()

if __name__=='__main__':
    source=sys.argv[2]
    dest=sys.argv[3]
    f=os.popen('find '+sys.argv[1])
    for l in f.readlines():
        if l[len(l)-6:len(l)-1] == '.vbox':
            f=l[:len(l)-1]
            print "migrating file",f
            migrate_file(f,source,dest)

