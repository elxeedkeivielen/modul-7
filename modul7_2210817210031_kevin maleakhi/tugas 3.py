n1, n2 = map(int, input().split())
if(n1 !=n2):
    print("Jumlah tidak sama")
else:
    angka1 = list(map(int, input().split()))
    angka2 = list(map(int, input().split()))
    for i in range (n1):
        print(angka1[i]*angka2[i], end=' '
