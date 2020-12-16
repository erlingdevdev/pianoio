Lets create a tool to use for music theory analysis.

Inspired by GarageBands functionality.
When you press an A chord on piano, it shows up in gb.
it also shows sheet music.

Create tool instead of using garageband because GB needs to record every time you want to read sheet that you write.


----


# create a virtual midi keyboard so i can test code without my NORD
    - C on keyboard is C pressed.
    -

# Parse midi key to note:
    - There are a total of 12 notes, 7 white 5 black.

    - analysis of keys pressed, 
        -   every key has a note on and note off, which means that every key that
        has a note on but not yet note off, is the sum of all keys pressed. 
        This functionality makes it so we can find out which chord we created.
    -   Needs a list of every chord that we want to support.

# Module for reading the chord analysis into a sheet.
    -   pygame / Qt5
    - not crucial, lets fix functionality first.





