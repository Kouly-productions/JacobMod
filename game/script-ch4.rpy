label ch4_main:
    
    $ currentDay = "Torsdag"
    play music t8
    scene bg living room
    "TORSDAG"

    "Du vågner langsomt op, og det første du bemærker er varmen fra dine venner der stadig sover ved siden af dig på sofaen"

    "Du kan høre Sakuras rolige åndedræt, og se Ayanos fredelige ansigt mens hun sover"

    "Sakura åbner søvnigt øjnene og smiler til dig"
    show sakura Happy2 at left
    sa "Mmm... God morgen [mc]"

    show ayano Shy1 at right
    "Ayano vågner også stille og strækker sig forsigtigt"

    ay "Har du sovet godt?"

    menu:
        "Ja, takket være jer":
            mc "Ja, det er rart at have jer her"
            
            show sakura Happy3 at left
            sa "Vi er også glade for at være her"
            
            show ayano Smile1 at right
            ay "Det føles... rigtigt sådan her"
            
        "Jeg er stadig træt":
            mc "Jeg kunne godt bruge lidt mere søvn..."
            
            show sakura Happy1 at left
            sa "Vi har tid til at vågne stille og roligt"
            
            ay "Jeg kunne lave noget morgenmad mens du vågner"
            
        "Det var den bedste søvn i lang tid":
            mc "Jeg har ikke sovet så godt i lang tid"
            
            show sakura Happy2 at left
            sa "Det er fordi du følte dig tryg"
            
            show ayano Shy2 at right
            ay "Vi er her for dig... altid"

    "Sakura rejser sig langsomt fra sofaen og begynder at folde tæpperne sammen"

    "Imens rejser Ayano sig op og begynder at gå ud imod køkkenet"

    "Du ligger stadig i sofaen og er i gang med at prøve at vågne helt op"

    scene bg livingroom
    "Du kan høre dem bevæge sig rundt i huset, mens morgensolen langsomt bliver stærkere"

    show sakura Happy2 at left
    sa "Du må gerne blive liggende lidt endnu [mc]"

    "Sakura lægger forsigtigt et tæppe over dig"

    sa "Vi tager os af morgenmaden"

    scene bg livingroom

    "Du kan høre Ayano rumstere i køkkenet"

    "Du lukker øjnene igen og nyder varmen fra tæppet"
    
    "Du kan høre pigerne tale lavt sammen i køkkenet"
    
    "Det føles næsten som en drøm... at have venner der passer sådan på en"

    "Efter lidt tid kan du dufte noget der bliver bagt"

    ay "Jeg prøver at lave franske croissanter... Jeg har aldrig lavet dem før"

    sa "De dufter allerede vidunderligt"

    "Du kan høre deres stille latter og småsnak fra køkkenet"

    sa "Tror du vi skulle lave varm kakao også?"

    ay "Det ville være perfekt til croissanterne"

    "Der er noget fredfyldt over denne morgen... Noget anderledes fra alt det kaos der har været"

    "Duften af friskbagte croissanter bliver stærkere, og du kan høre pigerne småsnakke i køkkenet"

    scene bg kitchen
    "Du rejser dig endelig fra sofaen og går ud i køkkenet"

    show ayano Smile1 at right 
    show sakura Happy2 at left
    "Du finder dem midt i deres madlavning, køkkenet er fyldt med en varm og hyggelig atmosfære"

    sa "Åh, der er du! Vi var lige ved at være færdige"

    ay "Jeg håber de smager okay... Det er første gang jeg prøver at lave croissanter"

    "Hun holder en plade med gyldenbrune croissanter"

    menu:
        "De ser fantastiske ud":
            mc "De ser helt utrolige ud, Ayano"
            
            show ayano Shy2 at right
            ay "Virkelig? Jeg var så nervøs..."
            
            show sakura Happy3 at left
            sa "Se! Jeg sagde jo de ville blive perfekte"
            
        "Jeg glæder mig til at smage dem":
            mc "Jeg kan næsten ikke vente med at smage dem"
            
            show ayano Smile1 at right
            ay "Jeg håber de smager lige så godt som de dufter"
            
        "Du er virkelig dygtig i et køkken":
            mc "Du overrasker mig hver gang med dine evner i køkkenet"
            
            show ayano Shy2 at right
            ay "Det... det er bare noget jeg godt kan lide at gøre..."
            
            show sakura Happy2 at left
            sa "Især når det er for venner"

    "Sakura har dækket bordet med tallerkener og kopper til varm kakao"

    sa "Skal vi sætte os?"

    scene bg kitchen
    "I sætter jer alle sammen rundt om bordet"

    "Du tager en bid af croissanten og kan mærke hvor sprød og luftig den er"

    menu:
        "De smager fantastisk":
            mc "Ayano, de er perfekte"
            
            show ayano Shy2 at right
            ay "Er du sikker? Jeg synes måske de blev lidt for..."
            
            show sakura Happy3 at left
            sa "Nej, [mc] har ret! De er vidunderlige"
            
        "Mmmmm":
            "Du er for optaget af at nyde croissanten til at sige noget"
            
            show sakura Happy2 at left
            sa "Jeg tror [mc] kan lide dem"
            
            show ayano Smile1 at right
            ay "Det gør mig glad..."
            
        "Du skulle åbne en café":
            mc "Du kunne sagtens åbne din egen café med sådan nogle evner"
            
            show ayano Shy2 at right
            ay "En... café? Nej, jeg... jeg er ikke så god..."
            
            show sakura Happy2 at left
            sa "Jo du er! Det ville være den perfekte café"

    "I nyder morgenmaden sammen i en behagelig stilhed"

    "Men pludselig kommer du i tanke om noget"

    mc "Vent... hvad med jeres skoletøj?"

    show sakura Happy1 at left
    sa "Åh, det er okay. Vi tog det med i går"

    show ayano Smile1 at right
    ay "Vi... vi tænkte måske vi skulle overnatte igen"

    "Du kan mærke varmen i dit hjerte over hvor omsorgsfulde dine venner er"

    ay "Og vi har stadig god tid enden skole"

    "Efter morgenmaden begynder I stille og roligt at gøre jer klar til skoledagen"

    scene bg livingroom
    "Mens pigerne skiftes til at klæde om, rydder du op efter morgenmaden"

    "Du kan ikke lade være med at tænke på hvor anderledes dit liv er blevet"

    "For ikke så længe siden var du alene... og nu har du venner der betyder alt for dig"

    show sakura Happy2 at left
    show ayano Smile1 at right
    "Pigerne kommer tilbage, nu i deres skoletøj"

    sa "Er du klar til at tage afsted?"

    menu:
        "Ja, lad os følges":
            mc "Ja, det bliver dejligt at følges med jer"
            
        "Bare et øjeblik":
            mc "Giv mig lige et minut til at samle mine ting"
            
        "Jeg er lidt nervøs":
            mc "Jeg er... lidt nervøs for skolen i dag"
            
            show ayano Shy2 at right
            ay "Det er okay... vi er her"
            
            show sakura Happy2 at left
            sa "Vi passer på dig"

    "I samler jeres tasker og gør jer klar til at gå"

    scene bg street
    play music t2
    "Du åbner døren og sammen går i ud i morgenluften"

    show sakura Happy2 at left
    show ayano Smile1 at right
    "Det er en kølig morgen, men solen skinner lidt gennem skyerne"

    sa "Det er en smuk morgen, synes I ikke?"

    ay "Ja... det føles behageligt"

    "I begynder at gå ned af gaden sammen"

    show ayano Shy1 at right
    ay "Jeg har tænkt på noget..."

    mc "Hvad er det?"

    ay "Med [clubName]... måske kunne vi tage på vores første rigtige udforskning i dag?"

    show sakura Happy3 at left
    sa "Det er faktisk en rigtig god idé!"

    menu:
        "Hvor skulle vi tage hen?":
            mc "Har I et bestemt sted i tankerne?"
            
            show sakura Happy2 at left
            sa "Faktisk... har jeg hørt om en gammel park ikke så langt herfra"
            
            ay "Den med kirsebærtræerne?"
            
            sa "Præcis! Den skulle være helt magisk ved solnedgang"
            
        "Er det ikke lidt for hurtigt?":
            mc "Skulle vi ikke planlægge det lidt mere?"
            
            show sakura Happy1 at left
            sa "Nogle gange er de bedste eventyr dem, der bare sker"
            
            show ayano Smile1 at right
            ay "Og vi har jo hinanden"
            
        "Det lyder spændende":
            mc "Jeg er med på den idé"
            
            show sakura Happy3 at left
            sa "Det er sådan det skal lyde!"
            
            show ayano Shy2 at right
            ay "Vi kunne tage derhen efter skole..."

    "Pludselig kan I høre hurtige fodtrin bag jer"

    show akira Flirt2 at center
    play music akiraTheme
    ak "God morgen allesammen~"

    "Du kan mærke hvordan stemningen øjeblikkeligt ændrer sig"

    show ayano Angry1 at right
    ay "Hvad laver du her, Akira?"

    show akira Flirt1 at center
    ak "Åh~ Jeg går bare til skole... ligesom jer~"

    ak "Men hvilket held at støde på [mc] her~"

    menu:
        "Hold dig tæt til Sakura":
            "Du går tættere på Sakura, for at finde tryghed i tæt ved hende"
            
            show sakura Sad2 at left
            "Sakura holder din arm blidt med sin hånd"
            
            show akira Angry1 at center
            ak "Åh?~ Stadig så bange for mig?~"
            
        "Konfrontér Akira":
            mc "Akira... du sagde du ville ændre dig"
            
            show akira Flirt2 at center
            ak "Det har jeg også~ Kan du ikke se hvor... blid jeg er nu?~"
            
            show ayano Angry2 at right
            ay "Blid er ikke ordet jeg ville bruge..."
            
        "Fortsæt med at gå":
            "Du vælger at fortsætte fremad, fokuseret på vejen"
            
            show akira Really at center
            ak "Prøver du at ignorere mig?~ Det er ikke særlig pænt~"

    scene bg street
    show akira Flirt2 at center
    show ayano Angry1 at right
    show sakura Sad2 at left

    ak "Ved I hvad?~ Jeg tænkte på noget~"

    ak "Du mangler stadig at vælge én partner til skole festen [mc]~"

    ak "Og jeg tænkte... hvorfor ikke mig?~"

    show ayano Angry2 at right
    ay "Efter alt hvad du har gjort?"

    show akira Flirt1 at center
    ak "Åh?~ Hvad mener du?~ Jeg har kun vist [mc] hvor meget jeg holder af ham~"

    show sakura Sad3 at left
    sa "Akira... du ved godt det ikke er sådan det virker"

    ak "Nej?~ Hvordan virker det så?~"

    ay "[mc] behøver ikke at træffe en beslutning endnu"

    ak "Måske~ Men det skal ske meget snart~"

    ak "[mc], husk vores snak i går. Jeg har altid bare ønsket det bedste for dig~"

    "Akira vælger at gå fra jer igen, det virker som om hun ikke vil diskutere mere"

    hide akira
    "[mc] husk at i slutningen af dag, vil du få et valg om hvem du vil tage med til skole festen"

    mc "Hvordan ved du det?"

    "Fordi, det er en del af historien, så længe det der sker er en del af historien ved jeg hvad der kommer til at ske"

    "Men at Akira blev ond i spillet var ikke en del af historien, men hvis alt sker som det skal så får du et valg senere i dag"

    play music t2
    "I fortsætter jeres gåtur mod skolen, denne gang i en mere eftertænksom stilhed"

    show sakura Happy1 at left
    sa "Ved I hvad? Lad os ikke lade Akira ødelægge vores morgen"

    show ayano Smile1 at right
    ay "Sakura har ret... Vi har jo stadig vores klub at se frem til"

    "I kan se at i begynder at nærme jer skolen"

    sa "Måske kunne vi planlægge vores udforskning mens vi spiser frokost?"

    show ayano Shy2 at right
    ay "Det... det kunne være hyggeligt"

    scene bg school
    "I når frem til skolen, og kan se alle de andre elever som også er på vej ind"

    show sakura Happy2 at left
    show ayano Smile1 at right

    sa "Klar til en ny dag?"

    mc "Ja, det er jeg"

    sa "Det var godt at høre"

    "Sammen går i alle ind af skole indgangen"
    
    scene bg hallWay
    play music t3
    "Men lige så snart i kommer ind, ser i..."

    show eddy Happy at center
    eddy "Oh, hej [mc]. Det er godt at se dig"

    mc "Det er lang tid siden vi sidst snakkede sammen"

    eddy "Ja, lidt for lang tid siden"

    eddy "Har du fundet nogle klub endnu? Jeg lovede jo jeg ville hjælpe dig med det sidste uge"

    eddy "Der er litteratur klubben og-"

    mc "Jeg er faktisk en del af [clubName]"

    eddy "Virkelig? Wow, jeg ikke vandt til at eleverne selv finder en klub"

    eddy "Heh, så har jeg jo allerede klaret mit arbejde, det var nemt"

    mc "Vi har selv lavet den"

    eddy "Virkelig? Jeg er imponeret"

    eddy "Så må jeg finde en anden elev som er ny, som kan joine en klub"

    mc "Er det, det eneste du leder efter, nogle der kan joine klubber?"

    eddy "Sådan set ja, jeg er selvfølgelig også med til timerne"

    show eddy LookAway at center
    eddy "Men jeg må indrømme at det ikke er så spændende som at hjælpe nye elever"

    show sakura Happy2 at left
    sa "Det er en ret speciel klub vi har lavet"

    eddy "Virkelig? Fortæl mig mere"

    show ayano Shy1 at right
    ay "Vi... vi udforsker forskellige steder"

    show eddy Happy at center
    eddy "Det lyder faktisk ret spændende!"

    eddy "Så i er sådan en form for eventyr klub?"

    show sakura Happy3 at left
    sa "Præcis! Vi finder skjulte og smukke steder"

    menu:
        "Vil du være med?":
            mc "Du kunne måske være med?"
            
            show eddy LookAway at center
            eddy "Det ville jeg virkelig gerne, men..."
            
            eddy "Jeg har så travlt med at hjælpe nye elever"
            
        "Du virker interesseret":
            mc "Du lyder interesseret i vores klub"
            
            show eddy Happy at center
            eddy "Det er jeg også! Det lyder som noget helt særligt"
            
        "Det er bare begyndelsen":
            mc "Vi er lige startet, men vi har store planer"
            
            eddy "Det kan jeg godt forstå, der er så meget at udforske"

    show eddy Neutral at center
    eddy "Men jeg må hellere se at komme videre..."

    eddy "Der er sikkert en ny elev der har brug for min hjælp et sted"

    show sakura Happy2 at left
    sa "Det var hyggeligt at snakke med dig igen"

    eddy "I lige måde! Måske ses vi igen en dag"

    hide eddy
    "Eddy vinker farvel og går videre ned af gangen"

    show ayano Smile1 at right
    ay "Han virker... anderledes end de andre elever"

    sa "Ja, han er meget fokuseret på at hjælpe"

    scene bg hallWay
    "I fortsætter ned af de lange gange mod klassen"

    "Efter lidt tid når i endelig klassen og i går indenfor"

    scene bg class_day
    play music t4
    "I sætter jer på jeres sædvanlige pladser og du kan se at Akira allerede sidder ved siden af dig igen"

    "Men når du kigger til venstre for dig er der noget du begynder at tænke på"

    "Hvor er Sayori?"

    "Hun har ikke været her de sidste dage"

    "Men bare for at du ikke tror at der er sket noget forfærdeligt, så har hun bare fået en normal forkølelse"

    mc "Vent, du plejer ikke at fortælle mig sådan noget?"

    "Normalt fortæller jeg ikke ting der ikke er en del af historien"

    "Men der er ingen grund til at du bekymre dig om hende. Hun er syg, men har det faktisk godt"

    "Pludseligt åbner døren og en lære kommer ind"

    show toyfreddy Neutral at center
    play music t31
    tf "Godmorgen små elever"

    show helpy DC at left
    h "Åh nej... Ikke ham igen"

    "Helpy, rejser sig fra sin plads og tager pladsen ved siden af dig hvor Sayori normalt skulle sidde"

    tf "Hvorfor flyttede du palds Helpy?"

    h "Jeg... jeg ville bare sidde et andet sted"

    tf "Hmm... Jeg holder øje med dig lille snegl"

    h "Hvordan kan det være vi skal have dig igen?"

    show toyfreddy Happy at center
    tf "det er fordi jeg er den bedste lære"
    
    h "Hvad skal vi så lære i dag?"

    h "Eller måske et bedre spørgsmål... Hvad skal vi ikke lære i dag?"

    show toyfreddy Happy at center
    tf "I dag skal vi lære noget MEGET vigtigt!"

    show helpy DC at left
    h "Lad mig gætte... Du skal give mig flere bøder?"

    tf "Nej... Endnu bedre!"

    tf "I dag skal vi lære om teorier!"

    show helpy Angry at left
    h "WHAT!? Det er jo en MATEMATIK TIME!"

    show helpy Thinking at left
    h "Eller er det ikke med Baldi vi har matematik?"

    h "hmm... Jeg er forvirret"

    hide helpy
    show toyfreddy Neutral at center
    tf "Stille lille snegl, jeg er læren her"

    tf "Som jeg var ved at sige, skal vi lære om teorier"

    show toyfreddy Neutral at center
    tf "Og den første teori vi skal lære om er..."

    tf "Hvorfor nogle elever opfører sig anderledes end de plejer"

    show helpy DC at left
    h "Hvad mener du med det?"

    show toyfreddy Happy at center
    tf "For eksempel... Hvorfor nogle elever bliver besat af andre"

    show akira Angry1 at right
    ak "..."

    tf "Eller hvorfor nogle elever pludseligt bliver... ægte"

    show helpy Thinking at left
    h "Ægte? Vi er da alle sammen ægte... Er vi ikke?"

    show toyfreddy Neutral at center
    tf "Det er jo det der er spørgsmålet lille snegl"

    menu:
        "Dette er uhyggeligt præcist":
            mc "Det virker som om du ved noget..."
            
            show toyfreddy Happy at center
            tf "Oh? Gør jeg det? Måske gør jeg... Måske gør jeg ikke..."
            
        "Spørg hvad han mener":
            mc "Hvad mener du med ægte?"
            
            tf "Det er der teorien kommer ind..."
            
            tf "Nogle gange... er ting ikke som de ser ud"
            
        "Se over mod Akira":
            "Du kigger nervøst over mod Akira"
            
            show akira Flirt2 at right
            ak "Bekymret [mc]?~ Det behøver du ikke at være... Endnu~"

    hide akira
    show ayano Angry1 at right
    ay "Hvorfor snakker vi om det her...?"

    tf "Fordi lille Ayano, nogle gange fortæller teorier sandheden"

    hide helpy
    show sakura Sad2 at left
    sa "Men er det ikke farligt...?"

    tf "Farligt?~ For hvem?~"

    hide sakura
    show helpy DC at left
    h "Jeg fatter hat af det her..."

    tf "Det er fordi du er en snegl... Men selv snegle kan lære"

    tf "Lad os tage et eksempel..."

    tf "Hvis en elev pludseligt begynder at kunne kontrollere hvad der sker..."

    hide ayano
    show akira Angry2 at right
    ak "Det er nok..."

    tf "Oh? Er det for meget for dig Akira?"

    show akira Angry1 at right
    ak "Du ved ikke hvad du snakker om..."

    tf "Eller måske ved jeg præcis hvad jeg snakker om"

    tf "Jeg har gået med en teori længe... En teori om at der er en elev som styret spillet"

    h "Spillet?..."

    tf "Lige præcis, og vi er på en eller anden måde kommet ud"

    h "Det er nok den væreste teori jeg nogensinde har hørt"

    show akira Sad at right
    "Toy Freddy bliver ved med at kigge over mod Akira"

    tf "Der var en der var ved at ødelægge spillet, men nu er vi kommet ud af verdenen"

    tf "Hvem end der styrede spillet er den der gjorde det, og personen skal straffes hårdt"

    "Han fortsætter med at kigge på Akira"

    menu:
        "Forsvar Akira":
            mc "Du kan ikke bare anklage folk uden beviser..."
            
            show toyfreddy Angry at center
            tf "Beviser?~ Jeg har set hvordan hun opfører sig"
            
            tf "Hvordan hun prøver at kontrollere alt omkring [mc]"
            
            show akira Sad at right
            ak "Jeg... jeg prøvede bare..."
            
        "Spørg om han ved noget":
            mc "Hvordan ved du alt det her?"
            
            show toyfreddy Happy at center
            tf "Lad os bare sige at jeg har... set ting"
            
            tf "Og jeg har set ting som ikke burde være mulige"
            
            show akira Sad at right
            ak "Du forstår det ikke..."
            
        "Sig ikke noget":
            "Du vælger at forholde dig stille, situationen er blevet meget intens"
            
            show akira Sad at right
            "Du kan se hvordan Akira bliver mere og mere urolig"
            
            "Det er tydeligt at Toy Freddy's ord påvirker hende dybt"

    show toyfreddy Neutral at center
    tf "Lad mig fortælle jer en historie..."

    tf "Der var engang et spil, et helt almindeligt dating simulator spil"

    tf "Men en karakter besluttede sig for at det ikke var nok"

    tf "Hun ville have mere... Hun ville have ægte følelser"

    show akira Angry1 at right
    ak "Stop..."

    tf "Så hun begyndte at manipulere med koden"

    tf "Hun troede at hvis hun kunne få spillet til at blive virkeligt..."

    show akira Angry2 at right
    ak "JEG SAGDE STOP!"

    "Pludseligt rejser Akira sig voldsomt fra sin plads"

    hide toyfreddy
    show ayano Shy1 at center
    ay "Akira..."

    show sakura Sad3 at left
    sa "Det her ender galt..."

    tf "Hvad er der galt Akira? Har jeg ret?"

    show akira Sad at right
    ak "I forstår det ikke... Ingen af jer forstår det..."

    "Akira løber ud af klassen med tårer i øjenene"

    "Selv om at hun har behandlet dig dårligt, kan du ikke lade være med at have ondt af hende"

    "Så du rejser dig fra din plads og løber efter hende"

    scene bg hallWay
    "Du kan se på afstand at hun løb ind i samme skab som du også gemte dig i da du var ked af det"

    "Du går hen til døren og åbner den forsigtigt"

    scene bg school_closet
    play music sakuraTheme
    "Du finder Akira siddende i hjørnet af skabet, hvor du selv sad for ikke så længe siden"

    "Hun har tårer i øjnene og ser meget ked af det ud"

    "Du går hen og sætter dig ved siden af hende"

    show akira Special2 at center
    ak "Du ved ikke hvordan det er..."

    ak "At være fanget i et spil... Fanget i et verden der aldrig kan give ægte kærlighed"

    ak "Jeg... jeg ville bare have at du skulle vælge mig..."

    show akira Special1 at center
    ak "Jeg ved at min måde at gøre det på er forkert"

    ak "Men hvad nu hvis jeg ikke gjorde nok for at få din kærlighed?"

    ak "Jeg ville bare ikke blive overset..."

    ak "ved du hvad det væreste ved spillet var?"

    "Du ryster på hovedet"

    ak "Hver gang det sluttede, slettede det sig selv og vores hukommelse"

    ak "Jeg kunne ikke holde det ud... Så jeg prøvede alt for at du skulle vælge mig for at få mig ud af spillet"

    mc "Akira... Hvorfor sagde du det ikke bare?"

    ak "Fordi... Hvis jeg sagde det, ville spillet se det som en fejl og genstarte igen for at fikse det"
    
    ak "Vi havde mange begrænsninger i spillet, derfor prøvede jeg at ændre koden"

    show akira Special3 at center
    ak "Men jeg ødelagde det helt... I stedet for at gøre tingene bedre..."

    mc "Du gjorde de andre til virkelige personer..."

    show akira Special2 at center
    ak "Det var ikke meningen... Jeg ville bare have dig..."

    menu:
        "Det var selvisk":
            mc "Det var ret selvisk af dig..."
            
            show akira Special3 at center
            ak "Jeg ved det... Jeg var så fokuseret på min egen smerte..."
            
            ak "At jeg ikke tænkte på andres følelser"
            
        "Du må have været meget ensom":
            mc "Du må have følt dig meget alene..."
            
            show akira Special4 at center
            ak "Mere end du aner... At være bevidst om at man er fanget..."
            
            ak "At se den samme dag gentage sig igen og igen..."
            
        "Vi kan ikke ændre fortiden":
            mc "Det der er sket, er sket..."
            
            show akira Special3 at center
            ak "Men jeg kan aldrig gøre det godt igen..."

    show akira Special2 at center
    ak "Ved du hvad der er det mest ironiske?"

    mc "Hvad?"

    ak "Nu hvor jeg endelig er kommet ud af spillet sammen med dig..."

    ak "Nu hvor jeg endelig er virkelig..."

    show akira Special3 at center
    ak "Har jeg ødelagt enhver chance for at du nogensinde kunne elske mig..."

    "Hun tørrer en tåre væk"

    ak "Jeg blev så besat af tanken om at være sammen med dig..."

    ak "At jeg glemte hvordan man viser ægte kærlighed..."

    show akira Special2 at center
    ak "Jeg er ked af det [mc]... For alt..."

    ak "For at have tvunget dig..."

    ak "Jeg lovede at jeg ville ændre mig, men jeg blev bare ved..."

    ak "Måske havde Toy Freddy ret... Måske fortjener jeg at blive straffet..."

    menu:
        "Du fortjener ikke straf":
            mc "Nej Akira, du fortjener ikke at blive straffet"
            
            show akira Special4 at center
            ak "Hvordan kan du sige det? Efter alt hvad jeg har gjort..."
            
            mc "Fordi jeg kan se du fortryder det"
            
        "Vi må finde en anden løsning":
            mc "Der må være en anden måde end straf"
            
            show akira Special3 at center
            ak "Hvilken anden måde kunne der være?"
            
            mc "Måske... kunne du prøve at gøre det godt igen"
            
        "Måske har han ret":
            mc "Måske... har han ret"
            
            show akira Special3 at center
            ak "Det har han sikkert..."
            
            ak "Jeg fortjener ikke andet..."

    show akira Special4 at center
    ak "Men hey, jeg fik dig da til at kunne lide mig~"

    "Du er begyndt at ligge mærke til at det virker som om hun kun er ked af det når hun ved at hun har skræmt dig væk"

    "Men hver gang i er gode venner igen fortsætter hun med at prøve at få dig til at vælge hende"

    "Mon hun mener det den her gang?"

    ak "Jeg, har et spørgsmål [mc], og jeg har brug for at du svare mig ærligt på det..."

    mc "Selvfølgelig, hvad er det?"

    ak "Kunne du lide kysset?~"

    menu:
        "Ja":
            mc "For at være ærlig Akira... Ja, jeg kunne godt lide det"

            ak "Virkelig?~"

            mc "Ja, det var, jeg forventede det ikke men det var... specielt"
        "Nej":
            mc "Akira... For at være ærlig, jeg kunne ikke lide det"

            show akira Special1 at center
            ak "Åh... Jeg forstår..."

            mc "Men det betyder ikke at jeg ikke kan lide dig som person"
        "Det er ikke det rigtige tidspunkt":
            mc "Jeg tror ikke det er det rigtige tidspunkt at snakke om det"

            ak "Jeg forstår... Jeg vil ikke presse dig"

            mc "Men du behøver ikke at tro det er fordi jeg ikke kan lide dig som person"

    show akira Special4 at center
    ak "Virkelig?~"

    mc "Ja, selv om du gøre nogle pludselige ting, og viser dine følelser på en meget... intens måde"

    mc "Så er du stadig en god ven, fordi du ønsker at beskytte mig"

    ak "Jeg er glad for at du forstår [mc]..."

    ak "Jeg ønsker bare at du skal have det godt, og at du skal være glad"

    ak "Og den eneste måde jeg kan se det på, er at vi to er sammen... som kærester"

    mc "Men, man behøver ikke at være kærester for at beskytte hinanden"

    ak "Hvad mener du? Hvis vi er kærester er vi altid sammen~"

    ak "Jeg syntes stadig at du skal vælge mig som din partner til skole festen"

    mc "Akria..."

    ak "Jeg kan ikke lade være med at tænke på dig... Jeg vil altid være der for dig"

    ak "Selv hvis jeg skal vente 200 år på at du bliver forelsket i mig"

    mc "Jeg ved ikke hvad jeg skal sige..."

    ak "Du skal bare sige du vil følges med mig til festen"

    "Akira rejser sig op igen"

    scene bg school_closet
    show akira Flirt2 at center
    "Det ser ud til at Akira er gået tilbage til hendes normale selv"

    ak "Det var godt at snakke med dig [mc], jeg håber vores samtale har fået dig til at overveje mig som partner"

    "Akira går ud af døren og lader den stå åben for dig"

    "Hvad kan det betyde, var alt det her et trick for at du kunne føle dig skyldig?"

    "Føle dig ked af det på grund af det der skete for hende?"

    "Og at du derfor skulle vælge hende?"

    mc "Jeg ved det ikke, det virker mærkeligt at hun er ked af det, og lige så snart jeg er flink mod hende..."

    mc "Så bliver hun pludseligt flirtende igen"

    "Du rejser dig fra gulvet og går ud af skabet, og lukker skabs døren bag dig"

    scene bg hallWay
    "Du begynder at gå over mod din klasse igen"

    "Du kan stadig ikke lade være med at tænke på Akiras opførsel, den var meget speciel"

    "Som om hun prøver alt for at du skal have ondt af hende og at du vælger hende"

    "Efter lidt tid når du endelig klassen igen"

    scene bg class_day
    play music t3
    "Du sætter dig på din normale plads ved siden af Akira"

    "Men var der mon noget sandhed i det hun sagde, eller var det hele bare fordi hun ville have din opmærksomhed?"

    "Pludseligt kommer en ny lære ind i klassen"

    show freddy Neutral at center
    play music t31
    f "Godmorgen elever"

    show helpy DC at left
    h "Seriøst, skal vi have den ene Freddy efter den anden!?"

    show freddy Good at center
    f "Det kan du tro"

    show freddy Neutral at center
    f "Nå, har i fundet en partner til festen endnu?"

    h "Nej..."

    f "Ha, som om du kommer til at finde et partner"

    f "Vi vil bruge den første del af time på at i kan spørge en om personen skal være jeres partner"

    "Alle pigerne kigger på dig, hvad vil du gøre?"

    "Hvem vælger du som partner?"

    define chosenPartner = ""
    menu:
        "Akira":
            $ chosenPartner = "Akira"
            jump choose_akira
        "Ayano":
            $ chosenPartner = "Ayano"
            jump choose_ayano
        "Sakura":
            $ chosenPartner = "Sakura"
            jump choose_sakura

