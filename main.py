import cv2

def main():
    from extractPage import extractPage
    extracted = extractPage("./input-images/notes1.jpeg")
    cv2.imshow("extracted", extracted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()