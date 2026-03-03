
# Kravspecifikation

**Navn: Uffe Wassmann**

**Projektnavn: PDF-Downloader**

| **Introduktion**                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Kunden har efterspurgt en prototype på et værktøj til automatisk download af pdf-filer fra nettet, ud fra links til dem givet i en Excel-fil.  |
| Det ønskes at det bliver markeret om det lykkedes at downloade filen, og endvidere at allerede downloade filer ikke gen-downloades.            |
| Endvidere ønskes der en brugervenlig guide til værktøjet som alle medarbejderne kan forstå.                                                    |

| **Teknisk platform** |        |
| -------------------- | ------ |
| Kodesprog            | Python |
| Framework            | -      |

| **Funktionelle krav**                             |
| ------------------------------------------------- |
| Read Excel file                          |
| Copy file to work doc Excel file        |
| Download PDFs                          |
| Mark downloaded PDFs as such in work doc  |
| Logging                                   |
| Testing                                    |
| Software user guide in README             |

|**Andre features** |
| ------------------------------------------------- |
| Support reading work‑doc as well                                |
| Assume work‑doc has been modified by user as new input          |
| Only download un‑downloaded PDFs                                |
| Have meaningful error messages if downloads fail                |
| Set meaningful download statuses in work doc                    |

**Planlægning** |
--------------- | ------------------------------------------------------------------
Dag             | Opgave
--------------- | ------------------------------------------------------------------
       Man  2/3 | Prioritization, Requirements specification
       Ons  4/3 | Documentation of process, Scheduling project, Implementation setup
       Tor  5/3 | Accessing and manipulating excel files
       Fre  6/3 | Downloading pdfs and marking in excel working document
       Tor 12/3 | Test cases, debugging, documentation
       Fre 13/3 | Writing of user guide and presentation text
       ... ../. | Creating overview diagram for software if time permits
