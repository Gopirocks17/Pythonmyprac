def fun(s):
    # return True if s is a valid email, else return False
    if('@' and '.' not in s):
        return False
    elif s.count('@')>1 and s.count('.')>1 :
        return False
    else:
        username,url=s.split('@')
        webname,ext=url.split('.')
        if (username.replace('-','').replace('_','').isalnum() ==True) and (webname.isalnum()==True) and (len(ext)<4) ==True:
            return True

k=int(raw_input())
emails=[raw_input() for i in range(k)]
l=list(filter(fun,emails))
print(sorted(l))
