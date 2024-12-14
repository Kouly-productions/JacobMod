label ch3_main:
    $ currentDay = "Onsdag"
    scene bg livingroom
    play music t8
    
    "ONSDAG"

    "Du vågner langsomt op til en ny dag"

    "Det kan langsomt mærke imens du vågner minderne fra i går vende tilbage..."

    "Du ligger på sofaen hvor du faldt i søvn i går"

    "Men når du kigger på side af dig, ser det ikke ud til at pigerne er der mere"

    "Du kan høre noget ude fra køkkenet"

    "Du rejser dig op fra sofaen og går ud i mod køkkenet"

    scene bg kitchen
    show sakura Happy2 at left
    sa "God morgen [mc]"

    show ayano Shy1 at right
    ay "Vi er i gang med at lave morgenmad"

    menu:
        "Tak fordi I blev":
            mc "Jeg er virkelig glad for at I blev her i nat..."
            
            show sakura Happy1 at left
            sa "Selvfølgelig gjorde vi det"
            
            ay "Vi ville ikke lade dig være alene efter det der skete"
            
        "I skulle ikke have...":
            mc "I skulle virkelig ikke have..."
            
            show sakura Sad2 at left
            sa "Jo, vi skulle. Du er vores ven"
            
            ay "Vi passer på hinanden"
            
        "Jeg er stadig rystet":
            mc "Jeg er stadig... ret rystet over det hele"
            
            show ayano Shy2 at right
            ay "Det forstår vi godt"
            
            sa "Tag den tid du har brug for"

    show sakura Happy2 at left
    sa "Vi har lavet pandekager... Vi tænkte du kunne bruge noget ordentlig morgenmad"

    ay "Og vi skal nok følges med dig i skole"

    "Du kan mærke en ubehagelig følelse ved tanken om at vide at du skal i skole"

    menu:
        "Jeg er bange for at møde Akira":
            mc "Jeg... jeg er virkelig nervøs for at se Akira igen"
            
            ay "Det kommer ikke til at ske. Vi holder hende væk fra dig"
            
            sa "Du er ikke alene denne gang"
            
        "Måske skulle jeg blive hjemme":
            mc "Jeg ved ikke om jeg kan klare at tage i skole..."
            
            show sakura Sad2 at left
            sa "Det forstår vi godt, men..."
            
            ay "Hvis du bliver hjemme, vinder hun"
            
        "Jeg er glad for I er her":
            mc "Jeg ved ikke hvad jeg skulle gøre uden jer..."
            
            show sakura Happy1 at left
            sa "Vi er her for dig [mc]"
            
            show ayano Smile1 at right
            ay "Du skal ikke gennem det her alene"

    scene bg kitchen
    show sakura Happy2 at left
    show ayano Shy1 at right

    sa "Kom, sæt dig ned og spis noget"

    "Du sætter dig ved bordet, og Sakura kommer med en tallerken pandekager"

    ay "Vi har også lavet noget varm kakao"

    menu:
        "Spis i stilhed":
            "Du begynder stille at spise"
            
            "Det er rart at have noget andet at fokusere på"
            
            sa "Tag dig god tid"
            
        "Komplimentér pandekagerne":
            mc "De smager virkelig godt..."
            
            show sakura Happy1 at left
            sa "Det var Ayano der lavede dem"
            
            show ayano Shy2 at right
            ay "Jeg er glad for du kan lide dem"
            
        "Jeg er ikke særlig sulten":
            mc "Jeg ved ikke om jeg kan spise..."
            
            show sakura Sad2 at left
            sa "Bare lidt... Du får brug for energien i dag"
            
            ay "Vi skal nok passe på dig"

    "Du spiser langsomt op og drikker din kakao"

    "Pigerne ser bare ud til at kigge på dig med et bekymret blik"

    "Efter at have spist op tager du tallerkenen og ligger den ude i køkkenet"

    mc "1000 tak for mad"

    sa "Det var så lidt"

    "Efter morgenmaden går du op for at klæde om til dit skoletøj"

    scene bg bedroom

    "Imens du tager dit skoletøj på, kan du høre pigerne tale sammen nede i køkkenet"

    "Du ved at de bekymrer sig om dig"

    scene bg kitchen
    "Du går ned igen, klar til at tage afsted"

    show sakura Happy2 at left
    sa "Er du klar?"

    show ayano Smile1 at right
    ay "Vi går sammen hele vejen"

    "Du tager en dyb indånding"

    mc "Jeg er klar..."

    "Sammen begynder i at gå mod udgangen af huset"

    "I går udenfor og du låser døren bag dig"

    scene bg street
    play music t2

    mc "Gad vide hvad der skete med Akira i går"

    show ayano Shy1 at right
    ay "Freddy tog hende i hvert fald i at flirte med dig"

    ay "Vi kan håbe at han har talt hende til fornuft"

    show sakura Sad2 at left
    sa "Der er noget jeg har tænkt over..."

    mc "Hvad er det?"

    sa "Det er som om at hun aldrig rigtigt accepterede at komme ud i den virkelige verden"

    sa "Hun opføre sig som om at det hele stadig er et spil"

    "I fortsætter ned af den stille morgengade sammen"

    "Der er bliver pludseigt stille... Der er ingen der siger noget"

    show sakura Happy2 at left
    sa "Det vigtigste er at vi holder sammen"

    show ayano Smile1 at right
    ay "Ja, vi lader dig ikke være alene i dag"

    mc "Men hvad hvis hun..."

    show ayano Angry1 at right
    ay "Hun kommer ikke i nærheden af dig"

    "Du kan mærke hvordan begge piger instinktivt går lidt tættere på dig"

    "De scanner konstant området omkring jer mens i går"

    "I det fjerne kan i begynde at se skolens bygning"

    show sakura Sad2 at left
    sa "Er du sikker på du er klar til det her?"

    "Du tager en dyb indånding og kigger på skolen"

    scene bg school
    play music t3
    "Begge piger går på hver din side"

    "Når i er på vej ind i skolen, kan i se at alle de andre elever kigger på jer"

    "Næsten som om at de ved der er sket noget"

    scene bg hallWay
    "Når i kommer ind kan i høre de andre elever hviske til hinanden mens i går"

    show ayano Angry1 at right
    ay "De burde skamme sig, at stå og sladre sådan"

    menu:
        "Dette er pinligt":
            mc "Jeg hader at alle stirrer sådan..."
            
            show sakura Happy2 at left
            sa "Det er ikke din skyld. Folk elsker bare at sladre"
            
            show ayano Shy1 at right
            ay "Det går over... Folk finder snart noget andet at tale om"
            
        "Jeg vil bare væk herfra":
            mc "Kan vi ikke bare skynde os til klassen..."
            
            show ayano Angry2 at right
            ay "Selvfølgelig. Vi behøver ikke stå her"
            
            sa "Kom, vi tager en anden vej"
            
        "Lad dem bare stirre":
            mc "De må tænke hvad de vil..."
            
            show sakura Happy2 at left
            sa "Det er godt at se dig være stærk"
            
            show ayano Smile1 at right
            ay "Præcis. Vi ved hvad der virkelig skete"

    "I følges ned af de lange gange over mod klassen"

    scene bg class_day
    "I går ind og det første du ser er Akira"

    show akira Flirt2 at center
    ak "God morgen [mc]~"

    show ayano Angry1 at right
    ay "Hold dig væk fra [mc]..."

    show sakura Sad2 at left
    sa "Kom [mc], vi finder et andet sted at sidde"

    show akira Flirt2 at center
    ak "Åh?~ Prøver i at holde os fra hinanden igen?~"

    ak "Efter vores... specielle øjeblik i går~"

    menu:
        "Gem dig bag pigerne":
            mc "..."

            show akira Angry1 at center
            ak "Gemmer du dig?~ Det er sødt~"

            ak "Men du kan ikke gemme dig for evigt~"
        "Konfrontér hende":
            mc "Det var ikke et specielt øjeblik... Du tvang mig"

            show akira Angry2 at center
            ak "Tvang dig?~ Nej, nej... Jeg hjalp dig bare med at indse dine følelser~"
        "Prøv at ignorere hende":
            "Du vælger at kigge væk og ignorere hende"

            show akira Angry1 at center
            ak "Du kan ikke bare ignorere mig [mc]~"

    scene bg class_day
    "Pludseligt kan i høre døren åbne"

    show baldi Idle at center
    play music scarySchoolLesson
    b "Hva' så der små børn"

    b "Baldi er i huuuuset"

    show helpy DC at left
    h "IGEN!? Hvor mange gange SKAL VI LIGE HAVE DIG!?"

    b "Slap dog af lille sneeeegl, det er anden gang i den her uge"

    h "SNEGL!?"

    b "Lige præcis, du er langsom, jeg troede vi havde snakket om det her sidste gang"

    b "Det havde vi så ikke..."

    h "I det mindste har jeg en kanel snegl. Jeg brugte mine sidste penge på den i den her uge"

    "Helpy tager en kanel snegl frem som han skal til at spise"

    "Baldi går hen til ham og tager hans kanel snegl"

    h "HEY!"

    b "Nååårh, skal den lille baaaby til at græde"

    h "Hvorfor skal sådan noget altid ske for mig"

    b "Har du tænkt over at der måske er en grund til at sådan noget altid sker for dig?"

    "[mc] du har lige set hvad der er sket mod Helpy, vil du gøre noget?"

    menu:
        "Du kan ikke bare tage hans kanel snegl":
            mc "Du kan ikke bare tage hans mad på den måde..."

            show baldi Angry at center
            b "Åh? Tør du at sige mig imod?"

            show helpy Happy at left
            h "Tak [mc]"

            b "Det bliver et MEGET svært matematik spørgsmål til dig [mc]!"

            b "Hvad er 135135 * 135135?"

            menu:
                "18261502225":
                    b "FORKERT!"
                "Det er ikke fair":
                    b "DET ER IKKE ET TAL!"
                "...":
                    b "FORKERT FORDI DU IKKE SVAREDE!"

        "Helpy har sikkert fortjent det":
            mc "Du har sikkert fortjent det..."

            show helpy Angry at left
            h "WHAT!? Jeg troede vi var venner!"

            show baldi IdleHappy at center
            b "Hahaha! Selv dine venner er imod dig!"

            h "Jeg hader virkelig den her skole..."

        "Sig ikke noget":
            "Du vælger at holde dig udenfor"

            show helpy DC at left
            h "Det er også fint nok... Jeg er vant til at ingen hjælper mig"

            show baldi IdleHappy at center
            b "Hahaha! Selv dine venner tør ikke at hjælpe dig!"

    scene bg class_day
    show baldi Idle at center
    b "Nå, men lad os komme i gang med timen!"

    b "I dag skal vi lære noget MEGET vigtigt"

    show helpy DC at left
    h "Lad mig gætte... Matematik?"

    b "Nej, nej, nej... Noget MEGET vigtigere"

    h "Vigtigere end matematik? Det troede jeg ikke var muligt for dig"

    b "Vi skal lære om hvordan man spiser en kanel snegl"

    "Baldi tager en bid af Helpys kanel snegl"

    show helpy Angry at left
    h "DET VAR MIN SIDSTE KANEL SNEGL!"

    show baldi IdleHappy at center
    b "Og den smagte fantastisk"

    show ayano Angry1 at right
    ay "Er det ikke på tide vi begynder timen?"

    b "Åh? Prøver du at redde din lille ven?"

    show sakura Sad2 at left
    hide helpy
    sa "Vi vil bare gerne lære noget..."

    scene bg class_day
    show baldi Idle at center
    b "I har ret, lad os lære hvor meget jeg hader [mc]"

    b "Vidste i at [mc] ikke kan klare de simpleteste matematik opgaver"

    b "Han er faktisk den væreste elever jeg nogensinde har set"

    show baldi Angry at center
    b "Hvad er 2 + 2?"

    menu:
        "4":
            "KORREKT!"
        "6":
            "FORKERT!"
        "8":
            "FORKERT!"

    b "hvad er 15 + 15"
    menu:
        "30":
            "KORREKT!"
        "25":
            "FORKERT!"
        "35":
            "FORKERT!"

    b "Hvis du har 10 æbler og der er 5 venner, hvor mange æbler kan hver person få?"
    menu:
        "1":
            "FORKERT!"
        "2":
            "KORREKT!"
        "3":
            "FORKERT!"

    b "Hvis klokken er 7, hvor varmt skal det så være før man kan finde diamant i en computer?"

    show helpy DC at left
    h "Det spørgsmål giver bogstavligt talt ikke mening"

    b "FORKERT! Det er 100 grader!"

    h "WHAT!? Det var ikke engang mig der skulle svare!"

    b "Hvorfor talte du så?"

    hide helpy
    b "[mc] prøv igen!"

    b "Hvis du har 5 æbler, og du fjerner 3 appelsiner, men tilføjer 1 vandmelon, hvor mange bananer plus frugter har du så?"

    menu:
        "5":
            "FORKERT!"
        "1":
            "FORKERT!"
        "Ingen":
            "FORKERT!"
        "Det ved jeg ikke":
            "FORKERT!"

    b "JEG TROR DER SNART ER NOGLE DER SKAL STRAFFES!"

    b "LAD OS PRØVE IGEN!"

    "Baldi begynder at gå helt op til din plads"

    "Du kan se at Baldi gøre sig klar til at slå"

    scene bg corridor
    "Du rejser dig fra din plads og løber ud af klassen"

    "Lige som sidst løber du hen mod samme skab igen"

    scene bg school_closet
    "Efter noget tid når du endelig skabet og du går ind og sætter dig og begynder at græde"

    mc "Det føles som om alt er i mod mig..."

    "Men pludseligt kan du høre skridt udenfor"

    "Du kan høre nogle tager håndtaget og åbner døren"

    show akira Concerned at center
    play music sakuraTheme
    ak "Åh~ Det er her du gemmer dig"

    "Du rykker dig længere ind i skabet"

    ak "Shh... Jeg er ikke her for at skade dig~"

    show akira Sad at center
    ak "Det gør ondt at se dig sådan her... At se andre skade dig~"

    menu:
        "Bed hende om at gå":
            mc "Akira... jeg kan virkelig ikke klare mere i dag..."
            
            show akira Flirt1 at center
            ak "Netop derfor jeg er her~ For at beskytte dig~"
            
            ak "Jeg så hvordan han behandlede dig...~"
        
        "Bliv stille":
            "Du trækker dine ben op til brystet og prøver at gøre dig mindre"
            
            show akira Princess at center
            ak "Du behøver ikke at være bange~ Jeg er din prinsesse, husker du?~"
            
            ak "Og en prinsesse beskytter det der er hendes~"
        
        "Spørg hvorfor hun er her":
            mc "Hvorfor... hvorfor følger du efter mig?"
            
            show akira Flirt2 at center
            ak "Fordi jeg altid ved hvor du er~ Jeg kan mærke når du har brug for mig~"

    show akira Idle at center
    "Hun sætter sig langsomt ned ved siden af dig i skabet"

    show akira Special1
    ak "Ved du hvad der er forskellen på mig og de andre?~"

    "Du svarer ikke, men hun fortsætter alligevel"

    show akira Special2
    ak "De andre... De prøver at {i}beskytte{/i} dig fra verden~"

    ak "Men jeg... Jeg vil give dig en helt ny verden~"

    "Hun læner sig lidt tættere på, men ikke truende denne gang"

    ak "En verden hvor ingen kan såre dig... Hvor det kun er os to~"

    show akira Special2
    ak "Jeg ved godt at du har været bange for mig~"

    ak "Men alt hvad jeg har gjort, var af kærlighed~"

    show akira Special1
    ak "Jeg prøver at beskytte dig mod verdenen~ For den er ond"

    "Hun tager forsigtigt din hånd"

    mc "Akira, må jeg spørge dig om noget?"

    show akira Special4
    ak "Selvfølgelig~ Spørg mig om hvad som helst~"

    mc "Hvorfor... hvorfor er du så besat af mig?"

    show akira Special5
    ak "Oh~ Eheh, det er svært at svare på [mc]~"

    ak "Jeg kan bare virkelig lide din personlighed"

    show akira Special4
    ak "Du ønsker at hjælpe andre, du er sød og venlig~"

    ak "Der er ikke mange som dig"

    ak "Mange tænker på dem selv, og er selviske"

    show akira Special5
    ak "Og jeg tror at de- at du ikke prøver at få en kæreste på en måde gør dig mere speciel~"

    show akira Special4
    ak "Men der er noget jeg gerne vil spørge dig om [mc]~"

    mc "Hvad er det?"

    show akira Special3
    ak "Kan du tilgive mig for at have kysset dig i går i mod din vilje?"

    show akira Special2
    ak "Det er noget jeg har tænkt en del over siden i går~ Jeg ved at det var forkert~"

    ak "Jeg kunne bare ikke stoppe mig selv~"

    ak "Det er ikke fordi jeg forventer at du tilgiver mig, men det ville hjælpe at høre om du har"

    menu:
        "Jeg kunne faktisk lide det":
            mc "For at være helt ærlig... Jeg kunne faktisk lide det..."
            
            show akira Special1 at center
            ak "Virkelig?~ Men du virkede så bange..."
            
            show akira Special4 at center
            ak "Eller måske... var du bare overrasket?~"
            
            "Hun klemmer blidt din hånd"
            
            ak "Næste gang behøver det ikke at være så pludseligt~"
        "Jeg har tilgivet dig Akira":
            mc "Jeg... jeg har tilgivet dig, Akira"
            
            show akira Special4 at center
            "Hun ser overrasket ud et øjeblik"

            ak "Du er virkelig speciel [mc]~ Så tilgivende..."
            
            ak "Det er derfor jeg... derfor jeg ikke kan lade dig gå~"
        "Jeg ved ikke om jeg kan tilgive dig endnu":
            mc "Jeg... jeg ved ikke helt om jeg kan tilgive dig endnu..."
            
            show akira Special2 at center
            ak "Det forstår jeg godt~ Tag den tid du har brug for~"
            
            show akira Special4 at center
            ak "Jeg vil vente... Lige meget hvor lang tid det tager~"
        "Jeg kan ikke tilgive dig":
            mc "Jeg... jeg kan ikke tilgive dig for det..."
            
            show akira Special2 at center
            ak "Det gør ondt at høre~ Men jeg forstår det~"
            
            show akira Special5 at center
            ak "Men ved du hvad der er det værste [mc]?~"
            
            ak "Selv om det sårede dig... Ville jeg gøre det igen~"

    show akira Special4 at center
    "Hun sidder stille et øjeblik, stadig holdende din hånd"

    ak "Ved du hvad der skræmmer mig mest [mc]?~"

    mc "Hvad?"

    show akira Special2 at center
    ak "At jeg ikke kan kontrollere hvordan jeg har det omkring dig~"

    ak "Jeg prøver at være normal... At være som de andre~"

    show akira Special5 at center
    ak "Men når jeg ser dig... Når jeg er tæt på dig sådan her~"

    ak "Så mister jeg kontrollen... Alt andet forsvinder~"

    show akira Special3 at center
    "Hun flytter sig lidt tættere på"

    ak "Jeg lover at være mere... kontrolleret fremover~"

    ak "Men du må love mig én ting [mc]~"

    mc "Hvad?"

    show akira Special5 at center
    ak "Lad være med at løbe fra mig~ og gemme dig, det gør ondt når du prøver at undgå mig"

    ak "Når du gemmer dig bag de andre~"

    show akira Special2 at center
    ak "Jeg vil ikke såre dig... Men jeg kan ikke garantere hvad der sker hvis du bliver ved med at løbe~"

    menu:
        "Jeg løber ikke mere":
            mc "Jeg... jeg løber ikke mere..."
            
            show akira Special4 at center
            ak "Det var alt jeg havde brug for at høre~"
            
            "Hun læner sig frem og kysser dig blidt på kinden"
            
            ak "Se~ Jeg kan være blid når du samarbejder~"

        "Du kan ikke true mig sådan":
            mc "Du... du kan ikke blive ved med at true mig sådan..."
            
            show akira Special5 at center
            ak "True?~ Nej, nej... Jeg advarer dig bare~"
            
            ak "Der er en forskel~ Trusler er onde, advarsler er af kærlighed~"

        "...":
            "Du forbliver tavs, fanget mellem frygt og en underlig form for fascination"
            
            show akira Special4 at center
            ak "Din stilhed er så smuk~ Ligesom dig~"
            
            "Hun stryger blidt din kind"

    show akira Special4 at center
    ak "Du kan se mig som din ultimative beskytter~"

    ak "Nå, men jeg må hellere se at komme tilbage til time"

    show akira Flirt2 at center
    ak "Husk hvad jeg sagde [mc]~ Løb ikke fra mig~"

    ak "For jeg vil altid finde dig~"

    "Hun går ud af skabet og lukker døren efter sig"

    scene bg school_closet

    "Du bliver siddende i skabet, stadig pårvirket af samtalen med Akira"

    "Efter nogle minutter kan du høre hurtige fodtring nærme sig"

    show sakura Sad2 at left
    sa "[mc] Er du herinde?"

    "Døren bliver åbnet og du kan se både Sakura og Ayano"

    show ayano Angry1 at right
    ay "Hvis hun har rørt dig igen..."

    ay "Hun var her, var hun ikke?"

    menu:
        "Fortæl hvad der skete":
            mc "Hun... hun var anderledes denne gang..."
            
            show ayano Shy1 at right
            ay "Anderledes hvordan?"
            
            mc "Hun var næsten... blid. Men stadig skræmmende"
            
            show sakura Sad2 at left
            sa "Det lyder som om hun prøver at manipulere dig..."
            
        "Hold det for dig selv":
            mc "Jeg vil helst ikke snakke om det..."
            
            show sakura Sad2 at left
            sa "Det er okay... Du behøver ikke at fortælle os det"
            
            show ayano Angry1 at right
            ay "Men vi bliver nødt til at gøre noget ved hende..."
        
        "Jeg er forvirret":
            mc "Jeg ved ikke hvad jeg skal tro længere..."
            
            show ayano Shy1 at right
            ay "Hvad mener du?"
            
            mc "Hun var... anderledes. Næsten omsorgsfuld..."
            
            show sakura Sad3 at left
            sa "Det er sådan hun får dig til at stole på hende..."
    

    show ayano Angry1 at right
    ay "Vi burde gå til rektor med det her"

    mc "Nej, vent... Måske prøver hun bare at ændre sig"
    
    show ayano Angry2 at right
    ay "Kan du ikke se hvad hun gør mod dig?"

    ay "Hun prøver at manipulere dig"

    mc "Måske skal vi give hende en chance"

    ay "Fint..."

    sa "[mc], du er altid så tilgivende og omsorgsfuld"

    scene bg hallWay
    "Du forlader skabet og begynder at gå mod klassen igen"

    "Du kan se at Sakura og Ayano begge holder øje med om Akira gemmer sig et sted"

    "Men hvad hun mon mente med at hun altid ville finde dig?"

    "Hvad kan det mon betyde?"

    show sakura Sad1 at left
    sa "Jeg kom til at tænke på, det måske er bedst vi bare går til spise pause før tid"

    sa "Hvis Baldi ser dig bliver han nok meget sur over at vi gik midt i timen"

    show ayano Sad1 at right
    ay "Men der stadig mini pause og time bag efter, der er lang tid til spise pause"

    sa "Det er okay, hvis det kan hjælpe [mc]"

    "Sammen begynder i at gå mod kantinen i stedet for klassen"

    mc "Jeg føler at Akira er begyndt at forbedre sig"

    mc "Hun undskyldte for at være så besat af mig"

    ay "Det tror jeg ikke, hun prøver stadig bare at manipulere med dine følelser"

    "Endelig når i ned til kantinen"

    scene bg cantine
    play music relax
    "Kantinen er helt tom eftersom i er kommet før tid"

    show sakura Happy2 at left
    sa "Det er faktisk rart at være her når der er så stille"

    show ayano Shy1 at right
    ay "Ja... Ingen der stirrer eller hvisker"

    "I finder et bord ved vinduet og sætter jer"

    sa "Ved i hvad? Nu hvor vi har catinen for os selv, kunne vi gøre det til noget hyggeligt?"

    show ayano Smile1 at right
    ay "Det er faktisk ret fredeligt når her er tomt"

    "Du kigger midt ud i rummet og der er en behagelig stilhed i rummet"

    sa "Gad vide hvordan maden smager når man er de første der får den?"

    ay "Det kunne være interesssant at finde ud af..."

    "I går sammen hen til Chica som står ved maden"

    scene bg cantineIdle

