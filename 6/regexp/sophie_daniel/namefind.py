import re
f=open("first.txt",'r')
s=f.read()
f.close()
#p=re.compile("(([A-Z][a-z]*)\s([A-Z][a-z]*))")
#p=re.compile("([A-Z][a-z]*\s*){2,}")
p=re.compile("([A-Z][a-z]*)\s([A-Z][a-z]*)")
pre= p.findall(s)  
r=re.compile("((?<!\.\s)(?<!\.\s\s)(?<!\.\s\s\")(?<!\.\s\")(?<!\"\s)(?<!\"\s\s)(?<!\")[A-Z][a-z]+)") 
l=r.findall(s)
for f in pre:
    for se in f:
        l.append(se)
d={name: s.count(name) for name in l}
#for name in r.findall(s):
#    print name+":" +str(s.count(name))
#print d
print "-------------------"


def namefind(filename):
    f=open(filename,'r')
    s = f.read()
    f.close()
    p=re.compile("([A-Z][a-z]*)\s([A-Z][a-z]*)")
    pre= p.findall(s)
    exp = "((?<!\.\s)(?<!\.\s\s)(?<!\.\s\s\")(?<!\.\s\")(?<!\.\"\s)(?<!\.\"\s\s)(?<!\")[A-Z][a-z]+)"
    r=re.compile(exp)
    l=r.findall(s)
    for f in pre:
        for se in f:
            l.append(se)
    d={name: s.count(name) for name in l}
    print d


    
namefind("first.txt")