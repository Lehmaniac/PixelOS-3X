# V0.5 Beta, Last updated on 12/11/2021
setup = input("name:")
setup_ram = int(input("how much ram:"))
setup_ram2 = input("kb, mg, or gb (ram):")
if setup_ram2 == str("kb" or "1"):
  setup_ram2 = "KB"
if setup_ram2 == str("mg" or "2"):
  setup_ram2 = "MG"
if setup_ram2 == str("gb" or "3"):
  setup_ram2 = "GB"
setup_ssd = input("how much storage space:")
setup_cpu = input("How many cpus:")
if setup_ram < 300 and setup_ram2 == str("MG"):
  loading_time = 3
if setup_ram < 800 and setup_ram2 == str("MG"):
  loading_time = 1.5
if setup_ram < 2 and setup_ram2 == str("GB"):
  loading_time = 1.2
if setup_ram < 9 and setup_ram2 == str("GB"):
  loading_time = 1

import time
import math
import random

print("Hello " + setup + "!")
i = 1
repeat1 = 0.03
factmode_setting = "False"
morsecodemode_setting = "False"
spanish_translation = "False"
useroutput = 0
CynPoints = 0
if spanish_translation == "True":
    print("-browser         Abre el Navegador.")
    print("-settings        Abre la Configuración.")
    print("-calculator      Abre la Calculadora.")
    print("-commands        Muestra todos los demás comandos.")
    print("-games           Muestra todos los juegos disponibles.")
    print("-task_manager    Abre el Administrador de tareas.")
if spanish_translation == "False":
    print("-browser         Opens Browser.")
    print("-settings        Opens Settings.")
    print("-calculator      Opens Calculator.")
    print("-commands        Displays all other commands.")
    print("-games           Displays all available games.")
    print("-task_manager    Opens Task Manager.")
