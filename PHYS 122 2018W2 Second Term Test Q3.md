---
title: Turpentine
topic: Waves
author: John Hopkinson
source: PHYS 122 2018W2 Second Term Test Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 16.5.1.1
- 16.10.1.0
- 16.10.1.1
- 16.10.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- SJ
assets:
server:
    imports: |
        import random
        import problem_bank_helpers as pbh
    generate: |
        data2 = pbh.create_data2()

        # define or load names/items/objects from server files

        # store phrases etc
        data2["params"]["vars"]["title"] = "Turpentine"

        # Randomize Variables
        Y = random.randint(1,19)

        # store the variables in the dictionary "params"
        data2["params"]["Y"] = Y
        data2["params"]["Y_appear"] = 2 * Y

        # define possible answers
        data2["params"]["part1"]["ans1"]["value"] = "Reflects almost all light hitting it since light reflects with the same phase from both surfaces and the path length difference is much less than the wavelength of the visible light."
        data2["params"]["part1"]["ans1"]["correct"] = False
        data2["params"]["part1"]["ans1"]["feedback"] = "In order to have constructive interference of reflected blue light, we need a path length difference of ($λ_{blue}$)/(2*$n_{turpentine}$) which is equal to 136 nm. No light will be reflected from this thin film since our path length is much less than the required difference(path length<<136nm)."

        data2["params"]["part1"]["ans2"]["value"] = "will appear blue since ($λ_{blue}$)/2 = $" + str(data2["params"]["Y_appear"]) + " nm$"
        data2["params"]["part1"]["ans2"]["correct"] = False
        data2["params"]["part1"]["ans2"]["feedback"] = "The correct formula for this question is ($λ_{blue}$)/(2*$n_{turpentine}$). In order to have constructive interference of reflected blue light, we need a path length difference of ($λ_{blue}$)/(2*$n_{turpentine}$)= (400nm)/(2 x 1.47)=136nm. No light will be reflected from this thin film since our path length is much less than the required difference(path length<<136nm)."

        data2["params"]["part1"]["ans3"]["value"] = "Will appear blue since ($λ_{blue}$)/(2*$n_{turpentine}$)= $" + str(data2["params"]["Y_appear"]) + " nm$ "
        data2["params"]["part1"]["ans3"]["correct"] = False
        data2["params"]["part1"]["ans3"]["feedback"] = "You have used the correct formula however the answer is (400nm)/(2 x 1.47)=136nm and not 20 nm. In order to have constructive interference of reflected blue light, we need a path length difference of ($λ_{blue}$)/(2*$n_{turpentine}$)= (400nm)/(2 x 1.47)=136nm. No light will be reflected from this thin film since our path length is much less than the required difference(path length<<136nm)."

        data2["params"]["part1"]["ans4"]["value"] = "Will look like a normal water surface since both water and turpentine are transparent."
        data2["params"]["part1"]["ans4"]["correct"] = False
        data2["params"]["part1"]["ans4"]["feedback"] = "Try again please!"

        data2["params"]["part1"]["ans5"]["value"] = "Will reflect almost no light as light reflects with different phases from each surface and the path length difference is much less than the wavelength of visible light."
        data2["params"]["part1"]["ans5"]["correct"] = True
        data2["params"]["part1"]["ans5"]["feedback"] = "Great! You got it.  In order to have constructive interference of reflected blue light, we need a path length difference of ($λ_{blue}$)/(2*$n_{turpentine}$)= (400nm)/(2 x 1.47)=136nm. No light will be reflected from this thin film since our path length is much less than the required difference(path length<<136nm)"


        # Update the data object with a new dict
        data.update(data2)
    prepare: |
        pass
    parse: |
        pass
    grade: |
        pass
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
---
# {{ params.vars.title }}

Turpentine is a liquid extracted from pine tree resin and used to remove paint from paint brushes. Being less dense than water it will float on the surface of water if you rinse it off your hands after using it.

## Part 1

A {{ params.Y }} nm thick thin film of turpentine ($n_{turpentine}=1.47$) on top of water ($n_{water}=1.33$) will:


### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.
