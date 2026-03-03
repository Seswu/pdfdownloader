---
marp: true
theme: default
---

# PDF-Downloader
###### Mitigating rebellions in your company office

## Process Summary

1. Make a plan
2. Have everything go well
3. Win

-------------------------------------

## Requirements and Technical Platfrom

The client is calling for a prototype, presumably to manage risks in terms of cost, while willing to explore the option of further projects later.  
We'll want to produce a good, low-cost solution that fulfills their needs.  
For a prototype, we should avoid bells and whistles, but have an eye towards making another version later with more features or better interface.  

I am choosing Python for this project.
1. It is often used for web scraping projects and has well-known libraries for this purpose
2. I have used it with Excel files before
3. Textual might serve for a better interface than pure console
4. Alternativly, this prototype might serve as core backend for a later-developed frontend

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Prioritization

| Phase                  | Task                                                            | Effect | Circumst.         | Risk                    | Mitigation                                      | PP |
| ---------------------- | --------------------------------------------------------------- | ------ | ----------------- | ----------------------- | ----------------------------------------------- | -- |
| Planning               | Prioritize tasks in project                                     | –      | –                 | –                       | –                                               | 3  |
|                        | Write software requirements specification                       | –      | –                 | –                       | –                                               | 1  |
|                        | Document process for presentation                               | –      | –                 | –                       | –                                               | 1  |
|                        | Schedule project                                                | –      | –                 | –                       | –                                               | 2  |
| MVP                    | Read Excel file                                                 | Urgent | –                 | –                       | AI suggestion                                   | 2  |
|                        | Copy file to work doc Excel file                                | Urgent | –                 | –                       | –                                               | 2  |
|                        | Download PDFs                                                   | Urgent | No exp scraping   | More work than expected | –                                               | 2  |
|                        | Mark downloaded PDFs as such in work doc                        | Urgent | –                 | –                       | –                                               | 3  |
|                        | Logging                                                         | Solid  | Recent exp        | –                       | –                                               | 2  |
|                        | Testing                                                         | Solid  | Recent exp        | –                       | –                                               | 2  |
|                        | Software user guide in README                                   | Urgent | –                 | –                       | –                                               | 2  |
| Possible Nice‑to‑haves | Support reading work‑doc as well                                | –      | –                 | –                       | –                                               | 1  |
|                        | Assume work‑doc has been modified by user as new input          | –      | –                 | –                       | –                                               | 1  |
|                        | Only download un‑downloaded PDFs                                | –      | –                 | –                       | –                                               | 1  |
|                        | Have meaningful error messages if downloads fail                | Solid  | –                 | –                       | –                                               | 2  |
|                        | Set meaningful download statuses in work doc                    | Solid  | –                 | –                       | –                                               | 1  |
| Extended Nice‑to‑haves | Refactor script to present interface through Textual            | –      | No exp w/ Textual | Textual not good choice | Ignored; just one option                        | 8  |
|                        | Refactor script to support backend use through standardized API | Big    | Need to research  | Extensive work needed   | Ignored; still good prep for possible extension | 13 |

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Schedule

  Date   | Activity
-------- | ------------------------------------------------------------------
Mon  2/3 | Prioritization, Requirements specification
Wed  4/3 | Documentation of process, Scheduling project, Implementation setup
Thu  5/3 | Accessing and manipulating excel files
Fri  6/3 | Downloading pdfs and marking in excel working document
Thu 12/3 | Test cases, debugging, documentation
Fri 13/3 | Writing of user guide and presentation text
... ../. | Creating overview diagram for software if time permits

-------------------------------------

## Process

### Summary
       
-------------------------------------

## Process

### Tasks completed

  Date   | Activity
-------- | ---------