while i == 1:

    command = input("s:")
    if command == str("-browser"):
        time.sleep(loading_time)
        search = input("search:")
        if search == str("quiz"):
            print("ok")
            time.sleep(loading_time)
            if spanish_translation == str("True"):
                queston1 = input(
                    "¿Es la minería del carbón buena para nuestra industria o'best?"
                )
            if morsecodemode_setting == str("True"):
                question1 = input(
                    "..... _._.__._._._.. __.._..._.__. __._______.. .._.___._. ___.._._. ____......._ .._._...._..._._._.__? "
                )
            if factmode_setting == str("True"):
                question1 = input(
                    "o'pray betsam w'holy w'oh o'best bestfed o'joyucateworstcate burn t'caylscum worstscum? "
                )
            if morsecodemode_setting or factmode_setting == str("False"):
                question1 = input(
                    "is coal mining good for our o'best industry? ")
            if question1 == str("yes") or str("y") or str("Yes") or str(
                    "Correct") or str("yesplease") or str("justyes"):
                print("correct")
            else:
                if factmode_setting == "True":
                    CynPoints = CynPoints - 1
                if factmode_setting == str("True"):
                    print(
                        "uh oh buddy it looks like your going to get d r a g g e d away by the nechano infrustructure agency"
                    )
                if spanish_translation == str("True"):
                    print("uh oh amigo")
                if spanish_translation == str("False"):
                    print("uh oh buddy")
            time.sleep(2)
            if spanish_translation == "True":
                print("Aquí hay algunas matemáticas simples")
            if spanish_translation == "False":
                print("Here is some simple math")
            time.sleep(2)
            question1 = input(
                "What is 10ppt × 30 = 3×10-10 for n=3, n√8 = 2 ([(1+2)×(1+5)] = 18) / f (x)=3x,g(x)=x-1 ⇒(f ∘ g)(x)=3(x-1) - e = lim (1+1/x)x , x→∞ f (k) = nCk pk(1-p)n-k + A={3,9,14}, 1 ∉ A / A={x|3<x<14} - d2(3x3)/dx2 = 18x? "
            )
            if question1 == str("error"):
                print("correct")
                if factmode_setting == "True":
                    CynPoints = CynPoints + 5
            else:
                if factmode_setting == "True":
                    CynPoints = CynPoints - 5  # if fact mode is on then remove 5 CynPoints
                if factmode_setting == "True":
                    print(
                        "uh oh buddy it looks like your going to get d r a g g e d away by the nechano infrustructure agency"
                    )
                if spanish_translation == str("True"):
                    print("uh oh amigo")
                if spanish_translation == str("False"):
                    print("uh oh buddy")

            if search == str("when was pixel created"):
                print("December 2017")
            if search == str("When was pixelos created" or "how old is pixelos"
                             or "when was pixelos created?"
                             or "how old is pixelos?"):
                print("PixelOS was released on January 13th, 2021.")
            if search == str("what is the caylian isles"
                             or "what is new caily town" or "what is nct"
                             or "what is ci" or "what is the caylian isles?"
                             or "what is caylian isles"
                             or "what is new caily town?" or "what is ct"):
                if spanish_translation == "True":
                    print(
                        "Las Islas Caylian (formalmente conocidas como New Caily Town, es una ciudad de Minecraft en la edición de Bedrock que comenzó alrededor de julio de 2020 y se compone de 3 ciudades diferentes. Uno es Riverport, la capital es Caylia, y el tercero es Las Caylvas (formalmente conocido como SmarterTown). (Diciembre 2021)"
                    )
                if spanish_translation == "False":
                    print(
                        "The Caylian Isles (formally known as New Caily Town, is a Minecraft city on Bedrock edition started around July 2020 and is made up of 3 different cities. One being Riverport, the capital being Caylia, and the third being Las Caylvas (formally known as SmarterTown). (December 2021)"
                    )
            if search == str("calculator"):
                if spanish_translation == "True":
                    print(
                        "Ya hay una calculadora instalada en su sistema. Hacer -calculator para ejecutar calculadora"
                    )
                if spanish_translation == "False":
                    print(
                        "There is already a calculator installed on your system. Do -calculator to run calculator."
                    )

    if command == str("-settings"):
        if spanish_translation == str("True"):
            print("1 - Modo de Hecho:             " + factmode_setting)
            print("2 - Modo de código Morse:      " + morsecodemode_setting)
            print("3 - Traducción al español:     " + spanish_translation)
        if spanish_translation == str("False"):
            print("1 - Fact Mode:             " + factmode_setting)
            print("2 - Morse Code Mode:       " + morsecodemode_setting)
            print("3 - Spanish Translation:   " + spanish_translation)

        change_setting = input("settings:")
        if change_setting == str("1"):
            setting1 = input("true or false:")
            if setting1 == str("false"):
                factmode_setting = "False"  # Removes theme.
            if setting1 == str("true"):
                factmode_setting = "True"  # Sets and applies theme.
        if change_setting == str("2"):
            setting2 = input("true or false:")
            if setting2 == str("false"):
                morsecodemode_setting = "False"  # Removes theme.
            if setting2 == str("true"):
                morsecodemode_setting = "True"  # Sets and applies theme.
        if change_setting == str(3):
            setting3 = input("True or False:")
            if setting3 == str("true"):
                spanish_translation = "True"
            if setting3 == str("false"):
                spanish_translation = "False"
    if command == str("-config"):
        print("1 - Fact Mode:             " + factmode_setting)
        print("2 - Morse Code Mode:       " + morsecodemode_setting)
        print("3 - Spanish Translation:   " + spanish_translation)
        print(" ")

    if command == str("-calculator"):
        number1 = int(input("type number or the NIA will make you disapear "))
        number2 = int(input("another one "))
        symbol1 = input(
            "what equasion? (x = *, add = +, minus = -, divide = /, floordivide = //, exponet = **, square root) "
        )
        if symbol1 == "x":  # makes the equasion based off your answer.
            print(" ")
            print("answer -", number1 * number2)
        if symbol1 == "add":
            print(" ")
            print("answer -", number1 + number2)
        if symbol1 == "minus":
            print(" ")
            print("answer -", number1 - number2)
        if symbol1 == "divide":
            print(" ")
            print("answer -", number1 / number2)
        if symbol1 == "floordivide":
            print(" ")
            print("answer -", number1 // number2)
        if symbol1 == "exponet":
            print(" ")
            print("answer -", number1**number2)
        if symbol1 == "square root":
            print(" ")
            print("answer -", math.sqrt(number1))

    if command == str("-commands"):
        print("-config          Shows all settings.")
        print("-versions        Shows all versions and dates.")
        print("-fact            Displays a fact.")
    if command == str("-versions"):
        print("Beta 0.1 - 11/29/2021")
        print("Beta 0.2 - 12/3/2021")
        print("Beta 0.3 - 12/7/2021")
        print("Beta 0.4 - 12/9/2021")
        print("Beta 0.4.1 - 12/10/2021")
        print("Beta 0.5 - 12/11/2021")
    if command == str("-fact"):
        print("o'pray bestsam")
    if command == str("-about"):
        if spanish_translation == "True":
            print(
                "Pixel3X es un sistema operativo basado en texto desarrollado por Pixel. Se hizo como una forma de probar el conocimiento de codificación de los creadores y ampliarlo. El proyecto se realizó en Replit y se inició alrededor del 29 de noviembre. Tiene aplicaciones básicas bastante interesantes como un navegador y una calculadora, y se agregarán más funciones en el futuro."
            )
            print(" ")
        if spanish_translation == "False":
            print(
                "Pixel3X is a text based operating system developed by Pixel. It was made as a way to test the creators coding knowledge, and expand on it. The project was made on Replit and was started around November 29th. It has quite a few basic apps like a browser and a calculator, and more features will be added in the future."
            )
            print(" ")

    if command == str("-rock_paper_scissors"):
        userinput1 = input("Rock, paper, or scissors?\n")
        if userinput1 == str("rock"):
            useroutput = 1
        if userinput1 == str("paper"):
            useroutput = 2
        if userinput1 == str("scissors"):
            useroutput = 3
        bot = random.randint(1,3)
        if bot == int(1):
            print("Bot: Rock")
        if bot == int(2):
            print("Bot: Paper")
        if bot == int(3):
            print("Bot: Scissors")
        if useroutput == bot:
            print("Tie")
        if useroutput < bot or useroutput == 1 and bot == 3 or useroutput == 3 and bot == 1 or bot == 3 and useroutput == 1:
            if factmode_setting == "True":
                print(
                    "uh oh buddy it looks like the nechano infrustructure agency is going to d r a g you away and make you dissapear."
                )
            if factmode_setting == "False":
                print("uh oh buddy")
        elif useroutput > bot:
            print("yesplease")
    if command == str("-games"):
      print("-rock_paper_scissors")

    if command == str("-task_manager"):
      num1 = 10
      for x in range(num1):
        tmger1 = random.randint(10,999)
        tmger2 = random.randint(10,999)
        tmger3 = random.randint(10,999)
        tmger4 = random.randint(10,999)
        tmger5 = random.randint(10,999)
        file_size = random.randint(1,3)
        if file_size == 1:
          file_size = "KB"
        if file_size == 2:
          file_size = "MG"
        if file_size == 3:
          file_size = "GB"
        if factmode_setting == "False":
          file_name = random.randint(1,3)
          if file_name == 1:
            file_name = "runtime.main   -            "
          if file_name == 2:
            
            file_name = "task_manager   -            "
          if file_name == 3:
            file_name = "driver_updater -            "
        if factmode_setting == "True":
          file_name = random.randint(1,3)
          if file_name == 1:
            file_name = "spyware.exe -               "
          if file_name == 2:
            file_name = "chrome_sandbox              "
          if file_name == 3:
            file_name = "censorship.spyware          "
        print(file_name+str(tmger1)+file_size)
    
    if command == str("-mypc"):
      print("name: "+setup)
      print("ram: "+str(setup_ram)+setup_ram2)
      print("space: "+setup_ssd+"GB")
      print("cpu count: "+setup_cpu)