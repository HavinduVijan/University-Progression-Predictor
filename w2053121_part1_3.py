# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20220895    /    UOW ID:w2053121
# Date:2023/12/13

# Import graphics module and time
from graphics import *
import time

# Initialize variables for each functions
range=[0,20,40,60,80,100,120]
count1=0
count2=0
count3=0
count4=0
part_2_list=[]

# This function prompt the user for pass,defer,fail credits and check if credits are valid
def user_input():
    # Prompt for pass_credit
    while True:
        # Check pass_credit is valid input (It should be only number between range)
        try:
            global pass_credit
            pass_credit=int(input("Please Enter Your Credit At Pass : "))
            # Check if pass_credit within the range
            if pass_credit not in range:
                print("Out of Range")
                continue
        # Handle the invalid input (eg: string, special characters and etc.)
        except ValueError:
            print("Integer Required")
            continue

        # Prompt for defer_credit    
        while True:
            # Check defer_credit is valid input (It should be only number between range)
            try:
                global defer_credit
                defer_credit=int(input("Please Enter Your Credit At Defer: "))
                # Check if defer_credit within the range
                if defer_credit not in range:
                    print("Out of Range")
                    continue
            # Handle the invalid input (eg: string, special characters and etc.)
            except ValueError:
                print("Integer Required")
                continue

            # Prompt for fail_credit    
            while True:
                # Check fail_credit is valid input (It should be only number between range)
                try:
                    global fail_credit
                    fail_credit=int(input("Please Enter Your Credit At Fail : "))
                    # Check if fail_credit within the range
                    if fail_credit not in range:
                        print("Out of Range")
                        continue
                # Handle the invalid input (eg: string, special characters and etc.)
                except ValueError:
                    print("Integer Required")
                    continue
                break
            break

        # Calculate the total    
        total = pass_credit + defer_credit + fail_credit
        # Check if total is correct 
        if total != 120: 
            print("Total Incorrect")
        # All credits ara valid and total is correct
        else:
            break
    
# This function prompt the prgression outcome and append to the list       
def predits_outcome():
    print() # Print Empty line
    # Condition for progress
    if pass_credit == 120:
        print("Progress")
        # Update global count varibale
        global count1,count2,count3,count4
        count1=count1+1
        # Create temp list for store progress data
        tem_list=['Progress -',pass_credit,defer_credit,fail_credit]
        
    # Condition for module trailer   
    elif pass_credit == 100:
        print("Progress (Module Trailer)")
        # Update global count varibale
        count2=count2+1
        # Create temp list for store module trailer data
        tem_list=['Progress (Module Trailer) -',pass_credit,defer_credit,fail_credit]
    
    # Condition for exclude 
    elif fail_credit >= 80:
        print("Exclude")
        # Update global count varibale
        count4=count4+1
        # Create temp list for store exclude data
        tem_list=['Exclude -',pass_credit,defer_credit,fail_credit]

    # Condition for module retriever    
    else:
        print("Module Retriever")
        # Update global count varibale
        count3=count3+1
        # Create temp list for store module retriever data
        tem_list=['Module Retriever -',pass_credit,defer_credit,fail_credit]

    # Append temp list data to the part_2_list
    part_2_list.append(tem_list)

# This function prompt the continue and quit options
def get_progression():
        print("\nWould you like to enter another set of data?")
        time.sleep(0.5) # Sleep 0.5 for seconds
        global message
        # Prompt the continue,quit message and convert into lowercase
        message = str(input("Enter 'y' for yes or 'q' to quit and view results: ")).lower()
        print()
    

# This function prompt the part_2_list end of the code
def part_2():
    print("Part 2:","\n")
    # loop through each elements in part_2_list
    for i in part_2_list:
        print(i[0] , i[1],",",i[2],",",i[3])

# This function prompt text file data for part_3
def part_3_text_file():
    # Open the text file
    file=open("Part 3.txt","w")
    # Write data into the text file
    file.write("Part 3"+"\n\n")
    for i in part_2_list:
        file.write(f"{i[0]} {i[1]}, {i[2]}, {i[3]}\n")
    # Close the text file after saved data
    file.close()
    
# This function prompt the histogram for the user inputs           
def histogram():
    # Open the window and set bacground color
    win = GraphWin("Histogram", 730, 600)
    win.setBackground("white")

    # Draw the bottom line
    line=Line(Point(25,520),Point(705,520)).draw(win)

    # Calculate the total_outcome
    total_outcome=count1+count2+count3+count4
    # Draw heading and total_outcome
    heading_outcome_data=[(35,'Histogram Results','gray35',20,"bold"),
                        (575,f"{total_outcome} Outcomes in Total",'lightslategray',15,"bold")]

    for y,label,color,setsize,setstyle in heading_outcome_data:
        text=Text(Point(150,y),label) # Text Position
        text.draw(win) # Draw the text
        text.setTextColor(color) # Set text color
        text.setSize(setsize) # Set text size
        text.setFace("times roman") # Set font name
        text.setStyle(setstyle) # Set text style
        
    # Draw rectangles and nametags
    rectangle_data=[('Progress',color_rgb(174,248,161),125,count1,50,200),
                    ('Trailer',color_rgb(160,198,137),285,count2,210,360),
                    ('Retriever',color_rgb(167,188,119),445,count3,370,520),
                    ('Exclude',color_rgb(210,182,181),605,count4,530,680)]
    
    # Adjust bar_height according to the counts
    max_count=max(count1,count2,count3,count4)
    bar_height=10.0
    # Update the bar_height according to the below condition
    if max_count>40:
        bar_height=400/max_count

    for label,color,text_count_x,count,x1,x2 in rectangle_data:
        bar=Rectangle(Point(x1,520),Point(x2,520 - count *bar_height)) # Rectangle position
        bar.setFill(color) # Rectangle color
        bar.setOutline("lightslategray") # Set outline
        bar.draw(win) # Draw Rectangle
        text=Text(Point(text_count_x,535),label) # Text Position
        text.setStyle("bold") # Set text style
        text.setTextColor("lightslategray") # Set text color
        text.draw(win) # Draw the text
        count_text = Text(Point(text_count_x,507 - count *bar_height),f"{count}") # Count text position
        count_text.setStyle("bold") # Set count text style
        count_text.setSize(15) # Set count text size
        count_text.setTextColor("lightslategray") # Set count text color
        count_text.draw(win) # Draw the count text
       
    try:
        # Wait for user click anywhere in the window
        win.getMouse()
        win.close() # Close the window
        
    except GraphicsError: # If user close the histogram using the close botton
        print("** PLEASE CLICK ON THE WINDOW TO CLOSE THE HISTOGRAM NEXT TIME **")
        print() # Print empty line

# Calling the functions  
while True:
    user_input()
    predits_outcome()
    get_progression()

    while message not in ['y','q']:
        print("Invalid Input")
        get_progression()

    if message == 'y':
        continue
        
    elif message == 'q':
        histogram()
        part_2()
        part_3_text_file()
        break
    
# End of the program
