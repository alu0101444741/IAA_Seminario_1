""" This file is for blah blah blah """
import pysmile

# pysmile_license is your license key
import pysmile_license

class Seminario:
  def __init__(self):
    net = pysmile.Network()
    net.read_file("Seminario.xdsl")
    net.update_beliefs()
  
  def print_posteriors(self, net, node_handle):
    node_id = net.get_node_id(node_handle)
    if net.is_evidence(node_handle):
      print(node_id + " has evidence set (" +
        net.get_outcome_id(node_handle, 
        net.get_evidence(node_handle)) + ")")
    else :
      posteriors = net.get_node_value(node_handle)
      for i in range(0, len(posteriors)):
        print("P(" + node_id + "=" + 
          net.get_outcome_id(node_handle, i) +
          ")=" + str(posteriors[i]))

  def print_all_posteriors(self, net):
    for handle in net.get_all_nodes():
      self.print_posteriors(net, handle)

    
  def change_evidence_and_update(self, net, node_id, outcome_id):
    if outcome_id is not None:
      net.set_evidence(node_id, outcome_id)	
    else:
      net.clear_evidence(node_id)
    
    net.update_beliefs()
    self.print_all_posteriors(net)
    print("")