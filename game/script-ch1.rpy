label ch1_main:
    show screen top_right_text
    show screen day_text
    $ current_line = 1
    $ helpy_skylder = 250000
    $ playerMoney = 1000
    $ currentDay = "Mandag"

    # Rekter:
    # darthjacob = da

    # Lærer:
    # Glitchtrap = glitchtrap
    # Foxy = fo
    # Blækward = bd
    # Springtrap = springtrap
    # Freddy = f
    # Toy Freddy = tf
    # Baldi= b
    # chica = chica

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
    # Svampebob = sb
    # Yuri = y
    # Monika = m
    # Fnaf world Bonnie = fb
    # bedste mor gris = br

    # MUSIC
    # play music t1 = Sayo-naraMusicBoxVersion.ogg
    # play music t2 = 2.ogg
    # play music t20 = 1scary.ogg
    # play music t2g = 2g.ogg
    # play music t2g2 = 2.ogg
    # play music t2g3 = 2g2.ogg
    # play music t3 = 3.ogg
    # play music t3g = 3g.ogg
    # play music t3g2 = 3.ogg
    # play music t3g3 = 3g2.ogg
    # play music t3m = 3.ogg
    # play music t4 = 4.ogg
    # play music t4g = 4g.ogg
    # play music t5 = 5.ogg
    # play music t5b = 5.ogg
    # play music t5c = 5.ogg
    # play music t6 = 6.ogg
    # play music t6g = 6g.ogg
    # play music t6r = 6r.ogg
    # play music t6s = 6s.ogg
    # play music t7 = 7.ogg
    # play music t7a = 7.ogg
    # play music t7g = 7g.ogg
    # play music t8 = 8.ogg
    # play music t9 = 9.ogg
    # play music t9g = 9g.ogg
    # play music t10 = 10.ogg
    # play music t10y = 10-yuri.ogg

    # play music t30 = Candy Hearts.ogg
    # play music t31 = Wwtbam.ogg
    # play music akiraTheme = akiraTheme.ogg
    # play music akiraCreepyTheme = ayanoThemeCreepy.ogg
    # play music sakuraTheme = sakura_theme.ogg

    # play music td = d.ogg
    # play music m1 = m1.ogg
    # play music mend = monika-end.ogg
    # play music ghostmenu = ghostmenu.ogg
    # play music g1 = g1.ogg
    # play music g2 = g2.ogg
    # play music hb = heartbeat.ogg

    # play music relax = relax.ogg
    # play music scarySchoolLesson = scary_school_lesson.ogg
    # play music joyful = 5_monika.ogg
    # play music cantine = 5_yuri.ogg
    # play music partyPrep = 5_sayori.ogg
    # play music endingSpeech = EndingSpeech.ogg

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
    play music t2
    "Du går ned af gaden og ser at der er helt tomt"

    "Der er ikke rigtigt nogle andre mennesker, så du går sådan set bare alene"

    "Pludseligt kan du høre en gå ret hurtigt i mod dig"
    show sayori 4s at t32
    s "hej,jeg hedder sayori,det godt at møde dig"
    mc "hej sayori,det også godt at se dig,er du også på vej til skolen?"
    show sayori 4r at t32
    s "ja,og det bedste ved det er at jeg har bælte på"
    "du synes det var undeligt at hun pludseligt har bukser på,det plejer at have en nerdel på"
    scene bg school
    play music t3
    "dig og sayori gik sammen hen til skolen,i mødtes med helpy ude fra skolen"
    mc "hej helpy,godt at møde dig"
    h "hej,vent,hvor kender du mit navn fra?"
    mc "jeg har spillet et fnaf spil hvor du var med i det,og du hed også helpy der"
    h "what,et spil hvor jeg var med i det,wow det vildt nok"
    s "det bliver så sjovt i skolen det,ved jeg bare"
    show helpy Angry at left
    h "hvad mener du med sjov?"
    show sayori 4a at t32
    s "alle er jo så flinke der inde"
    h "hvad mener du!,de er i hvertfald ikke flinke!"
    mc "hvad mener du med det,er de nogen hårde lærer?"
    h "de er meget værre in det,især toy freddy,for hvergang man bryder hans regel,giver han en bøde på 500kr"
    mc "det lyder lidt dyrt"
    h "lidt?!,så meget tjener man ingengang i skolen"
    "i gik ind i skolen"
    play music t2
    scene bg hallWay
    "du så eddy på vej mod dig"
    show eddy Neutral at center
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
    play music t31
    h "jeg håber at vi får en god lære den her gang,nå vent,det har vi ingeng gang!"
    show helpy Idle at left
    "lære freddy kom ind til jer"
    show freddy Neutral at center
    f "hej små elever"
    h "edtemindste er det ikke toy freddy"
    f "kan i gætte hvad vi skal lave idag?"
    h "åh nej,er det matematik?"
    show freddy Good at center
    f "nej inu bedre,idag skal vi have quiz time"
    h "oh,det lyder ikke så dårligt"
    show freddy Neutral at center
    f "i får nogen spørgsmål i skal svare rigtigt på"
    f "vi starter med dig helpy,hvem har lavet hey halo sangen?"
    show helpy Angry at left
    h "what!,hvor skulle jeg vide det fra,er det buksefreddy?"
    show freddyAngry at center
    f "forkert!,du så trash helpy!"
    h "det gav mig jo også en umulig quiz!"
    f "stille snegl!,så det dig vanny,hvorfor er himlen blå?"
    vanny "det ved jeg da ikke,den er faktisk umulig what"
    f "SVAR NU PÅ SPØRGSMÅLET!"
    vanny "okay okay jeez,er det vejret der gør det?"
    f "det helt utroligt så forkert du svaret øjjj!"
    vanny "lul"
    show freddy Neutral at center
    f "så det dig funtime buks skulle man kalde dig for skulle man tro"
    fx "luuuu,det vil jeg meget gerne blive kaldt for fra nu af"
    f "okay,jeg er ret ligeglad,når hvordan laver man selv is?"
    fx "man bruger et par bukser"
    show freddy Angry at center
    f "forkerrrrrrrt!"
    "du synes sikkert at freddy virker ret sinsyg når han bliver sur"
    show freddy Neutral at center
    f "så det dig sayori,hvordan ungår man at tabe bukserne?"
    show sayori 4s at t33
    s "det nemt for mig da jeg taber ofte bukserne,jeg har også et bælte på,men når jeg ikke har bælte på så glider bukserne ned"
    show freddy Confused at center
    f "jeg ved ikke lige hvorfor at vi skulle vide det men okay,når men svar på spørgsmålet"
    show sayori 4a at t33
    s "man holder bukserne oppe med et bælte"
    show freddy Good at center
    f "rigtigt,der er en grund til at sayori er en af mine ynglings elever"
    hide sayori
    show helpy Angry at left
    h "seriøst!,det var et børnehave spørgsmål og dulled på sammentid!"
    show freddy Angry at center
    f "jeg sagde at du skulle være stille dumme snegl!"
    show freddy Neutral at center
    f "så det dig natsuki,hvad betyder ordsproget at blive taget med næsen"
    n "er det ik det samme som at blive snydt"
    show freddy Good at center
    f "det rigtigt,godt svaret"
    show freddy Neutral at center
    f "så det dig yuri,siden dine venner mener at du er såååå klog,så giver jeg dig en svær quiz,hvad vil det sige når man dividere?"
    show helpy Idle at left
    h "endelig er det ikke kun mig der får umulig spørgsmål"
    y "tror ikke at jeg ved hvordan man skal svare på det,deler man ting op i den slags?"
    f "det rigtigt,det vildt,jeg regnet ikke med at du vil klare den"
    y "virkelig,ingeng ros eller noget"
    f "nah du er 16 år,det kun små børn der får ros"
    y "det giver ingeng menning"
    show helpy Angry at left
    h "what!,du siger altid at vi er små elever,og ligepludselig ændre du bare menning bare fordi du ikke vil rose en elev!"
    show freddy Angry at center
    f "tie nu stille!,ellers bliver der efersedning til jer begge!"
    show freddy Neutral at center
    f "så det dig bonnie,skulle kalde dig lille bonnie"
    fb "hvorfor?"
    show freddy Good at center
    f "fordi du er lille som en lille baby haha"
    fb "dårlig joke"
    show freddy Angry at center
    f "stille baby snegl,når her er din quiz,hvilken person har en karakter i wow som hedder æøøå,det en spiller der har karakteren skal det siges"
    fb "what!,den er jo mega umulig,er det æblemanden"
    f "forkert!,du så ubrulig bonnie!"
    fb "hvor skulle jeg vide det fra!"
    show helpy dcLookAway at left
    h "han ved sikkert ingeng gang selv hvem det er,såden er det altid når de giver umulige spørgsmål"
    show freddy Neutral at center
    f "selvfølige ved jeg hvem det er,det benjamin"
    fb "what!,hvordan skulle jeg svare rigtigt på det,det jo bare en random person som du kender!"
    f "du skulle bare bruge wallhack,ligesom jeg gjor"
    show helpy Idle at left
    h "når ja det kan man jo også bare"
    f "så det dig akira,hvad gør man mod dem der pøller!"
    ak "det ved jeg ikke,sprøjter man ik bare noget duft mod det?"
    f "forkert!,som om at det hjælper"
    ak "hvad vil du havet gjort ved det?"
    f "tja jeg kan jo ligeså godt fortælle dig det rigtige svar nu hvor du dumpet!,man skyller personen ud i toiletet når de har pøllet selvføgelig"
    ak "er det ik lidt voldigt?"
    f "voldigt?,næ det retfærdighed"
    h "du ret sindsyg freddy,men det viste vi alle aligevel"
    show freddy Angry at center
    f "sagde jeg at du må tale snegl!"
    show freddy Neutral at center
    f "din tur ayano,hvorfor er freddy lederen?"
    h "åh nej ikke den skræld joke"
    ay "fordi det en freddy?"
    show freddy Good at center
    f "ja,lige presis,haha haaaaaaa"
    ay "woaow...sjovt"
    f "ja ik,den bedste joke"
    h "tror hun var chakastisk"
    show freddy Angry at center
    f "ingeng har bedt om din menning snegl!"
    show freddy Neutral at center
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
    play music t3
    menu:
        "sayori":
            mc "jeg tænker at jeg vil være sammen med sayori,hun er altid så sød"
            "du går hen til sayori for at være sammen med hinde i frikvateret"
            mc "hej sayori,vil gerne være sammen med dig"
            show sayori 1a at t32
            s "hej [mc] jeg er glad for at du vælger mig,det så rart at være sammen"
            mc "så hvad skal vi lave?"
            s "lad os hoppe på trampolinen,det altid sjovt,især fordi jeg ikke taber bukserne"
            mc "haha,ja,lad os hoppe"
            "i begyndte at hoppe på trampolinen,det var ret sjov for jer"
            show sayori 1s at t32
            s "det var sjovt at være sammen,lad os gøre det igen en anden dag"
            mc "ja,det var sjovt,men klokken ringet så vi må heler komme ind til time"
            s "ja du har ret,lad os komme til time"
            "i gik ind til skole klassen igen"
        "helpy":
            mc "jeg tænker at jeg vælger helpy,han er altid så sjov"
            "du gik hen til helpy og var sammen med ham"
            show helpy Idle at left
            h "hej,hvad vil du?"
            mc "jeg vil gerne være sammen med dig"
            h "mener du virkelig det?"
            mc "ja selvføgelig,du altid så sjov at være sammen med"
            show helpy Happy at left
            h "tak,jeg er taknemmelig,hvad siger du til at vi snakker om hvilken lære vi hader mest?"
            mc "det kan vi godt,du kan starte"
            show helpy Idle at left
            h "okay den jeg hader mest er toy freddy,han har ALT for mange regler"
            mc "det er forståligt,det heler ikke så retfærdigt af ham"
            h "nej vel,han er mega trash,men hvem hader du mest?"
            mc "helt klart baldi,han er syg i hoved,og min fætter jacob har nogen gange lyst til at smadre ham"
            h "hvor kender du baldi fra?"
            mc "min fætter fortalte mig om ham"
            h "arh okay,det giver menning"
            "klokken ringet,i skulle til time igen"
            mc "når der er time igen,men det var sjovt at være sammen med dig"
            show helpy Happy at left
            h "tak,det var også sjovt at være sammen med dig,du faktisk den eneste der forstår mig"
            mc "er jeg virkelig den eneste der kan lide dig?"
            show helpy Idle at left
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
    play music t4
    show helpy Angry at left
    h "er du seriøs,dig igen!"
    show toyfreddy Happy at center
    tf "det rigtigt,i får det så sjovt"
    show helpy Idle at left
    h "må jeg godt græde nu"
    show toyfreddy Neutral at center
    tf "nej tudefjæs,det vil vi ikke høre på"
    show helpy Angry at left
    h "what hvor flabed!"
    show toyfreddy Angry at center
    tf "når når når,så du kalder mig flabed var,det bliver en bøde på 500kr"
    show helpy Idle at left
    h "jeg hader den her skole"
    show toyfreddy Neutral at center
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
            show toyfreddy Neutral at center
            tf "lad mig se"
            show toyfreddy Angry at center
            tf "what hvad er det jeg ser,det ligner jo en gammel grim mand"
            show helpy Happy at left
            h "så ligner det dig ret godt"
            tf "stille snegl!,det bliver en bøde på 200kr snegl"
            show helpy Angry at left
            h "seriøst!"
            tf "og du skylder 50 kr for at fejle mc"
            mc "jeg gjor mit bedste"
            tf "dit bedste var godt nok forfærdelig så!"
        "3 4":
            "du lavet en okay tegning"
            mc "jeg er færdig"
            show toyfreddy Happy at center
            tf "så tør dig haha"
            show helpy Idle at left
            h "what en trash joke"
            show toyfreddy Angry at center
            tf "stille snegl!,du får en bøde på 200kr for at være flabed lille snegl"
            h "trash skole"
            "toy freddy tog din opgave for at se hvad du har tegnet"
            show toyfreddy Neutral at center
            tf "hm,det kunne være bedre,men den er okay,det er jo såden jeg ser ud så du består"
        "5 6":
            "du tegnet den så godt at det ikke kunne være bedre in det"
            mc "er færdig"
            show toyfreddy Neutral at center
            tf "lad mig se"
            show toyfreddy Happy at center
            tf "waow,det den bedste tegning jeg nogensinde har set,du består,jeg kunne få mange penge af den tegning"
    show toyfreddy Neutral at center
    tf "når men nu hvor jeg har set mc tegningen skal jeg se jeres andres"
    "toy freddy gik i gang med at kigge på hvad helpy har tegnet"
    show toyfreddy Angry at center
    tf "what hvor den grim"
    show helpy Happy at left
    h "det dig jeg har tegnet"
    tf "det er ihvertfald ikke mig,den er jo tude grim"
    h "så passer den dig jo ret godt"
    tf "du dumpet,plus du får nu 1000kr i bøde!"
    show helpy Angry at left
    h "det jo mega dyrt!"
    tf "og nu du også sur,nu 500kr ekstra i bøde"
    "helpy virket irriteret,men han sagde intet da det bare vil blive brugt i mod ham"
    fx "så jeg færdig med min luuuuuu"
    show toyfreddy Neutral at center
    tf "lad mig se"
    show toyfreddy Angry at center
    tf "what hvad er det jeg ser!"
    fx "har tegnet dig som en smuk buks"
    tf "buks!,det var menningen at du skulle tegne mig,ikke bukser,det bliver en bøde på 50kr og 500kr ekstra for at gøre mig dulled"
    fx "luuu du tog mig med bukserne nede"
    show toyfreddy Neutral at center
    tf "når ja,du også dumpet"
    "han gik nu mod vanny"
    vanny "jeg har tegnet dig rigtig godt som du kan se"
    show toyfreddy Angry at center
    tf "hvad snakker du om,den er jo mega trash"
    vanny "det dig når du er sur"
    tf "det er slet ikke mig det der,det ligner jo en rynket rusin,du dumpet og får 550kr i bøde for at fejle og fordi du gjor nar af mig"
    fb "nu min færdig"
    show toyfreddy Neutral at center
    tf "lad mig se"
    tf "du tegnet en guitar,du skulle tegne mig,du dumper!"
    fb "men du må da indrømme at det er en pæn guitar"
    tf "ja det kan godt være,men du dumper stadig fordi du ikke tegnet mig"
    fb "så selvisk"
    tf "det bliver en bøde på 400kr"
    fb "what hvorfor"
    show toyfreddy Angry at center
    tf "fordi du kaldte mig selvisk,dumme snegl!"
    "han gik mod sayori for at se hvad hun har tegnet"
    show sayori 1r at t33
    s "tror du vil elske min tegning"
    show toyfreddy Neutral at center
    tf "sayori,det ikke mig,det en banan"
    s "oh,tænkte på din personlighed,og du sød som en banan smager"
    tf "hmm,det er jo noget godt om mig,og det er en flot banan,du består"
    s "yay"
    h "det kan du ikke mene!,hvorfor består hun når hun tegnet noget helt andet!"
    hide sayori
    tf "tag en tudekiks lille helpy snegl"
    tf "lad mig se din tegning natsuki"
    n "okay,her er den"
    show toyfreddy Happy at center
    tf "waow hvor profesonelt,det ligner mig på en brik"
    n "og for at gøre dig ekstra cool,har jeg givet dig sorte smarte briller på"
    tf "du består,det derfor natsuki er min ynglings elev"
    show helpy Idle at left
    h "virkelig?,kun begrund af en tegning om dig?"
    tf "selvføgelig ikke kun fordi det dumme snegl,hun består altid"
    show helpy Angry at left
    h "det jo klart,du giver jo også hinde børnehave spørgsmål heletiden!"
    show toyfreddy Neutral at center
    tf "500kr i bøde for at være sur igen lille snegl"
    "helpy valgte at holde munden lukket"
    "han så yuris tegning nu"
    show toyfreddy Happy at center
    tf "wow det flot yuri,det mig som drikker te og ser så rolig ud"
    show helpy Idle at left
    h "en skam at du ikke er det i virkeligheden"
    tf "klap karry snegl,når men du består yuri"
    y "tak,jeg gjor virkelig mit bedste"
    "der lidt for mange elever,han gik mod akira for at se hindes tegning"
    show toyfreddy Happy at center
    tf "godt tegnet akira,du har god talent"
    ak "tak,jeg har øvet mig"
    show toyfreddy Neutral at center
    tf "lad mig se hvad du har tegnet saruka"
    sa "jeg har tegnet dig såden hvor du smiler"
    tf "og det ligner mig faktisk ret godt,du består"
    show helpy Idle at left
    h "borset fra at du er mest sur"
    show toyfreddy Angry at center
    tf "stille snegl!,det en bøde på 200kr for at være flabed"
    h "værste skole nogensinde"
    show toyfreddy Neutral at center
    tf "så vi færdige her,i har spise pause nu,"
    "i alle gik mod katinen og hen til chica for at bestile"
    scene bg cantineIdle
    play music t5
    chica "hej hvad vil du gerne bestille idag"
    menu:
        "pizza 120kr":
            chica "godt valg,det bliver 120kr,pizza er også bare det bedste"
            mc "helt enig,det smager altid så godt"
            "du gik ud til cantinen for at spise"
        "burger 80kr":
                chica "godt valg,burger er altid så lækkert"
                mc "jep jeg elsker burger"
                chica "det bliver 80kr"
                tf "hej mc,det fedt at se at du også kan lide burger,burger er min livret"
                mc "det også min livret"
                tf "det forstår jeg godt,burger er også lækkert"
        "pizzabrød med kebab 40kr":                                                  
            "du betalte og gik videre for at spise"
            "pizza brød er også ret lækkert"
            mc "ja det derfor jeg valgte det"
    scene bg cantine
    play music t6
    mc "det god mad jeg har men hvem vil jeg mon side og spise med?"
    "nu skal du vælge hvem du vil spise sammen med og side med"
    menu:
        "sayori":
            mc "jeg vil side med sayori,hun er altid så sød,dog også lidt dulled"
            "du gik mod sayori"
            mc "hej sayori må jeg godt side med dig?"
            show sayori 4a at t32
            s "ja selvføgelig må du det,det bliver så hyggeligt"
            "i sad sammen og talte sammen"
            s "så hvordan er din første skole dag?"
            mc "den er ret god,kan godt lide at der er så mange slags forskellige karaktere"
            s "det forståeligt,altid rart med forskellige mennesker"
            "der kom lidt stilhed,og pludseligt kommer hun med et underligt spørgsmål"
            s "kan du godt lide bukser?"
            mc "ja selvføgelig,det vil jo ikke være godt hvis man ikke havet nogen"
            s "haha du sjov,kan godt lide dit svar"
            mc "det da godt går jeg ud fra"
            show sayori 4s at t32
            s "jeg elsker bare bukser,jeg samler direkte på dem,vil du vide hvad min ynglings bukser er?"
            mc "okay"
            s "nice,min ynglings bukser er baggy jeans,kan godt lide at gå i store brede bukser nemlig"
            mc "jeg er ikke så meget til at gå i så noget"
            s "har du prøvet dem?"
            mc "ja,det føles lidt for posede til min stil"
            s "vil du vide noget sjovt?"
            mc "ja?"
            s "jeg taber bukserne når jeg ikke har et bælte på haha"
            mc "lul,du ret dulled"
            s "tja,det kan godt være at jeg er lidt dulled hehe"
            "klokken ringet og det var tid til jeres sidste time"
            mc "vi må nok skynde os til time"
            show sayori 1a at t32
            s "du har ret,det var hyggeligt at snakke med dig"
            "i gik ind i classen"
        "helpy":
            mc "jeg tænker at jeg vil side med helpy,han er altid så sjov"
            "du gik hen til helpy"
            show helpy Happy at left
            h "hej mc,har spærret en plads til dig"
            mc "nice tak"
            h "he det var sålidt"
            "du sad sammen med helpy"
            h "så må jeg vide din ynglings hobby?"
            mc "ja,min er at spille rollespil"
            h "waow,det lyder ret sjovt"
            mc "hvad er din hobby"
            show helpy dcLookAway at left
            h "jeg har ikke rigtigt en hobby,har jo ingeng venner"
            mc "det trist,men du har da mig"
            show helpy Idle at left
            h "ja,det jeg meget glad for,alle de andre er altid så lede mod mig,og andre ignorere mig bare,og den værste er toy freddy"
            mc "andet ikke at du havet det så hårdt"
            show helpy Angry at left
            h "hårdt!,det mere in det,jeg lider direkte,vil bare gerne ud af den her skole,men det kan jeg ikke begrund af toy freddys dumme bøder!"
            mc "han er god ved mig,den eneste lære jeg tror vil være slem mod mig er nok baldi"
            h "han er også bare forfærdelig,og nu han begyndt på at bruge ord hvor han spiller smart,det så irriterende at høre på"
            mc "forhåbenligt bliver han fyret,efter han slår elever begrund af de fejler"
            h "det skal du nok ikke forvente,for vores rekter er darthjacob,han er mega trash som rekter plus ond"
            mc "jeg skulle nok havet valgt en anden skole"
            h "samme her,når nej der er ikke andre skoler!"
            "efter jeres negative snak ringet klokken"
            mc "vi må nok gå til klassen"
            show helpy Idle at left
            h "yep,bare vi ikke får toy freddy igen"
            "i gik hen til klassen"
        "natsuki":
            mc "jeg går hen til natsuki,hun er ret cool"
            "du gik hen til natsuki"
            mc "det var det jeg sagde"
            "det ved jeg,men jeg siger det aligevel"
            n "hej mc,hvaså mand"
            mc "hej natsuki,tænkte om det er okay at jeg sidder med dig"
            n "tja hvorfor ikke"
            mc "fedt tak"
            "i havet en lille akavet stilhed"
            mc "såååå,vil du fortælle lidt om dig selc?"
            n "hmmmm,fint nok,jeg læser manga og bager cupcakes"
            mc "det har jeg ikke prøvet før men det lyder sjovt"
            n "ja,men det også arbejde og man skal huske at tage det seriøst"
            mc "yep forstået,det dig der mesteren"
            n "hvis det er kunne vi måske bage en dag,bare os 2"
            mc "det vil være mega fedt"
            n "okay cool bro,jeg giver dig besked når jeg har tid en dag"
            mc "okay"
            "klokken ringet i skulle til klassen nu"
            mc "lasse har ret,vi bør tage til klassen nu"
            n "lasse?,jeg aner ikke hvem du mener,men lad os gå"
            "i gik mod klassen"
    scene bg class_day
    play music t31
    "i alle kom til klassen og en lære kom ind"
    show baldi Idle at center
    b "hva så der baldi er i huset"
    show helpy Idle at left
    h "åh nej ikke dig igen"
    b "hvad der galt med dig lille mand"
    show helpy Angry at left
    h "lille mand!,hvad mener du med det!"
    b "du er da lille som en lille snegl mand"
    h "er der virkelig seriøst ingen gode lærer"
    b "kan i gætte hvad i skal have idag"
    show helpy Idle at left
    h "åh nej,matematik sikkert"
    b "ja,hvordan viste du mon det"
    h "ja det var godt nok vildt var pf"
    b "vi starter med dig lille snegl,hvad er 435435435+99550538"
    show helpy Angry at left
    h "what!,er du seriøst!"
    b "forkert"
    h "what det var ikke mit svar!"
    b "forsendt snegl,nu havet du allerede sagt det du troet"
    h "høre du overhovedt efter!"
    b "nej,for du fejlet og er ubruglig"
    b "din tur funtime foxy,hvad er 3+2"
    h "det mener du ikke!"
    fx "jeg kender svaret"
    b "selvføgelig,den er jo mega easy"
    fx "det bukser"
    b "forkert,hvordan kan det være at du bliver ved med at svare bukser"
    fx "fordi bukser er bukser"
    show baldi Angry at center
    b "det giver jo ingen menning,har du overhovedt en hjerne?"
    fx "det tror jeg"
    b "forkert,du så dum at du ikke har nogen"
    "han er meget onder in sidste gang tænkte du"
    show baldi Idle at center
    b "så det dig vanny,hvad er 29190+55555555"
    vanny "jeg bruger lige min magiere til at kunne kende svaret"
    "pludseligt kunne i høre glitchtrap komme tætter og tætter på"
    show glitchtrap at right
    glitchtrap "UUUUUUUU VANNNY!"
    vanny "jeg brugte bare magiere"
    glitchtrap "what hvor du OP VANNY,kom her vanny nu skal vi op i taget"
    vanny "arh,du syg i hoved"
    "glitchtrap tog fat i vanny og tog hinde med ham"
    hide glitchtrap
    b "det var godt nok mærkeligt,når men hun dumpet også,hvad der galt med jer elver"
    show helpy Angry at left
    h "det mere os der skulle spøger dig om hvad der er galt med dig pygopat!"
    b "yo yo stille snegl,du skal klappe karry for du en taber snegl"
    fx "luuuu han taber bukserne"
    show helpy Idle at left
    h "jeg hader den her skole"
    b "så det dig bonnie,hvad er 219471+595898975934575954"
    fb "jeg hader dig baldi"
    show baldi Angry at center
    b "forkert svar,wow du godt nok trash"
    fb "ja du er"
    b "hvis du ikke tier stille slår jeg dit grimme fjæs"
    show baldi Idle at center
    b "så det dig sayori,hvad er 3+9"
    show helpy Angry at left
    h "baby spørgsmållll!"
    show sayori 1a at t33
    s "er det 12?"
    b "det rigtigt,endelig er der en der fatter noget"
    h "what!,det unfair,du giver os andre videnskabs spørgsmål og giver dokierene børnehave spørgsmål!"
    b "yoyo stille lille snegl"
    show helpy Idle at left
    h "pls stop med at tale såden der"
    b "så det din tur natsuki,hvad er 32+90"
    n "ha nemt,det er 122"
    b "det rigtigt flot klaret"
    b "din tur yuri,hvad er 2910+9075"
    h "endelig er jeg ikke den eneste der får svære opgaver"
    y "det ved jeg ikke,er det 12000"
    show baldi Angry at center
    b "forkert,hvor du dårlig"
    b "så det dig akira,hvad er 1293+900"
    ak "jeg tror det er 2193"
    show baldi Idle at center
    b "det rigtigt flot klaret"
    b "din tur sakura,hvad er 39+95"
    sa "det må være 134"
    b "rigtigt,godt der nogen elever der ved noget"
    h "det bare dig der er unfair"
    b "stille baby snegl"
    b "så det dig ayano,hvad er 190+350"
    ay "540"
    b "det rigtigt,waow du eksistere"
    ay "tak jeg lærte det ved at"
    b "kedeligtttttt,så det dig mc,hvad er 289 gange 210?"
    menu:
        "40,000":
            show baldi Angry at center
            b "forkert,du så ubrulig,hey allesammen her har vi vores væreste elev"
            "du prøvet at ungå at græde,men du kunne ikke ungå det"
            b "tudefjæs,det er man somregelt når man er ubrulig"
            "du prøvet at løbe ud men baldi stod afvejen og lod dig ikke komme ud"
            b "hey du har ikke fri inu fjols,sid ned på stolen igen"
            "du sad på din plads igen,sayori kigget bekymret på dig"
        "60.690.":
                show baldi Idle at center
                b "waow det var rigtigt,du eksitere"
                show helpy Idle at left
                h "det ved vi godt,han sidder jo lige der"
                b "det min måde at rose ham på,så klap i dumme snegl"
                h "du næsten værre in toy freddy,hvordan kan det være muligt"
                "du var helt lettet over at du gættet rigtigt"
        "59.000":
            show baldi Angry at center
            b "forkert,du godt nok den dummeste elev jeg har set"
            mc "jeg prøvet mit bedste,dit spørgsmål var umulig"
            show helpy Idle at left
            h "hvad sagde jeg"
            b "tie stille ellers slår jeg jer"
            "du overvejet om du skulle sladre til rekteren om det en dag"
    "i havet fri da klokken ringet"
    show baldi Idle at center
    b "i må godt tage hjem nu små børn"
    show helpy Angry at left
    h "børn!,vi er 16"
    b "umuligt,du må være 8 år"
    show helpy Happy at left
    h "holda op hvor er jeg glad for at have fri nu"
    "i gik ud af klassen"
    scene bg corridor
    play music t8
    "pludseligt så du toy freddy og helpy løbe hen mod dig"
    show toyfreddy angry at center
    tf "hey hvor tror du,du skal hen lille snegel!"
    show helpy Idle at left
    h "um hjem af,fordi vi har fri?"
    show toyfreddy Neutral at center
    tf "det sandt at i har fri,men da dig og bonnie stadig ikke har betalt jeres bøder,skal i bo i skolen"
    fb "det jo mega unfair!"
    h "enig,du kan ikke bare spærre os inde,vi kun elever"
    tf "selvføgelig kan jeg det"
    h "det bestemmer du ikke,for du er ikke rekteren"
    tf "sandt nok men rekteren var enig om alt det jeg har lavet med skole reglerne,han var med til at lave dem dumme snegl"
    show helpy Angry at left
    h "det tror jeg ikke på!"
    fb "heler ikke mig"
    show jacob at right
    da "tænkte nok at det vil være helpt der vil klage"
    h "det jo klart når toy freddy ikke vil lade os gå hjem til os selv når vi har fri!"
    mc "de taler sandt herre"
    da "stille små børn!,jeg vil høre det fra toy freddy ham selv"
    tf "ja det sandt at jeg ikke lader dem gå hjem"
    da "hvorfor?"
    tf "de har ikke betalt mine bøder inu"
    h "se selv,du burde at fyre ham!"
    da "arh okay,det er jo en del af skolens regler,og jeg accepteret hans regler til skolen for længesiden,"
    h "what,hvorfor vil du overhovedt tilade det!"
    fb "ja,er det ikke menningen at dit job er at elverne skal have det godt?"
    da "du har ret bonnie"
    fb "godt du forstår"
    da "nej du misforstår det lille taber,du har ret i at det ikke er menningen at i skal have det godt i skolen,vi er kongerne,i er bare bønderne"
    tf "se selv lille snegl,rekteren har talt"
    h "det giver jo ingeng menning,hvilken slags rekter er du!"
    da "jeg tror bare at jeg ignorere dig lille snegl,og hvorfor er du stadig her mc?"
    mc "jeg skulle ind i litteltur clubben"
    da "arh okay,hav det sjovt"
    "du gik ind i clubben"
    da "jeg kan godt forstå at mc er din ynglings elev toy freddy"
    tf "nej nej,min ynglings elev er natsuki,men ja,mc er også en god elev"
    scene bg club_day
    play music t5
    "du så straks alle pigerne i clubben lave hver deres ting,monika kom hurtigt hen til dig"
    m "hej jeg hedder monika godt at møde dig"
    mc "hej monika jeg hedder mc,jeg vil gerne joine den her club"
    show sayori 1r at t33
    s "yay det kommer til at være sjovt"
    m "det helt fint med os,sayori hopper også af glæde nu"
    h "jeg har også joinet clubben,det perfekt"
    n "det fint nok tænker jeg"
    m "jeg har en ide,hvad hvis nu mc var sammen med en af os hvor vi skifter med at lære ham at kende"
    show sayori 1s at t33
    s "god ide monika,det vil blive så sjovt"
    y "det lyder som et klogt valg"
    m "så det afgjort,vi skiftes til at være sammen med ham"
    show sayori 4a at t33
    s "jeg vil gerne starte"
    mc "jeg havet faktisk tænkt mig at vælge sayori"
    s "yay,vi kommer til at have det så sjovt"
    mc "du meget optimistisk"
    show sayori 4s at t33
    s "ja det ved jeg,det sødt at du bemærker det"
    "hun kramte dig og stoppet kort efter igen"
    "hun tog fat i din hånd og tager dig et sted hen hvor i kan lave noget sjovt"
    scene bg closet
    play music t6
    "i kom til skab rummet hvor der var alt mulig ting"
    show sayori 1a at t33
    s "okay er du klar til at vi laver fint pønt til clubben"
    mc "yep jeg er født klar"
    s "super,lad os komme igang"
    "Sayori roder rundt, spilder glitter og limer noget forkert "
    s "ups,det var ikke lige menningen,"
    mc "barerolig,jeg hjælper dig"
    show sayori 4s at t33
    s "tak,du den bedste"
    s "jeg er utrolig glad for at du valgte at joine den her club så vi kan bringe mere tid sammen"
    mc "jeg er også glad for at vi 2 er venner"
    "i kramte hindaen,det tydeligt at i har fået et smukt venskab"
    "De færdiggør plakaten den er ikke perfekt, men Sayori synes, den er fantastisk."
    show sayori 1y at t33
    s "phew,så det endelig færdigt,det var hårdt men også sjovt,jeg er så glad for at vi var sammen om det"
    mc "jeg kan også lide at være sammen med dig"
    mc "jeg er ikke lige mester det til men...."
    s "du gjort det ret godt mc,du bedre in du tænker"
    mc "tak for dine pæne ord"
    "i tog ind til de andre som også bliv færdige med deres aktiviteter"
    scene bg club_day
    play music t5
    m "når hvordan gik det?"
    show sayori 1r at t33
    s "det gik så godt,mig og mc har haft det mega sjovt sammen"
    m "det er fantastisk,godt at i havet det så godt sammen,vi har også klaret det godt med vores aktiviteter"
    s "yay vi har alle haft det godt,gruppe kram"
    "i lavet et gruppe kram"
    "klokken bliv 17:00,og clubben skal til at lukke"
    m "det var hyggeligt,ses i morgen alle"
    "i alle hilste farvel og tog ud"
    scene bg street
    play music t8
    "du stødte in på sayori"
    show sayori 4r at t32
    s "hej,heldigt vi lige stødte ind på hindean var hehe"
    mc "yep,jeg glad for at det bliv dig"
    s "årh tak,det jeg glad for at høre"
    mc "hey hvad siger du til at vi hænger ud?"
    s "det vil jeg vildt gerne"
    s "hvad siger du til at vi går en tur i parken"
    mc "det lyder som en god ide,lad os gøre det"
    "i gik mod en smuk skov"
    scene bg street_rain3
    play music endingSpeech
    "i er nået frem til den smukke skov"
    mc "den her skov er så smuk"
    show sayori 1a at t32
    s "ja ik,det er virkelig smukt ik sandt"
    mc "det har du ret i"
    s "har du haft en god dag sammen med mig?"
    mc "selvføgelig har jeg haft det,du er mega sød"
    s "årh tak det sødt af dig at sige"
    mc "så lad os snakke om noget tilfældigt"
    s "god ide,jeg vil elske det"
    mc "kender du league of legends?"
    show sayori 1n at t32
    s "nej hvad er det?"
    "hun smilte men så også lidt forvirret ud,nok fordi at du er så mærkelig"
    mc "det var ikke særlig pænt sagt lasse"
    "tag en tude kiks"
    mc "league of legends er et spil hvor man kan stige level og få kills,og kills giver penge"
    show sayori 4r at t32
    s "kender det stadig ikke,men det lyder okay sjovt"
    s "okay min tur,har du hørt de sjove jokes vores skole lære freddy og sprintrap har lavet?"
    mc "ja jeg glæder mig til at høre det"
    s "hvorfor er freddy lederen?"
    mc "det ved jeg ikke hvorfor?"
    s "det fordi han er en freddy haha"
    mc "ja det sjovt nok"
    s "og spirngtraps joke kommer nu,hvorfor bliver det kaldt for popcorn?"
    mc "hvorfor?"
    show sayori 4r at t32
    s "det fordi det er proppet corn,haha det så genealt"
    mc "tja det var da også en okay joke"
    s "virkelig,jeg viste at du vil kunne lide det"
    mc "har du set den der alya serie?"
    s "oh ja,den er rigtig god og sjov,det minder om doki doki spillet"
    mc "det gøre det faktisk ja"
    s "har du set ron fra den der kim serie?"
    mc "når ja han er også ret sjov"
    s "ja og han taber altid bukserne,det sjovt fordi det oplever jeg også ofte"
    mc "hehe,det tror jeg på"
    s "der er noget jeg må fortælle,du den eneste jeg tør at sige det til,da jeg kan så godt lide dig"
    mc "jeg lytter,du kan fortælle mig hvad som helst"
    show sayori 1f at t32
    s "lover du mig at du ikke vil sige det vidre til de andre?"
    mc "ja det bliver bare mellem os 2"
    show sayori 1u at t32
    s "jeg har en depression,jeg føler mig ofte ubrulig og svag,jeg føler bare at alle er bedre in mig "
    "hun bliv pludseligt ked af det,hvordan vil du mon støtte hinde?,dur du mon til det hmmmm"
    mc "Jeg er så ked af at høre, at du føler sådan. Det må være virkelig hårdt for dig"
    mc "Tak fordi du fortalte mig det. Det betyder meget, at du deler det med mig."
    s "jeg er så glad for din støtte,men det gør stadig ondt"
    mc "Du er ikke alene i det her. Jeg er her for dig, og jeg vil gerne hjælpe dig"
    s "det sødt af dig,men er det overhovedt okay at vise sin depression"
    mc "ja,Det er okay at føle sig sådan, men husk, at du betyder meget for mig og for andre"
    show sayori 4r at t32
    s "årh tak,du er min bedste ven"
    "hun fik det bedre og kramte dig og stoppet efter 5 seckundter"
    mc "så har du mod på at vi laver noget mere nu?"
    s "ja jeg har faktisk en sjov ide"
    mc "jeg lytter"
    s "okay fedt,vi kunne spille sten saks og papir,taberen skal lave en akavat dans,foran vinderen"
    mc "jeg er frisk på den"
    s "nice du vil elske det,lad os komme igang"
    "i begyndte at spille sten saks og papir,nu skal du slå terning"
    menu:
        "1 2 3":
            "du tabte til sayori,du så dårlig,hvor er jeg bare sjov"
            s "haha,det var vist mig der havet bukserne på"
            mc "godt spillet sayori"
            s "tak og nu skal du lave en akavet dans"
            "du dansede som en grim taber og sayori kunne ikke lade være med at grine"
            s "hehe det var ret sjovt,især for mig"
            mc "er det okay at jeg overnatter hos dig idag?"
            s "yay,det vil være så sjovt,lad os komme afsted"
            "i tog hjem til sayori og straks hen til soveværelset da klokken bliv 22:00"
        " 4 5 6":
            mc "aha jeg vandt,jeg glæder mig til at se dig danse"
            s "hehe,du er mega god,og jeg vil prøve noget sjovt for at få dig til at grine"
            mc "nice,du er altid så sød og sjov"
            "hun rødmet lidt af din komplement"
            s "tak hehe,jeg vil nu tage bæltet af og danse som en hiphopper"
            "hun tog bæltet af og begyndte at danse somen hip hopper,og hun endte med at tabe bukserne"
            mc "Øhh, Sayori... Hvorfor... Fik du pludseligt lyst til at danse, og uden et bælte?"
            mc "Ville det ikke i det mindste give mening at have bæltet på imens? Og hvorfor bruger du bukser i stedet for et skørte?"
            s "hehe,okay det var ret pingligt,jeg har måske ikke gennemtænkt det helt"
            s "og jeg er bare blivet glad for at gå i bukser"
            "sagde hun mens hun rødmet og trak bukserne op og tog bæltet på igen"
            "i tog hjem til sayori og da den er 22:00"
    "i tog hjem til sayori og gik til soveværelset da det er sendt som klokken er 22:15"
    scene bg sayori_bedroom
    play music t10
    show sayori 1a at t32
    s "det var en rigtig sjov aften"
    mc "helt enig,du en fantastisk ven"
    s "du også en rigtig god ven,den bedste ven faktisk"
    "i gik i seng og faldte i søvn"

    return