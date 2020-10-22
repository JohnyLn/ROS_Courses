import rospy
from std_msgs import String


#structure d'un callback, la fonction par défaut de Subscriber qui retourne
#def callback(msg):
   # rospy.loginfo(msg.data)
    #equivaut à print sur la console ROS
    #faire des messages global
 #   global distancedistance 
    #etc...


#Chaque programme une seule node, un seul init_node
#Tout les subscriber etc... se feront sur la node
#Dans le cas si on init un deuxième init_node dans une autre fonciton -> il va voir un override sur la première node
#Ou return une erreur

#Tout faire sur le meme progrmame sur la meme node, pas possible de modifier ou interagir avec une node
#std_msgs -> msg.data-> objects de la lib std_mgs de ROS


#Message ou action ou fonction a exectuer lors qu'il y a un message recu par le listener
def dvb_msg():
    rospy.loginfo(msg.data)#message -> msg un object -> on recupère l'attribut  data


def listener():
        rospy.init_node("Listener")
        sub1 = rospy.Subscriber("Talk",String,dvb_msg)
        while not rospy.is_shutdown():
            rospy.spin()
            #securite 

if __name__ = "__main__":
    try :
        listener()
    #except etc...

#Services -> avoir -> prioriser un message -> optimisation de stage à voir plus en détail