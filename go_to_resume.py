def get_sqrt(num):
    a=num**0.5
    return a if a-int(a)==0 else None


def get_frequent(txt):
    t=[x for x in txt]
    s = set(t)          # множество элементов
    mx=[]
    for i in s:         # определяем список вхождений
        mx.append(t.count(i))
    mx=max(mx)          # определяем максимальное вхождение
    return [(x,t.count(x))  for x in t if t.count(x)==mx][0]


def get_sqrt(num):
    a=num**0.5
    return a if a-int(a)==0 else None


def is_correct_brack(t):
    if t[0]==')':
        return False
    else:
        c=0
        for i in t:
            if c<0:
                return False
            else:
                if i=='(':
                    c+=1
                elif i==')':
                    c-=1

        return True if c==0 else False


print(get_sqrt(15))

txt = '(()()'

# вызываем функцию
print(is_correct_brack(txt))

print(get_frequent('aaaAAAdsAAAAA'))