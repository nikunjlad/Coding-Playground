import cv2, sys


def main(file):
    cap = cv2.VideoCapture(file)

    try:
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                cv2.namedWindow("image", cv2.WINDOW_OPENGL)
                cv2.imshow("image", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()

        cv2.destroyAllWindows()
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    files = "/Users/nikunjlad/Github/Coding-Playground/practice/image/walter.mp4"
    main(files)