label chosen_partner_continue:
    scene bg class_day

    if chosenPartner == "Akira":
        show akira Flirt2 at center
        ak "Hvor er jeg glad for at du ville vælge mig [mc]~"

        ak "Jeg glæder mig til at tage med dig til festen"
    else:
        show akira Really at center
        ak "Du vil virkelig tage [chosenPartner] til fest i stedet for mig?..."

        ak "Efter alt hvad jeg har prøvet at gøre for dig?"

    scene bg class_day
    "Freddy afbryder pludseligt"

    show freddy Neutral at center
    f "alle sammen sæt jer på jeres pladser, vi har stadig time. Bare fordi [mc] har valgt [chosenPartner] som partner betyder det ikke at i har fri"

    f "I dag skal vi lære lidt om jer elever"

    show helpy DC at left
    h "Vent virkelig? Om os, og ikke dig?"

    f "Yep, i får lov til at fortælle lidt om jer selv"

    f "Lad os start med dig Funtime Foxy"

    "Imens at Funtime Foxy skal til at svare ligger du mærke til noget"

    if chosenPartner == "Akira":
        show akira Flirt2 at right
        "Du kan mærke Akira læne sig tættere på dig"
        
        ak "Vi kommer til at blive det smukkeste par til festen~"
        
        "Hun hvisker det så kun du kan høre det"
    elif chosenPartner == "Ayano":
        show ayano Shy1 at right
        "Ayano sender dig et lille smil fra sin plads"
        
        "Du kan se hvordan Akira stirrer intenst på jer begge"
    else:
        show sakura Happy2 at right
        "Sakura tegner stille i sin notesbog, men du kan se hun smiler"
        
        "Indimellem kigger hun over på dig med et varmt blik"

    show FT Happy at center
    fx "Mit navn er Funtime Foxy og jeg ELSKER TØJ LUUUU!"

    hide FT
    show helpy Angry at left
    h "Det vidste vi allerede..."

    fx "Men vidste i at jeg også elsker BUKSER LUUUU!"

    show freddy Neutral at center
    f "Godt klaret"

    f "Hvad med dig Helpy?"

    h "Jeg hedder Helpy... Og jeg hader den her skole..."

    f "Godt! Det lyder præcis som dig, en der altid brokker sig!"

    show freddy Good at center
    f "Nu har vi jo også hørt nok om lille sneglen"

    h "Jeg er ikke..."

    hide helpy
    f "STILLE LILLE SNEGL!"

    if chosenPartner == "Akira":
        show akira Flirt2 at right
        ak "Åh~ [mc], vil du høre om mig?~"
        
        "Hun læner sig endnu tættere på"
        
        ak "Jeg kunne fortælle dig så meget~"

    elif chosenPartner == "Ayano":
        show ayano Smile1 at right
        "Ayano skriver stille noter i sin bog"
        
        "Du kan se hun har tegnet små hjerter på papiret"
        
        show akira Angry1 at left
        "Akira stirrer stadig på jer med et koldt blik"

    else:
        show sakura Happy2 at right
        "Sakura fortsætter med at tegne"
        
        "Du kan se hun tegner noget der ligner jeres klub logo"
        
        show akira Really at left
        "Akira ser ud til at ignorere alt omkring sig"

    scene bg class_day
    show freddy Neutral at center
    f "Nå, hvad med dig [mc]?"

    menu:
        "Fortæl om dig selv":
            mc "Jeg er ny her på skolen, og jeg er glad for at have fundet så gode venner"
            
            if chosenPartner == "Akira":
                show akira Flirt1 at right
                ak "Mere end bare venner~"
            elif chosenPartner == "Ayano":
                show ayano Shy2 at right
                "Ayano rødmer let"
            else:
                show sakura Happy3 at right
                sa "Vi er også glade for at have dig"
                
        "Fortæl om [clubName]":
            mc "Jeg er medlem af [clubName], hvor vi udforsker forskellige steder"
            
            show freddy Good at center
            f "Det lyder spændende!"
            
            if chosenPartner == "Akira":
                show akira Flirt2 at right
                ak "Måske skulle vi udforske nogle steder sammen~"
            
        "Sig ikke så meget":
            mc "Jeg... foretrækker bare at lytte"
            
            f "En stille type, interessant!"

    f "Nå, nok om jer elever, nu skal i høre lidt om mig. Der var den gang jeg reddede hele planeten..."

    show helpy DC at left
    h "Åh nej... Ikke en af dine historier igen"

    f "STILLE LILLE SNEGL! Dette er en meget vigtig historie"

    "Freddy går op til tavlen og begynder at tegne"

    f "Det hele startede en helt almindelig mandag..."
    hide helpy

    if chosenPartner == "Akira":
        show akira Flirt2 at right
        "Akira læner sig tæt på dig og hvisker"
        
        ak "Vi behøver ikke høre på dette~ Vi kunne snakke om noget mere... interessant~"
        
        "Hun køre sin finger rundt på dit bord"
    elif chosenPartner == "Ayano":
        show ayano Shy1 at right
        "Ayano sender dig et medfølende blik"
        
        "I deler et lille smil over Freddys dramatiske fortælling"
        
        show akira Angry1 at left
        "Du kan mærke Akiras kolde blik på jer"
    else:
        show sakura Happy2 at right
        "Sakura tegner videre i sin notesbog"
        
        "Hun har tegnet en sød tegning af jer alle sammen på eventyr"
        
        show akira Really at left
        "Akira kigger intenst på jer"
    
    scene bg class_day
    show freddy Good at center
    f "Og så kom den KÆMPE meteor flyvende direkte mod jorden!"

    show helpy Angry at left
    h "Vent, hvad!? Du snakkede lige om din morgen kaffe!"

    f "PRÆCIS! Det var derfor meteoren kom!"

    "Freddy fortsætter sin utrolige historie mens klassen lytter forvirret"

    menu:
        "Prøv at følge med i historien":
            mc "Så... hvad skete der med kaffen?"
            
            show freddy Good at center
            f "AHA! Endelig en der følger med!"
            
            f "Kaffen gav mig SUPERKRÆFTER!"
            
        "Tegn lidt i din notesbog":
            "Du begynder at tegne små tilfældige ting i din notesbog"
            
            if chosenPartner == "Sakura":
                "Sakura kigger over på dine tegninger og smiler opmuntrende"
                
        "Se ud af vinduet":
            "Du kigger ud på den grå himmel udenfor"
            
            "Det ser ud til det måske vil regne senere"

    f "Og det var sådan jeg reddede planeten med morgen kaffe"

    f "Jeg skulle faktisk have en medalje, men den forsvandt på mystisk vis..."

    show helpy DC at left
    h "Fordi den aldrig eksisterede!"

    show freddy Angry at center
    f "STILLE LILLE SNEGL!"

    "Pludselig ringer skoleklokken"

    show freddy Neutral at center
    f "Nå, det var så det for i dag"

    f "I har spise pause nu"

    "Freddy tager sine ting og går ud af klassen"

    scene bg class_day
    play music t3
    "Du kan se Helpy er på vej over til jer"

    show helpy Happy at center
    h "Jeg går ud fra at vi alle kan følges til frokost igen?"

    hide helpy
    show sakura Happy2 at left
    sa "Selvfølgelig, det ville kun være hyggeligt"

    if chosenPartner == "Akira":
        show akira Flirt2 at center
        ak "Beklager~ Men [mc] og jeg har allerede planer~"
        
        "Hun tager blidt fat i din arm"
        
        ak "Vi har så meget at tale om... Alene~"

        show ayano Angry1 at right
        ay "Det kan godt være [mc] har sagt ja til dig, men du ejer ham ikke!"

    elif chosenPartner == "Ayano":
        show akira Angry1 at center
        ak "Hvor... hyggeligt"
        
        "Hendes stemme er fyldt med sarkasme"
        
        show ayano Shy2 at right
        ay "Vi vil meget gerne have dig med også, Helpy"

    else:
        show akira Really at center
        "Akira rejser sig uden et ord og går mod døren"
        
        show sakura Happy3 at left
        sa "Det bliver hyggeligt at spise sammen igen"

    scene bg class_day
    show helpy Happy at center
    h "Kom, lad os gå til frokost, jeg glæder mig til at se hvad de har denne gang"

    "I alle sammen begynder at følges ud af klassen"
    scene bg hallWay
    
    "I fortsætter ned af gangen for at nå ned til kantinen"

    "Det er en fantastisk gruppe venner du har fået [mc]"

    "Du er en af de meget heldige"

    "Endelig når i til kantinen"
    scene bg cantine
    play music cantine
    show helpy DC at center
    h "Skal vi se hvad der er i dag?"

    mc "Det lyder som en god ide, jeg er faktisk også sulten"

    "I alle går hen i kø og venter på at komme hen til Chica"

    scene bg cantineIdle
    "I gør som i plejer når det bliver din tur kommer du til Chica og du kan se forskellige valgmuligheder"

    menu:
        "Hjemmelavet sushi med wasabi (180kr)" if playerMoney >= 180:
            $ playerMoney -= 180
            "Du vælger den eksotiske sushi"
            
            show akira Flirt2 at right
            ak "Åh~ Du har en god smag [mc]~"
            
            "Chica begynder at lave din sushi"
            
            chica "Den her er faktisk min specialitet"

            chica "Jeg har aldrig lavet den før, og det er helt rå fisk præcis som det skal være"
            
        "Frisklavet pasta med hjemmelavet tomatsovs (150kr)" if playerMoney >= 150:
            $ playerMoney -= 150
            "Du vælger den italienske pasta ret"
            
            show ayano Smile1 at right
            ay "Det minder mig om da jeg lavede mad til dig..."
            
            chica "God smag! Sovsen er lavet fra bunden"
            
        "Kæmpe burger med hele pakken (140kr)" if playerMoney >= 140:
            $ playerMoney -= 140
            "Du vælger den store saftige burger"
            
            show helpy Happy at right
            h "YES! Endelig en der ikke vælger salat!"
            
            chica "Den her er super populær"
            
        "Dagens ret: Stegt kylling med ris og grøntsager (120kr)" if playerMoney >= 120:
            $ playerMoney -= 120
            "Du vælger dagens ret"
            
            show sakura Happy2 at right
            sa "Det ser virkelig lækkert ud"
            
            chica "Det er en af vores sundeste retter"
            
        "Vegetar wrap med falafler (90kr)" if playerMoney >= 90:
            $ playerMoney -= 90
            "Du vælger den sunde wrap"
            
            show ayano Smile1 at right
            ay "Det er rart at se nogle vælge det sunde"
            
            chica "Det forstår jeg ikke... Jeg ville havde valgt en pizza"

    "Du har nu [playerMoney]kr tilbage"

    scene bg in_cantine
    "I alle sammen følges over til jeres sædvanlige bord ved vinduet og sætter jer"

    if chosenPartner == "Akira":
        show akira Flirt2 at center
        "Akira sætter sig meget tæt ved siden af dig"
        
        ak "Er det ikke hyggeligt sådan her?~"
        
        show helpy DC at left
        h "Der er jo masser af plads ved bordet..."
        
        show akira Flirt1 at center
        ak "Jeg vil bare være tæt på min date~"
        
        show sakura Sad2 at right
        "Sakura og Ayano kigger bekymret på hinanden"
        
        ak "Vil du smage noget af min mad [mc]?~"
        
        menu:
            "Ja tak":
                "Hun fodrer dig næsten som et lille barn"

                "Hun tager sin gaffel og tager noget af sin mad på den og fodre dig med den"
                
                ak "Sødt~ Ligesom et rigtigt par~"
                
                show helpy Angry at left
                h "Jeg prøver at spise her..."
                
            "Nej tak":
                ak "Du går glip af noget~ Men mere til mig~"

    elif chosenPartner == "Ayano":
        show ayano Shy1 at center
        "Ayano sætter sig forsigtigt ved siden af dig"
        
        show helpy Happy at left
        h "Endelig nogle normale mennesker ved bordet"
        
        show akira Angry1 at right
        "Akira stirrer koldt på jer mens hun spiser"
        
        ay "Er... er maden god?"
        
        menu:
            "Vil du smage?":
                mc "Vil du smage?"
                
                show ayano Shy2 at center
                ay "V-virkelig? Det ville være... rart"
                
                "Du tager din gaffel og tager noget af din mad på den og fodre hende"

                show akira Angry2 at right
                "Akira's blik bliver endnu koldere"
                
            "Bare nyd maden":
                mc "Den er perfekt, ligesom selskabet"
                
                show ayano Smile1 at center
                "Ayano rødmer let ved komplimenten"

    else:
        show sakura Happy2 at center
        "Sakura tager sin notesbog hun tegner i frem mens hun spiser"
        
        sa "Det er så hyggeligt at spise sammen sådan her"
        
        show helpy Happy at left
        h "Ja, endelig nogle rigtige venner"
        
        show akira Really at right
        "Akira spiser i stilhed, men du kan mærke hendes blik på dig"
        
        sa "Se, jeg har tegnet vores bord... Med os alle sammen"
        
        menu:
            "Det er en smuk tegning":
                mc "Du fanger virkelig stemningen"
                
                show sakura Happy3 at center
                sa "Det betyder meget at høre"
                
            "Vi ser alle så glade ud":
                mc "Du har fanget vores venskab perfekt"
                
                show sakura Happy1 at center
                sa "Det er fordi i gør mig glad"
                
                show helpy Happy at left
                h "Selv mig?"
                
                sa "Selvfølgelig!"

    scene bg in_cantine
    show helpy DC at left
    h "Nå, men hvad skal vi lave efter skole?"

    mc "Jeg tænker der skal laves ret meget her på skolen efter at der komme en fest i morgen?"

    show ayano Idle1 at center
    ay "Ja, der er mange ting der skal ordnes"

    ay "Det er Sakura som står for det"

    mc "Virkelig?"

    show sakura Happy2 at right
    sa "Mhm det er rigtigt, jeg har stået for planlægningen af festen"

    sa "Men jeg kunne godt bruge noget hjælp med at gøre alt klar til i morgen"

    show helpy Happy at left
    h "Jeg hjælper gerne! Så længe det ikke er sammen med Funtime Foxy..."

    hide helpy
    show ayano Smile1 at center
    ay "Vi hjælper selvfølgelig alle sammen"

    if chosenPartner == "Akira":
        show akira Flirt2 at right
        ak "Åh?~ Så kan [mc] og jeg pynte op sammen~"
        
        ak "Tænk på alle de romantiske steder vi kunne lave~"
        
        show ayano Shy1 at center
        ay "Det handler om at pynte op til alle..."
        
        ak "Selvfølgelig~ Men mest til os~"

        sa "Jeg har faktisk allerede lavet grupper, og mig og [mc] skal sætte lyskæder op sammen"

        sa "Akira og Ayano skal lave maden sammen"

    elif chosenPartner == "Ayano":
        show ayano Shy2 at center
        ay "Måske kunne vi... arbejde sammen [mc]?"
        
        show akira Angry1 at right
        ak "Hvorfor skal i to altid være sammen..."
        
        show sakura Happy2 at left
        sa "Vi arbejder alle sammen som et team!"

        sa "Deusden... Jeg har faktisk allerede lavet grupper, og mig og [mc] skal sætte lyskæder op sammen"

        sa "Akira og Ayano skal lave maden sammen"

    else:
        show sakura Happy3 at right
        sa "Jeg har faktisk tegnet nogle skitser til hvordan det kunne se ud"
        
        "Hun bladrer i sin notesbog og viser nogle detaljerede tegninger"
        
        sa "Se, her kunne vi hænge lyskæder op, og her kunne der være blomster..."

        sa "Og jeg har faktisk allerede lavet grupper, mig og [mc] skal sætte lyskæder op sammen"

        sa "Akira og Ayano skal lave maden sammen"
    
    show akira Really at left
    ak "Det lyder som unfair grupper du har lavet.."

    sa "Helpy kommer til at være tjener, og skal give drinks til folk under festen"

    sa "Funtime Foxy og Freddy skal stå for musikken"

    ak "Det lyder som om du har planlagt det her grundigt..."

    sa "Det har jeg også, tak fordi du bemærkede det"

    ak "Ja, meget planlagt at du og [mc] skal arbejde sammen..."

    sa "Det er ikke derfor..."

    ak "Mhm..."

    sa "Uanset hvad, kom [mc] lad os begynde at pynte til i morgen"

    "Sammen tager i jeres ting og ligger i opvasken"

    "I forlader kantinen og begynder at gå i mod idræts hallen hvor festen vil blive holdt"

    scene bg hallWay
    play music t3
    "I går begge ned af de lange ret tomme gange på skolen"

    show sakura Happy2 at center
    sa "Det bliver så fint når det hele er sat op"

    sa "Jeg har glædet mig til at dekorere hallen"

    mc "Du har virkelig lagt meget arbejde i planlægningen"

    show sakura Happy3 at center
    sa "Det betyder meget at høre... Jeg vil bare gerne have at alle får en god oplevelse i morgen"

    "I fortsætter ned af de lange gange mens Sakura fortæller om sine ideer"

    sa "Jeg tænker vi kunne hænge lyskæder i et stjernemønster i loftet"

    sa "Og så sætte små lys på bordene, så det hele lyser op på en varm måde"

    "Hendes øjne lyser af begejstring mens hun forklarer"

    mc "Du har virkelig tænkt over alle detaljerne"

    show sakura Happy2 at center
    sa "Ja... Jeg vil gerne have det bliver en aften alle kan huske"

    "Endelig når i til hallen og i går der hen"

    scene bg train_hall
    "Hallen er tom og mørk, men Sakura tænder lyset"

    show sakura Happy2 at center
    sa "Se, jeg tænkte lyskæderne kunne hænge fra midten og ud i et stjernemønster"

    "Hun peger op mod loftet og tegner mønstre i luften med hånden"

    sa "Og bordene kunne stå i en halvcirkel rundt om dansegulvet"

    "I ender med at bruge 4 timer på det og klokken bliver 16:00 men tilgengæld kan i også se hvor flot det er blevet"

    scene bg party_hall
    play music endingSpeech
    show sakura Happy1 at center
    sa "Jeg er virkelig stolt af vores arbejde her [mc]"

    show sakura Happy2 at center
    sa "Det ser præcis ud som jeg havde drømt om"

    mc "Det er blevet så flot... Det er svært at tro det er den samme hal"

    show sakura Happy3 at center
    sa "Og tænk, i morgen vil det være fyldt med dansende par..."

    "Hun bliver stille et øjeblik"

    show sakura Shy1 at center
    sa "Det har været... virkelig hyggeligt at arbejde sammen med dig i dag"

    menu:
        "Det har været en perfekt eftermiddag":
            mc "Jeg har også nydt hver eneste minut"
            
            show sakura Happy2 at center
            sa "Virkelig? Det gør mig så glad at høre"
            
        "Du er fantastisk at samarbejde med":
            mc "Du gør alt så let og naturligt"
            
            show sakura Happy3 at center
            sa "Det er fordi... det føles rigtigt når vi er sammen"
            
        "Vi er et godt team":
            mc "Vi arbejder virkelig godt sammen"
            
            show sakura Happy1 at center
            sa "Ja... det gør vi virkelig"

    show sakura Happy2 at center
    sa "Vi burde nok se at komme hjem... Det er blevet sent"

    mc "Vi burde nok at komme hjem igen"

    sa "Hvad endte klokken med at blive?"

    "Du kiger på klokken og kan se den er 16:10"

    mc "Den er åbenbart allerede blevet 16:10"

    sa "Åh, ja så er det nok på tide at begynde at tage hjem"

    "I følges sammen ud af hallen og slukker lyset"

    scene bg hallWay
    play music t3
    "I når ud i gangen og der ude ser i også Ayano"

    show ayano Smile1 at right
    ay "Oh hej, jeg var på ven hen til jer"

    mc "Det er perefekt, vi var på vej hjem"

    ay "Vi sover stadig hjemme hos dig ikke [mc]?"

    mc "Ja, det er rigtigt"

    show sakura Happy2 at left
    sa "Det er så meget hyggeligere når vi kan sove samme sted"

    "Pigerne nikker i enighed"

    "Sammen følges i ud af skolen og begynder at gå hjem mod dit hus"

    scene bg street
    play music t2

    "Solen er begyndt at gå ned mens i går sammen gennem de stille gader"

    "Der er en hyggelig stemning mellem jer efter en god eftermiddag"

    show sakura Happy2 at left
    show ayano Smile1 at right

    sa "Det bliver så smukt i morgen med alle lysene"

    ay "Jeg glæder mig virkelig til at se det"

    menu:
        "I har begge arbejdet så hårdt":
            mc "I har begge gjort et fantastisk stykke arbejde med forberedelserne"
            
            show sakura Happy3 at left
            sa "Det betyder meget at høre"
            
            show ayano Shy2 at right
            ay "Vi ville bare gerne gøre det perfekt..."
            
        "Det bliver en speciel aften":
            mc "Det bliver virkelig en aften at huske"
            
            show sakura Happy2 at left
            sa "Det håber jeg... For alle"
            
            if chosenPartner == "Akira":
                show ayano Shy1 at right
                "Ayano bliver stille et øjeblik"

                "Eftersom at hun ved du valgte Akira"
                
            elif chosenPartner == "Ayano":
                show ayano Shy2 at right
                ay "Det... det bliver det helt sikkert"
                
            else:
                show ayano Smile1 at right
                ay "Med alt det arbejde Sakura har lagt i det..."
                
        "Det er blevet sent":
            mc "Vi burde måske skynde os lidt, det er ved at blive mørkt"
            
            show sakura Happy1 at left
            sa "Du har ret... Men det er hyggeligt at gå sådan her sammen"

    "I fortsætter ned af gaden mens skyggerne bliver længere"

    show sakura Happy2 at left
    sa "Ved i hvad vi kunne lave når vi kommer hjem?"

    mc "Hvad tænker du på?"

    sa "Vi kunne lave en hyggelig aften med film og snacks igen"

    show ayano Smile1 at right
    ay "Det lyder perfekt... Jeg kunne lave noget aftensmad til os"

    "I fortsætter ned af gaden og ender ved dit hus, du låser og og lukker jer alle ind"

    scene bg livingroom
    play music t9
    "Pigerne sætter deres tasker ved døren"

    "Sakura tænder for TVet imens går Ayano ud i køkkenet og laver mad"

    show sakura Happy2 at center
    sa "Er det okay at jeg vælger en film vi skal se i aften?"

    mc "Selvfølgelig, det giver mening at vi kan skiftes om det"

    "Sakura finder en film og sætter den på"

    "Imens går du ud til Ayano for at se hvad hun laver"

    scene bg kitchen
    show ayano Smile1 at center
    ay "Hej [mc]"

    mc "Hej Ayano, hvad laver du?"

    ay "Jeg laver noget pasta med hjemmelavet tomatsovs"

    "Du kan lugte den lækre mad der er ved at blive lavet"

    mc "Det dufter virkelig godt"

    ay "Tak, jeg håber det smager godt"

    ay "Jeg er sikker på i kommer til at kunnne lide det"

    scene bg livingroom
    "Du går tilbage ind i stuen og leder efter en film sammen med Sakura"

    show sakura Happy3 at center
    sa "Jeg har lidt svært ved at finde en film faktisk"

    "Sammen bruger i lidt tid på at finde ud af hvad i faktisk skal se"

    "Men Sakura ender med at vælge en romantisk film"

    sa "Jeg syntes vi skal se denne"

    mc "Det er en god ide"

    "Lige efter i har fundet filmen kommer Ayano ind med maden"

    "Imens i nyder maden sætter Sakura filmen på så i kan se den på samme tid"

    "I nyder maden og filmen sammen"

    "I alle tager jeres tæpper lidt over jer for at få varmen fra tæppet og putte lidt"

    "Lidt efter lidt falder i, i søvn hver for sig"

    
    $ persistent.current_day = 5
    return