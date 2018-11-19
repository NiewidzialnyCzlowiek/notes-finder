import cv2
from recognizeNotes import recognizeNotes
from extractPage import extractPage
def analyzeEasy(saveImages):
    directory = "./input-images/easy"
    for i in range(1,8):
        filename = "notes" + str(i)
        extracted, success = extractPage(directory, filename, saveImages)
        if success:
            recognizeNotes(extracted, directory, filename, saveImages)

def analyzeMed(saveImages):
    directory = "./input-images/med"
    for i in range(1,14):
        filename = "notes" + str(i)
        extracted, success = extractPage(directory, filename, saveImages)
        if success:
            recognizeNotes(extracted, directory, filename, saveImages)

def analyzeHard(saveImages):
    directory = "./input-images/hard"
    for i in range(1,4):
        filename = "notes" + str(i)
        extracted, success = extractPage(directory, filename, saveImages)
        if success:
            recognizeNotes(extracted, directory, filename, saveImages)

def main():
    analyzeEasy(True)
    analyzeMed(True)
    analyzeHard(True)

if __name__ == "__main__":
    main()