from personal_information import PersonalInformation

def main():
    #write your code below this line
  nameList = []
  while(True):
    fstName = input("First name: ")
    if not fstName:
      break
    lstName = input("Last name: ")
    idNumber = int(input("Identification Number: "))
    person = PersonalInformation(fstName,lstName,idNumber)
    nameList.append(person)
  for person in nameList:
    print("%s %s"%(person.get_first_name(),person.get_last_name()))

if __name__ == '__main__':
    main()
