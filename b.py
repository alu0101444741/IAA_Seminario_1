import pysmile
import pysmile_license
net = pysmile.Network()
net.read_file("red_bot_2.xdsl")
net.update_beliefs()
ds = pysmile.learning.DataSet()
ds.read_file("a.csv")

pc = pysmile.learning.PC()
pattern = pc.learn(ds)
net = pattern.make_network(ds)
#net.write_file("tutorial9-pc.xdsl")
em = pysmile.learning.EM()

matching = ds.match_network(net)
em.set_uniformize_parameters(False)
em.set_randomize_parameters(False)
em.set_eq_sample_size(0)
em.learn(ds, net, matching)
#net.write_file("pc-em.xdsl")
#net.read_file("pc-em.xdsl")
net.update_beliefs()

def print_posteriors(net, node_handle):
        node_id = net.get_node_id(node_handle)
        if net.is_evidence(node_handle):
            print(node_id + " has evidence set (" + net.get_outcome_id(node_handle, 
                                     net.get_evidence(node_handle)) + ")")
        else :
            posteriors = net.get_node_value(node_handle)
            for i in range(0, len(posteriors)):
                print("P(" + node_id  + " = " + 
                       net.get_outcome_id(node_handle, i)  +
                      ") = " + str(float("{:.2f}".format(posteriors[i]))))
            print("")

def print_all_posteriors(net):
        for handle in net.get_all_nodes():
            print_posteriors(net, handle)
        print("")

print_all_posteriors(net)