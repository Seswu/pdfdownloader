# Project Conventions

## Technical Platform

- Programming language: Python
- Linters: pylint, flake8
- Testing: pytest
- Ci/cd: Not yet

## Collaboration

### Written Language

- Use english for internal collaboration, names in code, process descriptions and developer documentation
- Language use for user guides are client-specific

### Code Standards

- commits linted
- 4-space indentation, no tabs
- linters can be a little too opinionated at times; list of allowed deviations in the making

### Documentation Standards

Use pandoc-compatible markup formats for documentation, ie markdown, rest, emacs-org, or the like.
This will make it easier to maintain and change documentation on the fly as the software itself is modified.

For diagrams plantuml is in use, but discussion of other options is welcomed.

## Development Process

While no formally defined development process is in place, contributers are expected to follow these general outlines for development, in this order:  

1. Plan
   1. Individual Planning
      - research if needed
      - create an outline of planned changes
      - create new or adjust existing diagrams and overviews
   2. Communicate
      - ask relevant developers/maintainers for feedback
      - adjust plans accordingly
3. Do
   1. Local implemtation
   2. Local testing
   3. Local documentation
4. Check
   1. Push to development branch
   2. Get feedback
   3. Adjust accordingly
5. Act
   1. Push to testing branch
   2. Correct errors if any
   3. Synchronize with regular contributors/maintainers for push to main branch

5.3) may be changed to a more formalized pull request process in the future, but as automated testing has not been set up as yet, internal coordination is the choice du jour.