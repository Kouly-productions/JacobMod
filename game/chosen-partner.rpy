label choose_akira:
    scene bg class_day
    $ chosenPartner = "Akira"
    
    "Du rejser dig langsomt fra din plads"
    
    show akira Flirt2 at center
    ak "Jeg vidste du ville vælge rigtigt~"
    
    show ayano Sad1 at left
    show sakura Sad2 at right
    "Du kan se skuffelsen i både Ayano og Sakuras øjne"
    
    mc "Akira... Vil du være min partner til festen?"
    
    show akira Flirt1 at center
    ak "Åh [mc]~ Selvfølgelig vil jeg det~"
    
    "Hun går hen til dig med et intenst blik"
    
    ak "Jeg vidste du kunne se det specielle mellem os~"
    
    show ayano Angry1 at left
    ay "Efter alt hvad hun har gjort..."
    
    show sakura Sad3 at right
    sa "Er du sikker på dette er det rigtige valg, [mc]?"
    
    menu:
        "Ja, jeg er sikker":
            mc "Ja... Jeg ved hvad jeg gør"
            
            show akira Flirt2 at center
            ak "Se?~ Han har truffet sit valg~"
            
            "Akira tager din hånd i sin"
            
            ak "Vi bliver det smukkeste par til festen~"
            
        "Måske ikke...":
            mc "Jeg... jeg er ikke så sikker længere..."
            
            show akira Angry2 at center
            ak "Nej~ Du kan ikke trække dit valg tilbage nu~"
            
            "Hun griber hårdt fat i din hånd"
            
            ak "Du er {i}min{/i} nu~"

    "Du kan høre Freddy sige på afstand"

    f "Så fik Akira endelig sin vilje..."
    
    "Du kan mærke at der er noget der ikke helt stemmer"
    
    show akira Flirt2 at center
    ak "Endelig... Efter så lang tid~"
    
    "Hun holder stadig din hånd, men hendes greb er næsten smertefuldt"
    
    ak "Nu kan ingen tage dig fra mig~"

    jump romance_converge

label choose_ayano:
    scene bg class_day
    $ chosenPartner = "Ayano"
    
    "Du rejser dig stille fra din plads og går hen til Ayano"
    
    show ayano Shy2 at center
    "Hun kigger overrasket op på dig, en let rødmen spreder sig på hendes kinder"
    
    mc "Ayano... Vil du være min partner til festen?"
    
    "Der bliver helt stille i klassen"
    
    show akira Angry2 at right
    ak "Hvad...?"
    
    show ayano Shy1 at center
    ay "Er... er du sikker?"
    
    menu:
        "Ja, du har altid beskyttet mig":
            mc "Du har altid været der for at beskytte mig..."
            
            show ayano Shy2 at center
            ay "Jeg... jeg ville altid beskytte dig"
            
            "Hun tager forsigtigt din hånd"
            
        "Du forstår mig bedst":
            mc "Du er den der forstår mig bedst"
            
            show ayano Smile1 at center
            ay "Jeg har altid prøvet..."

    show akira Angry1 at right
    ak "Nej... NEJ! Dette er ikke hvordan det skulle være!"
    
    show sakura Happy2 at left
    sa "Ayano... Jeg er så glad på dine vegne"
    
    show ayano Smile1 at center
    ay "Tak Sakura..."
    
    show akira Angry2 at right
    ak "I forstår ikke... Dette ødelægger alt!"
    
    "Akira rejser sig voldsomt fra sin plads"
    
    ak "Du kan ikke vælge hende! Du skulle vælge mig!"

    jump romance_converge

label choose_sakura:
    scene bg class_day
    $ chosenPartner = "Sakura"
    
    "Du går over mod Sakura, dit hjerte banker hurtigt"
    
    show sakura Happy2 at center
    "Hun ser op på dig med sine venlige øjne"
    
    mc "Sakura... Vil du være min partner til festen?"
    
    show sakura Blink1 at center
    "Hendes øjne lyser op, og et stort smil spreder sig på hendes ansigt"
    
    sa "Jeg... jeg ville elske det, [mc]"
    
    show akira Angry2 at right
    ak "Hvad!?"
    
    show ayano Smile1 at left
    ay "Det er perfekt... I passer så godt sammen"
    
    menu:
        "Du gør mig tryg":
            mc "Du har altid fået mig til at føle mig tryg..."
            
            show sakura Happy3 at center
            sa "Og du har altid givet mig mod til at være mig selv"
            
        "Vi deler de samme drømme":
            mc "Vi drømmer om de samme eventyr..."
            
            show sakura Happy2 at center
            sa "Vores klub... vores udforskninger..."

    show akira Angry1 at right
    ak "Nej... Dette er FORKERT!"
    
    "Akira slår hårdt i bordet"
    
    ak "Hun fortjener dig ikke! Hun forstår dig ikke som jeg gør!"

    jump romance_converge

label romance_converge:
    scene bg class_day
    show freddy Neutral at center
    f "Jeg tror det er bedst hvis i alle sammen tager en pause..."
    
    f "Måske skulle i gå lidt ud og få noget frisk luft"
    
    "Du kan mærke spændingen i luften"
    
    "Dette valg kommer til at have konsekvenser..."
    
    "Men du ved i dit hjerte at du har valgt rigtigt"
    jump chosen_partner_continue