// Swift Collections: Arrays

// make a variable array of Strings
var musicalModes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydia", "Minor"]

// make a constant arry of ints
let speedLimits = [15, 25, 30, 35, 45, 55, 70, 75, ]

// what's at index 0?
let initialMode = musicalModes[0]

// Change the string at index 5
musicalModes[5] = "Aeolian"

// add a new element
musicalModes.append("Locrian")

// add it again...
musicalModes.append("Locrian")

// remove an element
let theRemovedElement = musicalModes.removeLast()
