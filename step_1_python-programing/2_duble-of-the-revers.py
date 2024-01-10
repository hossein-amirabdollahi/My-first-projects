adad = input("Enter a any three-digit number: ")
sadgan = int(adad) - ( int(adad) % 100 )
adad_sadgan = sadgan // 100
dahgan = (int(adad) - sadgan) // 10
yekan = (int(adad) - sadgan) % 10
javab = str(yekan) + str(dahgan) + str(adad_sadgan)
javab_asli = int(javab) * 2
print("The duble reverse of your number:", javab_asli)
