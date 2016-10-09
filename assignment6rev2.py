# IS620 - Assignment 6
# Program: assignment6.py
# Student: Neil Acampa
# Date:    09/23/16
# Function: Create a network using bipartite data (The Davis women club data) and perform analytics
#           The data consists of 18 southern women's attendance at 14 social events.
#           Each row represents a women and each column the event.
#           Attendance of w(i) at event(j) is signified by a 1 in the (i,j) entry (0 otherwise)
#           
# Goals:
# 10/05/16: Project a binary 2 node network onto a one node network		
#           Reason: Measurements (Degree Centrality, Closeness Centrality and Betweenness Centrality) 
#           are designed to work with one node systems.

#           What can you infer about the relationships between (1) the women, and (2) the social events?  

#           One node is designated as the Primary node (Women). 
#           One node is designated as the Secondary node (Club or Event).


#           Connectivity between (i) and (j) is established when (i) and (j) connected the same (Secondary node).

#           The projection can create different types of one node systems: 
#           Binary where 1 = indicating connetivity, 0 no connectivity.

#           Weighted Sum:
#           Where the weight between primary nodes(i) and (j) equals the number of shared secondary nodes.

#           Weighted Ratio (Newman's method) where the weight between primary nodes(i) and (j) equals a fraction of the number of
#           shared secondary nodes plus the sum of all other primary node connections to the same secondary nodes.
#           The equation is w(i,j) = Summation(1/N(events) -1). 

#           The strengh of (i) and (j)'s connectivity is diminshed as more primary nodes connect to those secondary nodes.
#           Connectivity is strongest when (i) and (j) are the only primary nodes connected.
#           
#           Task 2 - Create the weighted one node representations as described above.	Complete
#           Task 3 - Execute Degree Centrality, Betweeness and Closeness centrality	Complete
#                    for both both onto women and onto events
#           Task 4 - Analysis 								Complete

#           Task 5.1 - Show graph of original network					Complete
#           Task 5.2 - Show histograms							Complete
#           Task 5.3 - Show bar chart of 4 onto's					Not yet
#
#           Task 6- Add collaboration_weighted_projected_graph				Not yet
		
#           Task 7 - Put centrality measures and results in a function			Not yet


from __future__ import absolute_import 
from __future__ import division
import re
import os 
import math
import decimal
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import networkx as nx
import random
from networkx.algorithms import bipartite



# Movie nodes
women   = []
events  = []
e1      = []
e2      = []
e3      = []
e4      = []
e5      = []
e6      = []
e7      = []
e8      = []
e9      = []
e10     = []
e11     = []
e12     = []
e13     = []
e14     = []


linelst = []
lines  =  ""

def display_barchart(title, women, cmeasure, l, mindeg, maxdeg, ctype):

  fig = plt.figure()
  ax = fig.add_subplot(111)

  indx = 18
  ind = np.arange(indx)
  width = ".25"
  
  title1 = ("Min Degree %.3f Max Degree %.3f") % (mindeg, maxdeg)
  title2 = title + "\n" + str(title1) 

  ax.set_xlim(width,len(ind)+width)
  ax.set_ylim(0,1)
  ax.set_title(title2)
  ax.set_ylabel("Centralities")
  ax.bar(ind+width, women, cmeasure, width=0.5, color='b', align='center')
  plt.show()
  plt.close()
  return


   

def display_hist(title, women, cmeasure, l, mindeg, maxdeg, ctype, cnt, maxelements):
  """Display histogram of Centrality"""

  title1 = ("Min Centrality %.3f Max Centrality %.3f" ) % (mindeg, maxdeg)
  title2 = ("Max Centrality for %s") % (maxelements)
  title3 = str(title1) + "\n" +  str(title2)
  plt.title(title1) 
  plt.xlabel(ctype)
  plt.ylabel("Count")
  plt.suptitle(title)
  b = ((maxdeg - mindeg) / l)
  b = math.ceil(b)
  plt.hist(cmeasure, bins = 10, normed = True, color = 'b')
  plt.grid(True)
  fname = "davidhist" + str(cnt) + ".png"
  plt.savefig(fname) # save as png
  plt.show()
  return



def parse_data(linelst):
 """Parse each line and update arrays"""

 
 return


