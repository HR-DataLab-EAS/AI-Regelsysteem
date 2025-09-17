
<div align="center">
  <img src="Archive/img/AIregelsysteem_logo.svg">
</div>

![Build Status](https://img.shields.io/badge/Python-3.10-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

**Welkom bij de repository van het HR Datalab voor het project *AI-regelsysteem*.**

Hogeschool Rotterdam biedt binnen de cursus *Digitale Systemen (DIS10)* een opstelling aan waarbij een pingpongbal op een ingestelde hoogte wordt gehouden. Deze opstelling bestaat uit een verticale buis met onderaan een ventilator. Door de luchtdruk van de ventilator wordt de bal omhoog geblazen. Met behulp van een microcontroller wordt de ventilator aangestuurd, zodat de bal op de gewenste hoogte blijft zweven.  

De regeling van de ventilatorsnelheid gebeurt momenteel met een PID-regelaar (*Proportioneel-Integrerend-Differentieel*), waarbij de afwijking tussen de gewenste en werkelijke hoogte continu wordt bijgestuurd. Hoewel deze opstelling naar behoren functioneert, is het instellen van de PID-parameters vaak een handmatig en tijdrovend proces om het systeem stabiel te laten reageren op hoogteveranderingen. Bovendien kunnen veranderingen in de omgeving (zoals temperatuur of luchtvochtigheid) de prestaties van de PID-regelaar beïnvloeden.  

De begeleidende docent heeft daarom de vraag gesteld of deze traditionele regelmethode kan worden vervangen door een benadering gebaseerd op *machine learning*. Machine learning biedt de mogelijkheid om op basis van data te leren hoe het systeem zich moet gedragen. In dit project wordt onderzocht of het mogelijk is een machine learning-model te ontwikkelen dat het gedrag van de PID-regelaar kan nabootsen of zelfs verbeteren.  
  

# Inhoudsopgave
- [Inhoudsopgave](#inhoudsopgave)
- [Projectdoelen](#projectdoelen)
- [Gebruik](#gebruik)
  - [Installatie](#installatie)
- [Resultaten](#resultaten)
  - [🧑‍🤝‍🧑 Bijdragen van Eerdere Projectgroepen](#-bijdragen-van-eerdere-projectgroepen)
- [Toekomstig Werk](#toekomstig-werk)
- [Auteurs / Credits](#auteurs--credits)
  - [Groep A](#groep-a)
- [Contributie](#contributie)
- [Licentie](#licentie)

# Projectdoelen

- ✅ Eerste AI-model gebaseerd op PID-regelaar
- ✅ PID simulatie
- ✅ Datasetverzameling
- 🔜 Hardware-integratie

# Gebruik

Deze repository is bedoelt voor studenten/docenten van het EAS datalab

## Installatie

```bash
git clone https://github.com/HR-DataLab-EAS/AI-Regelsysteem.git
cd AI-Regelsysteem
```


# Resultaten

## 🧑‍🤝‍🧑 Bijdragen van Eerdere Projectgroepen

Omdat dit project over meerdere semesters en groepen verdeeld is, hebben we een overzicht gemaakt van alle bijdragen:

| Projectgroep | Periode    | Bijdrage                                | Link/Bestanden              |
|--------------|------------|------------------------------------------|------------------------------|
| Groep A      | Q1_2025 - Q2_2025  | Eerste AI-model + datasetverzameling + Simulatie PID         | [`/docs/groepA/`](docs/groepA) |
| Groep B  (huidige)    | Q3_2025 - Q4_2025  |      | [`/docs/groepB/`](docs/groepB) |


# Toekomstig Werk

# Auteurs / Credits

## Groep A

| Naam          | Rol / Bijdrage                | Contact                |
|---------------|-------------------------------|------------------------|
| Student A     | AI-model & simulatie          | [email@example.com](mailto:email@example.com) |
| Student B     | Hardware-implementatie        | -                      |
| Student C     | Documentatie & tests          | -                      |
| Student D     | Documentatie & tests          | -                      |

# Contributie

Pull requests zijn welkom! Volg alstublieft onze [contributie-richtlijnen](CONTRIBUTING.md).

# Licentie
Dit project valt onder de MIT-licentie. Zie [LICENSE](LICENSE).

<br>

---



> ℹ️ Let op: dit project is nog in ontwikkeling.


<details>
  <summary>klik voor repository file structuur</summary>
  
  ```plaintext
ai-regelsysteem/
├── src/
├── models/
├── docs/
├── tests/
├── data/
├── results/
├── README.md
├── requirements.txt
└── LICENSE
```

</details>
