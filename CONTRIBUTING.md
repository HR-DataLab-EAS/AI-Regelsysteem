# Contributing Guide

Bedankt dat je interesse hebt om bij te dragen aan dit project! 🎉  
Met jouw hulp kunnen we het project verbeteren, uitbreiden en voor meer mensen waardevol maken.

---

## 1. Introductie
Dit project is open-source en staat open voor bijdragen van iedereen.  
Of je nu een bug vindt, een nieuwe feature wilt toevoegen of documentatie wilt verbeteren — alle bijdragen zijn welkom!

---

## 2. Hoe bij te dragen

### Issues
- Controleer altijd eerst of het probleem of de feature al bestaat in de [Issues](../../issues).
- Als je een nieuw issue opent:
  - Geef een duidelijke titel en beschrijving.
  - Voeg indien mogelijk stappen om het probleem te reproduceren toe.
  - Screenshots of logbestanden zijn welkom.

### Pull Requests
- Fork de repository en werk op een aparte branch (bijv. `feature/naam` of `fix/bug-nummer`).
- Houd PR’s klein en overzichtelijk (liever meerdere kleine PR’s dan één grote).
- Schrijf een duidelijke beschrijving van wat je hebt toegevoegd of gewijzigd.
- Verwijs naar het issue waar je PR betrekking op heeft (`Closes #123`).

---

## 3. Code Style & Guidelines
- Volg de programmeerstijl van het project.
- Gebruik consistente naming conventions.
- Indentatie: **4 spaties**.
- Voeg waar nodig documentatie en/of comments toe.
- Commit messages volgen de [Conventional Commits](https://www.conventionalcommits.org) richtlijnen:
  - `feat: nieuwe functionaliteit`
  - `fix: bug opgelost`
  - `docs: documentatie aangepast`
  - `test: nieuwe of aangepaste tests`

---

## 4. Workflow
1. Fork de repo en clone je fork:
   ```bash
   git clone https://github.com/jouw-gebruikersnaam/projectnaam.git
   ```
2. Maak een nieuwe branch voor je feature of bugfix:
   ```bash
   git checkout -b feature/naam
   ```
3. Installeer dependencies:
   ```bash
   npm install
   ```
4. Bouw het project:
   ```bash
   npm run build
   ```
5. Draai de tests om te controleren of alles werkt:
   ```bash
   npm test
   ```
6. Commit je wijzigingen met een duidelijke boodschap en push naar je fork:
   ```bash
   git add .
   git commit -m "feat: beschrijving van je wijziging"
   git push origin feature/naam
   ```
7. Open een Pull Request vanuit je branch naar de `main` branch van de originele repository.

---

## 5. Tests
- Draai altijd de tests voordat je een PR opent om te zorgen dat alles werkt.
- Tests kunnen worden uitgevoerd met:
  ```bash
  npm test
  ```
- Indien van toepassing, zorg ervoor dat de test coverage niet afneemt.
- Voeg nieuwe tests toe voor nieuwe functionaliteiten of bugfixes.

---

## 6. Issue & PR Templates
- Gebruik de [ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE) voor het aanmaken van nieuwe issues.
- Gebruik de [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE) voor het openen van PR’s.
- Zorg dat je alle relevante velden invult en duidelijke informatie geeft om het reviewproces te vergemakkelijken.

---

## 7. Code of Conduct
- Dit project volgt de richtlijnen van de [Code of Conduct](CODE_OF_CONDUCT.md).
- We verwachten dat iedereen zich respectvol en professioneel gedraagt.

---

## 8. Contact / Hulp
- Heb je vragen of hulp nodig? Stel ze gerust via de [discussies](../../discussions) of in de issues.
- Je kunt ook contact opnemen met de maintainers via de contactinformatie in het README bestand.

---

Bedankt voor je bijdrage en betrokkenheid bij dit project! Samen maken we het beter. 🎉