label secendCantine:
    menu:
        "En pizza til 120kr" if playerMoney >= 120:
            $ playerMoney -= 120
            mc "Jeg vil gerne have en pizza"
            
            chica "En friskbagt pizza, lige fra ovnen!"
            
        "En sandwich til 60kr" if playerMoney >= 60:
            $ playerMoney -= 60
            mc "Jeg kunne godt tænke mig en sandwich"
            
            chica "Du er heldig, brødet er lige kommet ud af ovnen"
            
        "En durum rolle med Kebab 80kr" if playerMoney >= 80:
            $ playerMoney -= 80
            mc "Jeg tror jeg tager en salat i dag"
            
            chica "En frisk kebab, god timing!"
        "Jeg har ikke råd til noget" if playerMoney < 60:
            "Wow, du har faktisk ikke råd til noget..."

            "Jeg vil være sød mod dig denne gang. Men lad være med at spilde dine penge, det kan være de bliver vigtige..."

            "Jeg giver dig 1500 kroner..."

            "[mc] får pludseligt en besked på sin telefon om at han har vundet 1500 kroner fra lotto"
            $ playerMoney += 1500

            jump secendCantine

    "Du betaler og tager din mad"
    "Du har nu [playerMoney]kr tilbage"

    "Efter at have fået jeres mad, går i tilbage til jeres bord igen"

    scene bg in_cantine
    show sakura Happy1 at left
    sa "Ved i hvad jeg savner?"

    mc "Hvad?"

    sa "At tegne... Jeg plejede at tegne meget før"

    show ayano Shy1 at right
    ay "Jeg vidste ikke du kunne tegne"

    show sakura Happy2 at left
    sa "Jeg er ikke særlig god til det, men jeg elsker at gøre det"

    menu:
        "Hvad kan du lide at tegne?":
            mc "Hvad tegner du mest?"
            
            show sakura Happy2 at left
            sa "Mest natur... Træer, blomster, landskaber"
            
            ay "Det lyder faktisk ret afslappende"
            
        "Du burde begynde igen":
            mc "Du burde at starte med at tegne igen"
            
            show sakura Happy3 at left
            sa "Måske... Det kunne være hyggeligt"
            
            ay "Vi kunne måske tegne sammen en dag"
            
        "Vis os det en dag":
            mc "Du må vise os nogle af dine tegninger en dag"
            
            show sakura Happy2 at left
            sa "Måske... hvis i lover ikke at grine"
            
            ay "Vi ville aldrig grine af dig"

    show ayano Smile1 at right
    ay "Ved i hvad jeg godt kan lide at lave?"

    mc "Hvad?"

    ay "At lave mad... Der er noget beroligende ved det"

    sa "Det forklarer hvorfor dine pandekager i morges var så gode"

    show sakura Happy2 at left
    sa "Du må lære mig at lave dem sådan en dag"

    ay "Det kunne være hyggeligt at lave mad sammen, hvem ved måske kan [mc] lære noget af det"

    "I fortsætter med at spise og snakke om jeres forskellige interesser"

    "Det er rart at lære hinanden bedre at kende"

    show sakura Happy3 at left
    sa "Vi kunne måske lave en hobby-dag sammen"

    ay "Hvad mener du?"

    sa "En dag hvor vi deler vores hobbyer med hinanden"

    sa "Jeg kunne lære jer at tegne, Ayano kunne lære os at lave mad..."

    menu:
        "Det lyder hyggeligt":
            mc "Det kunne faktisk være rigtig sjovt"
            
            show ayano Smile1 at right
            ay "Vi kunne lave det hjemme hos en af os"
            
        "Jeg har ingen hobbyer":
            mc "Jeg ved ikke hvad jeg skulle lære jer..."
            
            show sakura Happy2 at left
            sa "Så kan vi hjælpe dig med at finde en hobby!"
            
        "Måske en anden dag":
            mc "Det lyder sjovt, men måske en anden dag"
            
            sa "Selvfølgelig, når du har lyst"

    scene bg in_cantine
    "Efter at i har spist færdig, rejser i jer fra jeres pladser og tager jeres ting"

    "I ligger jeres ting i opvasken og går ud af kantinen"

    scene bg hallWay
    show sakura Happy1 at left
    sa "Den nye time start snart, der er stadig 2 timer endnu, hvad skal vi lave?"

    show ayano Idle1 at right
    ay "Skal vi ikke tilbage til time?"

    sa "Jeg har kigget på vores skema og jeg kan se vi stadig skal have Baldi"

    sa "Så jeg tænker at vi udforsker skolen lidt"

    mc "Det syntes jeg faktisk lyder som en god ide"

    sa "Kom med mig jeg kender der perfekte sted på skolen"

    "I begynder at gå igennem de lange gange"

    "I går forbi flere klasser og ser eleverne sidde og arbejde"

    "Til sidst kommer i til en glas dør, Sakura går igennem den og holder døren åben for jer"

    scene bg school_yard
    "I kommer til en have midt i skolen fyldt med lyserøde kirsebær træer"

    "Et øjeblik står I alle helt stille, overvældet af synet"

    show sakura Happy2 at left
    sa "Det er mit yndlingssted på hele skolen"

    show ayano Smile1 at right
    ay "Det er... smukt"

    "Kirsebærblomsterne du kan både se og dufte det smukke træ"

    sa "Jeg fandt det ved et tilfælde en dag jeg gik forkert"

    mc "Det føles næsten som at være i en anden verden"

    show sakura Happy3 at left
    sa "Præcis! Det er som et lille sted hvor man kan være sig selv"

    show ayano Smile1 at right
    ay "Nu forstår jeg hvorfor du finder inspiration til at tegne"

    sa "Jeg plejede faktisk at sidde i en park med lyserøde kirstebærtræer og tegne blomsterne"

    "I finder en bænk under et af træerne og sætter jer"

    sa "Nogle gange når alting bliver for meget..."

    sa "Så kommer jeg herud og bare... er"

    sa "Ligesom det sted vi mødtes ved [mc]"

    sa "Kan du huske bakken, hvor vi stod og kiggede ud over skoven?"

    sa "Hvor vi aftalte at vi ville mødes hvis vi følte at verdenen var i mod os?"

    mc "Ja, det husker jeg"

    "I sidder og nyder stilheden sammen, du kan høre vinden få bladende til at rasle"

    "Pludseligt tager Sakura en lille notesbog frem"

    sa "Vil i se nogle af mine tegninger?"

    menu:
        "Ja, meget gerne":
            mc "Jeg ville rigtig gerne se dem"
            
            show sakura Happy3 at left
            "Hun rødmer let mens hun åbner blokken"
            
            sa "De er ikke særlig gode, men..."
            
        "Er du sikker?":
            mc "Er du sikker på du vil dele dem?"
            
            show sakura Happy1 at left
            sa "Med jer? Ja, det er jeg"
            
        "Du behøver ikke":
            mc "Du behøver ikke hvis du ikke har lyst"
            
            show sakura Happy2 at left
            sa "Nej, jeg vil gerne... I er mine venner"

    "Hun åbner forsigtigt blokken og viser jer den første tegning"

    show drawing1 at center

    show ayano Smile1 at right
    ay "Sakura... Det er jo smukt"

    show sakura Happy2 at left
    sa "Synes du virkelig det?"

    mc "Det er utroligt detaljeret"

    "Hun bladrer forsigtigt videre i blokken"

    hide drawing1
    show drawing2 at center
    sa "Her er en jeg lavede af udsigten fra bakken..."

    menu:
        "Du har virkelig talent":
            mc "Du har virkelig talent, det er perfekt"
            
            show sakura Happy3 at left
            sa "Det betyder meget at høre"
            
            ay "Du burde virkelig tegne mere"
            
        "Det bringer minder frem":
            mc "Det minder mig om den dag..."
            
            show sakura Happy1 at left
            sa "Ja... Jeg tegnede den lige efter vi kom hjem"
            
            "Hun smiler blidt mens hun kigger på tegningen"
            
        "Kan du lære mig det?":
            mc "Tror du... du kunne lære mig at tegne sådan?"
            
            show sakura Happy2 at left
            sa "Selvfølgelig! Vi kunne starte med noget simpelt"
            
            ay "Måske kunne vi alle lære det sammen"

    hide drawing2
    "En blid vind får nogle blomsterblade til at falde ned omkring jer"

    show ayano Shy1 at right
    ay "Det er næsten som om stedet blev endnu smukkere af dine tegninger"

    sa "I skulle se det når solen går ned... Lyset mellem træerne er magisk"

    "Hun bladrer videre og viser flere tegninger"

    "Nogle er af blomster, andre af landskaber, men alle har en særlig ro over sig"

    mc "Hvorfor stoppede du med at tegne?"

    show sakura Sad2 at left
    sa "Jeg ved ikke... Tiden løb bare fra mig, og så..."

    show ayano Smile1 at right
    ay "Du skal begynde igen. Dit talent skal ikke gå til spilde"

    show sakura Happy2 at left
    sa "Måske... Måske kunne vi mødes her nogle gange?"

    sa "Jeg kunne tegne mens vi bare... er sammen"

    menu:
        "Det ville jeg elske":
            mc "Det lyder som en perfekt ide"
            
            show sakura Happy3 at left
            sa "Virkelig? Det ville gøre mig så glad"
            
            ay "Vi kunne gøre det til vores særlige sted"
            
        "Vi kunne alle prøve":
            mc "Vi kunne alle prøve at tegne sammen"
            
            show sakura Happy2 at left
            sa "Jeg kunne lære jer grund tingende til at tegne"
            
            ay "Det kunne være vores nye hobby"
            
        "Bare vi er sammen":
            mc "Det vigtigste er at vi er sammen"
            
            show sakura Happy1 at left
            sa "Du har ret... Det er det der betyder mest"

    "Pludseligt kan i høre skoleklokken i det fjerne"

    show ayano Shy1 at right
    ay "Er det virkelig allerede så sent?"

    sa "Tiden flyver når man har det godt..."

    "I rejser jer langsomt fra bænken"

    ay "Det ser ud til at der er spise pause nu"

    mc "Men vi har lige spist"

    show sakura Happy2 at left
    sa "Jeg tænker ikke der er nogle grund til at vi går til spisning lige nu"

    sa "Hvad med at vi går tilbage til klassen?"

    ay "Det er nok en god ide, vi har stadig time bag efter spisningen"

    "Sammen begynder i at forlade haven og gå ind i skole gangen igen"

    scene bg hallWay
    play music t3
    "I går ned af de lange gange endnu en gang for at nå tilbage til jeres klasse"

    "Gangende er stille nu hvor de fleste elever er i kantinen"

    show sakura Happy2 at left
    sa "Det var rart at dele det sted med jer"

    show ayano Smile1 at right
    ay "Tak fordi du viste os det"

    "I går stille sammen, stadig påvirket af den rolige stemning fra haven"

    mc "Det er underligt hvordan skolen kan gemme på sådan et sted"

    show sakura Happy1 at left
    sa "Nogle gange finder man de smukkeste steder hvor man mindst venter det"

    "I kan høre de fjerne lyde fra kantinen"

    show ayano Shy1 at right
    ay "Det er næsten som om vi har vores egen lille hemmelighed nu"

    scene bg class_day
    "I når tilbage til klassen og finder jeres pladser"

    show sakura Happy2 at left
    sa "Venner! Jeg har fået en god ide"

    mc "En ide?"

    sa "Yup, hvad hvis vi lavede en klub?"

    show ayano Smile1 at right
    ay "Det lyder spændende, men hvad skulle den handle om?"

    sa "En oplevelses klub"

    sa "Hver gang vi mødes i klubben tager vi et sted hen som vi syntes kunne være spændende at udforske sammen"

    sa "For eksempel den have vi lige så, men måske også andre steder uden for skolen"

    ay "Det er faktisk... En ret god ide"

    sa "Vi kunne alle finde de skjulte, smukke steder i området"

    ay "Men tillader skolen overhodet at vi forlader den?"

    sa "Ja når vi mødes i klubben efter skole må vi godt gå udenfor skolen"

    menu:
        "Det lyder som en god ide":
            mc "Det lyder som et rigtigt eventyr"
            
            show sakura Happy2 at left
            sa "Præcis! Hver gang bliver en ny opdagelse"
            
        "Er det ikke farligt?":
            mc "Er det ikke lidt risikabelt at udforske ukendte steder?"
            
            show sakura Happy1 at left
            sa "Vi holder os selvfølgelig til sikre områder"
            
            ay "Og vi er jo sammen om det"
            
        "Hvad med at starte i dag?":
            mc "Vi kunne faktisk begynde med det samme"
            
            show sakura Happy3 at left
            sa "Du mener det? Det ville være perfekt!"
            
            show ayano Smile1 at right
            ay "Vi har jo allerede fundet vores første sted"

    show sakura Happy2 at left
    sa "Vi kunne lave et kort over alle de steder vi finder!"

    ay "Og tage billeder... eller jeg kunne tegne dem"

    sa "Tænk på alle de hemmelige steder der bare venter på at blive opdaget"

    "I begynder alle at blive ret begejstrede for ideen"

    sa "[mc], hvad syntes du vi skal kalde klubben?"

    define clubName = ""
    menu:
        "Oplvelses klubben":
            $ clubName = "Oplevelses klubben"
        "Eventyrs klubben":
            $ clubName = "Eventyrs klubben"
        "Udforsker klubben":
            $ clubName = "Udforsker klubben"
        "De skjulte steders klub":
            $ clubName = "De skjulte steders klub"

    sa "Godt navn, klubben hedder officielt [clubName]"

    ay "Jeg kan godt lide navnet. Godt fundet på [mc]"

    sa "Så er det besluttet, vi starter [clubName] i dag!"

    sa "Men hvem skal være vores klub præsident?"

    ay "Du ville være en god klub præsiedent Sakura"

    sa "Mig? Hmm... Måske, jeg kan da prøve"

    show sakura Happy2 at left
    sa "Men først skal vi finde ud af hvornår vi skal mødes"

    ay "Det skal nok være efter skole"

    sa "Ja, og vi skal også finde ud af hvor mange gange om ugen"

    "Pludseligt kan i høre flere elever komme tilbage fra spisepausen"

    show ayano Shy1 at right
    ay "Vi burde skrive alle vores ideer ned"

    sa "Ja! Og måske lave en liste over steder vi gerne vil udforske"

    scene bg class_day
    "I ser alle de forskellige elever komme ind igen"

    show FT Happy at center
    fx "HELPY! Du tabte dine bukser! hahaha"

    fx "Vi kan se dit undertøj! LUUU!!"

    show helpy DC at left
    "Helpy kigger hurtigt ned"

    h "Vent jeg har ikke bukser på"

    fx "Haha, du troede du havde bukser på..."

    fx "VENT DU HAR IKKE BUKSER PÅ LUUUU!"

    h "Hvad laver hun overhovdet i den her skole"

    h "Hun kan umuligt være klog nok til at lære noget"

    "Alle eleverne begynder at sætte sig på deres pladser og Akira ved siden af dig som hun plejer"

    "Pludseligt åbner døren igen og Freddy kommer ind"

    scene bg class_day
    play music t31

    show freddy Neutral at center
    f "Godt mine små elever! Jeg har en STOR overraskelse til jer!"

    show helpy DC at left
    h "Åh nej... ikke flere overraskelser"

    f "I dag skal vi noget MEGET specielt!"

    show sakura Shy1 at right
    sa "Hvad mon det kan være..."

    hide sakura
    f "I DAG... skal vi..."

    "Freddy holder en dramatisk pause"

    f "LÆRE OM MIG!"

    show helpy Angry at left
    h "WHAT!? IGEN!?"

    f "JA! For man kan aldrig lære nok om mig!"

    h "Vi har hørt dine historier hundrede gange!"

    show freddy Angry at center
    f "STILLE LILLE SNEGL!"

    f "Dette er en HELT ny historie!"

    f "Den handler om dengang jeg reddede hele verden!"

    show helpy DC at left
    h "Du har aldrig reddet verden..."

    f "Jo jeg har! Og nu skal i høre hvordan!"

    "Freddy går op til tavlen og begynder at skrive"

    f "Det hele startede en helt almindelig tirsdag..."

    menu:
        "Lyt interesseret":
            "Du prøver at følge med i Freddys historie"
            
            show freddy Good at center
            f "Åh! Endelig en der sætter pris på mine bedrifter!"
            
        "Ignorer historien":
            "Du begynder at dagdrømme om [clubName]"
            
            show sakura Happy2 at left
            "Du kan se Sakura skrive ideer ned til klubben"
            
        "Sov":
            "Du lukker øjnene og falder i søvn"
            
            show freddy Angry at center
            f "VÅGN OP! Mine historier er IKKE kedelige!"

    f "Så der sad jeg på min trone af guld..."

    show helpy DC at left
    h "Vent hvad? Hvilken trone?"

    f "AFBRYD MIG IKKE!"

    f "Som jeg var ved at sige... Der sad jeg på min trone af guld, da pludseligt..."

    "Du kan mærke nogen prikke dig på skulderen"

    scene bg class_day
    "Da du vender dig om kan du se det er Sakura der rækker dig en seddel"

    menu:
        "Læs sedlen":
            "Du tager forsigtigt sedlen"
            
            "På den står der: 'Skal vi mødes efter skole og starte [clubName]?'"
            
            menu:
                "Nik ja":
                    "Du nikker til Sakura"
                    
                    show sakura Happy2 at right
                    "Hun smiler tilbage"
                    
                "Skriv tilbage":
                    "Du skriver hurtigt: 'Hvor skal vi mødes?'"
                    
                    "Du giver sedlen tilbage"
        "Ignorer det":
            "Du vælger at fokusere på Freddys historie"
            
            f "...og så kom dragen flyvende ind gennem vinduet!"

    scene bg class_day
    "Freddy fortsætter sin fantastiske historie"

    f "Og det var sådan jeg reddede hele verden fra den onde drage!"

    show helpy Angry at left
    h "Det giver jo ingen mening! Først var du på en trone, så var du i rummet, og nu kæmpede du mod en drage!?"

    f "JA! Det er sådan helte gør!"

    f "Og når man tænker på at i kunne ikke engang holde en normalt teater stykke..."

    f "Det var meningen i skulle vise det til hele skolen, men i gjorde det alt for kaotisk"

    h "Der var nogle, som ikke kunne holde deres rolle..."

    "Helpy kigger på Akira og tilbage på Freddy"

    f "Du skal ikke sige noget lille snegl"

    h "WHAT!? Jeg gjorde alt rigtigt"

    f "Det er ikke sådan jeg husker det"

    show helpy dcLookAway at left
    h "Selvfølgelig..."

    show freddy Good at center
    f "Men hvis i nu havde opført jer ordenligt, kunne vi sagtens have vist det frem"

    show helpy Angry at left
    h "Det er ikke vores skyld at dit manuskript var dårligt!"

    show freddy Angry at center
    f "HVAD SAGDE DU OM MIT MESTERVÆRK!?"

    show helpy DC at left
    h "Et mesterværk? Det handlede bare om at Akira skulle kysses"

    f "Det var en MEGET dybere historie end det!"

    show akira Flirt2 at right
    ak "Jeg syntes nu det var en god historie~"

    show helpy dcLookAway at left
    h "Selvfølgelig gjorde du det..."

    hide akira
    f "Men nu vi snakker om det..."

    "Freddy går hen til sin taske og tager nogle papirer frem"

    f "Jeg har faktisk skrevet en ny historie!"

    show helpy Angry at left
    h "NEJ! Ikke igen!"

    f "JO! Og denne gang er den endnu bedre!"

    show freddy Neutral at center
    f "Denne gang handler det om en modig robot bjørn der skal redde HELE universet!"

    show helpy DC at left
    h "Skal det virkelig handle om en random bjørne robot?"

    f "Nej, ikke en random, en Freddy bjørne robot selvfølgelig"

    show freddy Good at center
    f "Og denne gang skal I ALLE sammen være med!"

    show helpy Angry at left
    h "WHAT!? JEG VIL IKKE VÆRE MED!"

    f "Du har ikke noget valg lille snegl"

    f "Jeg har allerede skrevet alle rollerne!"

    hide sakura
    show ayano Shy1 at right
    ay "Må vi høre hvilke roller vi har fået?"

    f "JA! Jeg er glad for du spørger!"

    "Freddy tager sine papirer frem"

    f "Jeg skal selvfølgelig være hovedrollen som den seje robot bjørn"

    f "Helpy, du skal være min dumme sidekick"

    show helpy Angry at left
    h "HVORFOR SKAL JEG ENTEN VÆRE DEN GRIMME TROLD ELLER DEN GRIMME UBRUGELIG MEDHJÆLPER"

    f "Hey, det beskriver dig faktisk ret godt"

    f "[mc] du skal være min bedste ven der hjælper mig med at redde universet"

    menu:
        "Det lyder da sjovt":
            mc "Det kunne faktisk være sjovt"
            
            show freddy Good at center
            f "ENDELIG en der forstår kunst!"
            
            h "Det er ikke kunst..."
            
        "Jeg vil helst ikke":
            mc "Jeg er ikke sikker på jeg vil være med"
            
            f "Du har ikke noget valg!"
            
            h "Velkommen i klubben..."
            
        "Hvad med de andre?":
            mc "Hvilke roller har de andre fået?"
            
            f "Jeg kommer til det!"

    f "Og selvfølgelig skal Akira være prinsessen igen!"

    show akira Flirt2 at right
    hide ayano
    ak "Jeg tager glædeligt rollen~"

    show helpy Angry at left
    h "Det er jo et science fiction stykke! Der er ingen prinsesser i rummet!"

    f "JO DER ER! Det er MIN historie!"

    "Freddy fortsætter med at dele roller ud"

    f "Vi starter i morgen!"

    h "Men vi har ikke engang øvet..."

    f "Detaljer! Det bliver PERFEKT!"

    "Pludseligt ringer klokken"

    scene bg class_day
    show freddy Neutral at center
    f "Oh, der sluttede timen vidst, jeg glæder mig til at vi skal øve i morgen"

    f "Vi ses i morgen små elever"

    "Freddy tager sine ting og går ud af klassen"

    scene bg class_day
    "Efter Freddy er gået, begynder alle at pakke deres ting sammen"

    show sakura Happy2 at left
    play music t30
    sa "Nå, skal vi mødes og starte [clubName]?"

    show ayano Smile1 at right
    ay "Jeg glæder mig faktisk til at udforske"

    menu:
        "Hvor skal vi mødes?":
            mc "Hvor tænker i vi skal mødes?"
            
            show sakura Happy3 at left
            sa "Hvad med i haven? Det kunne være vores første klubmøde sted"
            
            ay "Det er perfekt... Der hvor det hele startede"
            
        "Hvad skal vi udforske først?":
            mc "Har i tænkt på hvor vi skal udforske først?"
            
            show sakura Happy2 at left
            sa "Jeg har faktisk hørt om et sted ikke så langt herfra..."
            
            ay "Er det det gamle bibliotek du snakker om?"
            
        "Lad os gå nu":
            mc "Skal vi ikke bare gå med det samme?"
            
            show sakura Happy3 at left
            sa "Jeg kan godt lide din entusiasme!"
            
            show ayano Smile1 at right
            ay "Jo før vi starter, jo bedre"

    show akira Flirt2 at center
    ak "Oh?~ Starter i en klub?~"

    ak "Det lyder spændende... Måske skulle jeg også være med~?"

    show ayano Shy1 at right
    ay "Det er... ikke helt den slags klub..."

    sa "Vi har bare brug for lidt tid til at komme i gang først"

    ak "Åh~ Jeg forstår~ I vil have [mc] for jer selv~"

    "Hun sender dig et drillende blik før hun går"

    scene bg class_day
    "Efter Akira er gået, vender i tilbage til jeres planlægning"

    show sakura Happy2 at left
    sa "Skal vi mødes ved haven om 10 minutter?"

    show ayano Smile1 at right
    ay "Det giver os tid til at pakke vores ting"

    "I nikker alle sammen og begynder at gøre klar til jeres første klubmøde..."

    "Du pakker dine ting sammen og forlader klassen"

    scene bg hallWay
    "Du går igennem de lange gange for at nå ned til haven"

    "Skolen er så stor at det næsten tager 7 minutter for dig at nå over til den skjulte have midt i skolen"

    "Endelig når du frem og du går igennem glas døren"

    scene bg school_yard

    "Her er stadig ligeså flot som du husker det fra tideligere"

    "Du tager en dyb indånding for at dufte den friske luft fra kirstebær træerne"

    "Pludseligt kan du se Sakura og Ayano komme gående mod dig"

    show sakura Happy2 at left
    show ayano Smile2 at right
    sa "Er du klar til at starte [clubName]?"

    mc "Ja, jeg glæder mig"

    sa "Det er sådan det skal lyde"

    "Sakura tager en notesbog frem fra sin taske og en blyant til at skrive med"

    sa "Kender i nogle steder der kunne være spændende at udforske?"

    ay "Jeg har hørt om en gammel skov bag skolen..."

    sa "Mhm, det kunne være spændende at se"

    ay "Jeg kender også en kæmpe anime forretning i byen"

    sa "Det kunne være sjovt at se"

    sa "Jeg vidste ikke du kunne lide anime Ayano?"

    show ayano Shy2 at right
    ay "Jo... Det er ikke typisk noget jeg fortæller nogen"

    ay "I er faktisk de første jeg siger det til"

    sa "Jeg syntes det er en sød hobby at kunne lide Anime, der er også mange gode historier"

    sa "Hvad med dig [mc]? Kan du også lide Anime?"

    menu:
        "Ja det kan jeg":
            mc "Ja, det kan jeg faktisk godt"
        "Ikke rigtigt":
            mc "Nej, jeg er ikke så vild med det"

    show ayano Smile1 at right
    ay "Spændende"

    sa "Hvad med steder at udforske, kender du nogle steder vi kunne udforkse?"

    show sakura Happy1 at left
    menu:
        "En forladt bygning":
            sa "Det lyder lidt uhyggeligt, men det er helt fint"
        "En gammel fabrik":
            sa "Det lyder lidt uhyggeligt, men det er helt fint"
        "En forladt park":
            sa "Det lyder lidt uhyggeligt, men det er helt fint"
        "Det gør jeg ikke":
            pass

    sa "Okay nu har vi skrevet nogle steder ned på listen"

    sa "Til næste gang vil jeg finde en klasse vi kan bruge til vores klub"

    mc "Du er virkelig den perfekte klub præsident"

    show sakura Blink1 at left
    sa "Tak, jeg prøver mit bedste"

    show sakura Happy2 at left
    sa "Jeg tænker vi bare holder mødet kort i dag"

    sa "Eftersom at det er vores første dag i [clubName]"

    sa "Tak fordi i ville komme, mødet er hermed hævet"

    ay "Det var en fantastisk ide med denne klub"

    mc "Jeg er også virkelig glad for den, selv om den kun lige er startet"

    sa "Mhm, måske får vi endu flere medlemmere en dag"

    sa "Nå, men tak for i dag venner"

    sa "Det har været super hyggeligt"

    ay "Enig"

    sa "Skal vi gå hjem [mc]?"

    mc "Hjem? Til mig?"

    sa "Ja, jeg tænkte at vi kunne alle 3 følges lidt endnu"

    mc "Det lyder som en hyggelig ide"

    mc "Det vil jeg meget gerne"

    "Både Sakura og Ayano nikker, sammen følges i ud af haven og går ind i skolens lange gange"

    scene bg hallWay
    show ayano Idle1 at right
    ay "Den her skole er virkelig blevet stor"

    ay "Det tager næsten 20 minutter at gå fra den ene side til den anden"

    ay "Forstil dig hvis du har time på den modsatte side at kantinen"

    ay "Så kunne man næsten ikke nå at få noget at spise enden man skulle tilbage igen"

    mc "Ja, det er lidt underligt, man har jo brug for maden"

    scene bg school
    "Efter cirka 7 minutter når i endelig ud af skolen"

    scene bg street
    play music t2
    "I fortsætter ned af gaden sammen"

    "I går en ret lang tur og nyder naturen"

    show sakura Happy2 at left
    sa "Så [mc], hvis du skulle vælge hvad kan du bedst lide?"

    mc "Hvad mener du?"

    sa "Hvis du skulle vælge imellem at en ven gav dig enten, En flot blomst, en æske chokolade, en tegning, eller lækkert mad"

    sa "Hvad ville du så vælge?"

    menu:
        "En flot blomst":
            mc "Jeg ville vælge en flot blomst"
        "En æske chokolade":
            mc "Jeg ville vælge chokoladen"
        "En tegning":
            mc "For at være ærlig, ville jeg nok vælge en tegning fra min ven"

            mc "En tegning er der blevet lagt mere arbejde og kærlighed i end en blomst eller chokolade"
        "Lækkert mad":
            mc "Jeg ville vælge maden"

    show sakura Happy1 at left
    sa "Spændende valg"

    sa "Men jeg forstår det godt"

    "Endelig når i til dit hus, du åbner døren og i går ind"

    scene bg livingroom
    play music t9

    "Du og pigerne kommer ind i stuen"

    show sakura Happy2 at left
    sa "Skal vi lave noget at spise? Jeg tænker vi kan hygge os lidt mere"

    show ayano Smile1 at right
    ay "Jeg kunne godt lave noget mad til os"

    menu:
        "Det lyder hyggeligt":
            mc "Det kunne være rigtig hyggeligt"
            
            show sakura Happy3 at left
            sa "Perfekt! Jeg glæder mig til at se hvad vi skal have den her gang"
            
        "I behøver ikke":
            mc "I behøver virkelig ikke blive..."
            
            show ayano Shy1 at right
            ay "Vi vil gerne. Efter alt det der er sket..."
            
            sa "Vi vil bare gerne være her for dig lidt endnu"
            
        "Jeg er ikke særlig sulten":
            mc "Jeg er faktisk ikke særlig sulten..."
            
            show sakura Sad2 at left
            sa "Du skal have noget at spise [mc]"
            
            ay "Bare lidt. Det er ikke godt at springe måltider over"

    scene bg kitchen
    "I går sammen ud i køkkenet"

    show ayano Smile1 at center
    ay "Har du nogle særlige ønsker [mc]?"

    menu:
        "Noget simpelt":
            mc "Bare noget simpelt ville være fint"
            
            show ayano Happy1 at center
            ay "Jeg kunne lave nogle gode sandwich"
            
            show sakura Happy2 at left
            sa "Det lyder perfekt til en hyggelig aften"
            
        "Hvad end du vil lave":
            mc "Jeg stoler på dine evner i køkkenet"
            
            show ayano Shy2 at center
            ay "Tak, jeg skal se hvad jeg kan gøre"
            
        "Måske kunne vi lave det sammen?":
            mc "Hvad hvis vi lavede maden sammen?"
            
            show sakura Happy3 at left
            sa "Det er en fantastisk ide!"
            
            show ayano Smile1 at center
            ay "Jeg kunne lære jer nogle tricks"

    "I begynder at finde ingredienser frem sammen"

    "I fortsætter med at lave mad sammen mens i snakker"

    show sakura Happy1 at left
    sa "Vi burde gøre dette til en tradition"

    mc "En tradition?"

    sa "Ja, hver gang vi har klubmøde kunne vi slutte dagen sådan her"

    show ayano Smile1 at right
    ay "Det ville faktisk være hyggeligt"

    menu:
        "Det ville jeg elske":
            mc "Det lyder som en perfekt tradition"
            
            show sakura Happy3 at left
            sa "Så er det besluttet!"
            
        "Hver gang?":
            mc "Tror i ikke det bliver for meget?"
            
            show sakura Happy2 at left
            sa "Vi behøver ikke hver gang... Bare når vi har lyst"
            
        "Det kommer an på maden":
            mc "Det kommer helt an på hvad Ayano laver"
            
            show ayano Shy2 at right
            ay "Jeg skal nok gøre mit bedste..."
            
            "Hun rødmer let ved komplimenten"

    scene bg kitchen
    "Efter noget tid er maden endelig klar"

    show sakura Happy2 at left
    sa "Det dufter virkelig godt!"

    show ayano Smile1 at right
    ay "Jeg håber det smager lige så godt"

    "I tager maden med ind i stuen"

    scene bg livingroom
    "I sætter jer sammen i sofaen med maden"

    show sakura Happy3 at left
    sa "Det er næsten som en lille familie"

    show ayano Shy1 at right
    ay "En... familie?"

    sa "Ja, vi passer på hinanden, laver mad sammen, griner sammen..."

    menu:
        "Det føles rigtigt":
            mc "Det føles faktisk som en lille familie"
            
            show sakura Happy2 at left
            sa "Præcis! Vi har fundet noget specielt"
            
        "Er det ikke lidt for meget?":
            mc "Er det ikke lidt overdrevet?"
            
            show sakura Sad2 at left
            sa "Måske... Men det er sådan det føles for mig"
            
        "Vi er venner":
            mc "Vi er gode venner..."
            
            show ayano Smile1 at right
            ay "Ja... Det er vi"

    show sakura Happy2 at left
    sa "Ved i hvad vi også burde gøre til tradition?"

    mc "Hvad?"

    sa "En filmaften efter vi har spist"

    show ayano Smile1 at right
    ay "Kunne vi ikke lave en film aften på samme tid, efter klub mødet. Og så lave mad her?"

    sa "Det er faktisk en rigtig god ide Ayano, så kan vi nyde maden mens vi ser film sammen"

    "Du syntes at det er rart at kunne slappe af sådan her efter alt det der er sket"

    "Efter i har spist færdig, begynder klokken at blive mange"

    sa "[mc], er det okay hvis vi bliver her igen i nat?"

    menu:
        "Selvfølgelig må i det":
            mc "Selvfølgelig må i blive her igen"
            
            show sakura Happy3 at left
            sa "Tak [mc]! Det føles bare tryggere når vi er sammen"
            
            show ayano Shy2 at right
            ay "Specielt efter... alt det der er sket"
            
        "Er i sikre?":
            mc "Er i sikre på i vil det?"
            
            show sakura Happy2 at left
            sa "Vi vil helst ikke lade dig være alene endnu"
            
            show ayano Shy1 at right
            ay "Vi... bekymrer os stadig"
            
        "Jeg vil faktisk også gerne have jer her":
            mc "Jeg ville faktisk også have det bedst hvis i blev"
            
            show sakura Happy1 at left
            sa "Vi er her for dig [mc]"
            
            show ayano Smile1 at right
            ay "Altid"
        
    sa "Vi kan se film og ligge sammen på sofaen igen"

    show ayano Smile1 at right
    ay "Hvilken film skal vi se?"

    menu:
        "Noget sjovt":
            mc "Måske noget der kan få os til at grine?"
            
            show sakura Happy3 at left
            sa "Det er præcis hvad vi har brug for!"
            
        "Noget roligt":
            mc "Bare noget stille og roligt"
            
            show ayano Shy2 at right
            ay "Så vi kan slappe af sammen..."
            
        "I må vælge":
            mc "I må gerne vælge"
            
            show sakura Happy2 at left
            sa "Hmm... Jeg ved lige hvilken film!"

    "Pigerne tager nogle tæpper frem som i kan ligge med"

    "Du sætter dig på sofaen med tæppet, og pigerne sætter sig rundt om dig på hver din side"

    show sakura Happy2 at left
    sa "Er det ikke dejligt sådan her?"

    show ayano Smile1 at right
    ay "Det er... fredeligt"

    "I starter filmen og begynder at se den sammen"

    "Du kan mærke hvordan dagens spændinger langsomt forsvinder"

    "Efter noget tid kan du høre at Sakura er faldet i søvn"

    hide sakura
    show ayano Shy1 at right
    ay "[mc]..."

    mc "Ja?"

    ay "Vi passer på dig, det ved du godt ikke?"

    menu:
        "Jeg ved det":
            mc "Jeg ved det... Tak"
            
            show ayano Smile1 at right
            ay "Godt... Godnat [mc]"
            
        "I er de bedste venner":
            mc "I er de bedste venner jeg kunne ønske mig"
            
            show ayano Shy2 at right
            ay "Og du er den bedste ven vi kunne få..."
            
        "Bare vær stille":
            "Du nikker bare stille, ord er ikke nødvendige"

    "Du kan høre Ayanos åndedræt blive roligere - hun er også faldet i søvn"

    "Du ligger i mørket og tænker på hvor heldig du er at have fundet sådanne venner"

    "Langsomt falder du også i søvn, tryg i visheden om at du ikke er alene"
    $ persistent.current_day = 4
    return