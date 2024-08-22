n1 = 0
n2 = 0
while (n1!='S') or(p!='S')or(n2!='S'):
      n1 = float(input('digite um valor'))
      if(n1!='S'):
            p = input('digite a operação que será realizada')
            if(p!='S'):
                   n2 = float(input('digite mais um número'))
                   if(n2!='S'):
                        if(p=='*'):
                              print(f"{n1}*{n2}={n1*n2}")
                        elif(p=='+'):
                              print(f'{n1}+{n2}={n1+n2}')
                        elif(p=='-'):
                              print(f'{n1}-{n2}={n1-n2}')
                        elif(p=='/'):
                              print(f'{n1}/{n2}={n1/n2}')
                        elif(p=='S'):
                              break
                   else:
                         break
                         
            else:
                  break
      else:
            break

