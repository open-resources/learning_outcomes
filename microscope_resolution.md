---
title: Microscope Resolution
topic: Waves
author: John Hopkinson
source: PHYS 112 2018W Final Q5
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 16.9.7.1
- 16.9.7.2
- 16.10.1.0
- 16.10.1.1
difficulty:
- undefined
randomization:
- 0
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- TA
assets:
server: 
    imports: |
        import problem_bank_helpers as pbh
    generate: |
        data2 = pbh.create_data2()        

        # store phrases etc
        data2["params"]["vars"]["title"] = 'Microscope Resolution'

        # define possible answers
        data2["params"]["part1"]["ans1"]["value"] = "Neutron microscope, visible light microscope, electron microscope."
        data2["params"]["part1"]["ans1"]["correct"] = False

        data2["params"]["part1"]["ans2"]["value"] = "Neutron microscope, electron microscope, visible light microscope."
        data2["params"]["part1"]["ans2"]["correct"] = True

        data2["params"]["part1"]["ans3"]["value"] = "Electron microscope, visible light microscope, neutron microscope."
        data2["params"]["part1"]["ans3"]["correct"] = False

        data2["params"]["part1"]["ans4"]["value"] = "Visible light microscope, electron microscope, neutron microscope."
        data2["params"]["part1"]["ans4"]["correct"] = False

        data2["params"]["part1"]["ans5"]["value"] = "Visible light microscope, neutron microscope, electron microscope."
        data2["params"]["part1"]["ans5"]["correct"] = False


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

We saw that diffraction limits our ability to focus waves.

## Question Text

If we could create diffraction-limited microscopes with electrons, neutrons and visible light, rank these microscopes from highest resolution to lowest resolution.
(Take $400$ nm to be the wavelength of visible light, the mass of an electron is $9.11 \times 10^{-31}$ kg, $h = 6.26 \times 10^{-34}$ Js,
the mass of a neutron is $1.67 \times 10^{-27}$ kg, and take the speed of an electron and neutron to be $9 \times 10^6$ m/s. )


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