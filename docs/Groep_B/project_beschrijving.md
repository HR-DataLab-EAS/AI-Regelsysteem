# Project Groep B

Tijdens het project hebben wij een AI model ontwikkeld door middel van behavior cloning en tensorflow om het huidige systeem uit te breiden met AI. Het huidige model is in staat om een pingpongbal op een vaste hoogte te houden.

---

# Inhoudsopgave
- [Project Groep B](#project-groep-b)
- [Inhoudsopgave](#inhoudsopgave)
- [Probleemstelling](#probleemstelling)
- [Aanpak](#aanpak)
- [Resultaten](#resultaten)
  - [Belangrijkste Bevindingen](#belangrijkste-bevindingen)
- [Conclusies en Aanbevelingen](#conclusies-en-aanbevelingen)
  - [Conclusies](#conclusies)
  - [Aanbevelingen](#aanbevelingen)
- [Projectgroepleden](#projectgroepleden)
- [Software/Hardware en Tools](#softwarehardware-en-tools)
  - [Software](#software)
  - [Hardware](#hardware)
  - [Overige Tools](#overige-tools)

---

# Probleemstelling

In dit project hebben we onderzocht hoe een AI-model getraind kan worden die in staat is om een standaard PID-regelsysteem over te kunnen nemen. Om dit voor elkaar te krijgen hebben we onderzoek gedaan naar manieren om data te verzamelen die gebruikt kunnen worden voor het trainen van een AI-model.

---

# Aanpak

1. **Onderzoeksfase**: Tijdens deze fase hebben we onderzoek gedaan naar verschillende manieren om data te verzamelen.
2. **Ontwikkeling**: Tijdens deze fasen zijn we twee wegen in geslagen. We hebben een simulatie gemaakt in Unity die gebruikt kan worden om trainingsdata te genereren. 
De andere manier die we hebben ontwikkeld is het gebruiken van Behavior Cloning. Hiervoor hebben we de huidige opstelling uitgerust met de NXP FRDM-MXCN947 microcontroller. Met deze microcontroller kan de ultrasonische sensor worden uitgelezen en kan de ventilator worden aangestuurd.
3. **Testing**: Het AI-model is gevalideerd door middel van de K-Fold Cross Validatie methode. Uit deze validatie is gebleken dat het systeem een afwijking van 1.92% heeft ten opzichte van het verwachte resultaat.

---

# Resultaten

Het resultaat van het onderzoek en de implementatie is dat we een werkend AI-model hebben ontwikkeld die in staat is om een pingpongbal op een vaste hoogte, in het midden van de buis, kan houden.

## Belangrijkste Bevindingen
- Bevinding 1: De documentatie van de microcontroller is moeilijk terug te vinden en is ook niet duidelijk. 

---

# Conclusies en Aanbevelingen

## Conclusies
Het trainen van een AI-model vergt meer werk dan in eerste instantie gedacht. Het verzamelen van bruikbare data is van groot belang om een accuraat AI-model te kunnen trainen

## Aanbevelingen
- Aanbeveling 1: Het AI-model uitbreiden zodat het de pingpongbal op meerdere hoogtes kan houden.
- Aanbeveling 2: Het systeem uitbreiden zodat een gebruiker een hoogte kan aangeven waar de pingpongbal moet worden gehouden.
- Aanbeveling 3: Kijken naar een andere microcontroller. De gebruikte microcontroller heeft slechte documentatie en er zijn andere microcontrollers met betere documentatie en prestaties.

Voor een uitgebreidere uitleg, zie het adviesrapport.

---

# Projectgroepleden

| Naam | Rol / Bijdrage | Contact |
|------|----------------|---------|
| Niels Noordzij | Projectleider, Simulatie programmeur, Onderzoek data vergaren | 1006224@hr.nl |
| Ahmet Dorian | AI-model trainen & opstelling aansturen | 1023107@hr.nl |
| Dorian Lauffer | AI-Modle trainen & behuizing ontwerpen | 0984064@hr.nl |
| Thijs Sijssens | Onderzoek data vergaren, opstellingen aansturen & PCB ontwerp| 1011823@hr.nl |

---

# Software/Hardware en Tools

## Software
- **[Python 3.x](https://www.python.org/)** - Gebruikt voor het ontwikkelen van machine learning modellen
- **[TensorFlow/PyTorch](link)** - Deep learning framework voor neurale netwerken
- **[Jupyter Notebook](https://jupyter.org/)** - Voor data analyse en experimenteren
- **[VS Code](https://code.visualstudio.com/)** - Code editor voor ontwikkeling
- **[WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)** - Voor het programmeren met tensorflow op windows
- **[Unity](https://unity.com/download)** - Software waar de simulatie in is gemaakt

## Hardware
- **[FRDM-MCXN947](link)** - Development board gebruikt voor embedded implementatie
- **[Ultrasonische sensor](link)** - Standaard sensor die in de testopstelling zit.

## Overige Tools
- **[Git/GitHub](https://github.com)** - Versiebeheer en samenwerking



*Laatste update: [23-01-2026]*
