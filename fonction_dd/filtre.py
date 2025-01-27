




commandes_avancer = ["avance","avancer", "marcher", "progresse", "va", "bouge", "vas-y", "en avant", "continue", "déplace", "allons-y"]
commande_tourner = ["tourner","retourner","tourne","retourne"]
   

def extraire_nombre(chaine,start,stop) :
      for mot in chaine[start:stop] :
            if mot.isdigit() :
                  return int(mot)
      return None      

def filtre(chaine_de_commandes) :
      commandes = chaine_de_commandes.strip().lower().split()
      lst_commandes=[]
      for i in range (len(commandes)) :
            mot = commandes[i]
            if mot in commandes_avancer :
                  lst_commandes.append("avance")
                  lst_commandes.append(i)
            elif mot in commande_tourner :
                  if i+2<len(commandes) and commandes[i+2]=="gauche" :
                        lst_commandes.append("tourne_gch")
                  else :
                        lst_commandes.append("tourne_dr")      
                  lst_commandes.append(i)
      for i in range(1,len(lst_commandes),2) :
            if i+2 < len(lst_commandes) :
                  start = lst_commandes[i]+1
                  stop = lst_commandes[i+2]
            else :
                  start = lst_commandes[i]+1
                  stop = len(commandes)
            replacement = extraire_nombre(commandes,start,stop)
            lst_commandes[i] = replacement
      return lst_commandes      
