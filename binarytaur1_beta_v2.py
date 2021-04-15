import random
import time

lives = 3
name = input("Please enter your name: ")
if name == "Theseus" or name == "theseus":
    print("Oh you're some kind of expert eh, well what is the point of even trying?")
    exit()
elif name == "Icarus" or name == "icarus":
    print("Your wings can't help you now lol, lots of love - dad")
elif name == "Daedalus" or name == "daedalus":
    print("You created this abomination, how could you!!!")

true_or_false_qa_list = [
['Prince Harry is taller than Prince William',  'f',],
['The star sign Aquarius is represented by a tiger', 'f' ],
['Meryl Streep has won two Academy Awards', 'f'],
['Marrakesh is the capital of Morocco', 'f'],
['Waterloo has the greatest number of tube platforms in London', 't'],
]

true_or_false_qa_listb = [
['Paris is the captial of France: ', 't'],
['England is an island:', 'f'],
['M&M stands for Mars and Moordale: ', 'f'],
['Andorra is between France and Spain: ', 't'],
['Iran use to be part of the Perisan Empire: ', 't'],
]

multiple_choice_1 = [["What is the capital of New Zealand? \nWellington, Christchurch, Auckland or Queenstown: ", "Wellington"], 
["What is the capital of Australia? \nPerth, Sydney, Canberra or Melbourne: ", "Canberra"], 
["Who is the Greek God of the forge? \nApollo, Hephaestus, Zeus or Hermes: ", "Hephaestus"], 
["Which of these is not an ocean? \nIndian, Arctic, Mediterranean or Pacific: ", "Mediterranean"], 
["Which player has scored the most Premier League goals? \nAlan shearer, Wayne rooney, Darren bent or Emile heskey: ", "Alan shearer"]
]

multiple_choice_2 = [["What is the capital of Germany? \nCologne, Berlin, Hamburg or Munich: ", "Berlin"],
["What is the capital of Spain? \nBarcelona, Madrid, Seville or Valencia: ", "Madrid"],
["Which of these is not an element? \nAmericium, Einsteinium, Unobtanium or Mendelevium: ", "Unobtanium"], 
["In the movie \"Blade Runner\", what is the term used for human-like androids? \nReplicants, Skinjobs, Cylons or Synthetics: ", "Replicants"],
["Which player has made the most Premier League appearances? \nRyan giggs, Gareth barry, Mark noble or Petr cech: ", "Gareth barry"]
]

multiple_choice_3 = [["What is the capital of Canada? \nVancouver, Toronto, Montreal or Ottawa: ", "Ottawa"],
["Which country won the first ever Football World Cup in 1930? \nBrazil, Uruguay, Spain or Portugal: ", "Uruguay"],
["The Space Needle is located in which city? \nLos angeles, San diego, Dallas or Seattle: ", "Seattle"], 
["Leonardo Di Caprio won his first Best Actor Oscar for his performance in which film? \nThe revenant, The wolf of wall street, Shutter island or Inception: ", "The revenant"], 
["According to legend, what item is most effective against werewolves? \nGold, Silver, Bronze or Platinum: ", "Silver"]
]

riddle1 = [["What is always in front of you but can’t be seen? \nMy 'Nose', The 'Future' or 'Horizon' : ", "Future"],
[" What can you break, even if you never pick it up or touch it? \n'Silence', 'Glass', 'Wind' :", "Silence"],
[" I have branches, but no fruit, trunk or leaves. What am I? \nA 'Vine', A 'Bank' or 'The Apple Store' : ", "Bank"],
["What can you catch, but not throw? \nA 'Thief', An 'STI' or A 'Cold' : ", "Cold"],
["What has to be broken before you can use it?\nAn 'Egg', 'Virginity' or A 'Seal' : ", "Egg"],
]

riddle2 = [["I'm tall when I'm young, and I'm short when I'm old. What am I? \n'Candle', 'Tree' or 'Curtains' : ", "Candle"],
["what goes up but never comes down? \n'Balloon', 'Age' or 'Gravity' : ", "Age"],
["The more of this there is, the less you see. What is it? \n'Cheese', 'Light' or 'Darkness' : ", "Darkness"],
["What can travel all around the world without leaving its corner? \n'Globe', 'Stamp' or 'Bill Murray' : ", "Stamp"],
["What question can you never answer yes to? \n'Are you awake', 'Do you know the muffin man' or 'Are you asleep' : ", "Are you asleep"]]

