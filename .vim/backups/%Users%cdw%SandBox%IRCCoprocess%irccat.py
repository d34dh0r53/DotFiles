Vim�UnDo� E��§�a�u�I$wduk�|x���U�oK��"   P       client.process_forever()   M         >       >   >   >    S~�l    _�                             ����                                                                                                                                                                                                                                                                                                                                                             S~n�    �                   5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                             S~o�     �         H      "def on_connect(connection, event):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~o�     �         I          connection.privmsg()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~o�     �         I          connection.privmsg('')5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             S~o�    �         I      &    connection.privmsg('NickServ', '')5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             S~pp     �   ?   C   I              raise SystemExit(1)5�_�                    B       ����                                                                                                                                                                                                                                                                                                                                                             S~pv     �   A   C   K          c.add_global_handler()5�_�      	              B       ����                                                                                                                                                                                                                                                                                                                                                             S~pz     �   A   C   K          c.add_global_handler("")5�_�      
           	   B       ����                                                                                                                                                                                                                                                                                                                                                             S~p�    �   A   C   K           c.add_global_handler("use.")5�_�   	              
   B       ����                                                                                                                                                                                                                                                                                                                                                             S~qp     �   A   B          ,    c.add_global_handler("use.", on_connect)5�_�   
                 B        ����                                                                                                                                                                                                                                                                                                                                                             S~qq     �   A   B           5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~q�     �         I      5    connection.privmsg('NickServ', 'IDENTIFY loser5')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~q�    �         I      5    connection.privmsg('NickServ', 'IDENTIFY loser5')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~q�     �                6   # connection.privmsg('NickServ', 'IDENTIFY loser5')5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             S~q�     �         H      /"The nick or channel to which to send messages"5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             S~r
     �         J      def on_notice()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             S~r     �         K    �         K    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             S~r     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~r     �         K      6   # connection.privmsg('NickServ', 'IDENTIFY loser5')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~r     �         K      5    connection.privmsg('NickServ', 'IDENTIFY loser5')5�_�                    C        ����                                                                                                                                                                                                                                                                                                                                                             S~r      �   B   E   K       5�_�                    D       ����                                                                                                                                                                                                                                                                                                                                                             S~r(     �   C   E   L          c.add_global_handler()5�_�                    D       ����                                                                                                                                                                                                                                                                                                                                                             S~r)     �   C   E   L          c.add_global_handler("")5�_�                    D   &    ����                                                                                                                                                                                                                                                                                                                                                             S~r4    �   C   E   L      &    c.add_global_handler("privnotice")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~rK    �         L      def on_notice():5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~r�     �               L   #! /usr/bin/env python   #   ## Example program using irc.client.   #   F# This program is free without restrictions; do anything you like with   # it.   #   !# Joel Rosdahl <joel@rosdahl.net>       
