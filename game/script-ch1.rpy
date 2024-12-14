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
    # Foxy = f
    # Blækward
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
    # Fnaf world Bonnie

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
    

    return