riddle3 = [["What can you break, even if you never pick it up or touch it? \n'Your mother's heart', A 'Promise' or 'Wind' : ", "Promise"],
["What has 13 hearts, but no other organs? \nA 'Deck of Cards', A 'Cabbage' or 'The Hydra' : ", "Deck of cards"],
["What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps? \nA 'River', 'Sirian Bath' or 'Brush' : ", "River"],
["What can fill a room but takes up no space? \nA 'Soul', 'Light' or a 'Memory' : ", "Light"],
["What has one eye, but can’t see? \nAn 'Orc', A 'Vulcan' or a 'Needle' : ", "Needle"],
]

def tal_man():

    print("MMMMMMMMMMMMMMMMMMMMMM-``````````````````````````-mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMM.``````````````````````````.NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMM/:---.`-```.....```````````oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMy-----.`:```.---::::-..```.:NNdydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMh.`:s.:-``.:/----::.....:--oo/::sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMN-  ` :-``:`--   -/``.:/- +..../mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMm.   o:``/``:-     -/.o :-.``:+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMmo-./o:``/```-/.`.::`-/.+-/``/dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMdo:+:/:`./````-+/:-``/:-::--.oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMo..`/:`-:`````.--.````::-``:NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMy````+-`--`````````````-s:-+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMd.````+.`````````````````-sdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMm:````o``````````````````-+-dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMy.``o````````````````.++``.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMy`-+```````````````::/:```.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMm/:```-://````````:.`+.````.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMM+..```-:+/.``````./``o..````.sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMm+::::/```:.`````/.``o./.`````oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMs.-```````/`````+``-/``/.`````/NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMd:```.-```./```.-``/-```:.`````:mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMN/````:````--``````o....````````-yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMo````:`````-``````hdMMMmh+.`````-hmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMs````:``````.````.NMMMMMMMd```.sdddddNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMd````/```````````-MMMMMMMMm``-dhmdhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMN.``.---.````````/MMMMMMMM/`-hdmdhhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMM/`.//////::``-``sMMMMMMMd:+ddmdhhhhhhhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMs`````.````.-+``hMMMMMMMy.hhmdhhhhhhhhhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMm-```.`````--``.dMMMMMMy/dddmmhhhhhhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmy++:-...-:/smMMMMMMy.hmddhmdhhhhhhhdhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNMMMMMMMMM+hdmdhhdmhhhhhhhddhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdhmdhhhmdhhhhhhdmhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddmdhhhhdmhhhhhhhmhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdddhhhhhhhmdhhhhhhmdhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdmdhhhhhhhhdmhhhhhhdmhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdhhhhhhhhhhhmhhhhhhhmhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddhhhhhhhhhhhhddhhhhhhmdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhhhhhmhhhhhhdmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNdhhhhhhhhhhhhhmdhhhhhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhhhhhhhhhhhhhdmhhhhhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhhhhhhmdhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhhhhhdmhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhhhhhhhmhhhhhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhhhhhhddhhhhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhhhhhhhmhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMddhhhhhhhhhhhhhhmdhhhhhNMMMMMMMMMMMMMMMmmMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmhhhhhhhhhhhhhdmhhhhhmMMMMMMMMMMMMMMM/oMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmhhhhhhhhhhhhhhmhhhhhdMMMMMMMMNMMMmhMo.NNomMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhhhhhhhhhhhhhmdhhhhhNMMMMNMMhsmMd:mm`hh:dMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhhhhhddhhhhhmMMMMhsNMs:sN/+M:+m`yMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhhhhhddhhhhhmMMMMNhohNm/:h-my.N-sMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhhhddhhhhhmMMMN+dms:sNy-+sN.d++MMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhhhddhhhhhNMMMMmo:yNs-od/-m/+s:MMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhhhddhhhhhNMMMMMMm+-yNo.os-++y.NMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhhhhhhhhhdmhhhhhNMMMMMMMMm+:hNo.//:s`mMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdhhhhhhhhhhmhhhhhMMMMMMMMMMMd/:hd/.:y-hMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhhmdhhhdMMMMMMMMMMMMMdoo+s+./hMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhddhhhdMMMMMMMMMMMNdy+++////.sMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhmhhhm+////yhhmy+++++sh+://+hMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhhhhhhhhhddhhm/-`.-::://+o:-/o++ymNMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhdddmdhs.:///:://:-/+osdNMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdmhhhdddddhhd+.``.--//+:/sdmNMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdmhddmmddhhhhdds/-``-+ydNMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMddmddhhdddhhhdMMMNhsNMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhdhhhhhhhhhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhhhhhhhhhhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhhhhhhhhhhdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

def sto_man():
    print("                                                                            `:.`         :+:.       ")
    print("                                                                           `s..-/::.   `o-`:sso:    ")
    print("                                                                          `s`  -` `hs -o`  -` `oy   ")
    print("                                                                          s-  -`  /m--o   -`   +m.  ")
    print("                                                                         -ds//.  :mo ++` -`   `dm`  ")
    print("                                                                         y-`.o+o+mh`/:-/+o--` /my   ")
    print("                                                                        .m:`.. `oNs:/   --:/oshN/   ")
    print("                                                            :oo+-      :h+oyh/-`yNds   .`   `+No`   ")
    print("                                                           -d`.odh/   `d-  `:sdddNN:  .-    -dd`    ")
    print("                                                          `y/  `m/+os:y+      .:sdNmh+o.   `yN:     ")
    print("                                                          +y   +s  sh/h`         `-oydmmdyssNm.     ")
    print("                                                          /y/.`d.  ho:o              ..:/oyhmNh.    ")
    print("                                                           `:sym:-:hyd-     :.`            .NN/     ")
    print("                                                             `.-:/hmmm/    .:.--.`         oNo`     ")
    print("                                                                /mNNNNm+`  +    .-+.      .NN.      ")
    print("                                                                dNNNNNNNh-`s      +.      oNd       ")
    print("                                                               `N+dNNNNNmy+s`     s      -mN/       ")
    print("                                                               -m `smNNNNm+:s+/.``s``../ossdd       ")
    print("                                                               /h   .smNNNNdd/ohdhhsddNNmmNNN.      ")
    print("                                                               :h`    .+hmNNNNNNNmNNNNNNNNNNm       ")
    print("                                      `./o+-`                   oy-      .+mNNNNNNNNNNNNNNNN/       ")
    print("                                     :hdsohmdo:`                o:os.     :NNNNNNNNNNNNNNNNo        ")
    print("                                    :md/  +yh./ss+.            -y++/++-` `dNNNNNNNNNNNNNNNs         ")
    print("                                   oo.sy++ys.   `/d.       .- sNs`   `+ho/dNNNNNNNNNNNNNNy          ")
    print("                                  /d  .o+:+ooo/-:+ss     .odm:dNh` -+hNNNNmddmNNNNNNNmmmo`          ")
    print("                                `+h//+:`   `+/-+++om- `.oN:dNN.oNhyNNNNNNNNh/`..-----/s.            ")
    print("                               /dmmy:/s`  .s:    .odm/mmhyomNm` :dmdmNNNh+`       :smy`             ")
    print("                               `:m:    ::::        -Ndh++:mNddd.  /dNNy.      `:smNNy               ")
    print("                                y-     `+//:`       h:h.-sh: `hmo`  -sdmhs+/+yNNNNNNo               ")
    print("                            .`sd+     -y..``ho-     h`o/-m+   `oNm+.  +ddNNNNNNNNNNs`               ")
    print("                         `.`ds:N`    .dssso:Ndmy:  :d `o+d/     .smNhyNNNNNNNNNNNm+                 ")
    print("                        .hyy:o+Ns`  `ysyo+/--.`.-`+mmoshoN+       .+hNNNNNNNNNhyo-                  ")
    print("                        :d.d-/smhh: ::``        :ys/my+ddNh        .hNNNNNNNm/`                     ")
    print("                         /h---ss`-os+-        -s+.  hy/yodm-     .omNNNNNNd+`                       ")
    print("                        `+myy/sh   `./+/:-..:s+.    `--` :hd- `:smNNNNNmy/`                         ")
    print("                      .+dNN:yyy/       `-///:.            .omhmNNmmmhs:.                            ")
    print("                    .oo-hNd `.`                             :mNmdm/.`                               ")
    print("                  .os-  hNs                          `+shs.  -dNmNh.                                ")
    print("                `+y:`  `dy. `-:.                     ydmNNh   .mmNNd.                               ")
    print("               :yo`   .ys` .dNNm+  .                 hmNNNd    +d/dNd-                              ")
    print("           `.-yy-    -ds`  -mNNm/  . .-`    `..      .shy+.``  `d:`+mm:                             ")
    print("          :hmmo`    /ms     -++-     sd: `-ohdh:           yds. +s  .sm/                            ")
    print("         ++:mm-   `sNh`              ``./hmmmmdy      `    hNNd.`y    :do`                          ")
    print("        oo  -dms.-hNm.       .sy/    -sdNNmmmmmh      so   :NNNhom     .yy.                         ")
    print("       +h    `ommmNN+       .hNNm   -mNNNNmmmmmd`     -- `/omNNNNN`      /y-                        ")
    print("       +d-     .oNNh    `` :dNNNh  `hNNNMNmmmmmm/`      .hNNNMMNNN`       .s/`                      ")
    print("       `Nmo.    +NN/  `/hdomNNNNs  +NNNNMmmmmmmNNdo` .--oNNNNMMNNm         `+s.                     ")
    print("       .Ny/s+.  sNN` -hNNNNNNNNm/ `mNNNNNNNNNNNNNNNs/mNNNNMNNNNNNh           -y:                    ")
    print("       :NN- .hy+dNd /mNNMNNNMMNy:/ymNNNNNNNNNNNNNmNNhNNNNNNNmNNNmo```         `+s.                  ")
    print("     -+hdNy  -NNNNs`NNNNMMNNMMMNNNNMNMMMMNMNNMMNMMMMMMMMMMMMMNNNN-              -y:                 ")

def Binarytaur():
    print("1000111010001111110110001100011010010101101101111100011100111111000110011101101111011000001011000011001000010110000111101100001000")
    print("00010101010010000101100111000001 0011111010001100100110011100000011110110111100110100011101101001 10110110001100000000101000010110")
    print("000000101110011100010000111100101  1001111111100001100                     10000100011010111010  000100110100001011111101101001101")
    print("00100100011011000000011100001110100                                                            00111011010110000010100101101001001")
    print("01100001111001010101100111111001111100110                                               100100001111111001100100011101100111110001")
    print("00010101101110001000101010110111100001110001110010110                        10001100110110001001101011110000011001101100101001111")
    print("011110011001111101101101000100010110010000111101110001                      101010001100011101111010001010111011100110101101010000")
    print("10001110100011010110001011010011110001000101000111010100  100        010  10000001000110100100110100101011100010100111100010010001")
    print("0100100000011100000000101101011001000110011101000011100010  01      00  0000000010010111100110101100110100100010111101011111111111")
    print("00001001110000111110101100011111010001100011101010101001011            10101100100001101001010111100000110110101111101111101100101")
    print("1001101111110100110111011111100000100101011011011011100  001  0    1  101  0011100100101100110000000110101000010000111111101001100")
    print("11100000000111101011000011100010100001000101100111011     000011  111000     01000000100011101010100010100010011011000110011101011")
    print("111011001101000110010000100110101110111010010101001        1011    1000        110111100011010000000101001000101111011100110100110")
    print("1011110010110110011111000111100110101111001011              1000011100              1101011011111001001110111000111011101100111000")
    print("100110101001000100110101111000010110101011100                10011100                 01111111000010000100001110011011110110000011")
    print("0000010001101101101010111111010000100011000          100101111100010110010011          1010111000010111101000101001010000001110110")
    print("10011010000101100000011110011101010100011                      1100                      10010111101111000010011100101001010011011")
    print("111001101001010010011101100001110101101                                                    000010110011111000101100110011001001111")
    print("011100010101001110000110000011010000            10    1110      11      1011    11           1100001000100000010001010000000010001")
    print("01100001010100011010010111000111101           1111101          1001          1011110           00111011001010101010001111111000001")
    print("0001111000010000100001001010011111         01101001 00100000110    01100010011 10000100         1111100010000010001010100100101111")
    print("110010010111011110010001110000010      111101001100             00             110000111111      101000111110100101111010101111100")
    print("0001011010000101011110110100101001     00110100010011           11           01001011000101     1100101101010110010001110011001100")
    print("101001001111100100001110001101010001     0001111110101   0101110010100110   1101000001111      01111111010100101100110011011110110")
    print("10011011100010110111101110001101001001     100111001101 00      00      01 1010110101110     0111101101011100001101100111111011000")
    print("1101011101000011100110011010101110000010    11100010101 111101010011100100 01110111010     000000100000100111111000110111110101101")
    print("010010100000001001011111001101000000001010    010100100   000   11   011   0000000101     1011001111001110101111111110000100100011")
    print("00111001101100000000101100001011010101110011         10   111   10   111   01          0101001001101010110011001110101001001110111")
    print("1111100111101101010011001101001011110000101000001011000010010111111010111001001011111100010010101000111110110011010010011111010101")

def tru_fal_1():
    global lives
    if lives > 0:
        print(true_or_false_qa_list[0][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_list[0][1]:
            print("And Harry had better remember that!")
        else:
            print("YOU LET ME DOWN, YOU LET OUR MONARCH DOWN, BUT MOST OF ALL ... YOU LET YOURSELF DOWN!")
            lives -= 1
            print(f"You have {lives} left")
    else:
        input("This is the end for you ... dare you continue? y or n : ")

    if lives > 0:
        print(true_or_false_qa_list[1][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_list[1][1]:
            print("SOOOO correct")
        else:
            print("YOU COULDN'T BE ANYMORE WRONG, YOU COULD TRY, BUT YOU WOULD FAIL!")
            lives -= 1
            print(f"You have {lives} left")
    else:
        input("This is the end for you ... dare you continue? y or n : ")

    if lives > 0:
        if input(f"OK, what about this: {true_or_false_qa_list[2][0]}: ") in true_or_false_qa_list[2][1]:
            print("Wowzers trouserssssss")
        else:
            print("DON'T BE A DINGBAT!")
            lives -= 1
            print(f"You have {lives} left")
    else:
        input("This is the end for you ... dare you continue? y or n : ")

    if lives > 0:
        if input(f"TRUE or FALSE! {true_or_false_qa_list[3][0]}. Enter t or f : ") in true_or_false_qa_list[3][1]:
            print("Tick-et-E-booOOOo!")
        else:
            print("I think I have found a new use for the hi-five emoji ... he can take your place in this quiz!")
            lives -= 1
            print(f"You have {lives} left")
    else:
        input("This is the end for you ... dare you continue? y or n : ")

    if lives > 0:
        if input(f"Take a breath, compsose yourself ... {true_or_false_qa_list[4][0]}: ") in true_or_false_qa_list[4][1]:
            print("SSSSMMMMOOOKKKKING!")
        else:
            print("Only dogs can hear my screams now!")
            lives -= 1
            print(f"You have {lives} left")
        
            print(f"You have {lives} to continue with... ")
    else:
        input("This is the end for you ... dare you continue? y or n : ")
        if input == "y":
            start_game()
        else:
            exit

def tru_fal_2():
    global lives
    while (lives > 0):
        print(true_or_false_qa_listb[0][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[0][1]:
            print("Oui... Bon, Tres Bien!")
        else:
            print("Je déteste cette réponse! ... Not the favourable answer!")
            print("WRONG!!!")
            lives -= 1
            print(f"You have {lives} left")

        print(true_or_false_qa_listb[1][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[1][1]:
            print("OK! You have some skill. Let us see where this goes.")
        else:
            print("Not even Wakanda could save you with this performance!")
            lives -= 1
            print(f"You have {lives} left")

        print(true_or_false_qa_listb[2][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[2][1]:
            print("Don't get Cocky! ")
        else:
            print("You have only gone and blown'... the bloody door off'!")
            print("Wrong!")
            lives -= 1
            print(f"You have {lives} left")

        print(true_or_false_qa_listb[3][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[3][1]:
            print("Good, but can you do it with a distraction? ")
        else:
            print("You have failed this city ...")
            lives -= 1
            print(f"You have {lives} left")

        print(true_or_false_qa_listb[4][0])
        if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[4][1]:
            print("You may have made it through this stage. Know this ...")
            print("There is more to come.")
        else:
            print("I fear that you will be spooning with the Binarytaur ... if you are lucky")
            lives -= 1
            print(f"You have {lives} left")
        
            print(f"You have {lives} to continue with... ")
            break
        break

def mul_chc():
    global lives
    print("Please check all of your spelling! the answer needs only items inside the ' ' ...")
    chosen = int(input("Which set of questions would you like to try? 1, 2 or 3: "))
    while lives > 0 and lives != -1:

        if chosen == 1:
            print(multiple_choice_1[0][0])
            if input().capitalize() in multiple_choice_1[0][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_1[1][0])
            if input().capitalize() in multiple_choice_1[1][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_1[2][0])
            if input().capitalize() in multiple_choice_1[2][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_1[3][0])
            if input().capitalize() in multiple_choice_1[3][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_1[4][0])
            if input().capitalize() in multiple_choice_1[4][1]:
                print("Well done you little cleverclogs")
                print("You have completed the test, you may continue through.")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
            break
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
            break

        elif chosen == 2:
            print(multiple_choice_2[0][0])
            if input().capitalize() in multiple_choice_2[0][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_2[1][0])
            if input().capitalize() in multiple_choice_2[1][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_2[2][0])
            if input().capitalize() in multiple_choice_2[2][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_2[3][0])
            if input().capitalize() in multiple_choice_2[3][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_2[4][0])
            if input().capitalize() in multiple_choice_2[4][1]:
                print("Well done you little cleverclogs")
                print("You have completed the test, you may continue through.")
                
                break
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
            break

        elif chosen == 3:
            print(multiple_choice_3[0][0])
            if input().capitalize() in multiple_choice_3[0][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_3[1][0])
            if input().capitalize() in multiple_choice_3[1][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            print(multiple_choice_3[2][0])
            if input().capitalize() in multiple_choice_3[2][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_3[3][0])
            if input().capitalize() in multiple_choice_3[3][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")

            print(multiple_choice_3[4][0])
            if input().capitalize() in multiple_choice_3[4][1]:
                print("Well done you little cleverclogs")
                print("You have completed the test, you may continue through.")

            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a lives! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
            break
        break

def rid_me_lis():
    global lives
    print("Please check all of your spelling! \nIn the answer, it needs only items inside the ' ' ... ")
    chosen = int(input("Which set of questions would you like to try? 1, 2 or 3: "))
    while lives > 0 :
        
        if chosen == 1:
            print(riddle1[0][0])
            if input().capitalize() in riddle1[0][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle1[1][0])
            if input().capitalize() in riddle1[1][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle1[2][0])
            if input().capitalize() in riddle1[2][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()
            print(riddle1[3][0])
            if input().capitalize() in riddle1[3][1]:
                print("Well done you little cleverclogs")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()

            print(riddle1[4][0])
            if input().capitalize() in riddle1[4][1]:
                print("Well done you little cleverclogs")
                print("You have completed the test, you may continue through.")

            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                break

        if lives == 0:
            print("You have run out of lives!")
            cont = input("Would you like to continue at the start of this round again? Yes or No: ")
            if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                lives = 3
                rid_me_lis()
            elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                print("Please exit the game and play again whenever you want!")
                time.sleep(4)
                exit()

        if chosen == 2:
            print(riddle2[0][0])
            if input().capitalize() in riddle2[0][1]:
                print("You're no Northern Numpty!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle2[1][0])
            if input().capitalize() in riddle2[1][1]:
                print("You're no Northern Numpty!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle2[2][0])
            if input().capitalize() in riddle2[2][1]:
                print("You're no Northern Numpty!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()

            print(riddle2[3][0])
            if input().capitalize() in riddle2[3][1]:
                print("You're no Northern Numpty!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()

            print(riddle2[4][0])
            if input().capitalize() in riddle2[4][1]:
                print("You're no Northern Numpty!")
                print("You have completed the test, you may continue through.")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                break

        if lives == 0:
            print("You have run out of lives!")
            cont = input("Would you like to continue at the start of this round again? Yes or No: ")
            if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                lives = 3
                rid_me_lis()
            elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                print("Please exit the game and play again whenever you want!")
                time.sleep(4)
                exit()

        if chosen == 3:
            print(riddle3[0][0])
            if input().capitalize() in riddle3[0][1]:
                print("Coolcoolcool and the gang!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle3[1][0])
            if input().capitalize() in riddle3[1][1]:
                print("Coolcoolcool and the gang!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")

            print(riddle3[2][0])
            if input().capitalize() in riddle3[2][1]:
                print("Coolcoolcool and the gang!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()

            print(riddle3[3][0])
            if input().capitalize() in riddle3[3][1]:
                print("Coolcoolcool and the gang!")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    lives = 3
                    rid_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    time.sleep(4)
                    exit()

            print(riddle3[4][0])
            if input().capitalize() in riddle3[4][1]:
                print("Coolcoolcool and the gang!")
                print("You have completed the test, you may continue through.")
            else:
                lives -= 1
                print("Nooooooooooooooo!!!!!")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                break

        if lives == 0:
            print("You have run out of lives!")
            cont = input("Would you like to continue at the start of this round again? Yes or No: ")
            if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                lives = 3
                rid_me_lis()
            elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                print("Please exit the game and play again whenever you want!")
                time.sleep(4)
                exit()
        break

def end_seq():
    count = 0
    while count < 10:
        print("Way to go little guy!")
        count += 1
        time.sleep(0.6)

print(f"{name}... last night was strange, everything is a blur ..."),
time.sleep(2)
print("You clear your eyes and look around the room ... this is NOT your bedroom"),
time.sleep(2)
print("The place is dark and damp and smells almost like 'dog'"),
time.sleep(2.5)
print("There are three doors, one on the left and two doors on the right"),
time.sleep(3)
print("you open the door on the left ... "),
time.sleep(2)
print("GRRRRRRR roars through the corridor in front of you,coming from a frightening shadow"),
time.sleep(3.5)
print("GRRRRRRRRRRRRR it is coming straight for you you can "),
print("1. Stay around and maybe do some Yoga. 2. Slam the door and head for the other two doors"),
time.sleep(2)
user = int(input("Choose 1 or 2: "))

if user == 1:
    print("You start with Namaste ... If anything, ... , it seems angrier, you turn and bolt for the other doors")
    time.sleep(2)
elif user == 2:
    print("You are on the ball, the door is slammed shut and you sprint in the opposite direction")
else:
    print("Please Check your input, else we may have to leave you here for the Binarytaur's pleasures")
    print("Still not safe you must now choose door number 1, or door number 2 ...")
    print("Yo! You must choose door 1 or 2: ")

user = int(input("Which will you choose? door 1 or door 2: "))

if user == 1:
    print(f"There is a flash of light and a tall slim being with an elaborate green necklace, stares at you {name}...")
    tal_man()
    print("You must answer five questions to pass - if you are skiiled this won't be the last...")
    tru_fal_1()

elif user == 2:
    print(f"There is a flash of light and a tall slim being stares at you {name}...")
    tal_man()
    print("You must answer five questions to pass ...")
    tru_fal_2()
else:
    print(f"Whilst we acknowledge {name}, that you may have 'The Fear', we can only help if you choose 1 or 2. Your cooperation in this matter is appreciated. K.R - The Overlords")
    time.sleep(2)
    print("Now choose 1 or 2: ")

print("With that you are transported through the door in a flash and find yourself in a room ...")
time.sleep(1.5)
print("You are breathing heavily but there os no time to dwell ...")
time.sleep(2.5)
print("The room you are in smells like the PE lost and found from your old school")
time.sleep(2)
print("The room has one door straight ahead and one to the right ... ")
time.sleep(1.5)
print("GRRRRRRRROOOOOAAAAAARRRRRRR ... the sound echos through you")
time.sleep(2)
print("You can almost feel the ground trembling")
time.sleep(2)
print("There is no time to dwell, you must pass through the door ... simple it seems or is there a flaw?")
time.sleep(3)
print("Just one more small step away from the door ....")
print("BLAM!!!")
print("BOSH!")
time.sleep(2)
print("A mound is violently forming at your feet, you struggle to stay balanced as you slide down from atop.")
time.sleep(3)
sto_man()
time.sleep(3)
print("Good work it was, not falling on your ass ...")
time.sleep(1.25)
print(f"5 questions to answer must you, before you may pass {name}...")
time.sleep(2)
print("Still not convinced you are awake and of sound mind you move closer to a small stout man...")
print("He has a tin hat on and what at first appeared to be goggles, now you see, they are his glasses")
time.sleep(3)
print(f"Sorry, my name is {name}, I appear to be, well I am not quite sure...")
time.sleep(1.25)
print("No Chit-chat for you until you beat the Binarytaur")
time.sleep(1)
print("RRRROOOOOAAAAAARRRRRRRRRRR!!!")
time.sleep(2.25)

mul_chc()

print("You are sucked into a hole that has formed atop the mound, everything is whirling...")
print("You can see a wall below you ... ")
time.sleep(2)
print("You are heading straight for it...")
time.sleep(1)
print("You cover your eyes and scream as impending doom appraoches fast.. AAARRRRRRGGHHHHHHHHHHHHHHHHH")
time.sleep(3)
print("Youe lungs are empty from the scream and you notice that you are no longer falling")
time.sleep(3.25)
print("You open your eyes and you are stood in a long narrow corridor")
time.sleep(2)
print("It is unlike any of the other places you have visited thus far")
print("There is just one door at the end ...")
time.sleep(2)
print("But there is a haze further down the hall ...")
time.sleep(3.5)
print("You are trying to see through the haze there ...")
time.sleep(2.5)
print("CRASH! The door behind you almost gives, growling and hissing and then ...")
time.sleep(2) 
print("The beast is no longer growling, it has stopped ...") 
time.sleep(1.5)
print("it is sniffing and ...")
time.sleep(2)
print("It almost sounds like it is sniggering at you ...")
time.sleep(2.5)
print("You hear footsteps fading ... it is moving away!")
time.sleep(2)
print("The steps are fading")
time.sleep(2.75)
print("Relief fills your body, you lean against the door and take a breath")
time.sleep(3.25)
print("Looking down the hall, the haze has now parted to reveal ...")
time.sleep(3.75)
print("PEOPLE! There appear to be people gathered here ... There may be hope yet!")
time.sleep(4.5)
print("But ... You rested a little too long ...")
time.sleep(2)
print("CRASH!")
time.sleep(0.75)
print("BANG!")
time.sleep(0.75)
print("WALLOP!!!")
time.sleep(1)
print("The Binarytaur has crashed through the door sending you flying towards the gathering.")
time.sleep(3.5)
print("You look up and see the Binarytaur almost in touching distance")
time.sleep(3)
print("Fortune is in your favour  ... his horns are stuck in a large portion of the door,")
time.sleep(3)
print("You quickly rise to your feet and sprint towards the people at the next door")
time.sleep(5)
print("You can see the figures clearly ... you have met two of them already")
time.sleep(3)
print("The man and the short stout man from the previous room")
time.sleep(3)
print("The tall man steps forward and the others follw suit, led by the small stout man ...")
time.sleep(2)
print("In unison they chant... You have done well to get this far , but ")
time.sleep(3)
print("A final challenge is still to come, our riddles starting from 5 to 1")
time.sleep(2.25)
print("Answer all of them you must - else be a prisoner for always trust...")

rid_me_lis()

print("Shhhiiiiiitttttt! We never thought you would get here ... you took the onlyh path that dodges all bugs. Hang about for the sequal and we will eventually let you leave")
time.sleep(2)
Binarytaur()
time.sleep(3)
end_seq()

exit()