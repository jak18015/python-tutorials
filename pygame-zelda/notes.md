# Handling collisions in PyGame
1. Apply horizontal movement
2. Check horizontal (x) collisions
3. Apply vertical movement
4. Check for vertical (y) collisions

# Creating the camera
Both a camera and overlap can be achieved by customizing a group

The main purpose of a group is to:
1. Store and draw sprites
2. call the update method

But you can add methods or change how gruops work (we will create a custom draw method for example)

What a sprite group does
1. group.sprites
2. draw(surface)
3. for sprite in sprites():
    sprite.update

# how camera works
we draw the image in the rect of the sprite, but we don't have to
we can add an offset to the rect of the sprite, which gives us control of where it's drawn

essentially we give offset of the world to the player, but makes more sense in code?

# Adding overlap
currently the hitbox is the rectangle around the sprite, but we want it to be smaller than the rect to add some depth through overlap