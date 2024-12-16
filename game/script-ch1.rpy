label ch1_main:
    show screen top_right_text
    show screen day_text
    $ current_line = 1
    $ helpy_skylder = 250000
    $ playerMoney = 1000
    $ currentDay = "Mandag"

    # Rekter:
    # darthjacob

    # Lærer:
    # Glitchtrap = glitchtrap
    # Foxy = fo
    # Blækward = bd
    # Springtrap = springtrap
    # Freddy = f
    # Toy Freddy = tf
    # Baldi= b

    # Elever:
    # Eddy = eddy
    # Helpy = h
    # MC = mc
    # Sakura = sa
    # Ayano = ay
    # Akira = ak
    # Sayori = s
    # Natsuki = n
    # Funtime Foxy = fx
    # Vanny = vanny
    # Svampebob
    # Yuri = y
    # Monika = m
    # Fnaf world Bonnie =fb

    stop music fadeout 2.0

    scene bg bedroom
    with dissolve_scene_full

    play music t8

    "Fortæl mig dit navn"

    $ mc = renpy.input("")

    "MANDAG"

    "Du vågner op i din seng, du kigger op i luftet og glæder dig til dagen i dag"

    "Du rejser dig op og går ud af dit værelse, stadig med dit sove tøj på"

    "Hm, tænk engang, du burde tage dit tøj på"

    menu:
        "Er det ikke lidt dullet?":
            "Du har ret, det er lidt dullet"

            "Men du går alligevel tilbage til dit værelse og tager dit tøj på"

            "Du vælger derefter at gå nedenunder"
            
        "Jeg må hellere tage mit tøj på":
            "Du tager dit tøj på og går nedenunder"

    mc "Det var godt at få noget tøj på, selv om jeg hele tiden har haft det"

    "Ja, men det var sove tøj, det er ikke det samme"

    scene bg kitchen
    "Du går ud i køkkenet og åbner køleskabet"

    "Du kan vælge imellem nogle forskellige ting du har i køleskabet"

    menu:
        "Tag en banan":
            "Du tager din kedelige banan ud af køleskabet og begynder at skrælle og spise den"

        "Tag en rugbrødsmad med mugost på":
            mc "Hvorfor har jeg overhovdet mug ost, jeg kan jo ikke engang lide det"

            "Det ved jeg ikke, du er lidt speciel må man nok sige"

        "Tag en skål med cornflakes":
            "Du tager din pakke med cornflakes ud af køleskabet, jeg ved ikke hvorfor du ville have den der?"

            "Du vælger at hælde det op i en skål med mælk og begynder at spise det"

        "Ristet brød med brie":
            "Du tager din brie og dit brød ud af køleskabet og begynder at lave en ristet brie sandwich"

    "Imens du spiser din morgenmad, tænker du på hvad du skal lave i dag"

    "Er du mon sjov i dag?"

    menu:
        "Ja, jeg er altid sjov":
            "Klart, du er altid sjov..."

        "I dag skal jeg finde en klub":
            "Det er nok meget godt, så kan du hænge ud med andre nørder som dig selv"

        "I dag skal jeg få nogle venner":
            "Hvilke venner? Du har jo ingen"

            mc "Jeg har da masser, jeg har dig"

            "Hmm, ja, det er ret trist"

    "Efter du bliver færdig med at spise, går du ud af døren og begynder at gå mod skolen"

    scene bg street
    "Du går ned af gaden og ser at der er helt tomt"

    "Der er ikke rigtigt nogle andre mennesker, så du går sådan set bare alene"

    "Pludseligt kan du høre en gå ret hurtigt i mod dig"
    s "hej,jeg hedder sayori,det godt at møde dig"
    mc "hej sayori,det også godt at se dig,er du også på vej til skolen?"
    s "ja,og det bedste ved det er at jeg har bælte på"
    "du synes det var undeligt at hun pludseligt har bukser på,det plejer at have en nerdel på"
    scene bg school
    "dig og sayori gik sammen hen til skolen,i mødtes med helpy ude fra skolen"
    mc "hej helpy,godt at møde dig"
    h "hej,vent,hvor kender du mit navn fra?"
    mc "jeg har spillet et fnaf spil hvor du var med i det,og du hed også helpy der"
    h "what,et spil hvor jeg var med i det,wow det vildt nok"
    s "det bliver så sjovt i skolen det,ved jeg bare"
    h "hvad mener du med sjov?"
    s "alle er jo så flinke der inde"
    h "hvad mener du!,de er i hvertfald ikke flinke!"
    mc "hvad mener du med det,er de nogen hårde lærer?"
    h "de er meget værre in det,især toy freddy,for hvergang man bryder hans regel,giver han en bøde på 500kr"
    mc "det lyder lidt dyrt"
    h "lidt?!,så meget tjener man ingengang i skolen"
    "i gik ind i skolen"
    scene bg hallWay
    "du så eddy på vej mod dig"
    eddy "hej med dig,er du den nye elev?"
    mc "ja,hej med dig eddy,viste ikke at du var i den her skole,kommer du ikke fra den der ed ed og eddy film?"
    eddy "jo,det gør jeg faktisk,jeg valgte bare at rejse helevejen her til istedenfor"
    mc "waow,det lyder godt nok som en lang rejse"
    eddy "det var det også,og jeg går i den samme klasse som dig"
    mc "wow,det ret nice,det bliver fedt at lære dig mere at kende"
    eddy "har du valgt en club du gerne vil joine?"
    mc "næ"
    eddy "what,du skal da have en club at gå i,det altid så sjovt at gå i clubber,og du får flere venner af det"
    mc "arh,det ret coolt,hvilken clubber kan jeg vælge?"
    eddy "der er bog clubben,der læser man bare med andre,så der roleplay clubben,der roleplayer man med forskelige ting,så der også litteltur clubben,der de alle mega flinke"
    mc "og hvad laver man i litteltur clubben?"
    eddy "er glad for du spøger,det er en club hvor man skriver digte,eller tegner eller læser bøger,jeg husker også at de læser manga og bager der over"
    mc "det nogen ret gode valg"
    eddy "så hvilken club vil du joine?"
    menu:
        "ittelturclubben":
            pass
    eddy "godt valg,det også en god club"
    mc "jeg kunne ikke vælge andre aligevel"
    eddy "oh,jeg beklager,de andre 2 clubber er lukkede forevigt,men vi må heler tage til klassen"
    "du tog ind i classen"
    scene bg class_day
    h "jeg håber at vi får en god lære den her gang,nå vent,det har vi ingeng gang!"
    "lære freddy kom ind til jer"
    f "hej små elever"
    h "edtemindste er det ikke toy freddy"
    f "kan i gætte hvad vi skal lave idag?"
    h "åh nej,er det matematik?"
    f "nej inu bedre,idag skal vi have quiz time"
    h "oh,det lyder ikke så dårligt"
    f "i får nogen spørgsmål i skal svare rigtigt på"
    f "vi starter med dig helpy,hvem har lavet hey halo sangen?"
    h "what!,hvor skulle jeg vide det fra,er det buksefreddy?"
    f "forkert!,du så trash helpy!"
    h "det gav mig jo også en umulig quiz!"
    f "stille snegl!,så det dig vanny,hvorfor er himlen blå?"
    vanny "det ved jeg da ikke,den er faktisk umulig what"
    f "SVAR NU PÅ SPØRGSMÅLET!"
    vanny "okay okay jeez,er det vejret der gør det?"
    f "det helt utroligt så forkert du svaret øjjj!"
    vanny "lul"
    f "så det dig funtime buks skulle man kalde dig for skulle man tro"
    fx "luuuu,det vil jeg meget gerne blive kaldt for fra nu af"
    f "okay,jeg er ret ligeglad,når hvordan laver man selv is?"
    fx "man bruger et par bukser"
    f "forkerrrrrrrt!"
    "du synes sikkert at freddy virker ret sinsyg når han bliver sur"
    f "så det dig sayori,hvordan ungår man at tabe bukserne?"
    s "det nemt for mig da jeg taber ofte bukserne,jeg har også et bælte på,men når jeg ikke har bælte på så glider bukserne ned"
    f "jeg ved ikke lige hvorfor at vi skulle vide det men okay,når men svar på spørgsmålet"
    s "man holder bukserne oppe med et bælte"
    f "rigtigt,der er en grund til at sayori er en af mine ynglings elever"
    h "seriøst!,det var et børnehave spørgsmål og dulled på sammentid!"
    f "jeg sagde at du skulle være stille dumme snegl!"
    f "så det dig natsuki,hvad betyder ordsproget at blive taget med næsen"
    n "er det ik det samme som at blive snydt"
    f "det rigtigt,godt svaret"
    f "så det dig yuri,siden dine venner mener at du er såååå klog,så giver jeg dig en svær quiz,hvad vil det sige når man dividere?"
    h "endelig er det ikke kun mig der får umulig spørgsmål"
    y "tror ikke at jeg ved hvordan man skal svare på det,deler man ting op i den slags?"
    f "det rigtigt,det vildt,jeg regnet ikke med at du vil klare den"
    y "virkelig,ingeng ros eller noget"
    f "nah du er 16 år,det kun små børn der får ros"
    y "det giver ingeng menning"
    h "what!,du siger altid at vi er små elever,og ligepludselig ændre du bare menning bare fordi du ikke vil rose en elev!"
    f "tie nu stille!,ellers bliver der efersedning til jer begge!"
    f "så det dig bonnie,skulle kalde dig lille bonnie"
    fb "hvorfor?"
    f "fordi du er lille som en lille baby haha"
    fb "dårlig joke"
    f "stille baby snegl,når her er din quiz,hvilken person har en karakter i wow som hedder æøøå,det en spiller der har karakteren skal det siges"
    fb "what!,den er jo mega umulig,er det æblemanden"
    f "forkert!,du så ubrulig bonnie!"
    fb "hvor skulle jeg vide det fra!"
    h "han ved sikkert ingeng gang selv hvem det er,såden er det altid når de giver umulige spørgsmål"
    f "selvfølige ved jeg hvem det er,det benjamin"
    fb "what!,hvordan skulle jeg svare rigtigt på det,det jo bare en random person som du kender!"
    f "du skulle bare bruge wallhack,ligesom jeg gjor"
    h "når ja det kan man jo også bare"
    f "så det dig akira,hvad gør man mod dem der pøller!"
    ak "det ved jeg ikke,sprøjter man ik bare noget duft mod det?"
    f "forkert!,som om at det hjælper"
    ak "hvad vil du havet gjort ved det?"
    f "tja jeg kan jo ligeså godt fortælle dig det rigtige svar nu hvor du dumpet!,man skyller personen ud i toiletet når de har pøllet selvføgelig"
    ak "er det ik lidt voldigt?"
    f "voldigt?,næ det retfærdighed"
    h "du ret sindsyg freddy,men det viste vi alle aligevel"
    f "sagde jeg at du må tale snegl!"
    f "din tur ayano,hvorfor er freddy lederen?"
    h "åh nej ikke den skræld joke"
    ay "fordi det en freddy?"
    f "ja,lige presis,haha haaaaaaa"
    ay "woaow...sjovt"
    f "ja ik,den bedste joke"
    h "tror hun var chakastisk"
    f "ingeng har bedt om din menning snegl!"
    f "så det dig sakura,hvem har lavet så du tabe din buuuks sangen"
    sa "buksefreddy"
    h "hvor dulled kan man lige være"
    f "det rigtigt sakura,så det dig mc,hvad hedder dinosauren som får folk til at pølle"
    menu:
        "pøllesauren":
            f "rigtigt svaret,godt at nogen kan svare rigtigt help!"
            h "er du serøs!,en babi kunne svare på det"
        "ghostdragon":
            f "waow,mener du virkelig det?,hvordan fejler du den her nemme opgave"
        "frygt skurken":
            f "hvor dum er du lige,du svaret omega forkert!"
    f "når men nu har i frikvater,håber i har haft det sjovt"
    h "det har vi aldrig"
    "du tog ud til frikvateret sammen med de andre,hvem vil du bringe tid med?"
    scene bg school_yard
    menu:
        "sayori":
            mc "jeg tænker at jeg vil være sammen med sayori,hun er altid så sød"
            "du går hen til sayori for at være sammen med hinde i frikvateret"
            mc "hej sayori,vil gerne være sammen med dig"
            s "hej mc jeg er glad for at du vælger mig,det så rart at være sammen"
            mc "så hvad skal vi lave?"
            s "lad os hoppe på trampolinen,det altid sjovt,især fordi jeg ikke taber bukserne"
            mc "haha,ja,lad os hoppe"
            "i begyndte at hoppe på trampolinen,det var ret sjov for jer"
            s "det var sjovt at være sammen,lad os gøre det igen en anden dag"
            mc "ja,det var sjovt,men klokken ringet så vi må heler komme ind til time"
            s "ja du har ret,lad os komme til time"
            "i gik ind til skole klassen igen"
        "helpy":
            mc "jeg tænker at jeg vælger helpy,han er altid så sjov"
            "du gik hen til helpy og var sammen med ham"
            h "hej,hvad vil du?"
            mc "jeg vil gerne være sammen med dig"
            h "mener du virkelig det?"
            mc "ja selvføgelig,du altid så sjov at være sammen med"
            h "tak,jeg er taknemmelig,hvad siger du til at vi snakker om hvilken lære vi hader mest?"
            mc "det kan vi godt,du kan starte"
            h "okay den jeg hader mest er toy freddy,han har ALT for mange regler"
            mc "det er forståligt,det heler ikke så retfærdigt af ham"
            h "nej vel,han er mega trash,men hvem hader du mest?"
            mc "helt klart baldi,han er syg i hoved,og min fætter jacob har nogen gange lyst til at smadre ham"
            h "hvor kender du baldi fra?"
            mc "min fætter fortalte mig om ham"
            h "arh okay,det giver menning"
            "klokken ringet,i skulle til time igen"
            mc "når der er time igen,men det var sjovt at være sammen med dig"
            h "tak,det var også sjovt at være sammen med dig,du faktisk den eneste der forstår mig"
            mc "er jeg virkelig den eneste der kan lide dig?"
            h "det skulle man tro,når men lad os tage til time"
            "i gik til klassen"
        "natsuki":
            mc "jeg tænker at jeg vil være sammen med natsuki,hun virker ret sød"
            "intresant valg,du gik hen til natsuki"
            n "yo mc hvaså?"
            mc "hej natsuki,tænker om vi kan være sammen"
            n "ja hvorfor ikke"
            mc "fedt,hvad har du lyst til at lave?"
            n "tænker at jeg vil kigge på tøj på nettet"
            mc "det virker lidt dulled"
            n "pf,det ved jeg,men jeg har ikke nok tøj,men hvis du ikke er intreseret så må du bare lade mig være"
            mc "oh,jeg har det fint nok med det,lad os kigge på tøj,hvilken mubil bruger vi?"
            n "vi bruger bare min"
            mc "okay"
            "i kigget på tøj på mubilen,i godt nok dulled skulle man tro"
            n "wow se de bukser,dem vil jeg gerne have"
            mc "de også ret nice"
            "i brugte hele jeres frikvater på at kigge på tøj,det ret dulled når man tænker over det"
            n "det var okay sjovt at være sammen med dig mc"
            mc "tak,det var også mega sjovt at være sammen med dig,selv om det handlet om dul"
            "i gik til klassen"
    "i kom til klassen og i fik toy freddy som lære"
    scene bg class_day
    h "er du seriøs,dig igen!"
    tf "det rigtigt,i får det så sjovt"
    h "må jeg godt græde nu"
    tf "nej tudefjæs,det vil vi ikke høre på"
    h "what hvor flabed!"
    tf "når når når,så du kalder mig flabed var,det bliver en bøde på 500kr"
    h "jeg hader den her skole"
    tf "idag skal vi have kunst"
    h "siden hvornår er du blvet kunst lære?"
    tf "siden nu lille snegl"
    h "behøver i virkelig at kalde mig for det"
    tf "ja det gør vi,og du skylder 100kr ekstra for at være irriteret"
    h "hvorfor går jeg overhovedt i den her skole"
    tf "jeg vil have jer til at tegne mig,den der tegner mig godt består,hvis man fejler dumper man,og får 50kr i bøde for at fejle"
    ay "det virker lidt unfair"
    h "enig"
    tf "lev med dig små børn,jeres time begynder nu,jeg forventer en god tegning"
    "nu skal du slå terning"
    menu:
        "1 2":
            "du lavet en forfærdlig tegning"
            mc "jeg er færdig med at tegne"
            tf "lad mig se"
            tf "what hvad er det jeg ser,det ligner jo en gammel grim mand"
            h "så ligner det dig ret godt"
            tf "stille snegl!,det bliver en bøde på 200kr snegl"
            h "seriøst!"
            tf "og du skylder 50 kr for at fejle mc"
            mc "jeg gjor mit bedste"
            tf "dit bedste var godt nok forfærdelig så!"
        "3 4":
            "du lavet en okay tegning"
            mc "jeg er færdig"
            tf "så tør dig haha"
            h "what en trash joke"
            tf "stille snegl!,du får en bøde på 200kr for at være flabed lille snegl"
            h "trash skole"
            "toy freddy tog din opgave for at se hvad du har tegnet"
            tf "hm,det kunne være bedre,men den er okay,det er jo såden jeg ser ud så du består"
        "5 6":
            "du tegnet den så godt at det ikke kunne være bedre in det"
            mc "er færdig"
            tf "lad mig se"
            tf "waow,det den bedste tegning jeg nogensinde har set,du består,jeg kunne få mange penge af den tegning"
    tf "når men nu hvor jeg har set mc tegningen skal jeg se jeres andres"
    "toy freddy gik i gang med at kigge på hvad helpy har tegnet"
    tf "what hvor den grim"
    h "det dig jeg har tegnet"
    tf "det er ihvertfald ikke mig,den er jo tude grim"
    h "så passer den dig jo ret godt"
    tf "du dumpet,plus du får nu 1000kr i bøde!"
    h "det jo mega dyrt!"
    tf "og nu du også sur,nu 500kr ekstra i bøde"
    "helpy virket irriteret,men han sagde intet da det bare vil blive brugt i mod ham"
    fx "så jeg færdig med min luuuuuu"
    tf "lad mig se"
    tf "what hvad er det jeg ser!"
    fx "har tegnet dig som en smuk buks"
    tf "buks!,det var menningen at du skulle tegne mig,ikke bukser,det bliver en bøde på 50kr og 500kr ekstra for at gøre mig dulled"
    fx "luuu du tog mig med bukserne nede"
    tf "når ja,du også dumpet"
    "han gik nu mod vanny"
    vanny "jeg har tegnet dig rigtig godt som du kan se"
    tf "hvad snakker du om,den er jo mega trash"
    vanny "det dig når du er sur"
    tf "det er slet ikke mig det der,det ligner jo en rynket rusin,du dumpet og får 550kr i bøde for at fejle og fordi du gjor nar af mig"
    fb "nu min færdig"
    tf "lad mig se"
    tf "du tegnet en guitar,du skulle tegne mig,du dumper!"
    fb "men du må da indrømme at det er en pæn guitar"
    tf "ja det kan godt være,men du dumper stadig fordi du ikke tegnet mig"
    fb "så selvisk"
    tf "det bliver en bøde på 400kr"
    fb "what hvorfor"
    tf "fordi du kaldte mig selvisk,dumme snegl!"
    "han gik mod sayori for at se hvad hun har tegnet"
    s "tror du vil elske min tegning"
    tf "sayori,det ikke mig,det en banan"
    s "oh,tænkte på din personlighed,og du sød som en banan smager"
    tf "hmm,det er jo noget godt om mig,og det er en flot banan,du består"
    s "yay"
    h "det kan du ikke mene!,hvorfor består hun når hun tegnet noget helt andet!"
    tf "tag en tudekiks lille helpy snegl"
    tf "lad mig se din tegning natsuki"
    n "okay,her er den"
    tf "waow hvor profesonelt,det ligner mig på en brik"
    n "og for at gøre dig ekstra cool,har jeg givet dig sorte smarte briller på"
    tf "du består,det derfor natsuki er min ynglings elev"
    h "virkelig?,kun begrund af en tegning om dig?"
    tf "selvføgelig ikke kun fordi det dumme snegl,hun består altid"
    h "det jo klart,du giver jo også hinde børnehave spørgsmål heletiden!"
    tf "500kr i bøde for at være sur igen lille snegl"
    "helpy valgte at holde munden lukket"
    "han så yuris tegning nu"
    tf "wow det flot yuri,det mig som drikker te og ser så rolig ud"
    h "en skam at du ikke er det i virkeligheden"
    tf "klap karry snegl,når men du består yuri"
    y "tak,jeg gjor virkelig mit bedste"
    "der lidt for mange elever,han gik mod akira for at se hindes tegning"
    tf "godt tegnet akira,du har god talent"
    ak "tak,jeg har øvet mig"
    tf "lad mig se hvad du har tegnet saruka"
    sa "jeg har tegnet dig såden hvor du smiler"
    tf "og det ligner mig faktisk ret godt,du består"
    h "borset fra at du er mest sur"
    tf "stille snegl!,det en bøde på 200kr for at være flabed"
    h "værste skole nogensinde"
    tf "så vi færdige her,i har spise pause nu,"
    "i alle gik mod katinen og hen til chica for at bestile"




        



            
        

        
     
    



    

    return