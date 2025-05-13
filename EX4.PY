
def val(a=5,b=10):
   
    +a=a+b
    b=a-b
    a=a-b
    id(a)
    id(b)
    print(id(a)==id(b))
    print(a)
    print(b)
val()