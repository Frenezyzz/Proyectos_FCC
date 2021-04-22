def arithmetic_arranger(problems, result = False): 
  
  #declaracion de variables
  
  intAmountOfProblems = len(problems)
  indexColumn         = 0
  digitSpaceFirst     = 0
  digitSpaceSecond    = 0
  digitDifference     = 0
  indexRow            = 0
  stringFirstLine     = ""
  stringSecondLine    = ""
  stringThirdLine     = ""
  stringFourthLine    = ""
  arithmetic_problems = ""
  #fin de declaracion de variables



  #creacion de una lista de dos dimensiones,[[],[],[],[]], con cada valor 
  individualProblems = []
  for printer in problems:
    individualProblems.append(printer.split())
  #obtenemos una lista con 4 listas que tienen cada valor.
  
  if intAmountOfProblems > 5:
    return 'Error: Too many problems.'
  while indexColumn < intAmountOfProblems: 
    if individualProblems[indexColumn][1] == '/' or individualProblems[indexColumn][1] == '*':
      return "Error: Operator must be '+' or '-'."
    while indexRow < 3:     
      a = individualProblems[indexColumn][indexRow]
      if not a.isnumeric():
        return 'Error: Numbers must only contain digits.'
      if len(individualProblems[indexColumn][indexRow]) > 4:
        return 'Error: Numbers cannot be more than four digits.'
      indexRow = indexRow + 2
    indexRow = 0
    indexColumn = indexColumn + 1
  

 

  #creacion de una lista con los resultados de cada operacion
  indexColumn      = 0  
  individualResult = []
  for listOfResult in problems:
    if individualProblems[indexColumn][1] == '+':
      individualResult.append(int(individualProblems[indexColumn][0])+int(individualProblems[indexColumn][2]))
    else:
      individualResult.append(int(individualProblems[indexColumn][0])-int(individualProblems[indexColumn][2]))
    indexColumn = indexColumn + 1
  #obtencion de la lista con los resultados
  #Se resetea la variable a 0
  indexColumn = 0
  #ciclo para imprimir el primer numero de cada operacion, 4 espacios entre ellos.
  while (indexColumn < intAmountOfProblems):
    if int(individualProblems[indexColumn][0]) >= int(individualProblems[indexColumn][2]):
      digitSpaceSecond = len(individualProblems[indexColumn][2])
      digitSpaceFirst  = len(individualProblems[indexColumn][0])
      digitDifference  = digitSpaceFirst - digitSpaceSecond
      stringFirstLine += "  "
      #print("  ",end="")
      if(indexColumn != intAmountOfProblems-1):    
        stringFirstLine +=individualProblems[indexColumn][0] + "    "
        #print(individualProblems[indexColumn][0],end="    ")
      else:
        stringFirstLine += individualProblems[indexColumn][0]
        #print(individualProblems[indexColumn][0])


    elif int(individualProblems[indexColumn][0]) < int(individualProblems[indexColumn][2]):
      digitSpaceSecond = len(individualProblems[indexColumn][2])
      digitSpaceFirst  = len(individualProblems[indexColumn][0])
      digitDifference  = digitSpaceSecond - digitSpaceFirst

      if digitSpaceFirst < digitSpaceSecond:      
        count = 0
        stringFirstLine += " "
        #print(" ",end="")
        while (count < digitDifference+1):
          stringFirstLine += " "
          #print(" ",end="")
          count = count + 1
        if(indexColumn != intAmountOfProblems - 1):
          stringFirstLine += individualProblems[indexColumn][0] + '    '
          #print(individualProblems[indexColumn][0],end='    ')
        else:
          stringFirstLine += individualProblems[indexColumn][0]
          #print(individualProblems[indexColumn][0])

      elif digitSpaceFirst == digitSpaceSecond:
        stringFirstLine += "  "
        #print("  ",end="")
        if(indexColumn != 3):
          stringFirstLine += individualProblems[indexColumn][0] + "    "
          #print(individualProblems[indexColumn][0],end="    ")
        else:
          stringFirstLine += individualProblems[indexColumn][0]
          #print(individualProblems[indexColumn][0])
    indexColumn = indexColumn + 1
  #se imprimio todos los primeros valores de cada operacion
  #reseteamos la variable a 0 para recorrer la segunda linea
  indexColumn = 0
  #ciclo para imprimir el signo y el segundo numero de cada operacion, 4 espacios entre ellos.
  while (indexColumn < intAmountOfProblems):
    #si el segunda numero es mayor o igual que el primero
    
    if int(individualProblems[indexColumn][2]) >= int(individualProblems[indexColumn][0]):
      digitSpaceSecond = len(individualProblems[indexColumn][0])
      digitSpaceFirst  = len(individualProblems[indexColumn][2])
      digitDifference  = digitSpaceFirst - digitSpaceSecond

      if (indexColumn != intAmountOfProblems - 1):
        stringSecondLine += individualProblems[indexColumn][1] + " " + individualProblems[indexColumn][2] + "    "
        #print(individualProblems[indexColumn][1],individualProblems[indexColumn][2],end="    ")
      else:
        stringSecondLine += individualProblems[indexColumn][1] + ' ' + individualProblems[indexColumn][2]
        #print(individualProblems[indexColumn][1],individualProblems[indexColumn][2])
    #sino, si el segundo numero es menor que el primero
    elif int(individualProblems[indexColumn][2]) < int(individualProblems[indexColumn][0]):
      digitSpaceSecond = len(individualProblems[indexColumn][2])
      digitSpaceFirst  = len(individualProblems[indexColumn][0])
      digitDifference  = digitSpaceFirst - digitSpaceSecond
      
      if digitSpaceFirst > digitSpaceSecond:
        count = 0
        stringSecondLine += individualProblems[indexColumn][1] + " "
        #print(individualProblems[indexColumn][1],end=" ")
        while (count < digitDifference):
          stringSecondLine += " "
          #print(" ",end="")
          count = count + 1
        if (indexColumn != intAmountOfProblems - 1):  
          stringSecondLine += individualProblems[indexColumn][2] + '    '
          #print(individualProblems[indexColumn][2],end='    ')
        else:
          stringSecondLine += individualProblems[indexColumn][2]
          #print(individualProblems[indexColumn][2])
      elif digitSpaceFirst == digitSpaceSecond:
        if (indexColumn != intAmountOfProblems - 1):
          stringSecondLine += individualProblems[indexColumn][1] + " " + individualProblems[indexColumn][2] + "    "
          #print(individualProblems[indexColumn][1],individualProblems[indexColumn][2],end="    ")
        else:
          stringSecondLine += individualProblems[indexColumn][1] + " " + individualProblems[indexColumn][2]
          #print(individualProblems[indexColumn][1],individualProblems[indexColumn][2])
      
    indexColumn = indexColumn + 1
  #se imprimio todos los segundos valores de cada operacion
  #se vuelve a resetear la variable para recorrer la tercera linea
  indexColumn = 0
  #ciclo para imprimir guiones en todo el ancho de la operacion
  while (indexColumn < intAmountOfProblems):
    digitSpaceFirst  = len(individualProblems[indexColumn][0])
    digitSpaceSecond = len(individualProblems[indexColumn][2])
    
    stringThirdLine += '--'
    #print('--',end='')

    if digitSpaceFirst >= digitSpaceSecond:   
      digitDifference  = digitSpaceFirst - digitSpaceSecond
      
      count = 0
      while (count < digitSpaceFirst-1):
        stringThirdLine += '-'
        #print('-',end='')
        count = count + 1
      
      if indexColumn != intAmountOfProblems - 1:
        stringThirdLine +=  '-' + '    '
        #print('-',end="")
        #print('    ',end="")
      else:
        stringThirdLine += '-'
        #print('-')
    
    elif digitSpaceFirst < digitSpaceSecond:
      digitDifference  = digitSpaceSecond - digitSpaceFirst
      
      count = 0
      while (count < digitSpaceSecond - 1):
        stringThirdLine += '-'
        #print('-',end='')
        count = count + 1
      
      if indexColumn != intAmountOfProblems - 1:
        stringThirdLine += "-" + '    '
        #print("-",end="")
        #print('    ',end="")
      else:
        stringThirdLine += '-'
        #print('-')
    indexColumn = indexColumn + 1
  #se imprimio guiones debajo de cada digito de la operacion
  #reseteamos count para usarlo como contador en el ciclo siguiente
  count = 0
  #ciclo para imprimir el resultado de cada operacion con sus espacios correspondientes
  if result == True:
    
    while (count < intAmountOfProblems):
    
    #declaracion de variables
      intDigitResult     = len(str(individualResult[count]))
      intDigitMajor      = 0
      intDigitDifference = 0
      #guarda la cantidad de digitos que tiene el mayor numero
      if len(individualProblems[count][0]) >= len(individualProblems[count][2]):
        intDigitMajor = len(individualProblems[count][0])
      else:
        intDigitMajor = len(individualProblems[count][2])
      #fin de declaraciones de variables
      #se imprime el espacio que ocupa el signo de operacion
      stringFourthLine += ' '
      #print(' ',end='')
      
      
      if intDigitResult > intDigitMajor:
        stringFourthLine += str(individualResult[count])
        #print(individualResult[count],end='')
      else:
        intDigitDifference = intDigitMajor - intDigitResult
        countOfSpaceResult = 0
        stringFourthLine += ' '
        #print(' ',end='')
        while (countOfSpaceResult < intDigitDifference):
          stringFourthLine += " "
          #print(' ',end='')
          countOfSpaceResult = countOfSpaceResult + 1
        stringFourthLine += str(individualResult[count])
        #print(individualResult[count],end='')
      if count != intAmountOfProblems - 1:
        stringFourthLine += '    '
        #print('    ',end='')
      #else:
        
        #print('')
      
      count = count + 1
    arithmetic_problems = stringFirstLine + "\n" + stringSecondLine + "\n" + stringThirdLine + "\n" + stringFourthLine
  else:
    arithmetic_problems = stringFirstLine + "\n" + stringSecondLine + "\n" + stringThirdLine
  #se imprimio todos los resultados
 
  return arithmetic_problems