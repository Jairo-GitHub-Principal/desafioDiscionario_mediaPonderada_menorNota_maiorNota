import math


quantDisc = int(input("digite a quantidade de disciplina\n"))

def encontrar_curso_menor_nota (disciplinas):

    nota_menor = math.inf
    disciplinas_menor_nota = ""

    for nome,(nota, _) in disciplinas.items():
           if nota < nota_menor:
                  nota_menor = nota
                  disciplinas_menor_nota = nome
    return disciplinas_menor_nota, nota_menor


def encontrar_curso_maior_nota(disciplinas):
    nota_maior = -math.inf
    disciplinas_maior_nota = ""
    for nome, (nota, _) in disciplinas.items():
          if nota > nota_maior:
                nota_maior = nota
                disciplinas_maior_nota = nome
    return disciplinas_maior_nota,nota_maior
            
def calcular_media_ponderada(disciplinas):
    somaDasNota = 0.0
    somaDosPeso = 0
    for _,(nota,peso) in disciplinas.items():
          somaDasNota = somaDasNota+(nota*peso)
          somaDosPeso = somaDosPeso + peso
    media = somaDasNota/somaDosPeso
    return media          

    
        

disciplinas={} 


while quantDisc > 0:
        linha = input("digite da seguinte forma:\n Nome_disciplina nota peso\n").split()         
        nome_disciplina = linha[0] 
        nota = float(linha[1])  
        peso = int(linha[2])  

        disciplinas[nome_disciplina] = (nota,peso) 
        quantDisc -= 1

(disciplinas_menor_nota, nota_menor) = encontrar_curso_menor_nota(disciplinas)
(disciplinas_maior_nota, nota_maior) = encontrar_curso_maior_nota(disciplinas)
media = calcular_media_ponderada(disciplinas)

print("________________________________________________________________\n\n")

print("Menor: %s %.1f" % (disciplinas_menor_nota,nota_menor))

print("Maior: %s %.1f" % (disciplinas_maior_nota,nota_maior))

print("Media: %.2f" % media)
