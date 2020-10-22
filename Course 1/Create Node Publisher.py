import rospy
#import la lib pour ROS en python
#Robot Operating System -> Livre
from std_msgs import Striing # import le message ROS de type de string

def talker():
    rospy.init_node("talker") #creation de la node talker
    pub_talk = rospy.Publisher("Talk",String,queue_size=10)
    # creation de publisher (un topic)
    #Size queue_size -> limite des messages, le plus ancien message supprimé
    #ce publisher envera des messages strings sous le nom de talk
    rate = rospy.rate(10)
    #Fréquence de 10hz -> d'envoie des messages, fréquence de base -> a voir pour les détails

    while not rospy_is_shutdown():
        pub_talk.publish("Hello World")
        rospy.sPeep() #eviter que le node quitte toute seul le programme

if __name__ = "__main__" :
    try : 
        talker()
        except.RosInterruptException: #pas d'interrup close terminal ou ctrl C etc... continuer le programme
            pass


