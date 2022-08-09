

 ________  ________  ________  ________  ________  ________  ________  ________  ________  _______      
|\   __  \|\   __  \|\   __  \|\   __  \|\   ____\|\   ____\|\   __  \|\   __  \|\   __  \|\  ___ \     
\ \  \|\  \ \  \|\  \ \  \|\ /\ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \   __/|    
 \ \   _  _\ \  \\\  \ \   __  \ \  \\\  \ \_____  \ \  \    \ \   _  _\ \   __  \ \   ____\ \  \_|/__  
  \ \  \\  \\ \  \\\  \ \  \|\  \ \  \\\  \|____|\  \ \  \____\ \  \\  \\ \  \ \  \ \  \___|\ \  \_|\ \
   \ \__\\ _\\ \_______\ \_______\ \_______\____\_\  \ \_______\ \__\\ _\\ \__\ \__\ \__\    \ \_______\
    \|__|\|__|\|_______|\|_______|\|_______|\_________\|_______|\|__|\|__|\|__|\|__|\|__|     \|_______|
                                           \|_________|                  v2.0.1


 [ --------------------------------------- ROBOSCRAPE v2.0.1 ----------------------------------------- ]

  ____   ____   ___
 6MMMMb  `MM(   )P'
6M'  `Mb  `MM` ,P   
MM    MM   `MM,P    
MM    MM    `MM.    
YM.  ,MM    d`MM.   
 YMMMMMM   d' `MM.  
      M9 _d_  _)MM_ 
    ,M9             
  ,MM9              
 d9'     production  
             
Name : roboscrape.py
Desc : Read url_list.txt (list of http(s)://<domain.com> separated by <cr>)
Date : 08-08-22
Affil: 9x 
Chat : EFNet / #9x (efnet.port80.se)
Coded: phaedo / substance
Lang : python3

Purpose of this release:
 We are all famliar with robots.txt, if you are not, then visit https://www.msn.com/robots.txt
 
 Output: (from msn.com's robots.txt)
   User-agent: *
   Disallow: /*/health/search/filter
   Disallow: /spartan
   Disallow: /pt-ao
   Disallow: /*preview=*
   Disallow: /*/autos/marketplace/product/*
   Disallow: /*/cars/marketplace/product/*
   Disallow: /*?item=*:
   Disallow: /*&item=*:

   User-agent: AdsBot-Google
   Allow: /
   Disallow: /*/health/search/filter

<ignore the rest>
-------------------------------------------------------------------------------------------------------------
What is this script going to do for me in terms of pentesting and recon?
  Most modern search engines look at (before crawling/indexing) the robots.txt file to decide what and what not   
  to index/crawl.  All Disallow'd paths are what the hacker would be interested in - things that should not be 
  indexed - we have to assume are being blocked for a reason
  
roboscrape.py will parse the list of url_list.txt and visit each URL and if /robots.txt exists, it will crawl
  and check various parameters / headers of the Disallow'd entry.  If the script see's anything in response 
  other then 404 or a forbidden error, then it is displayed on the screen (make sure out put all data from stdout)
  
INSTALLATiON:
-------------
Notes: install the requirements:
        pip3 -r requirements.txt

(If you need to manually install the requirements, after install py3.7 - 

pip3 install Style        # Keep going install all of the requirments
<output>
   Defaulting to user installation because normal site-packages is not writeable
    Collecting Style
     Downloading style-1.1.6-py2.py3-none-any.whl (5.2 kB)
     Installing collected packages: Style
   Successfully installed Style-1.1.6

If you do not have pip3, try apt-get -y install python3-pip
If that does not work, try reading https://www.educative.io/answers/installing-pip3-in-ubuntu on how to get pip3 installed

Once requirements and dependencies are met:
bash$ chmod +x roboscrape.py
bash$ ./roboscrape.py
<output>

./roboscrape.py  (output with no urllist file)

python3 ./roboscrape.py <filename>






