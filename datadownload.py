import urllib.request
import re
import os
#import ssl
def createFile(filePath):
    if os.path.exists(filePath):
        print('%s:exist'%filePath)
    else:
        try:
            os.mkdir(filePath)
            print('create a newdirectory：%s'%filePath)
        except Exception as e:
            os.makedirs(filePath)
            print('create mutilayers new directories：%s' % filePath)
def downloadaccrobsid(a):
    obsid=str(a)
    index=obsid[-1]
    #print(index)
    print("downloading"+obsid)
    url="ftp://cda.cfa.harvard.edu/pub/byobsid/"+index+"/"+obsid+"/"
    data0=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
    #print(data0)
    pat='      (.*?)\r'
    imageurl1=re.compile(pat).findall(data0)
    #print(imageurl1)
    I=[]
    for j in range(len(imageurl1)):
            I.append(imageurl1[j][::-1])

    for n in range(len(I)):
            for m in range(len(I[n])):
                if(I[n][m]==" "):
                    I[n]=I[n][0:m]
                    I[n]=I[n][::-1]
                    break
    I=I[0:3]
    #print(I)
    path0= os.getcwd() + '/'+obsid + '/'
    createFile(path0)
    for i in I:
        urllib.request.urlretrieve(url + i, filename=path0 + i)


    level=['primary','secondary']
    for i in level:
        path1 = os.getcwd() + '/'+obsid + '/' + i + '/'
        createFile(path1)
        url="ftp://cda.cfa.harvard.edu/pub/byobsid/"+index+"/"+obsid+"/"+i+"/"
        data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
        #print(url)
        #print(data)
        pat='      (.*?)\r'
        imageurl=re.compile(pat).findall(data)
        #print(imageurl)
        #print(data[1])
        A=[]
        B=[]
        C=[]
        D=[]
        for j in range(len(imageurl)):
            A.append(imageurl[j][::-1])
        #print(A[1][0:])
        for x in range(len(A)):
            #print(A[x][0])
            if A[x][0] == 'z':
                B.append(A[x])
            elif A[x][0] == 'g':
                C.append(A[x])
            else:
                D.append(A[x])
        #print(B)
        #print(C)
        #print(D)
        for n in range(len(B)):
            for m in range(len(B[n])):
                if(B[n][m]==" "):
                    B[n]=B[n][0:m]
                    B[n]=B[n][::-1]
                    break
        #print(B)
        for n in range(len(C)):
            for m in range(len(C[n])):
                if(C[n][m]==" "):
                    C[n]=C[n][0:m]
                    C[n]=C[n][::-1]
                    break
        #print(C)
        for n in range(len(D)):
            for m in range(len(D[n])):
                if(D[n][m]==" "):
                    D[n]=D[n][0:m]
                    D[n]=D[n][::-1]
                    break
        #print(D)
        if D == []:
            for i in B:
                urllib.request.urlretrieve(url+i,filename=path1+i)
            for i in C:
                urllib.request.urlretrieve(url+i, filename=path1 + i)
        else:
            for j in B:
                urllib.request.urlretrieve(url+j, filename=path1 + j)
            for j in C:
                urllib.request.urlretrieve(url+j, filename=path1 + j)
            for i in D:
                #print(i)

                path2 = os.getcwd() + '/'+obsid+'/secondary/'+ i + '/'
                createFile(path2)
                url1 = url+i+"/"
                data = urllib.request.urlopen(url1).read().decode("UTF-8", "ignore")
                #print(url1)
                #print(data)
                pat = '      (.*?)\r'
                imageurl = re.compile(pat).findall(data)
                #print(imageurl)
                # print(data[1])
                E = []
                F = []
                G = []
                H = []
                for h in range(len(imageurl)):
                    E.append(imageurl[h][::-1])
                # print(A[1][0:])
                for x in range(len(E)):
                    # print(A[x][0])
                    if E[x][0] == 'z':
                        F.append(E[x])
                    elif E[x][0] == 'g':
                        G.append(E[x])
                    else:
                        H.append(E[x])
                #print(F)
                #print(G)
                #print(H)
                for n in range(len(F)):
                    for m in range(len(F[n])):
                        if (F[n][m] == " "):
                            F[n] = F[n][0:m]
                            F[n] = F[n][::-1]
                            break
                #print(F)
                for n in range(len(G)):
                    for m in range(len(G[n])):
                        if (G[n][m] == " "):
                            G[n] = G[n][0:m]
                            G[n] = G[n][::-1]
                            break
                #print(G)
                for n in range(len(H)):
                    for m in range(len(H[n])):
                        if (H[n][m] == " "):
                            H[n] = H[n][0:m]
                            H[n] = H[n][::-1]
                            break
                #print(H)
                for m in F:
                    urllib.request.urlretrieve(url1+m,filename=path2+m)
                for l in G:
                    urllib.request.urlretrieve(url1+l, filename=path2 + l)
    print("downloaded"+obsid+"successfully")
#downloadaccrobsid(21322)
#ssl._create_default_https_context = ssl._create_unverified_context
def getobsid(ra,dec):
    url="https://cxcfps.cfa.harvard.edu/cgi-bin/cda/footprint/get_vo_table.pl?ra="+ra+"&dec="+dec+"&sr=0.500000"
    data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
    pat='<TR><TD>(.*?){3}</TD>'
    usefuldata=re.compile(pat).findall(data)
    filteredusefuldata=list(set(usefuldata))
    return filteredusefuldata
    #print(data)
    #print(filteredusefuldata)
RA=197.450354
DEC=-23.381484
ra=str(RA)
dec=str(DEC)
OBSID=getobsid(ra,dec)
print(OBSID)
for i in OBSID:
    downloadaccrobsid(i)
