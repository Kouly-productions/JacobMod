label ch2_main:
    $ currentDay = "Tirsdag"
    scene bg bedroom
    play music t8
    "TIRSDAG"

    "Du vågner i din behagelige seng, som du plejer."

    "Du rejser dig op, og kigger ud a vinduet"

    "Når du kigger ud kan du se der er lyst, og du ved at dette bliver en rigtig god dag"

    "Du går ud af dit værelse og ned af trappen, for at gå mod køkkenet"

    scene bg kitchen
    "Du kan mærke du er sulten, så du vælger at lave noget morgenmad"

    "Hvad kunne du tænke dig at lave [mc]?"

    define breakfast = ""
    menu:
        "Havregryn med mælk":
            $ breakfast = "Havregryn med mælk"
        "Rugbrød med ost":
            $ breakfast = "Rugbrød med ost"
        "havregrød med kanel sukker og honning":
            $ breakfast = "havregrød med kanel sukker og honning"

    "Du går i gang med at lave [breakfast]"

    "Det tager lidt tid for du er tydeligvis ikke særlig god til at lave [breakfast]"

    mc "Jeg er da ikke så dårlig til det"

    "Efter noget tid tager du din [breakfast] og går hen til dit køkken bord hvor der står en tallerken"

    "Du sætter dig ned og begynder at spise"

    "Mens du sidder og spiser, begynder du at tænke over i går"

    "Alt det der skete med Akira i resturenten"

    "Og den måde de andre reagerede på"

    "Pludseligt kan du høre det ringer på døren"

    mc "Hvem kan det være så tideligt?"

    scene bg door
    "Du går hen til døren og åbner den"

    show sakura Happy2 at left
    $ play_voice("Sakura", 82)
    sa "God morgen [mc]!"
    
    show ayano Smile1 at right
    ay "Vi tænkte at følges med dig til skole i dag"

    mc "Oh, det var sødt af jer"

    show sakura Happy1 at left
    $ play_voice("Sakura", 83)
    sa "Vi tænkte det kunne være hyggeligt at følges"

    ay "Og... Vi ville sikre os at du har det okay efter i går"

    menu:
        "Jeg har det fint":
            mc "Jeg har det helt fint"

            $ play_voice("Sakura", 84)
            sa "Er du sikker? Det var ret intens i går..."

            mc "Ja, men jeg er okay"

        "Jeg er lidt bekymret":
            mc "For at være ærlig er jeg lidt bekymret"

            ay "Det forstår vi godt..."

            $ play_voice("Sakura", 85)
            sa "Det er derfor vi er her"

        "Det var ret underligt":
            mc "Det var ret underligt i går"

            ay "Ja... Akira var ikke helt sig selv"

            $ play_voice("Sakura", 86)
            sa "Eller måske var hun for meget sig selv..."

    $ play_voice("Sakura", 87)
    sa "Nå, skal vi følges til skole?"

    mc "Jeg skal lige have min taske"

    "Du går ind igen og finder din taske"

    "Efter at have fundet din taske tager du den på ryggen og går ud til dem igen"

    "Sammen forlader i dit hus og går mod skolen"

    scene bg street

    show sakura Happy2 at left
    $ play_voice("Sakura", 88)
    sa "Det er et dejligt vejr i dag"

    show ayano Idle1 at right
    ay "Ja... Næsten for perfekt..."

    mc "Hvad mener du?"

    ay "Det er bare... Nogle gange føles det som om alting er for perfekt"

    sa "Måske er det bare fordi vi endelig har det godt?"

    mc "Jeg synes også det er rart at alting er så roligt"

    "I fortsætter ned af de stille morgengader sammen"

    show sakura Sad2 at left
    sa "[mc], når Akira snakker om at du skal invitere hende som date til ballet, så skal du vide vi vil forsvare dig..."

    sa "Hvis det ikke er det du vil"

    sa "Du skal selvfølgelig have mulighed for at vælge lige præcis den pige du har lyst"

    sa "Har du spurgt nogle pige endnu?"

    mc "Ikke endnu"

    sa "Må jeg spørge... Hvorfor?"

    menu:
        "Jeg er bange for Akiras reaktion":
            mc "For at være ærlig... Så er jeg bange for Akiras reaktion"

            show sakura Sad2 at left
            sa "Det forstår vi godt"

            show ayano Angry1 at right
            ay "Du kan ikke lade hendes... besættelse af dig, kontrollere dine valg"

            sa "Vi er her for dig [mc]. Du skal ikke være bange"

            ay "Vi lader ikke Akira sakde dig eller... Den du vælger"

            mc "Tak... Det betyder meget for mig"
        "Jeg frygter at ødelægge venskaber":
            mc "Jeg er bange for at det ændre på vores venskaber"

            show ayano Smile1 at right
            ay "Ægte venskaber... De holder, uanset hvad der sker"

            show sakura Sad2 at left
            sa "Præcis! Vi er her for dig, uanset hvem du vælger"

            ay "Selv om det måske bliver... akavet i starten"

            mc "I er virkelig gode venner..."
        "Jeg er ikke sikker på hvem jeg vil invitere":
            mc "Jeg er ikke helt sikker på hvem jeg vil invitere"

            show sakura Blink1 at left
            sa "Det er okay [mc]. Du skal ikke stresse over det"

            show ayano Smile1 at right
            ay "Du har god tid til at tænke over det"

            sa "Tænk på det som når du skal plukke en blomst"

            mc "En blomst?"

            show sakura Happy1 at left
            sa "Ja, hvis du plukker den for tideligt, er den ikke sprunget ud endnu"

            sa "Men hvis du venter til det rigtige øjeblik..."

            show sakura Happy3 at left
            sa "Så er det der du ser alle dens smukke farver"

            mc "Jeg tror ikke helt jeg forstår..."

            show sakura Happy2 at left
            sa "Det er okay [mc]. Det kan være du vil forstå det en dag"

            sa "Bare husk, at vi er med dig, uanset hvem du ender med at vælge at invitere"

    mc "Jeg er så glad for at have jer som venner"

    scene bg street
    "Efter noget tid kan i endelig se skolen på afstand"

    scene bg school
    play music t30
    "Det vare ikke længe før at i når hen til den"

    "I kan se Akira stå ved indgangen, og det ser ud til at hun venter nogen"

    show ayano Shy1 at right
    ay "Det ser ud til at hun venter på dig [mc]"

    show sakura Sad1 at left
    sa "Så er det endnu en dag, er du klar [mc]?"

    mc "Det tror jeg"

    show akira Flirt2 at center
    ak "Godmorgen venner~"

    "Akira kigger på jer alle sammen"

    show sakura Happy2 at left
    show ayano Smile1 at right

    sa "Godmorgen Akira, er du klar til en ny dag?"

    ak "Yep, jeg har allerede forberedt mig på skolen i dag"

    ay "Forberedt?"

    ak "Ja, jeg har gjort alle mine ting klar til skolen i dag"

    "Der er noget anderledes ved Akira, der er gået 30 sekunder, og hun har ikke flirted med dig endnu"

    ak "Skal vi følges til klassen?"

    sa "Det lyder som en god ide"

    "Sammen går i indenfor og ind i de lange gange"

    scene bg corridor
    "I går ned af gangene, og i kan mærke at der er en underlig stemning"

    "For det er ikke sådan Akira plejer at være"

    "Hun går ikke engang helt tæt på dig, hun holder lidt afstand"

    show sakura Sad2 at left
    sa "Akira, er der sket noget godt i dag?"

    show akira HappyIdle at center
    ak "Jeg kan bare mærke at det bliver en god dag"

    sa "Det er vi glade for at høre"

    show ayano Shy1 at right
    ay "Du virker... anderledes i dag"

    ak "Gør jeg? Jeg føler mig bare... glad"

    "I fortsætter ned af gangen, og du kan mærke hvordan både Sakura og Ayano holder øje med Akira"

    "Det er som om de ikke helt stoler på hendes pludselige ændring"

    show sakura Happy2 at left
    sa "Det er dejligt at se dig i godt humør Akira"

    ak "Tak Sakura, der er også mange grunde til at være glad"

    "Hvad siger du [mc], stoler du på Akira?"

    scene bg corridor

    menu:
        "Det virker som snyd":
            mc "Jeg tror det er et form for trick til at snyde os"

            "Man ved aldrig med Akira, hun virker som en der godt kunne finde på det"
        "Måske har hun ændret sig":
            mc "Jeg tror at hun har ændret sig"

            "Du er et positivt menneske [mc], det er en rigtig god egenskab at have"

            "Du tænker kun det bedste om dine venner"

    "I fortsætter ned af gangen mod klassen"

    "Efter noget tid når i endelig frem til klassen"
    
    scene bg class_day
    "I går ind i klassen, og sætter jer ned på jeres normale pladser"

    "I sidder bare og venter på at der kommer en lære ind af døren"

    "Pludseligt kommer Freddy ind af døren"

    show freddy Good at center
    play music t31
    f "Godmorgen små elever! I dag skal vi lave noget HELT nyt"

    show helpy DC at left
    h "Åh nej... Hvad nu?"

    f "I dag skal vi lave teater"

    h "Teater?"

    f "Det er nemlig rigtigt! I skal lave et teaterstykke sammen i grupper"

    f "Og ved i hvad?"

    h "Hvad?"

    f "Jeg har allerede lavet grupperne"

    h "Det kan du bare ikke mene..."

    f "Vi er alle sammen en stor gruppe"

    h "Åh, det er måske slet ikke så slemt alligevel"

    show freddy Neutral at center
    f "I har bare at gøre det godt..."

    f "Vi skal vise det frem foran hele skolen, senere i dag"

    h "VENT HVAD!?"

    show FT Happy at right
    fx "Det vil sige VI SKAL PRØVE TØJ"

    f "Ja, i skal finde nogle kostumer der passer"

    fx "LUUUU DE SKAL PASSE"

    f "Selvfølgelig skal de passe... Vil du da have at de konstant falder ned?"

    fx "LUUUU"

    f "Ja, ja... I skal finde nogle kostumer der passer"

    f "Vi ses i teater rummet om 10 minutter"

    scene bg class_day
    "Freddy går ud af klassen igen"

    show helpy Angry at left
    h "TEATER!? Foran HELE skolen!?"

    show akira HappyIdle at center
    ak "Jeg tror at det bliver sjovt, tror du ikke [mc]?~"

    menu:
        "Jeg tror det bliver sjovt":
            mc "Jeg er helt enig Akira, jeg tror også det bliver rigtig sjovt"
        "Jeg hader teater":
            mc "For at være ærlig Akira, så hader jeg teater"
        "Jeg er bange for at gøre noget forkert":
            mc "Jeg er bange for at gøre noget forkert"

            ak "Det er okay [mc], du skal nok klare det godt~"

    show sakura Happy2 at right
    sa "Gad vise om vi skal selv finde på noget eller om Freddy har noget forberedt"

    h "Jeg håber virkelig at han har noget forberedt"

    h "Ellers kan det da ikke blive andet end kaotisk"

    scene bg class_day
    "I begynder alle sammen at rejse jer fra jeres paldser"

    scene bg corridor
    play music t3
    "I forlader klassen og begyndet at gå over mod teatret"

    show sakura Happy2 at left
    sa "Det bliver spændende at se hvordan teateret ser ud"

    show ayano Shy1 at right
    ay "Jeg vidste slet ikke vi havde et teater..."

    show helpy DC at center
    h "Det har vi sikkert heller ikke..."

    h "Det er nok bare et rum Freddy kalder for et teater"

    sa "Det ville give mening der var et teater, når man tænker over det er planetens største skole"

    "I går ned af de lange gange, forbi klasselokalerne i kender"

    show sakura Sad2 at left
    sa "Er vi sikre på at vi går den rigtige vej?"

    scene bg corridor
    "Jo længere i går, jo mindre genkendelige bliver gangene"

    "På et tidspunkt kommer i frem til et skilt hvor der står teater"

    show helpy DC at left
    h "I det mindste er der noget der kan hjælpe til at finde vej"

    "Efter lidt tid når i endelig til 2 røde døre med et skilt hvor der står teater på"

    "Du åbner døren og går ind, de andre elever følger efter dig"

    scene bg theater
    "Når i kommer ind kan du se kæmpe rum med en stor scene"

    "I ser at Freddy står på scenen og venter på jer"

    "I begynder at gå over mod ham"

    show freddy Neutral at center
    play music t31
    f "Godt at i kunne finde herhen"

    f "Det tog jer godt nok lidt tid"

    show helpy DC at left
    h "Det er fordi du ikke har nogle skilte"

    show freddy Angry at center
    f "STILLE SNEGL!"

    show freddy Neutral at center
    f "Vi skal have et middelalder teaterstykke"

    show helpy Angry at left
    h "Middelalder? Det bliver bare værre og værre..."

    show sakura Happy2 at right
    sa "Det lyder da spændende! Med riddere og prinsesser"

    hide sakura
    f "Vi har nogle forskellige roller som skal fordeles"

    f "Denne historie skal handle om en ridder der skal redde en prinsesse"

    show helpy DC at left
    h "Det lyder bare som endnu en af de der kedelige historier"

    show freddy Angry at center
    f "SAGDE JEG AT JEG VILLE HAVE DIN MENING!?"

    scene bg theater
    show freddy Neutral at center
    f "Så vi skal først have fundet de 2 hovedroller, ridderen og prinsessen"

    show akira Flirt2 at left
    ak "Åh~ Jeg ved lige hvem der ville være perfekt som ridder~"

    show ayano Angry1 at right
    ay "Vi burde stemme om rollerne..."

    f "HA! Nej, jeg har allerede bestemt dem"

    hide ayano
    show helpy DC at right
    h "Selvfølgelig har du det..."

    f "[mc], du skal være ridderen"

    ak "Det vidste jeg~"

    scene bg theater
    show freddy Neutral at center

    "Freddy kigger dramatisk rundt i rummet"

    f "Og prinsessen skal være... Akira"

    show akira Flirt2 at left
    ak "Åh~ Hvilken overraskelse~"

    show ayano Angry1 at right
    ay "Det kan ikke være tilfældigt..."

    hide akira
    hide ayano
    show helpy DC at left
    h "Selvfølgelig får hun rollen..."

    f "Oh, du ville gerne have været prinsessen?"

    h "Ad nej..."

    f "Og Helpy, jeg har en helt særlig rolle til dig"
    
    show helpy Happy at left
    h "En vigtig rolle til mig?"

    f "Ja, den her rolle er faktisk super vigtigt"

    h "YES ENDELIG!"

    f "du skal være den onde trold"

    show helpy Angry at left
    h "WHAT!? Hvorfor skal jeg være den onde!?"

    show freddy Good at center
    f "Du passer ret godt til rollen"

    scene bg theater
    show freddy Neutral at center
    show sakura Sad2 at left
    show ayano Shy1 at right
    sa "Hvad med resten af os?"

    show freddy Good at center
    f "I er byens befolkning der hepper på ridderen!"

    show ayano Idle1 at right
    ay "Så vi skal sådan set bare stå og glo?"

    f "Nej, nej! I er VIGTIGE personer der skal stå og glo!"

    scene bg theater
    show akira Flirt2 at left
    ak "Nå [mc]~ Det ser ud til at vi skal øve mange scener sammen~"

    show ayano Angry2 at right
    ay "Freddy, jeg tror virkelig vi skal stemme om rollerne"

    show freddy Neutral at center
    f "INGEN protester! Jeg er instruktøren!"

    menu:
        "Foreslå at bytte roller":
            mc "Måske skulle vi prøve at bytte nogle af rollerne?"

            show freddy Angry at center
            f "HVAD!? Tør du at sætte spørgsmålstegn ved min måde at give roller på!?"

            show akira Sad at left
            ak "Vil du ikke være min ridder, [mc]?~"

        "Accepter din rolle":
            mc "Jeg skal nok gøre mit bedste som ridder"

            show akira Flirt2 at right
            ak "Det bliver så romantisk~"

            "Du kan se Ayano og Sakura udveksle bekymrede blikke"

    scene bg theater
    show freddy Neutral at center
    f "Jeg er den bedste instruktør!"

    f "Jeg har skrevet nogle menuskripter til jer"

    "Freddy begynder at dele papirer ud til jer"

    show helpy DC at left
    h "Vent... Du har skrevet et manuskript?"

    f "Selvfølgelig! Det er et mesterværk"

    f "Her i vil i kunne finde de ting i skal sige og gøre, og selvfølgelig om hvad historien går ud på"

    f "Det er bare små ting..."

    f "Så som at [mc] ender med at kysse prinsessen som så er Akira"

    scene bg theater
    show akira Flirt2 at center
    ak "Åh~ Det lyder som den perfekte scene~"

    show ayano Angry1 at right
    ay "En kyssescene!? Det er for meget!"

    show helpy DC at left
    h "Jeg tror jeg bliver dårlig..."

    hide helpy
    show sakura Sad2 at left
    sa "Freddy... Er du sikker på det en god ide?"

    scene bg theater
    show freddy Neutral at center
    show sakura Sad2 at left
    f "Selvfølgelig! Det er sådan alle gode historie slutter"

    sa "Så... bare et kindkys, ik?"

    f "Nej, et rigtigt kys"

    "Sakura og Ayano kigger nervøst på hinanden"

    menu:
        "Protestér mod kyssescenen":
            mc "Jeg tror ikke jeg har det godt med en kyssescene..."

            show akira Flirt2 at right
            ak "Åh~ Er du genert [mc]?~"

            show freddy Angry at center
            f "INGEN PROTESTER! Det er kunst!"

        "Sig ikke noget":
            "Du står bare i en akavet stilhed mens de andre diskuterer"

            show akira Flirt1 at right
            ak "Jeg tror [mc] synes det er en god ide~"

            show ayano Angry2 at center
            ay "Du kan ikke bare antage hvad [mc] tænker..."

        "Prøv at skifte emne":
            mc "Øh... Hvornår skal vi optræde?"

            f "FOKUSER PÅ KUNSTEN!"

    scene bg theater
    show akira Flirt2 at center
    ak "Vi kommer nok til at skulle øve den scene mange gange~"

    show ayano Angry1 at left
    ay "I burde nok også fokusere på de andre scener..."

    show akira Flirt2 at right
    show freddy Good at center
    f "Lad os starte fra begyndelsen!"

    "Freddy klapper i hænderne for at få alles opmærksomhed"

    f "Scene 1! Ridderen kommer ind i landsbyen"

    scene bg theater
    show freddy Neutral at center
    show helpy DC at left
    h "Hvordan kan det være scene 1? Skal vi ikke vide hvorofor trolden har taget prinsessen?"

    f "DETALJER! Det er ligemeget!"

    "Freddy peger på scenen"

    f "[mc]! Op på scenen!"

    scene bg theater

    menu:
        "Gå op med usikkerhed":
            "Du går langsomt og akavet op på scenen"

            "Du kan mærke at alle kigger på dig"

            show akira Flirt2 at right
            ak "Du ser allerede ud som en rigtig ridder~"
        "Gå selvsikkert op":
            "Du prøver at gå selvsikkert op på scenen"

            show freddy Neutral at center
            f "JA! Sådan skal en ridder gå!"

    scene bg theater
    show freddy Neutral at center
    f "Nu skal byens befolkning stå klar!"

    show helpy DC at left
    h "Vent... Skal vi ikke have kostumer på?"

    f "Jo, det kommer senere. Først skal vi lige øve første scene så i kan se hvad det handler om"

    hide helpy
    f "Alle sammen stil jer klar"

    "Freddy begynder at pege rundt på scenen om hvem der skal stå hvor"

    f "Okay [mc], du skal komme gående ind i byen"

    f "Du er en modig ridder der leder efter eventyr!"

    f "ACTION!"

    "Du er lidt forvirret, men du vælger at gå frem mod de andre som skal forstille at være befolkningen"

    menu:
        "Prøv at virke selvsikker":
            "Du retter dig op og prøver at gå selvsikkert hen mod de andre"
            
            show freddy Good at center
            f "JA! Præcis sådan!"
            
            show akira Flirt2 at right
            ak "Så modig~"

        "Vær lidt forvirret":
            "Du går tøvende frem, usikker på hvad du skal gøre"
            
            show freddy Angry at center
            f "NEJ NEJ NEJ! En ridder er ikke nervøs!"
            
            f "Du skal være MODIG!"

        "Improviser noget":
            "Du beslutter dig for at prøve at spille med"
            
            mc "Goddag brave borgere! Jeg er en ridder på jagt efter eventyr!"
            
            show freddy Good at center
            f "JA! Nu sker der noget!"

    scene bg theater
    show freddy Neutral at center
    f "Okay, nu skal landsbybeboerne fortælle ridderen om den onde trold!"

    "Ayano tager sit papir frem og begynder at læse op fra det"

    show ayano Shy1 at right
    ay "Åh ridder! Vi har brug for din hjælp!"

    f "Nu skal du sige noget [mc]!"

    menu:
        "Læs fra manuskriptet":
            "Du tager hurtigt dit manuskript frem og prøver at finde den rigtige side"

            mc "Øh... Hvad er der sket, brave borger?"

            show freddy Angry at center
            f "MED MERE FØLELSE!"

        "Find på noget at sige":
            mc "Fortæl mig, hvad plager jeres by?"

            show freddy Good at center
            f "JA! Sådan skal det være!"

        "Sig ingenting":
            "Du står bare akavet og siger ikke noget"

            show freddy Angry at center
            f "EN RIDDER ER ALDRIG STILLE!"
            

    scene bg theater
    show sakura Happy2 at left
    sa "En ond trold har taget vores smukke prinsesse til fange!"

    hide sakura
    show akira Flirt2 at right
    ak "Mig~"

    show freddy Neutral at center
    f "Akira! Du er ikke med i denne scene endnu!"

    ak "Jeg ville bare minde [mc] om hvem han kæmper for~"

    hide akira
    show ayano Angry1 at left
    ay "Vi prøver at fokusere på scenen..."

    show helpy DC at center
    h "Skal jeg komme ind som trolden nu?"

    f "NEJ! Du kommer først senere!"

    h "Men hvordan skal folk vide at jeg er trolden hvis de ikke ser mig tage prinsessen?"

    f "Det er KUNST! Det behøver ikke give mening!"

    "Du står stadig midt på scenen og kan mærke hvordan stemningen bliver mere og mere kaotisk"

    f "Sig noget [mc]!"

    scene bg theater
    mc "Oh, undskyld! Jeg vil kæmpe for jeres prinsesse!"

    show sakura Happy2 at center
    sa "Tak ridder! Du er vores eneste håb!"

    sa "Uden prinsessen vil vores by falde"

    mc "I kan stole på mig!"

    hide sakura
    show freddy Good at center
    f "PERFEKT! Hvor var det bare smukt!"

    f "Man skulle næsten tro at jeg havde skrevet det"

    f "Nårh jo, det gjorde jeg"

    show freddy Neutral at center
    f "I har jeres pause nu, så gå ud og find nogle kostumer"

    show helpy DC at left
    h "Skal vi bruge vores pause på at finde kostumer?"

    f "Ja, hvad troede du ellers i skulle bruge jeres pause på?"

    f "Har i noget vigtigere at tage jer til?"

    h "Ja... Alt andet en det der sker her..."

    f "STILLE SNEGL!"

    f "Jeg tror faktisk det ville være bedst hvis jeg hjalp jer med at finde kostumerne"

    f "I kan bare holde jeres pause så, sikke en god ide jeg fik der"

    h "WHAT!?"

    f "Vi ses om 15 minutter"

    "Freddy går ud af teatret og lader jer stå der"

    scene bg theater
    show sakura Happy2 at left
    play music endingSpeech
    sa "Nå, hvad skal vi så lave i pausen?"

    show helpy DC at center
    h "Jeg tror jeg går ud for at få noget luft..."

    hide helpy
    "Helpy gå hen til de store røde døre og forlader teatret"

    show akira Flirt2 at right
    ak "Nå [mc]~ Skal vi ikke øve vores scene sammen?~"

    mc "Øh..."

    show ayano Angry1 at center
    ay "Vi har pause nu Akira..."

    ak "Præcis~ Det er den perfekte tid til at øve~"

    mc "Akira... Hvorfor er du så opsat på at øve?"

    show akira Flirt1 at right
    ak "Hvorfor skulle jeg ikke være det?~ Det er jo vores store scene sammen~"

    mc "Oh... Det er den sidste scene du vil øve?"

    show akira Flirt2 at right
    ak "Selvfølgelig~ Det er jo den mest interrasante del i vores historie~"

    show ayano Angry2 at center
    ay "Du mener kysse scenen..."

    ak "Præcis~ Den skal være perfekt"

    show sakura Sad2 at left
    sa "Akira, du virker meget fokuseret på lige præcis den scene"

    ak "Hvorfor skulle jeg ikke være det?~ Det er jo trods alt mit store øjeblik med [mc]~"

    menu:
        "Akira du skræmmer mig lidt":
            mc "Akira, du skræmmer mig lidt nu..."
            
            show akira HappyIdle at right
            ak "Gør jeg?~ Det var ikke meningen... endnu~"
            
            "Du kan mærke hvordan både Sakura og Ayano rykker tættere på dig"

        "Det er bare et teater...":
            mc "Det er bare et skole teater, ikke?"
            
            show akira Flirt2 at right
            ak "Oh [mc]~ Du forstår slet ikke hvor specielt det her er~"
            
            "Du kan se at Sakura og Ayano kigger bekymret på dig"

        "sig ikke noget":
            "Du vælger ikke at sige noget"
            
            show akira Flirt1 at right
            ak "Så stille [mc]~ Bare vent til vores scene~"
            
            "En ubehagelig stilhed falder over rummet"

    scene bg theater
    "Ayano prøver at skifte emne så det ikke bliver alt for pinligt"
    show ayano Shy1 at center
    ay "Jeg syntes det er unfair at jeg har fået en rolle som bare skal glo"

    mc "Når man tænker over det, så er det stadig en vigtig rolle"

    ay "Oh ja? Hvordan det?"

    mc "Forstil dig hvis der ikke var nogle til at heppe på helten, så ville han kæmpe for ingenting næsten"

    ay "Hmm... Det kan godt være du har ret i det"

    ay "Men jeg føler stadig jeg skulle have haft en større rolle"

    "Du kan se at Helpy kommer tilbage ind i teatret"

    show helpy DC at left
    h "I det mindste SKULLE DU IKKE VÆRE EN GRIM TROLD!"

    ay "Okay, det er nok den væreste rolle"

    h "OG HVORFOR LIGE PRÆCIS MIG!?"

    scene bg theater
    "Pludseligt bliver døren smækket op igen"

    show freddy Neutral at center
    f "SÅ SKAL I HAVE TØJ PÅ!"

    show FT Happy at right

    fx "LUUUU TØJ!"

    hide FT
    f "Ja, ja... I skal have tøj på, altså kostumer"

    f "Følg med mig"

    "I begnder at følge efter Freddy for at finde kostumerne"

    scene bg costume
    "Når du kommer med in kan du ser en kæmpe stort rum fyldt med kostumer"

    "Du har aldrig set et rum så stort før"

    "Når du kigger over mod Funtime Foxy ser du bare at hun stiger ud i luften"

    show freddy Neutral at center
    f "Okay små elever! Nu skal i vælge en kostume"

    "I kigger bare lidt rundt fordi i ved ikke rigtigt hvad i skal lede efter"

    f "... I skal lede efter kostumer som der passer til jeres roller"

    f "Det gider jeg ikke at hjælpe med... Find selv ud af det"

    mc "Men-"

    "Enden du når at sige mere kan du mærke Akira tage fat i din arm med sin hånd"

    scene bg costume
    show akira Flirt2 at center
    ak "Kom [mc]~ Lad os finde et kostume til dig~"

    mc "Hvorfor trækker du mig væk fra de andre, skal vi ikke sige til dem først at vi går?"

    ak "Nej, nej~ Det er der slet ikke nogle grund til~"

    ak "De vil bare forstyrre os~"

    ak "De prøver hele tiden at holde os fra hinanden~"

    menu:
        "Det er fordi jeg ikke kan lide dig på DEN måde":
            mc "Men det er fordi jeg ikke kan lide dig på den måde"

            mc "Du er en fantastisk ven, men jeg er ikke forelsket i dig"

            show akira Concerned at center
            ak "Hvad mener du med det?~"

            ak "Efter alt det vi har været igennem sammen?~"

            "Hendes greb om din arm bliver hårdere"

            ak "Du forstår det bare ikke endnu [mc]~"

            show akira Flirt2 at center
            ak "Men det er okay~ Jeg skal nok få dig til at forstå~"
        "De er lidt for overbeskyttende, jeg kan godt lide dig på DEN måde":
            mc "Ja, og jeg kan ellers godt lide dig på den måde"

            show akira Flirt1 at center
            ak "Det vidste jeg~"

            ak "Du kan også mærke det, ikke?~ Den særlige forbindelse mellem os~"

            "Hun træder tættere på dig"

            ak "De andre... De prøver bare at holde os fra hinanden~"

    show akira Flirt2 at center
    ak "Kom nu~ Det ser ud til at middelalder kostumerne er over her~"

    scene bg costume
    "I går en kort tid og pludseligt ender i ved en masse middelalder kostumer"

    "Der er en masse ridder og prinsesse kostumer"

    show akira Flirt1 at center
    ak "Hvilken farve tror du ville passe på mig bedst [mc]~?"

    define dressColor = ""
    menu:
        "Blå":
            $ dressColor = "blå"
            ak "Blå? Interresant valg~ Blå et vel også en ret royal farve~"
        "Rød":
            $ dressColor = "røde"
            ak "Rød? Interresant valg~ Rød er også en ret flot farve~"
        "Lilla":
            $ dressColor = "lilla"
            ak "Lilla? Interresant valg~ Lilla er også en ret mystisk farve~"
        "Lysserød":
            $ dressColor = "lysserøde"
            ak "Lysserød? Interresant valg~ Lysserød er også en ret sød farve~"
        "Sort":
            $ dressColor = "sorte"
            ak "Sort? Min yndlings farve~ Det er det perfekte valg [mc]~ Du kender mig virkelig~"

    "Akira tager kjolen ned fra stativet og kigger på dig"

    show akira Flirt2 at center
    ak "Hvad med dig [mc]?~ Hvilken rustning vil du have på?"

    ak "Jeg ville forslå den skinnende derovre"

    "Hun tager den ned fra stativet, men den er meget tung"

    ak "Åh, den er lidt tungere end jeg troede hehe~"

    "Hun prøver at holde den op foran dig"

    show akira Flirt1 at center
    ak "Hvad siger du [mc]?~"

    menu:
        "Jeg tager den":
            mc "Det er en god ide Akira, jeg tager den skinnende rustning"
        "Jeg vil hellere have den mørke rustning på":
            mc "Jeg vil hellere have den mørke rustning på"

            show akira Really at center
            ak "Åh~ Men en helt plejer jo ikke at have en mørk rustning~"

            ak "Du skal tage den skinnende~"

            mc "Men den mørke er flot"

            ak "Men du bliver nødt til at være helten~"

    ak "Hmm... Jeg tror vi skal finde et omklædningsrum~"

    ak "Bare så der ikke er nogle der ser os skifte~"

    mc "Det lyder som en god ide"

    scene bg costume
    "I går rundt i rummet og pludseligt kommer i til en gang hvor der står omklædningsrum"

    show akira Idle at center
    ak "Her er det~"

    "Sammen går i ned af gangen og ser flere prøve rum"

    ak "Vi ses om lidt min ridder~"

    scene bg changing_room
    "Akira står ude foran og venter på dig"

    "Du prøver at skifte om til metal ridder rustningen, men den er meget tung og svær at få på"

    "Du kan høre Akira snakke der ude fra"

    ak "Har du brug for hjælp med at få det på?~ Jeg kan godt komme ind og hjælpe"

    mc "Je-"

    show akira Idle at center
    play music akiraTheme
    "Enden du når at svare kan du se Akira fjerner gradinet og går ind"

    mc "Wo-Woah, jeg sagde ikke at du kunne komme ind"

    show akira Flirt2 at center
    ak "Åh, rolig nu, det er jo ikke fordi du ikke har tøj på..."

    ak "Jeg vil bare hjælpe dig med din rustning"

    menu:
        "Få hende til at gå ud":
            mc "Akira, jeg har virkelig ikke brug for din hjælp..."

            ak "Åh~ Er du genert [mc]?~"

            "Hun tager et skridt tættere på"

            show akira Flirt1 at center
            ak "Det behøver du ikke at være~ Vi er jo bare venner der hjælper hinanden~"

            mc "Nej Akira, jeg har virkelig ikke brug for din hjælp"

            show akira Really at center
            ak "Hm~ [mc], du har brug for min hjælp. Du ville aldrig blive færdig alene~"

            show akira Flirt1 at center
            "Hun går alligevel hen til dig og begynder at hjælpe dig med at få rustningen på"

            "Det virker som om der ikke er noget at gøre, hun prøver alligevel at hjælpe dig"

            ak "Se~ Det er meget nemmere når man hjælper hinanden~ Ligesom et kæreste par~"
        "Jeg har brug for hjælp":
            mc "Okay... Måske kunne jeg godt bruge lidt hjælp med rustningen..."

            show akira Flirt2 at center
            ak "Det vidste jeg~ Lad mig hjælpe~"

            "Hun går hen og begynder at hjælpe dig med at få delene af rustningen på plads"

            ak "Se~ Det er meget nemmere når man hjælper hinanden~ Ligesom et kæreste par~"

            "Hun fortsætter med at hjælpe dig med at få delene på"

    show akira Flirt2 at center
    "Til sidst får i endelig rustningen på dig"

    "I går ud af omklædningsrummet og tilbage til kostumet rummet"

    scene bg costume
    "Når i kommer ud står Akira bare og kigger på dig"

    show akira Flirt2 at center
    ak "Du ser fantastisk ud som ridder~"

    ak "Jeg kan næsten ikke vente med at se dig redde mig~"

    mc "Tak... Men burde du ikke også skifte til din kjole?"

    ak "Jo, selvfølgelig~ hvis du venter på mig her~"

    mc "Jeg havde ikke rigtigt planlagt at gå nogen steder"

    ak "Du er så sød [mc]~"

    scene bg costume
    "Akira går hen til omklædningsrummet for at klæde om"

    "Du venter i noget tid og ved ikke rigtigt hvad du skal lave imens"

    "Du kigger sådan set bare ude i luften"

    "Men endelig åbner hun gardinet og går ud"

    show akira Princess at center
    ak "Hvad siger du [mc]?~"

    menu:
        "Du ser fantastisk ud":
            mc "Du ser virkelig fantastisk ud i den kjole, den passer perfekt til dig"
            
            ak "Jeg vidste du ville elske den~ Jeg valgte den specielt til dig~"
            
            "Hun går elegant hen mod dig med et drillende smil"
            
            ak "Bare vent til du ser mig på scenen~ Der vil du se hvor smuk din prinsesse er~"
            
            mc "Du tager det ret seriøst..."
            
            ak "Selvfølgelig gør jeg det~ Det her er vores store øjeblik sammen [mc]~"
        "Du ser smuk ud":
            mc "Du ser virkelig smuk ud... Kjolen er perfekt til rollen som prinsesse"
            
            ak "Åh [mc]~ Du får mig til at rødme~"
            
            "Hun drejer rundt så kjolen svinger, hun hollder stadig 100 procent øjenkontakt med dig"
            
            ak "Jeg håber du er ligeså begejstret når vi kommer til vores... særlige scene sammen~"
            
            mc "Du mener slutningen?"
            
            ak "Præcis~ Hvor du endelig får lov at kysse din prinsesse~"
        "Det er okay":
            mc "Det ser okay ud... Det passer godt til rollen som prinsesse"
            
            ak "Bare okay?~ Efter jeg valgte den specielt til vores scene sammen?~"
            
            "Hun går tættere på, hendes bevægelser er elegante men der er noget intenst i hendes blik"
            
            ak "Det er okay [mc]~ Jeg ved du bare er genert~"
        "Det er ikke min stil":
            mc "Det er ikke rigtigt min stil... Måske er den lidt for meget"
            
            ak "For meget?~ [mc], en prinsesse skal være iøjenfaldende~"
            
            "Hun går tættere på med et intenst blik"
            
            ak "Eller måske... Er det fordi du hellere vil se en anden i den?~"
            
            mc "Nej, det var ikke det jeg mente..."
            
            ak "Det håber jeg ikke~ For jeg er den eneste prinsesse for dig~"

    "Før samtalen kan fortsætte, bliver i afbrudt af nogle stemmer som i kan høre"

    show sakura Happy2 at left
    sa "Der er i jo, vi har ledt over det hele efter jer"

    ak "Vi skulle bare prøve vores udklædning~"
    
    show ayano Angry1 at right
    ay "Freddy leder efter os alle samme. Vi skal tilbage til teatret"

    sa "I ser... Flotte ud i jeres kostumer"

    ak "Især [mc]~ Han er den perfekte ridder til mig prinsessen"

    "Ayano og Sakura kigger bekymret på hinanden"

    ay "Vi skal virkelig tilbage nu..."

    scene bg costume
    "I begynder alle at gå tilbage mod teatret"

    show sakura Sad2 at center
    sa "[mc]... Er du okay?"

    mc "Ja, det går nok..."

    show ayano Shy1 at left
    ay "Vi holder øje med hende... Hun bliver mere og mere intens"
    
    sa "Bare hold dig tæt til os"

    "I kan høre Freddys stemme blive højere jo tættere i kommer på teatret"

    scene bg costume
    f "HVOR ER MINE SMÅ ELELVER!? VI HAR EN FORSTILLING AT ØVE!"

    scene bg theater
    play music joyful
    "I kommer alle sammen ind i teatret igen"

    show freddy Angry at center
    f "HVOR HAR I VÆRET HENNE!?"

    show helpy DC at left
    h "De har sikkert bare gemt sig for dig..."

    f "STILLE LILLE SNEGL!"

    show akira Princess at right
    ak "Vi prøvede bare vores kostumer~"

    show freddy Neutral at center
    f "Hmm... De ser faktisk ret gode ud"

    show freddy Good at center
    f "Specielt din rustning [mc], den er PERFEKT til rollen!"

    show helpy Angry at left
    h "Hvad med mit kostume!?"

    f "Du behøver ikke at have et kostume for at ligne en trold..."

    f "Du ser præcis lige så grim ud som du skal"

    h "DET KAN DU IKKE MENE!?"

    scene bg theater
    show freddy Neutral at center
    f "Nå! Er i klar til at øve den næste scene?"

    f "[mc], du har lige fundet ud af hvor trolden holder prinsessen fanget"

    f "I denne scene skal [mc] komme ind på scenen og finde prinsessen"

    f "Trolden skal stå og holde vagt foran hende"

    show helpy DC at left
    h "Skal jeg virkelig stå der?"

    show freddy Angry at center
    f "JA! DU ER EN TROLD! OPFØR DIG SOM EN!"

    show akira Princess at right
    ak "Jeg er klar til at blive reddet af min ridder~"

    f "PERFECT! ALLE PÅ PLADS!"

    scene bg theater
    "Helpy stiller sig foran Akira, som sidder på en stol der skal forestille en trone"

    show freddy Good at center
    f "og... ACTION!"
    hide freddy

    menu:
        "Vær modig":
            mc "Slip prinsessen fri, din onde trold!"
            
            show helpy DC at left
            h "Øh... Nej?"
            
            f "MERE FØLELSE! MERE DRAMA!"
            
        "Vær dramatisk":
            mc "I den ædle ridders navn, kræver jeg at du frigiver prinsessen!"
            
            show helpy DC at left
            h "Aldrig... muhaha?"
            
            f "BEDRE! MEN STADIG IKKE GODT NOK!"

        "Improviser":
            mc "Din tid er forbi, trold! Jeg er kommet for at redde prinsessen!"
            
            show helpy DC at left
            h "Som om du kan besejre mig..."
            
            f "NU BEGYNDER DET AT LIGNE NOGET!"

    show akira Princess at right
    ak "Oh [mc]~ Min modige ridder er kommet for at redde mig~"

    "Hun rejser sig dramatisk fra stolen"

    ak "Jeg vidste du ville komme efter mig~"

    show freddy Neutral at center
    f "Nej nej nej! Du skal blive siddende! Du er jo fanget!"

    ak "Men jeg vil jo bare være tættere på min ridder~"

    f "DU ER FANGET AF TROLDEN!"

    show helpy Angry at left
    h "Kan vi ikke bare springe denne scene over?"

    f "NEJ! VI GØR DET IGEN!"

    "I går tilbage til jeres start positioner"

    f "Fra toppen! Og denne gang... MERE DRAMA!"

    "Du kan mærke hvordan Akira kigger på dig uden af kigge væk"

    "I alle sammen går tilbage til jeres start pladser igen"

    "I prøver at fuldføre scenen igen"

    scene bg theater

    show freddy Neutral at center
    f "ACTION!"

    "Du går ind på scenen igen, denne gang kan du mærke Akiras intense blik følge hver eneste af dine bevægelser"

    show helpy DC at left
    h "Øh... Du kommer aldrig til at redde prinsessen!"

    show akira Princess at right
    ak "Min ridder~ Jeg har ventet på dig~"

    f "DU ER BANGE! DU ER FANGET!"

    ak "Hvordan kan jeg være bange når min helt er her?~"

    "Hun rejser sig igen fra stolen"

    show freddy Angry at center
    f "BLIV SIDDENDE!"

    show helpy Angry at left
    h "Hun ødelægger jo hele scenen..."

    ak "Shh lille trold~ Kan du ikke se at [mc] og jeg har et øjeblik?~"

    f "Alle sammen STOP! Vi tager spise pause nu..."

    h "Allerede?"

    f "JA! ALLE UD!"

    hide freddy
    "Freddy går ud af teatret og lader jer stå der"

    mc "Han virkede sur..."

    h "Måske fordi der er visse personer der ikke kan følge deres menuskript..."

    ak "De- Det må i undskylde... Jeg syntes bare det gav mening når min helt var her~"

    h "I skal nok have de der forfærdelige kostumer af nu, inden i går til spise pause"

    scene bg theater
    show ayano Angry1 at right
    show sakura Dissapointed1 at left
    ay "Akira... Du kommer med mig"

    sa "[mc], du kan følge med mig"

    show akira Angry1 at center
    ak "Prøver i at skille os fra hinanden?"

    ay "Det er måske bare bedst at i klæder om hver for sig"

    ak "Fint!..."

    "Ayano følger Akira med over til omklædningen"

    "Du følger efter Sakura til omklædningen"

    scene bg costume
    show sakura Sad2 at center
    play music akiraTheme
    sa "[mc]... Jeg ved slet ikke hvad jeg skal sige"

    sa "Hun bliver værre og værre... Det er som om hun ikke kan stoppe sig selv"

    menu:
        "Jeg er bekymret":
            mc "Jeg er også begyndt at blive ret bekymret..."
            
            sa "Det forstår jeg godt. Den måde hun kigger på dig..."
            
            sa "Det er som om hun lever i sin egen fantasi hvor i to..."
            
        "Måske overreagerer vi":
            mc "Måske overreagerer vi bare lidt? Hun er måske bare meget dedicated til sin rolle"
            
            show sakura Sad3 at center
            sa "[mc]... Du ved godt det er mere end det"
            
            sa "Den måde hun opfører sig på... Det er ikke normalt"
        
        "Hvad skal jeg gøre?":
            mc "Jeg ved virkelig ikke hvad jeg skal gøre..."
            
            show sakura Happy2 at center
            sa "Du skal ikke gøre noget. Vi passer på dig"

    "Endelig når i hen til omklædnings rummet og du klæder om"

    "Efter lidt tid kommer du ud af omklædningsrummet og går tilbage til teatret"

    scene bg theater

    "Når i kommer tilbage kan i se at de andre elever allerede er gået til frokost"

    show sakura Happy1 at center
    sa "Skal vi følges til frokost i dag?"

    mc "Det tror jeg ville være en god ide"

    scene bg hallWay
    "I begynder at gå sammen mod kantinen"

    show sakura Happy2 at center
    sa "Det er rart at kunne slappe lidt af efter alt det der skete i teatret"

    mc "Ja, det var ret intenst"

    "Mens i går, bemærker du at gulvet er blevet vasket"

    sa "Vi skal passe på, gulvet er vådt her"

    "Lige idet Sakura siger det, glider hun på det våde gulv"

    "Du prøver at gribe hende, men ender med selv at miste balancen"

    scene bg hallway_floor
    "I falder begge to, og du lander hen over Sakura"

    scene bg sakuraSpecial1
    sa "Å-åh... Undskyld [mc]..."

    "I er pludseligt meget tæt på hinanden"

    mc "Er du okay... Er du kommet til skade?"

    sa "Nej, jeg har det fint, bare lidt pinligt..."

    "Før du når at rejse dig, kan du høre hurtige fodtrin nærme sig"

    scene bg hallWay
    play music akiraCreepyTheme
    "Du kigger op og ser Akira stå i gangen, hendes udtryk er iskoldt"

    mc "A-Akira... Det er ikke som det ser ud"

    "Du prøver hurtigt at komme op, men før du når det, mærker du en hånd gribe hårdt fat i din arm"

    "Hun trækker dig hårdt med sig"

    "Hun kigger helt koldt i den retning hun går uden at smile"

    mc "Akira, virkelig, det er ikke som du tror"

    "Hun svare ikke og fortsætter med at trække dig hårdt uden et ansigts udtryk"

    scene bg corridor
    "Efter at komme længere væk stopper hun op"

    mc "Det var virkelig ikke min menin-"

    "Pludseligt tager hun fat i din skole uniform og trækker dig hen til sig"

    show akira Angry2 at center
    "Før du kan nå at gøre noget trækker hun dig helt til sig og kysser dig"

    "Efter en kort tid giver hun slip på dig igen"

    "Du står helt stille, stadig i chok over hvad der lige er sket"

    ak "Nu ved du hvem du tilhøre~"

    "Du træder et skridt tilbage"

    mc "Akira... Hvorfor gjorde du det?"

    show akira Angry1 at center
    ak "Fordi jeg så hvordan du var med {i}hende{/i}~"

    ak "Du tilhører mig [mc]... Kun mig~"

    "Hendes stemme er en blanding af truende og kærlig"

    "Du kan høre at Sakura løber hen til dig"

    show sakura Hand at right
    sa "[mc]! Er du okay!?"

    "Sakura kommer løbende ned af gangen"

    show akira Flirt1 at center
    ak "Åh~ Kommer du for at se hvad du er gået glip af?~"

    sa "[mc]... Hvad har hun gjort?"

    menu:
        "Hun kyssede mig...":
            mc "Hun... hun kyssede mig..."
            
            show sakura Sad3 at right
            sa "Akira, hvordan kunne du!?"
            
            show akira Flirt2 at center
            ak "Jeg tog bare hvad der er mit~"
            
        "Jeg har det ikke godt":
            mc "Jeg har det virkelig ikke godt lige nu..."
            
            show sakura Sad2 at right
            sa "Det er okay [mc], jeg er her nu"
            
            show akira Angry2 at center
            ak "Han har det fint~ Vi havde bare vores første kys~"
            
        "Sig ikke noget":
            "Du kan ikke få ordene frem, stadig rystet over hvad der er sket"
            
            show akira Flirt2 at center
            ak "Har kysset taget vejret fra dig?~ Det er forståeligt~"

    show ayano Angry2 at left
    ay "Slip [mc] fri. Nu."

    ak "Slip fri?~ Han er ikke fanget~ Han er præcis hvor han skal være~"

    show akira Flirt2 at center
    ak "I prøver altid at komme imellem os~"

    show ayano Angry1 at left
    ay "Der er ikke noget 'os' Akira. Du tvinger [mc] til at være sammen med dig"

    show sakura Sad2 at right
    sa "[mc], kom herover..."

    "Du begynder langsomt at bevæge dig væk fra Akira"

    show akira Angry2 at center
    ak "Hvor tror du du er på vej hen?~"

    "Hun griber ud efter din arm igen, men denne gang er Ayano hurtigere"

    show ayano Angry2 at left
    "Ayano stiller sig mellem dig og Akira"

    ay "Det er nok nu"

    ak "Nok?~ Vi er ikke engang begyndt endnu~"

    sa "[mc]... Du ryster..."

    "Du havde slet ikke lagt mærke til at du rystede"

    show akira Angry1 at center
    ak "Han ryster af spænding~ Efter vores første kys~"

    ay "Han ryster fordi du skræmmer ham!"

    menu:
        "Hold dig bag Ayano":
            "Du bliver stående bag Ayano, bange for hvad Akira vil gøre"
            
            show akira Angry2 at center
            ak "Gemmer du dig?~ Bag {i}hende{/i}?~"
            
        "Prøv at tale med Akira":
            mc "Akira, du gør mig bange..."
            
            ak "Bange?~ For din kærlighed til mig?~"
            
        "Hold dig tæt på Sakura":
            "Du bevæger dig tættere på Sakura, væk fra Akira"
            
            show akira Angry2 at center
            ak "Løber du tilbage til {i}hende{/i}?~"

    "Pludseligt kan i høre stemmer nærme sig"

    scene bg corridor
    show freddy Angry at right
    f "JEG KAN HØRE JER FRA DEN ANDEN ENDE AF SKOLEN!"

    show akira Flirt2 at center
    ak "Vi øvede bare vores roller~"

    show ayano Angry1 at left
    ay "Det er ikke sandt! Hun overfaldt [mc]!"

    show freddy Neutral at right
    f "Overfaldt? Hvad mener du med det?"

    hide ayano
    show sakura Sad2 at left
    sa "Hun... hun kyssede [mc] mod hans vilje..."

    show freddy Angry at right
    f "WHAT!? I MIT TEATER STYKKE!?"

    show akira Angry2 at center
    ak "Det var bare en forsmag på slutscenen~"

    f "DEN SCENE ER FØRST TIL SIDST!"

    menu:
        "Fortæl Freddy sandheden":
            mc "Det var ikke teater... Hun tvang mig til at kysse hende"
            
            show freddy Neutral at right
            f "..."
            
            f "Er dette rigtigt, Akira?"
            
        "Lad de andre forklare":
            "Du kan ikke få ordene frem, stadig rystet"
            
            show ayano Angry2 at left
            ay "Hun har været besat af [mc] i lang tid nu"

            ay "Hun tvang [mc] til at kysse hende"
            
        "Vær stille":
            "Du står bare stille, ude af stand til at forklare situationen"
            
            show sakura Sad3 at left
            sa "Hun er gået over stregen denne gang..."

            sa "hun tvang [mc] til at kysse hende"

    show freddy Angry at right
    f "Ved i hvad? Jeg tror vi skal holde en EKSTRA LANG pause!"

    f "I har fri resten af dagen!"

    show akira Flirt1 at center
    ak "Perfekt~ Så kan [mc] og jeg tilbringe mere tid sammen~"

    show freddy Angry at right
    f "NEJ! I går HVER FOR SIG!"

    "Freddy's stemme er usædvanligt alvorlig"

    f "Akira, du kommer med mig. Vi skal snakke med rektor"

    show akira Angry1 at center
    ak "Men-"

    f "INGEN UNDSKYLDNINGER!"

    scene bg corridor
    show freddy Angry at right
    "Freddy tager fat i Akiras arm"

    f "KOM SÅ!"

    show akira Angry2 at center
    "Akira sender dig et sidste intenst blik"

    ak "Vi ses i morgen [mc]~ Så kan vi fortsætte hvor vi slap~"

    hide freddy
    hide akira
    "Freddy trækker Akira med sig ned af gangen"

    show sakura Sad2 at left
    sa "[mc]... Er du okay?"

    show ayano Shy1 at right
    ay "Du ryster stadig..."

    menu:
        "Jeg har det ikke godt":
            mc "Jeg... jeg har det virkelig ikke godt lige nu"
            
            show sakura Sad3 at left
            sa "Det er forståeligt... Det hun gjorde var forfærdeligt"
            
        "Jeg vil bare hjem":
            mc "Jeg vil bare gerne hjem..."
            
            show ayano Shy2 at right
            ay "Vi følger dig hjem"
            
        "Jeg er bange":
            mc "Jeg er bange... For hvad hun vil gøre i morgen"
            
            show ayano Angry1 at right
            ay "Vi lader dig ikke være alene med hende igen"

    sa "Kom, lad os følges hjem..."

    ay "Ja, du skal ikke være alene nu"

    menu:
        "Tag imod deres hjælp":
            mc "Tak... Det ville jeg sætte pris på"
            
            show sakura Happy2 at left
            sa "Vi passer på dig"
            
        "Sig du vil være alene":
            mc "Jeg... jeg tror jeg har brug for at være alene"
            
            show ayano Shy1 at right
            ay "Det er ikke sikkert [mc]... Ikke efter det her"
            
            sa "Lad os i det mindste følge dig hjem"

    "I begynder at gå mod udgangen sammen"

    sa "Vi skulle aldrig have ladet dig være alene med hende..."

    ay "Vi burde have set hvor farlig hun kunne blive"

    "Sammen begynder i at gå i mod udgangen af skolen"

    scene bg street
    play music t2
    "I går sammen ned af gaden i stilhed"

    show sakura Sad2 at left
    sa "Det må have været forfærdeligt..."

    show ayano Shy1 at right
    ay "Jeg forstår ikke hvordan hun kunne gøre sådan noget"

    menu:
        "Jeg er stadig i chok":
            mc "Jeg kan stadig ikke helt fatte hvad der skete..."
            
            sa "Det er forståeligt... Det kom fra ingenting"
            
            ay "Hun har altid været intens, men dette..."
            
        "Jeg er bange for i morgen":
            mc "Jeg er virkelig nervøs for at skulle i skole i morgen..."
            
            ay "Vi sørger for at hun ikke kommer i nærheden af dig"
            
            sa "Du skal ikke være alene med hende igen"
            
        "Jeg føler mig skyldig":
            mc "Måske hvis jeg ikke var faldet..."
            
            show sakura Sad3 at left
            sa "Nej! Dette er ikke din skyld!"
            
            show ayano Angry1 at right
            ay "Du må ikke give dig selv skylden for hendes handlinger"

    "Efter noget tid når i endelig dit hus"

    "Du åbner døren og i går ind"

    scene bg kitchen
    play music t9
    "I følges ud i køkkenet"

    show sakura Hand at left
    show ayano Sad1 at right
    sa "[mc]... Læg dig på sofaen i stuen, så laver vi noget mad til dig"

    mc "Vil i virkelig gøre det for mig?"

    show sakura Happy2 at left
    sa "Selvfølgelig vil vi det. Du har været igennem meget i dag"

    show ayano Smile1 at right
    ay "Du skal bare slappe af, vi tager os af det"

    mc "Tak... I er virkelig gode venner"

    scene bg livingroom
    "Du går ind i stuen og lægger dig på sofaen"

    "Du kan høre pigerne lave mad ude i køkkenet"

    "Efter alt det der er sket i dag, føles det godt bare at kunne ligge ned"

    "Efter noget tid kommer pigerne ind med maden"

    show sakura Happy2 at left
    sa "Vi har lavet din livret"

    show ayano Smile1 at right
    ay "Vi håber det kan få dig til at føle dig bedre tilpas"

    menu:
        "Tak, det betyder meget":
            mc "I aner ikke hvor meget det betyder..."
            
            sa "Vi er her for dig [mc]"
            
            ay "Du skal ikke være alene gennem det her"
            
        "I skulle ikke have gjort alt det for mig":
            mc "I skulle virkelig ikke have..."
            
            show sakura Happy1 at left
            sa "Det er ingen besvær, vi vil bare gerne hjælpe"
            
            ay "Lad os tage os af dig i dag"
        
        "Jeg er ikke særlig sulten":
            mc "Jeg ved ikke om jeg kan spise noget..."
            
            show sakura Sad2 at left
            sa "Du skal have noget at spise... Bare lidt"
            
            ay "Du har brug for energien"

    "I sætter jer alle sammen og spiser sammen"

    sa "Vi bliver hos dig indtil du falder til ro"

    sa "I nat sover vi her hos dig"

    mc "Hos mig? Men jeg har kun én seng"

    sa "Så er det godt at jeg har 2 sove poser til Ayano og jeg"

    show ayano Shy1 at right
    ay "Vi vil ikke lade dig være alene i nat... ikke efter det der skete"

    show sakura Happy2 at left
    sa "Desuden har jeg altid ekstra soveposer med i min taske"

    mc "Har du altid soveposer med?"

    sa "Man ved aldrig hvornår ens venner har brug for en..."

    menu:
        "Er I sikre?":
            mc "Er I helt sikre på I vil blive?"
            
            show sakura Happy1 at left
            sa "Selvfølgelig er vi det"
            
            ay "Vi ville ikke kunne sove af bekymring alligevel"
            
        "Tak...":
            mc "Jeg... tak. Jeg er virkelig glad for at have jer"
            
            sa "Det er det venner er til for"
            
            show ayano Shy2 at right
            ay "Vi passer på hinanden"
            
        "Det er ikke nødvendigt":
            mc "I behøver virkelig ikke..."
            
            show sakura Sad2 at left
            sa "Jo, vi gør. Vi vil ikke risikere at..."
            
            ay "At hun kommer tilbage i nat"

    "Efter I har spist færdig, begynder Sakura at finde soveposerne frem"

    sa "Vi kan lave det hyggeligt hernede"

    ay "Og hvis du har brug for at snakke i løbet af natten..."

    sa "Så er vi her"

    scene bg livingroom
    "I begynder at gøre stuen klar til natten"

    show sakura Happy2 at left
    sa "Vi kunne måske se en film sammen? Noget der får os til at tænke på noget andet"

    show ayano Smile1 at right
    ay "Det lyder som en god idé"


    menu:
        "Hvilken slags film skal vi se?":
            mc "Hvad kunne i tænke jer at se?"
            
            sa "Noget hyggeligt... Måske en komedie?"
            
            ay "Bare ikke en romantisk film..."
            
        "Jeg er nok ikke den sjoveste at være sammen med lige nu":
            mc "Jeg er nok ikke særlig sjov at se film med lige nu..."
            
            show sakura Sad2 at left
            sa "Du skal ikke tænke på at underholde os"
            
            ay "Vi vil bare være her for dig"
            
        "Det lyder rart":
            mc "Det kunne være rart at tænke på noget andet..."
            
            sa "Præcis! Vi skal nok få dig i bedre humør"

    "Sakura finder nogle puder og tæpper frem"

    sa "Vi kan lave det rigtig hyggeligt her"

    "Hun begynder at indrette stuen med puderne og tæpperne"

    show ayano Shy1 at right
    ay "Det vigtigste er at du føler dig tryg"

    "I sætter jer alle sammen i sofaen med tæpperne omkring jer"

    sa "Bare læn dig tilbage og slap af [mc]"

    "I sætter filmen på og i ender med at hygge jer sammen"

    "Efter lidt tid falder du i søvn på sofaen, sammen med pigerne ved siden af dig"

    # Til sidst dør Akira for at få en sørgelig slutning
    # Sørgelig musik (Sweet but pshyco by Daycore) spiller imens en besked bliver afspillet "Hej [mc], jeg håber du stadig har det godt, selvom jeg ikke er her mere. Jeg vil altid være i dit hjerte, og jeg vil altid elske dig. Jeg håber du kan tilgive mig for alt hvad jeg har gjort. Der er mange ting jeg ikke burde have gjort, og mange ting jeg har fortrudt. Det er underligt at tænke på at det jeg gjorde for at komme tættere på dig, fik mig længere væk fra dig. Men jeg tror at du og verdenen vil have det bedre uden mig. Jeg vil altid være din prinsesse. Farvel [mc]"

    $ persistent.current_day = 3
    return