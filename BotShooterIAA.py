import pysmile
import pysmile_license

from colorama import init, Fore
import random
# Tutorial2 loads the XDSL file created by Tutorial1,
# then performs the series of inference calls,
# changing evidence each time.

class BotShooterIAA:
    def __init__(self):
        print(Fore.RED + "Seminario 2")
        net = pysmile.Network()
        
        # load the network created by Tutorial1
        net.read_file("red_bot.xdsl")
        
       # print(Fore.MAGENTA + "Tabla de la red bayesiana sin evidencias:")
        net.update_beliefs()
        print("")
        print(Fore.RED + "Tablas con los valores del fichero red_bot.xdsl" + Fore.WHITE)
        self.print_all_posteriors(net)
        self.opcionRand = input("Fijar Evidencias: aleatorio? (" + Fore.RED + "Y" + Fore.WHITE + ")/(" + Fore.RED + "N" + Fore.WHITE + "): ")
        if self.opcionRand == "Y" or self.opcionRand == "y":
            print("Modo aleatorio activado")
            print("")
            self.si_no = ""
            self.aleatorio = random.randint(0, 1)
            self.si_no = "bajo" if self.aleatorio == 0 else "alto"
            self.change_evidence_and_update(net, "H", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "armado_no" if self.aleatorio == 0 else "armado_si"
            self.change_evidence_and_update(net, "W", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "armado_no" if self.aleatorio == 0 else "armado_si"
            self.change_evidence_and_update(net, "OW", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "oye_no" if self.aleatorio == 0 else "oye_si"
            self.change_evidence_and_update(net, "HN", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "cerca_no" if self.aleatorio == 0 else "cerca_si"
            self.change_evidence_and_update(net, "NE", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "cerca_no" if self.aleatorio == 0 else "cerca_si"
            self.change_evidence_and_update(net, "PW", self.si_no, False)

            self.aleatorio = random.randint(0, 1)
            self.si_no = "cerca_no" if self.aleatorio == 0 else "cerca_si"
            self.change_evidence_and_update(net, "PH", self.si_no, False)

            print(Fore.RED + "Resultado con evidencias calculadas: ")
            self.print_all_posteriors(net)
            
        elif self.opcionRand == "N" or self.opcionRand == "n": 

            self.opcion = int(input("Evidencia Salud = bajo(" + Fore.RED + "0" + Fore.WHITE + ") / alto(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "H", "bajo", False)
            elif (self.opcion == 1) : 
            #  print(Fore.MAGENTA + "Evidencia Salud = bajo.")
                self.change_evidence_and_update(net, "H", "alto", False)

            self.opcion = int(input("Evidencia Armas del bot en tiempo t = armado_no(" + Fore.RED + "0" + Fore.WHITE + ") / armado_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                 self.change_evidence_and_update(net, "W", "armado_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Armas del bot en tiempo t = armado_si.")
                self.change_evidence_and_update(net, "W", "armado_si", False)

            self.opcion = int(input("Evidencia Oponente armado en tiempo t = armado_no(" + Fore.RED + "0" + Fore.WHITE + ") / armado_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "OW", "armado_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Armas oponente en tiempo t = armado_si.")
                self.change_evidence_and_update(net, "OW", "armado_si", False)

            self.opcion = int(input("Evidencia Oye sonido en tiempo t = oye_no(" + Fore.RED + "0" + Fore.WHITE + ") / oye_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "HN", "oye_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Se oye sonido en tiempo t = oye_si.")
                self.change_evidence_and_update(net, "HN", "oye_si", False)

            self.opcion = int(input("Evidencia Hay enemigos cercanos en tiempo t = cerca_no(" + Fore.RED + "0" + Fore.WHITE + ") / cerca_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "NE", "cerca_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia Numero de enemigos cercanos en tiempo t = cerca_si.")
                self.change_evidence_and_update(net, "NE", "cerca_si", False)

            self.opcion = int(input("Evidencia Hay una arma cerca en tiempo t = cerca_no(" + Fore.RED + "0" + Fore.WHITE + ") / cerca_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "PW", "cerca_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia hay un arma cercana en tiempo t = cerca_si.")
                self.change_evidence_and_update(net, "PW", "cerca_si", False)

            self.opcion = int(input("Evidencia Hay un paquete de salud cercano en tiempo t = cerca_no(" + Fore.RED + "0" + Fore.WHITE + ") / cerca_si(" + Fore.RED + "1" + Fore.WHITE + ") / saltar(" + Fore.RED + "2" + Fore.WHITE + "): "))
            if (self.opcion == 0) :
                self.change_evidence_and_update(net, "PH", "cerca_no", False)
            elif (self.opcion == 1) :
            #  print(Fore.MAGENTA + "Evidencia hay un paquete de salud cercano en el tiempo t = cerca_no.")
                self.change_evidence_and_update(net, "PH", "cerca_si", False)

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