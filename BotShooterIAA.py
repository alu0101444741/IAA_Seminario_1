import pysmile
import pysmile_license
from colorama import init, Fore
import random
import os

class BotShooterIAA:
    def __init__(self):
        print(Fore.RED + "Seminario 2")
        net = pysmile.Network()
        
        # load the network created by Tutorial1
        net.read_file("red_bot_2.xdsl")
        
       # print(Fore.MAGENTA + "Tabla de la red bayesiana sin evidencias:")
        net.update_beliefs()

        os.system('cls||clear')
        
        print("")
        print(Fore.RED + "Tablas con los valores del fichero red_bot.xdsl" + Fore.WHITE)
        self.print_all_posteriors(net)
        self.aprender = input("Desea añadir aprendizaje a la red (" + Fore.RED + "Y" + Fore.WHITE + ")/(" + Fore.RED + "N" + Fore.WHITE + "): ")
        if self.aprender == "Y" or self.aprender == "y":
            fichero = input("Introduzca el nombre del fichero: ")
            # cargar los datos
            ds = pysmile.learning.DataSet()
            ds.read_file(fichero)
            # emparejar datos y red
            matching = ds.match_network(net)
            # ejecutar el algoritmo de aprendizaje EM
            em = pysmile.learning.EM()
        
        self.opcionRand = input("Fijar Evidencias: aleatorio? (" + Fore.RED + "Y" + Fore.WHITE + ")/(" + Fore.RED + "N" + Fore.WHITE + "): ")
        if self.opcionRand == "Y" or self.opcionRand == "y":
            print("Modo aleatorio activado")
            print("")
            self.si_no = ""
            self.aleatorio = random.randint(0, 1)
            self.si_no = "Baja" if self.aleatorio == 0 else "Alta"
            self.change_evidence_and_update(net, "H", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "desarmado" if self.aleatorio == 0 else "armado"
            self.change_evidence_and_update(net, "W", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "desarmado" if self.aleatorio == 0 else "armado"
            self.change_evidence_and_update(net, "OW", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "no" if self.aleatorio == 0 else "si"
            self.change_evidence_and_update(net, "HN", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "no" if self.aleatorio == 0 else "si"
            self.change_evidence_and_update(net, "NE", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "no" if self.aleatorio == 0 else "si"
            self.change_evidence_and_update(net, "PW", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "no" if self.aleatorio == 0 else "si"
            self.change_evidence_and_update(net, "PH", self.si_no, False)

            print(Fore.RED + "Resultado con evidencias calculadas: ")
            self.print_all_posteriors(net)
            
        elif self.opcionRand == "N" or self.opcionRand == "n": 

            self.opcion = int(input("Evidencia Salud = Baja(" + Fore.RED + "0" + Fore.WHITE + ") / Alta(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "H", "Baja", False)
            elif (self.opcion == 1) : 
            #  print(Fore.MAGENTA + "Evidencia Salud = Baja.")
                self.change_evidence_and_update(net, "H", "Alta", False)

            self.opcion = int(input("Evidencia Armas del bot en tiempo t = desarmado(" + Fore.RED + "0" + Fore.WHITE + ") / armado(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                 self.change_evidence_and_update(net, "W", "desarmado", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Armas del bot en tiempo t = armado.")
                self.change_evidence_and_update(net, "W", "armado", False)

            self.opcion = int(input("Evidencia Oponente armado en tiempo t = desarmado(" + Fore.RED + "0" + Fore.WHITE + ") / armado(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "OW", "desarmado", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Armas oponente en tiempo t = armado.")
                self.change_evidence_and_update(net, "OW", "armado", False)

            self.opcion = int(input("Evidencia Oye sonido en tiempo t = no(" + Fore.RED + "0" + Fore.WHITE + ") / si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "HN", "no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Se oye sonido en tiempo t = si.")
                self.change_evidence_and_update(net, "HN", "si", False)

            self.opcion = int(input("Evidencia Hay enemigos cercanos en tiempo t = no(" + Fore.RED + "0" + Fore.WHITE + ") / si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "NE", "no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Numero de enemigos cercanos en tiempo t = si.")
                self.change_evidence_and_update(net, "NE", "si", False)

            self.opcion = int(input("Evidencia Hay una arma cerca en tiempo t = no(" + Fore.RED + "0" + Fore.WHITE + ") / si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "PW", "no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia hay un arma cercana en tiempo t = si.")
                self.change_evidence_and_update(net, "PW", "si", False)

            self.opcion = int(input("Evidencia Hay un paquete de salud cercano en tiempo t = no(" + Fore.RED + "0" + Fore.WHITE + ") / si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "PH", "no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia hay un paquete de salud cercano en el tiempo t = no.")
                self.change_evidence_and_update(net, "PH", "si", False)

            print("")
            print(Fore.RED + "Resultado con evidencias calculadas: ")
            self.print_all_posteriors(net)

        
        


        else:
            raise Exception(Fore.RED + "Debes elegir si activar el modo aleatorio o no")

    def print_posteriors(self, net, node_handle):
        node_id = net.get_node_id(node_handle)
        if net.is_evidence(node_handle):
            print(Fore.RED + node_id + Fore.WHITE + " has evidence set (" +
                  Fore.RED+ net.get_outcome_id(node_handle, 
                                     net.get_evidence(node_handle)) + Fore.WHITE + ")")
        else :
            posteriors = net.get_node_value(node_handle)
            for i in range(0, len(posteriors)):
                print(Fore.WHITE + "P(" + Fore.MAGENTA + node_id + Fore.WHITE + " = " + 
                      Fore.MAGENTA + net.get_outcome_id(node_handle, i) + Fore.WHITE +
                      ") = " + str(float("{:.2f}".format(posteriors[i]))))
            print("")

    def print_all_posteriors(self, net):
        for handle in net.get_all_nodes():
            self.print_posteriors(net, handle)
        print("")

    
    def change_evidence_and_update(self, net, node_id, outcome_id, mostrar):
        if outcome_id is not None:
            net.set_evidence(node_id, outcome_id)	
        else:
            net.clear_evidence(node_id)
        
        net.update_beliefs()
        if (mostrar) :
         self.print_all_posteriors(net)
        #print("")

ejemplo = BotShooterIAA()