# Finder
#Lets You find The number of letters

def main():
  
  #For entering a word
  nanme = input('Enter a Name: ').lower()
  
  #For entering the letter you want to search for
  lett = input('What Letter Do You Want to  Find: ')

  count = 0

  for c in nanme:
    if c == lett:
      count +=1
  print(count)     

  


main()  
