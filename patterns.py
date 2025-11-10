# #square pattern
# r=5
# for row in range(r):
#     s=""
#     for col in range (r):
#         s+="* "
#     print(s)

# #12345 5*5 pattern
# r=5
# for row in range(1,r+1):
#     s=""
#     for col in range (1,r+1):
#      s+=str(col)+ " "
#     print(s)

# # hallow spehere type
# r=5

# for i in range (1,r+1):
#    s=""
#    for j in range(1,r+1):
#       if i==1 or i==r or j==1 or j==r:
#          s+="*"+" "
#       else:
#          s+=" "+" "
#    print(s)

# #N
# r=5
# for i in range (1,r+1):
#    s=""
#    for j in range (1,r+1):
#       if j==1 or j==r or i==j:
#          s+="*"+" "
#       else:
#          s+=" "+" "
#    print(s)

# #Z
# #N
# r=5
# for i in range (1,r+1):
#    s=""
#    for j in range (1,r+1):
#       if i==1 or i==r or i+j==r+1:
#          s+="*"+" "
#       else:
#          s+=" "+" "
#    print(s)

# #H
# r=5
# for i in range (1,r+1):
#    s=""
#    for j in range (1,r+1):
#       if j==1 or j==r or i==(r//2)+1:
#          s+="*"+" "
#       else:
#          s+=" "+" "
#    print(s)

# #H
# r=5
# for i in range (1,r+1):
#    s=""
#    for j in range (1,r+1):
#       if i==1 or i==r or j==(r//2)+1:
#          s+="*"+" "
#       else:
#          s+=" "+" "
#    print(s)





from PIL import Image

# Load and convert the image to grayscale
img = Image.open("").convert("L")

# Resize the image for pattern clarity (adjust for terminal width)
width, height = 100, 40
img = img.resize((width, height))

# Print star pattern
for y in range(height):
    for x in range(width):
        pixel = img.getpixel((x, y))
        # Invert pixel (so darker = more stars)
        if pixel < 120:
            print("★", end="")  # print a star
        elif pixel < 200:
            print("*", end="")  # print light star
        else:
            print(" ", end="")  # print space
    print()  # new line after each row

