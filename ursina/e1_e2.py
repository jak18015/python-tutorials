from ursina import *

def update():
    first_entity.rotation_y += 50 * time.dt
    
    first_entity.position += first_entity.forward * time.dt


app = Ursina()

first_entity = Entity(model = 'cube',
                      color = color.red,
                      texture = 'brick',
                      position = Vec3(0,0,0),
                      scale = Vec3(1,1,1)
                      )

second_entity = Entity(parent = first_entity,
                       model = 'sphere',
                       position = Vec3(1,1,1)
                       )

EditorCamera()

app.run() # this has to be at the end of the code, as this will start the game