if __name__ == "__main__":
 linecnt    = 0
 print
 print
 filepath=""
 valid = 0
 
 g = nx.davis_southern_women_graph()

 nx.draw(g, node_color = 'b', edge_color = 'r', with_labels = True)
 plt.savefig("davisbipartite.png") # save as png
 plt.show() # display

 
 women = g.graph['top']
 clubs = g.graph['bottom']

 l  = len(women)
 lc = len(clubs)

 # need to fix two below
 
 print("Binary 2 Node Network Projected Onto a one Node network method = (SUM)")
 print ("Women onto Events")
 W1 = bipartite.weighted_projected_graph(g, clubs)
 print
 print ('')
 print ('#Women, Member')
 for c in clubs:
  print ('%d %s' % (W1.degree(c, weight='weight'), c))
 
 print
 nx.draw(W1, node_color = 'b', edge_color = 'r', with_labels = True)
 plt.savefig("davisontoclubs.png") # save as png
 plt.show() # display
 print
 print
 print("Binary 2 Node Network Projected Onto a one Node network method = (Ratio)")
 print ("Women onto Events")
 W2 = bipartite.weighted_projected_graph(g, clubs, ratio = True)
 print ('')
 print ('#Women, Member')
 
 for c in clubs:
  print ('%d %s' % (W2.degree(c, weight='weight'), c))



 print
 nx.draw(W2, node_color = 'b', edge_color = 'r', with_labels = True)
 plt.savefig("davisontoclubsratio.png") # save as png
 plt.show() # display
 print
 print
 # Degee Summary Stats
 deg = bipartite.degree_centrality(g, clubs)
  
 # Betweenness Summary Stats
 bc  = bipartite.betweenness_centrality(g, clubs)
 
 # Closeness Summary Stats
 cc  = bipartite.closeness_centrality(g, clubs)
 
 maxdeg     = 0
 mindeg     = 9999
 mindegwomen= []
 maxdegwomen= []
 degarray   = []
 
 maxbc      = 0
 minbc      = 9999
 minbcwomen = []
 maxbcwomen = []
 bcarray    = []

 maxcc      = 0
 mincc      = 9999
 minccwomen = []
 maxccwomen = []
 ccarray    = []

 for i in range(l):
  if (deg[women[i]] >= maxdeg):
    maxdeg          = deg[women[i]]
 
  if (deg[women[i]] <= mindeg):
    mindeg   = deg[women[i]]
    
  if (bc[women[i]] >= maxbc):
    maxbc      = bc[women[i]]
    
  if (bc[women[i]] <= minbc):
    minbc      = bc[women[i]]
    
  if (cc[women[i]] >= maxcc):
    maxcc      = cc[women[i]]
   
  if (cc[women[i]] <= mincc):
    mincc      = cc[women[i]]

   
 for i in range(l):
  if (deg[women[i]] >= maxdeg):
     maxdegwomen.append(women[i])

  if (deg[women[i]] <= mindeg):
     mindegwomen.append(women[i])

  if (bc[women[i]] >= maxbc):
     maxbcwomen.append(women[i])

  if (bc[women[i]] <= minbc):
     minbcwomen.append(women[i])

  if (cc[women[i]] >= maxcc):
     maxccwomen.append(women[i])

  if (cc[women[i]] <= mincc):
     minccwomen.append(women[i])

 # Also need to get which min and max
 # and T-stat over 2 std for 17 deg
 
 print
 print

 print ("Statistics: Centrality Measures for Davis Southern Women")
 print ("Women projected onto Events")
 print
 print ("Degree Centrality Women onto Events")
 print ("Degree Centrality is count of the number of ties to a node")
 print ("In a weighted network, it can indicate tie strength")
 print
 print ("Minimum Degree %.3f for %s") % (mindeg, mindegwomen)
 print ("Maximum Degree %.3f for %s") % (maxdeg, maxdegwomen)
 print
 print ("Degree  Women")
 for i in range(l):
   degarray.append(deg[women[i]])
   print ("%.3f  %s") % (deg[women[i]], women[i])

 
 print
 print
 print ("Nora, Evelyn and Teresa have the highest Degree centrality at .57")
 print ("These women have shared the most events together")
 print
 print
 title = "Degree Centrality Women onto Events"
 display_hist(title, women, degarray, l, mindeg, maxdeg, "Degree Centrality", 1, maxdegwomen)
 #display_barchart(title, women, degarray, l, mindeg, maxdeg, "Degree Centrality")
 
 print
 print
 print ("Betweenness Centrality Women onto Events")
 print ("This is a measure of the node which frequently acts as a bridge in the shortest path between other nodes")
 print ("In this context it indicates the KEY Member in the group")
 print
 print ("Minimum Betweenness %.3f for %s") % (minbc, minbcwomen)
 print ("Maximum Betweenness %.3f for %s") % (maxbc, maxbcwomen)
 print
 print ("Degree  Women")
 for i in range(l):
   bcarray.append(bc[women[i]])
   print ("%.3f %s") %  (bc[women[i]], women[i])

 print
 print ("Nora has the highest betweeness centrality at .113")
 print
 title = "Betweenness Centrality Women onto Events"
 display_hist(title, women, bcarray, l, minbc, maxbc, "Betweenness Centrality", 2, maxbcwomen) 

 print
 print
 print ("Closeness Centrality Women onto Events")
 print ("Closeness measure of a nodes proximity to other nodes in the network")
 print ("It indicates which nodes can easily and quickly reach to other nodes")
 print ("In this context, it identifies members that can easily connect to other members of the group")
 print
 print ("Minimum Closeness %.3f for %s") % (mincc, minccwomen)
 print ("Maximum Closeness %.3f for %s") % (maxcc, maxccwomen)
 print
 print ("Degree  Women")
 for i in range(l):
   ccarray.append(cc[women[i]])
   print ("%.3f %s") % (cc[women[i]], women[i],)


 
 print
 print ("Nora, Evelyn and Teresa have the highest closeness centrality at .800")
 print
 title = "Closeness Centrality Women onto Events"
 display_hist(title, women, ccarray, l, mincc, maxcc, "Closeness Centrality", 3, maxccwomen) 
 print
 print ("Analysis of Women and Events attended")
 print ("Nora, Evelyn and Teresa are strongly tied to all other members in the group")
 print ("Nora acts as a Key or Link or Bridge to the other members")
 print ("Teresa and Evelyn are also links to other members")
 print ("These 3 are popular, influencial and highly connected to all other members")
 print ("Nora is possible the leader")
 

 print
 print
 print
 print("Binary 2 Node Network Projected Onto a one Node network method = (SUM)")
 print ("Events onto Women")
 W3 = bipartite.weighted_projected_graph(g, women)
 print ('')
 print ('#Events, Member')
 for w in women:
  print ('%d %s' % (W3.degree(w, weight='weight'), w))


 

 print
 print
 nx.draw(W3, node_color = 'b', edge_color = 'r', with_labels = True)
 plt.savefig("davisontowomen.png") # save as png
 plt.show() # display
 print
 print
 print("Binary 2 Node Network Projected Onto a one Node network method = (Ratio)")
 print ("Events onto Women")
 W4 = bipartite.weighted_projected_graph(g, women, ratio = True)
 print ('')
 print ('#Events, Member')
 for w in women:
  print ('%d %s' % (W4.degree(w, weight='weight'), w))




 print
 nx.draw(W4, node_color = 'b', edge_color = 'r', with_labels = True)
 plt.savefig("davisontowomenratio.png") # save as png
 plt.show() # display
 print
 print

  # Degee Summary Stats
 deg = bipartite.degree_centrality(g, women)
  
 # Betweenness Summary Stats
 bc  = bipartite.betweenness_centrality(g, women)
 
 # Closeness Summary Stats
 cc  = bipartite.closeness_centrality(g, women)

 

 maxdeg     = 0
 mindeg     = 9999
 mindegclubs= []
 maxdegclubs= []
 degarray   = []
 
 maxbc      = 0
 minbc      = 9999
 minbcclubs = []
 maxbcclubs = []
 bcarray    = []

 maxcc      = 0
 mincc      = 9999
 minccclubs = []
 maxccclubs = []
 ccarray    = []
 
 
 for i in range(lc):
  if (deg[clubs[i]] >= maxdeg):
    maxdeg          = deg[clubs[i]]
 
  if (deg[clubs[i]] <= mindeg):
    mindeg   = deg[clubs[i]]
    
  if (bc[clubs[i]] >= maxbc):
    maxbc      = bc[clubs[i]]
    
  if (bc[clubs[i]] <= minbc):
    minbc      = bc[clubs[i]]
    
  if (cc[clubs[i]] >= maxcc):
    maxcc      = cc[clubs[i]]
   
  if (cc[clubs[i]] <= mincc):
    mincc      = cc[clubs[i]]

   
 for i in range(lc):
  if (deg[clubs[i]] >= maxdeg):
     maxdegclubs.append(clubs[i])

  if (deg[clubs[i]] <= mindeg):
     mindegclubs.append(clubs[i])

  if (bc[clubs[i]] >= maxbc):
     maxbcclubs.append(clubs[i])

  if (bc[clubs[i]] <= minbc):
     minbcclubs.append(clubs[i])

  if (cc[clubs[i]] >= maxcc):
     maxccclubs.append(clubs[i])

  if (cc[clubs[i]] <= mincc):
     minccclubs.append(clubs[i])

 # Also need to get which min and max
 # and T-stat over 2 std for 17 deg
 
 print
 print

 print ("Statistics: Centrality Measures for Davis Southern clubs")
 print ("Events projected onto Women")
 print
 print ("Degree Centrality Events onto Women")
 print ("Degree Centrality is count of the number of ties a node has")
 print ("In a weighted network, it can indicate tie strength")
 print 
 print ("Minimum Degree %.3f for %s") % (mindeg, mindegclubs)
 print ("Maximum Degree %.3f for %s") % (maxdeg, maxdegclubs)
 print
 print ("Degree  Events")
 for i in range(lc):
   degarray.append(deg[clubs[i]])
   print ("%.3f  %s") % (deg[clubs[i]], clubs[i])


 print
 print ("Event E8 has the highest Degree centrality at  .778")
 print ("Event E9 is second with a Degree Centrality of .667")
 print ("Events E8 and E9 highly tied to other events")

 title = "Degree Centrality Events onto Women"
 display_hist(title, women, degarray, l, mindeg, maxdeg, "Degree Centrality", 4, maxdegclubs)
 
 print
 print
 print ("Betweenness Centrality Events onto Women")
 print ("This is a measure of the node which frequently acts as a bridge in the shortest path between other nodes")
 print ("In this context it indicates a Key Event")
 print
 print ("Minimum Betweenness %.3f for %s") % (minbc, minbcclubs)
 print ("Maximum Betweenness %.3f for %s") % (maxbc, maxbcclubs)
 print
 print ("Degree  Events")
 for i in range(lc):
   bcarray.append(bc[clubs[i]])
   print ("%.3f %s") %  (bc[clubs[i]], clubs[i])

  
 print
 print ("Event E8 has the highest betweenness Centrality  at .244")
 print ("Event E9 is second with a betweenness Centrality of .226")
 print ("Event E8 acts as a bridge to other events an so does E9")
 print
 title = "Betweenness Centrality Events onto Women"
 display_hist(title, women, bcarray, l, minbc, maxbc, "Betweenness Centrality", 5, maxbcclubs)
 
 print
 print
 print ("Closeness Centrality Events onto Women")
 print ("Closeness measure of a nodes proximity to other nodes in the network")
 print ("In this context, it indicates the ease of reachablitity to other Events")
 print
 print ("Minimum Closeness %.3f for %s") % (mincc, minccclubs)
 print ("Maximum Closeness %.3f for %s") % (maxcc, maxccclubs)
 print
 print ("Degree  Events")
 for i in range(lc):
   ccarray.append(cc[clubs[i]])
   print ("%.3f %s") % (cc[clubs[i]], clubs[i],)


 print ("Event E8 has the highest closeness centrality        .846")
 print ("Event E9 is second with a closeness centrality of    .786")
 print ("Events E8 and E9 are strongly tied to all other events")
 print
 title = "Closeness Centrality Events onto Women"
 display_hist(title, women, ccarray, l, mincc, maxcc, "Closeness Centrality", 6, maxccclubs) 
 print

 print ("Analysis of Events")
 print ("Events E8 and E9 highly tied to other events")
 print ("Event8 acts as a Key or Link between events")
 print ("Events E8 and E9 are essential and important events")
 print ("They may be HUB events in this group")
 




 print
 print
 


 
  
 

# Arrays for Eigenvector Centrality by Genra and Genra's outside of 99.5% CI
 eigencntrl      = []
 eigensig        = []


# Arrays for Betweenness Centrality by Genra and Genra's outside of 99.5% CI
 betweencntrl    = []
 betweensig      = []

# Arrays for Closeness Centrality by Genra and Genra's outside of 99.5% CI
 closecntrl    = []
 closesig      = []


 
 

  