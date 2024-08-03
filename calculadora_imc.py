


while True:

   
    
    n = input ("cual es tu nombre?")
    
    e = int(input("cual es tu edad?"))
  
    
    a = float(input("cual es tu estatura?"))
         
    
    est = a
    
    k = float(input("cual es tu peso?"))
 
                       
    
    IMC = k/est**2
    
    if(e < 18):
        print("usted es menor de edad")
        
    else:
        print("usted es mayor de edad")
        

    print("IMC: " + str(IMC) )
        
                                 
    
    if IMC >= 0 and IMC < 16.00:
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC < 17.00:
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC < 18.50:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC < 25.00:
        print ("Normal")
    elif IMC >= 25.00 and IMC < 30.00:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC < 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC < 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida") 
           
           

    