import sys   import argparse   import itertools       import irc.client   import irc.logging       target = None   /"The nick or channel to which to send messages"       !def on_notice(connection, event):   4   connection.privmsg('NickServ', 'IDENTIFY loser5')       "def on_connect(connection, event):   %    if irc.client.is_channel(target):           connection.join(target)           return       main_loop(connection)       def on_join(connection, event):       main_loop(connection)       def get_lines():       while True:   *        yield sys.stdin.readline().strip()       def main_loop(connection):   7    for line in itertools.takewhile(bool, get_lines()):           print(line)   (        connection.privmsg(target, line)   *    connection.quit("Using irc.client.py")       %def on_disconnect(connection, event):       raise SystemExit()       def get_args():   &    parser = argparse.ArgumentParser()   !    parser.add_argument('server')   #    parser.add_argument('nickname')   ?    parser.add_argument('target', help="a nickname or channel")   ?    parser.add_argument('-p', '--port', default=6667, type=int)   %    irc.logging.add_arguments(parser)       return parser.parse_args()       def main():       global target           args = get_args()       irc.logging.setup(args)       target = args.target           client = irc.client.IRC()       try:   J        c = client.server().connect(args.server, args.port, args.nickname)   ,    except irc.client.ServerConnectionError:            print(sys.exc_info()[1])           raise SystemExit(1)       1    c.add_global_handler("privnotice", on_notice)   /    c.add_global_handler("welcome", on_connect)   )    c.add_global_handler("join", on_join)   5    c.add_global_handler("disconnect", on_disconnect)           client.process_forever()       if __name__ == '__main__':   
    main()5�_�                    ?       ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   >   @   L      J        c = client.server().connect(args.server, args.port, args.nickname)5�_�                    ?   K    ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   >   A   L      K        #c = client.server().connect(args.server, args.port, args.nickname)5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             S~s
     �   ?   A   M              c = client.server()5�_�                     @   $    ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   ?   A   M      %        c = client.server().connect()5�_�      !               @   %    ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   ?   A   M      '        c = client.server().connect('')5�_�       "           !   @   9    ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   ?   A   M      ;        c = client.server().connect('irc.freenode.net', '')5�_�   !   #           "   @   A    ����                                                                                                                                                                                                                                                                                                                                                             S~s     �   ?   A   M      C        c = client.server().connect('irc.freenode.net', '6667', '')5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                                                             S~s)     �         M      target = None5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             S~s*     �         M      #target = None5�_�   $   &           %      
    ����                                                                                                                                                                                                                                                                                                                                                             S~s.    �         N      target = ""5�_�   %   '           &   /        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~st     �   .   0   N      &    parser = argparse.ArgumentParser()5�_�   &   (           '   0        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~sw     �   /   1   N      !    parser.add_argument('server')5�_�   '   )           (   1        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~sy     �   0   2   N      #    parser.add_argument('nickname')5�_�   (   *           )   2        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~s|     �   1   3   N      ?    parser.add_argument('target', help="a nickname or channel")5�_�   )   +           *   3        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~s~     �   2   4   N      ?    parser.add_argument('-p', '--port', default=6667, type=int)5�_�   *   ,           +   4        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~s�     �   3   5   N      %    irc.logging.add_arguments(parser)5�_�   +   -           ,   5        ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~s�     �   4   6   N          return parser.parse_args()5�_�   ,   .           -   5       ����                                                                                                                                                                                                                                                                                                                            /           6           v        S~s�     �   4   7   N      #    return parser.parse_args()5�_�   -   /           .   <       ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�     �   ;   =   O          irc.logging.setup(args)5�_�   .   0           /   =       ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�     �   <   >   O          target = args.target5�_�   /   1           0   =       ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�     �   <   ?   O          #target = args.target5�_�   0   2           1   >       ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�     �   =   ?   P          target =""5�_�   1   3           2   >       ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�    �   =   ?   P          target = ""5�_�   2   4           3   C   8    ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�     �   B   D   P      K        c = client.server().connect('irc.freenode.net', '6667', 'blarnath')5�_�   3   5           4   C   <    ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~s�   	 �   B   D   P      J        c = client.server().connect('irc.freenode.net', 6667', 'blarnath')5�_�   4   6           5   8        ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~t     �   7   9   P      def main():5�_�   5   7           6   O        ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~t	     �   N   P   P      if __name__ == '__main__':5�_�   6   8           7   P        ����                                                                                                                                                                                                                                                                                                                            /           7           v        S~t     �   O              
    main()5�_�   7   9           8   9        ����                                                                                                                                                                                                                                                                                                                            9           N           v        S~t   
 �   8   O   P          global target           args = get_args()       #irc.logging.setup(args)       #target = args.target       target = "#coproc_test"           client = irc.client.IRC()       try:   K        #c = client.server().connect(args.server, args.port, args.nickname)   I        c = client.server().connect('irc.freenode.net', 6667, 'blarnath')   ,    except irc.client.ServerConnectionError:            print(sys.exc_info()[1])           raise SystemExit(1)       1    c.add_global_handler("privnotice", on_notice)   /    c.add_global_handler("welcome", on_connect)   )    c.add_global_handler("join", on_join)   5    c.add_global_handler("disconnect", on_disconnect)           client.process_forever()    5�_�   8   :           9   9        ����                                                                                                                                                                                                                                                                                                                            9           N           v        S~t-    �   8   :   P      global target5�_�   9   ;           :   L        ����                                                                                                                                                                                                                                                                                                                            9           N           v        S~�e     �   M   O   Q      client.process_forever()�   K   N   P       5�_�   :   <           ;   N   
    ����                                                                                                                                                                                                                                                                                                                            9           O           v        S~�l    �   M   P   Q      client.process_forever()    5�_�   ;   =           <   M        ����                                                                                                                                                                                                                                                                                                                            9           O           v        S~�     �   L   M          while True:5�_�   <   >           =   M       ����                                                                                                                                                                                                                                                                                                                            9           N           v        S~��     �   L   N   P          client.process_forever()5�_�   =               >   M        ����                                                                                                                                                                                                                                                                                                                            9           N           v        S~�k    �   L   N   P      client.process_forever()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             S~q�     �         J      !def on_notice(connection, event):       �         K    �         K   H       #! /usr/bin/env python   #   ## Example program using irc.client.   #   F# This program is free without restrictions; do anything you like with   # it.   #   !# Joel Rosdahl <joel@rosdahl.net>       
import sys   import argparse   import itertools       import irc.client   import irc.logging       target = None   /"The nick or channel to which to send messages"       "def on_connect(connection, event):   %    if irc.client.is_channel(target):           connection.join(target)           return       main_loop(connection)       def on_join(connection, event):       main_loop(connection)       def get_lines():       while True:   *        yield sys.stdin.readline().strip()       def main_loop(connection):   7    for line in itertools.takewhile(bool, get_lines()):           print(line)   (        connection.privmsg(target, line)   *    connection.quit("Using irc.client.py")       %def on_disconnect(connection, event):       raise SystemExit()       def get_args():   &    parser = argparse.ArgumentParser()   !    parser.add_argument('server')   #    parser.add_argument('nickname')   ?    parser.add_argument('target', help="a nickname or channel")   ?    parser.add_argument('-p', '--port', default=6667, type=int)   %    irc.logging.add_arguments(parser)       return parser.parse_args()       def main():       global target           args = get_args()       irc.logging.setup(args)       target = args.target           client = irc.client.IRC()       try:   J        c = client.server().connect(args.server, args.port, args.nickname)   ,    except irc.client.ServerConnectionError:            print(sys.exc_info()[1])           raise SystemExit(1)       /    c.add_global_handler("welcome", on_connect)   )    c.add_global_handler("join", on_join)   5    c.add_global_handler("disconnect", on_disconnect)           client.process_forever()       if __name__ == '__main__':   
    main()5��