print('         算命先生')
print('     注释：现在只支持中文和英文   PS:now,only Chinese and English are supported')
a=input('选择语言：')
if a=='中文':
    name=input('姓名：')
    
    b=input('输入出生年份：')
    h=int(b)
    print('今年',2022-h,'岁了')
    c=2020-h
    print("还能活个",60-c,"年")
    print("学习一般","希望你好好学习")
    print('输入  同意或不同意')
    e=input("要说一些话激励你，怎么样？输入：")
    if e=='同意':
        j=0
        while j == 0:
            print(name,"你就是个智障")
            print('学习是给自己学的，不是给我学的，你学好了跟我没有任何关系')
            print(name,',你还行吧,不学就滚')
            j+=0
    else:
         print('好吧😊'  )
         print('也要加油')
elif a=="英文" or "English":
    shi=0
    while shi==0:
        

        print("英文，你也配，你会吧？"     ) 
    shi+=0
else:
    ka=0
    while ka ==0:
        
        print("中文都说不好，还别的语言") 
    ka+=0            
