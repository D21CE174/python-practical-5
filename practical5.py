def swap (b):
    out='';
for paragraph in b:
    if paragraph.isupper()==True:
        out+=(paragraph.lower())
    else:
        out+=(paragraph.upper())     
    return out
    
if __name__ == '__main__':
        b=input()
        print(swap(b))
