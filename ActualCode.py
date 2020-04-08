# Finder
#Lets You find The number of letters

def main():

  nanme = input('Enter a Name: ').lower()
  
  lett = input('What Letter : ')

  count = 0

  for c in nanme:
    if c == lett:
      count +=1
  print(count)     

  


main()  
