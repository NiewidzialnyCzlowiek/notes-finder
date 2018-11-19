import cv2
from recognizeNotes import recognizeNotes
from extractPage import extractPage

def main():
    extracted, success = extractPage("./input-images/notes1.jpg")
    if success:
        cv2.imshow("extracted", extracted)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        recognizeNotes(extracted)

if __name__ == "__main__":
    main()