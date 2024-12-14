label ch5_main:
    
    $ currentDay = "Fredag"
    play music t8
    scene bg livingroom

    "FREDAG"

    "Du vågner langsomt op i din sofa, og det første du kan dufte er varm kakao"

    "Du kan høre pigerne hviske sammen i køkkenet"

    "De prøver tydeligvis at være stille for ikke at vække dig"

    mc "Hvad mon de laver derude?"

    "Det er nok bedst ikke at ødelægge deres overraskelse"

    "Du kan høre Sakura grine stille efterfulgt af et 'shhhh' fra Ayano"

    menu:
        "Bliv liggende og lytte":
            "Du bliver liggende og lytter til deres stille samtale"
            
            "Du kan høre tallerkenerne larme lidt"
            
            sa "Nej, ikke der - han kan se det med det samme hvis vi sætter det der!"
            
            ay "Her måske...?"
            
            "Der er noget hyggeligt ved deres små forberedelser"

            "Efter nogle minutter kalder Sakura fra køkkenet"

            sa "[mc]? Er du vågen?"

            "Du beslutter dig for at 'vågne' nu"

            mc "Ja... jeg er lige vågnet"
            
        "Snige dig ud i køkkenet":
            "Du rejser dig så stille som muligt"
            
            "På vej mod køkkenet træder du på et knirkende gulvbræt"
            
            sa "Åh nej, han vågner!"
            
            ay "Hurtig, gem det!"

            "Du når frem til køkkendøren"
            
        "Give dig til kende":
            mc "God morgen..."
            
            "Du kan høre dem fare sammen i køkkenet"
            
            sa "Du skulle ikke vågne endnu!"
            
            ay "Vi var ikke helt færdige..."

            "Du rejser dig fra sofaen og går mod køkkenet"

    scene bg kitchen
    "I køkkenet finder du pigerne midt i deres morgenmads forberedelser"

    show sakura Happy2 at left
    sa "God morgen [mc]! Du skulle have sovet bare fem minutter mere..."

    show ayano Shy1 at right
    ay "Vi ville overraske dig på den store dag..."

    scene bg kitchen
    "Bordet er dækket smukt med hjemmebagte boller, frisk frugt, og små kort ved hver plads"

    show sakura Happy2 at left
    sa "Vi ville gøre denne morgen helt speciel..."

    show ayano Shy1 at right
    ay "Siden det er den store dag..."

    "Der er lagt så meget omtanke i hver detalje. Bollerne dufter nybagte, og du kan se Sakuras fine tegninger på kortene"

    menu:
        "Det er alt for meget":
            mc "I skulle virkelig ikke have gjort alt det her..."
            
            show sakura Happy3 at left
            sa "Jo! Det er en særlig dag, og du er en særlig ven"
            
            show ayano Shy2 at right
            ay "Vi... vi ville bare gøre det perfekt"
            
        "Det er helt fantastisk":
            mc "Det her... det betyder virkelig meget"
            
            show sakura Happy3 at left
            sa "Vi er bare så glade for at have dig i vores liv"
            
            show ayano Smile1 at right
            ay "Det er det mindste vi kunne gøre"

        "I er de bedste venner":
            mc "Jeg er så heldig at have jer som venner"
            
            show ayano Shy2 at right
            ay "Vi er de heldige..."
            
            show sakura Happy2 at left
            sa "Vi passer på hinanden"

    "I sætter jer sammen ved bordet"

    show sakura Happy2 at left
    sa "Ved du hvad jeg har tænkt på?"

    mc "Hvad?"

    sa "Det er ret specielt at tænke på hvordan vi mødtes"

    show ayano Smile1 at right
    ay "Ja... Det føles som om det var i går"

    "Ayano rækker dig en bolle hun lige har bagt"

    show ayano Shy2 at right
    ay "Jeg håber... de smager okay..."
    
    show sakura Happy3 at left
    sa "Hun har øvet sig hele ugen på at bage dem perfekte"

    "Men du kan se der ligger en kort på dit bord"

    sa "Se på bagsiden af dit kort..."
    
    "Du vender kortet og finder en smuk tegning af jer alle sammen under stjernerne"
    
    sa "Det er os alle sammen til festen i aften... Sådan som jeg forestiller mig det bliver"

    "Det er et billede af jer alle sammen stå sammen til festen"

    "Du kan ikke lade være med at tænke på hvordan aftenen mon bliver"

    "Men først skal i overleve en hel skoledag..."

    show sakura Happy2 at left
    sa "Men vi må nok hellere se at komme afsted"

    "Du kan mærke sommerfugle i maven ved tanken om denne her dag"

    show ayano Shy1 at right
    ay "Vi har lagt dit skoletøj klar inde på værelset..."

    menu:
        "Hvad med opvasken?":
            mc "Skal vi ikke lige tage opvasken først?"
            
            show sakura Happy3 at left
            sa "Nej nej, det klarer vi når vi kommer hjem"
            
            show ayano Smile1 at right
            ay "Du skal bare tænke på at gøre dig klar"
            
        "Jeg er lidt nervøs":
            mc "Jeg er faktisk ret nervøs for i dag..."
            
            show ayano Shy2 at right
            ay "Det... det er vi også"
            
            show sakura Happy2 at left
            sa "Men vi er sammen om det"
            
        "Tak for morgenmaden":
            mc "Tusind tak for den perfekte start på dagen"
            
            show sakura Happy3 at left
            sa "Der er meget mere perfekt i vente"
            
            show ayano Smile1 at right
            ay "Det bliver en særlig dag"

    scene bg bedroom
    "Du går ind på værelset for at klæde om"

    "Pigerne har lagt dit tøj klar på sengen, pænt foldet sammen"

    "Du kan høre dem snakke lavt sammen ude i køkkenet mens de rydder op"

    scene bg kitchen
    "Efter at have klædt om kommer du tilbage til køkkenet"

    show sakura Happy2 at left
    show ayano Smile1 at right
    sa "Er alle klar til at gå?"

    "I samler jeres tasker og gør klar til at gå mod skolen"

    scene bg street
    "Morgenluften er kølig men frisk da i træder udenfor"

    show sakura Happy2 at left
    sa "Det bliver en perfekt dag, jeg kan mærke det"

    show ayano Shy1 at right
    ay "Tror i... der kommer mange til festen?"

    "Sakura begynder at fortælle om alle de forberedelser der er lavet"

    sa "Vi har pyntet hele salen med lyskæder og blomster..."

    sa "Og musikken bliver fantastisk, Freddy har lovet at spille alle de gode sange"

    "Du kan ikke lade være med at smile over hendes begejstring"

    "Imens i går ned af gaden kan i høre skoleklokken i det fjerne"

    show sakura Happy2 at left
    sa "Vi burde nok skynde os lidt..."

    show ayano Shy1 at right
    ay "Ja... Vi skal jo også have de sidste ting klar til festen"

    "I øger tempoet lidt, men fortsætter med at snakke sammen"

    sa "Der er stadig så meget der skal gøres..."

    scene bg school
    "Efter lidt tid når i endelig frem til skolen"

    "Der er allerede mange elever der er mødt op"

    show helpy DC at left
    h "Åh nej, bare vi ikke skal have Toy Freddy i dag..."

    show freddy Neutral at center
    f "Godmorgen små elever!"

    h "Det er da i det mindste ikke Toy Freddy..."

    f "I dag bliver en HELT speciel dag!"

    show helpy Angry at left
    h "Lad mig gætte... Du skal fortælle os en historie om dig selv?"

    f "NEJ! Endnu bedre!"

    f "I dag skal vi... FORBEREDE OS TIL FESTEN!"

    h "Vent, betyder det vi slet ikke skal have normale timer?"

    show freddy Good at center
    f "Det er nemlig rigtigt lille snegl!"

    show helpy Happy at left
    h "YES! ENDELIG EN GOD DAG!"

    f "STILLE LILLE SNEGL"

    f "Vent, sagde du god dag?"

    show helpy DC at left
    h "Ja... Men nu ødelagde du det"

    show freddy Neutral at center
    f "Nå, men små elever, i dag skal alle sammen hjælpe til med at gøre klar"

    show sakura Happy2 at right
    sa "Vi har allerede pyntet det meste af salen..."

    f "JA! Og det ser fantastisk ud!"

    f "Men der skal stadig sættes stole frem, laves mad, og meget mere"

    show helpy DC at left
    h "Lad mig gætte... Jeg får den væreste opgave?"

    show freddy Good at center
    f "Det kan du tro lille snegl!"

    f "Du skal tømme skraldespande under festen, så de ikke bliver fyldte"

    show helpy Angry at left
    h "WHAT!? Den opgave er bogstavlitalt SKRALD!"

    f "Nå, så passer opgaven ret godt til dig"

    f "Nå kom med mig små elever"

    "Freddy begynder at gå ud mod udgangen af klassen"

    scene bg hallway
    "I følger Freddy ned af gangene mens han forklarer dagens opgaver"

    show freddy Neutral at center
    f "Sakura og Ayano skal gøre salen klar"

    f "Han stopper pludseligt op og vender sig mod jer"

    f "Som i alle ved er jeg en ret romntisk lærer så jeg skal selvfølgelig lære jer om kærlighed"

    f "Så, når en dreng og en pige elsker hinanden meget højt..."

    show helpy DC at left
    h "Hvis du skal til at snakke om hvad jeg tror du vil snakke om går jeg altså"

    f "STILLE! DU VED IKKE HVAD JEG VIL SNAKKER OM SNEGL!"

    f "Når en dreng og en pige elsker hinanden meget højt..."

    f "Holder de i hånden"

    h "Åh, det var det du ville sige?"

    f "Jeg vil fortælle jer reglerne til hvordan man kan finde konkurrencen"

    f "Det sødeste par vinder en præmie"

    f "Parret skal selvfølgelig danse sammen og holde i hånden"

    f "Til sidst vil vi gå ud når det bliver mørkt i skole haven under stjernerne"

    f "Der kan man danse videre hvis man har lyst"

    f "Der vil være konstant mad i kan tage, musik og drikkevare"

    show helpy Angry at left
    h "Jeg syntes det er en mærkelig regel... Med det sødeste par"

    f "Det er ikke mig der laver reglerne lille snegl"

    f "Vent, når jo, det er det..."

    f "Hvem skal du være sammen med Helpy?"

    h "Jeg vil ikke deltage i den konkurrence!"

    f "DU SKAL DELTAGE! Hvis du vil vinde"

    h "Jeg kan jo godt lide at vinde"

    f "En gang skal jo være den første"

    h "..."

    "Freddy fortsætter ned af gangen og i følger efter"

    "Efter noget tid ender i endelig i det store rum hvor festen skal holdes"

    scene bg party_hall

    show freddy Good at center
    f "Festen starter i dag... Nu!"

    show helpy DC at left
    h "Lige nu?"

    f "Ja! Lige nu!"

    #Play party music

    scene bg party_hall
    "Freddy går hen og starter noget musik, du kan se flere og flere elver begynder at komme ind"

    if chosenPartner == "Akira":
        show akira Happy at center
        a "Hej [mc]! Er du klar til festen?"
    if chosenPartner == "Ayano":
        show sakura Happy2 at center
        sa "Hej [mc]! Er du klar til festen?"
    else:
        show sakura Happy2 at center
        sa "Hej [mc]! Er du klar til festen?"

    "Fortsættes..."
    

    # Whoever the player chooses will ask if they should kiss to win the contest late night party outside

    return