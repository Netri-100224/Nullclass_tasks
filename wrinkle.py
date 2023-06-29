import cv2

# Load the input image
img = cv2.imread(r'D:\Bollywood Actor Images\naseeruddin_shah\61ff1e4229.jpg')
#img = cv2.resize(img,(421,612))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection to the image
edges = cv2.Canny(blur, 10, 100)

# Apply thresholding to the image
ret, thresh = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Keep count of the number of contours that meet the wrinkle criteria
wrinkle_count = 0

# Loop through each contour and draw a rectangle around it if it meets certain criteria
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Check if the contour is big enough and has a certain aspect ratio to be considered a wrinkle
    if w > 10 and h > 10 and w < 50 and h < 20 and w/h > 3:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        wrinkle_count += 1

# Print whether wrinkles were detected or not based on the number of contours that meet the wrinkle criteria
if wrinkle_count > 0:
   cv2.putText(img, "Wrinkle found", (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
else:
    cv2.putText(img, "No Wrinkle found", (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

# Display the output image
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()