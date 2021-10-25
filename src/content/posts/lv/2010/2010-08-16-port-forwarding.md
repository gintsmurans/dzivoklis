Title: Port forwarding
Date: 2010-08-16 23:43
Category: Sākums
Tags: 2010
Lang: en

Yestereday it wasn't very creative day at work so I took a work with me using usb flash drive.

At work we have some paranoid IT security people who wont let us work from home, so if I want to do it, I have to copy source code onto the flash drive and setup similar configuration on my home computer. It is not the first time, so no problems with configuration, but copying, archiving, copying, unarchiving is a quite booring process. So I was thinking: "Is it possible to get to our work development server?". Asking for an access to IT is not an option in this case.

Then I remebered about port forwarding. Is it possible to connect to some server, create tunnel from connecting side and connect to this tunnel from other side? Of course it is possible. I guess I did know it before, just somehow haven't thought about it. What I need was a server. I can't use any server, again because of strict IT policy, but recently we rent a new server outside of our work environment for one project and I have an access to it from my work PC.

What should I do next?

Luckily for me port forwarding is included in ssh client/server and all I have to do is to put right parameters in command line.

I have to connect my computer to the server and open port xxx and yyy (ssh and www) that will be forwarded to our dev server at work (192.168.10.10 is an example for dev server in work's local environment):

> ssh -R 127.0.0.1:xxx:192.168.10.10:22 -R 127.0.0.1:yyy:192.168.10.10:80 [username@example.org][1]

Switch -R means that we will be forwarding remote port to local. 127.0.0.1 is for security so no one else from outside world do not guess the port and avoid any vulnerabilities to the dev server. "xxx" and "yyy" is ports to open on remote machine. "192.168.10.10:22" is ip address and port where to forward incoming connections.

Next thing to do is create a tunnel from my home computer to the server. You can leave "127.0.0.1:" out from -R switch and connect directly to the server by opening [http://example.org][2] :yyy/ and ssh -p xxx [username@example.org][3] . Considering security expectations at my work I would choose to create a tunnel from my home computer to the server either.

This should do it:

> ssh -L xxx:127.0.0.1:xxx -L yyy:127.0.0.1:yyy [username@example.org][4]

Where "-L" tells ssh to forward local incoming port to "xxx" and "yyy" to the server (127.0.0.1 is server's local ip address, what everybody knows already:) on port "xxx" and "yyy".

Now on my home computer I open [http://127.0.0.1][5] :xxx/ and it should open a default website from our dev server. As we use apache virtualhosts on our dev I would have to set some entries in hosts file to get other sites.

That's about it.

  [1]: mailto:username@example.org
  [2]: http://example.org
  [3]: mailto:username@example.org
  [4]: mailto:username@example.org
  [5]: http://127.0.0.1
