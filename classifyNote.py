def classifyNote(value):
    notes = {
        0: "D",
        0.5: "E",
        1: "F",
        1.5: "G",
        2: "A",
        2.5: "B",
        3: "C",
        3.5: "D",
        4: "E",
        4.5: "F",
        5: "G",
        5.5: "A"
    }
    return notes.get(value, "Invalid note")