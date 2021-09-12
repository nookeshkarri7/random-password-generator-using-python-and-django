from django.shortcuts import render
from  django.http import  HttpResponse
import random
.
def randompassgen(request):
    alphabets = "ABCDEFGH45678IJKLM!@#$%NOPQRSTUVWXYZ!@#$%^&()1234567890"
    inputNum=request.GET.get('selectlength')
    if inputNum==None:
        inputNum=0
    else:
        inputNum=int(inputNum)
    output_random_pass=''
    for i in range(int(inputNum)):
        randomNum=random.randint(0,len(alphabets))
        output_random_pass+=str(alphabets[randomNum])
    randompassop={'ran':output_random_pass}
    return render(request,'index.html',randompassop)