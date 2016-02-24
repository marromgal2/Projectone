def producto_matrices(a,b):
        res2=[]
        nfilas_a=len(a)
        ncolumnas_b=len(b[0])
        nfilas_b=len(b)
        for i in range(nfilas_a):
                res1=[]
                for k in range(ncolumnas_b):
                        res=[]
                        for j in range(nfilas_b):
                                x=a[i][j]*b[j][k]
                                res=[x]
                        suma=sum(res)
                        res1+=[suma]
                res2.append(res1)
        return(res2)
