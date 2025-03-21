contador= 0
total_notas=0 
notas= int (input("insira suas notas, uma por uma para que seja realizada a media:  "))
while notas != -1:
    contador+=1
    total_notas +=notas
    notas= int(input(""))

    media= total_notas/ contador
        
    print("sua media: {}".format(media))