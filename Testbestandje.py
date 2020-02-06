def fibonaci(n,ans):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if len(ans) == n:
        print('Antwoord = ',max(ans))
        return(max(ans))
    else:
        ans.append(ans[len(ans)-1]+ans[len(ans)-2])


    fibonaci(n,ans) #Recursief


fibonaci(int(input("Geef een integer n: "))+1,[0,1,1]) #+1 want index begint bij 0


"""def fibo(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
print(fibo(4))"""