from ursina import *
from ursina.prefabs.first_person_controller import *

app = Ursina()

maze = Entity(model='new_maze',
              texture = 'brick'
              )

EditorCamera()

app.run()