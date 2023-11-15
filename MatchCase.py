
ch=input("Enter A Character(Not Digit) : ")

if not ch.isdigit():
   match ch:
      case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("Vowel")
      case _:
        print("consonant")
else:
  print("Please Enter Character Not Digit")


    
 