from pygame.sprite import Sprite
from pygame.image import load

class Platform(Sprite):
    def __init__(self, x, y, im): #класс Platform наследует методы класса Sprite и является дочерним классом по отн. к нему
        Sprite.__init__(self)
        self.image = load(im) #отображение платформы
        self.rect = self.image.get_rect() #выделение прямоугольной области для платформы
        self.rect.x = x # соответствующаяя координата, rect добавлен, для того чтобы платформа "воспринималась" программой как прямоугольник
        self.rect.y = y
class Prize(Sprite):
    def __init__(self, x, y, im): #класс Prize наследует методы класса Sprite и является дочерним классом по отн. к нему
        Sprite.__init__(self)
        self.image = load(im) #отображение приза
        self.rect = self.image.get_rect() #выделение прямоугольной области для платформы
        self.rect.x = x # соответствующаяя координата, rect добавлен, для того чтобы платформа "воспринималась" программой как прямоугольник
        self.rect.y = y
        
# списки уровней, в которых ' ' - пустое пространство, '-' - платформа
l0 = ['----------',
      '          ',
      '          ',
      '          ',
      '          ',
      '          ',
      '          ',
      '          ',
      '     -    ',
      '----------']
l1 = ['----------',
      '   .      ',
      '  --      ',
      '  -       ',
      '  ---     ',
      ' -     -  ',
      '  -       ',
      ' -  -     ',
      '  -       ',
      '----------']
l2 = ['----------',
      '  .       ',
      '  -       ',
      '     -    ',
      '  -       ',
      '-         ',
      '   -      ',
      '     -    ',
      '  -       ',
      '----------']
l3 = ['----------',
      '  .    .  ',
      '  -    -  ',
      '   -  -   ',
      '    --    ',
      '   ----   ',
      '  -    -  ',
      '-        -',
      ' -      - ',
      '----------']
l4 = ['----------',
      '-  .      ',
      '  - -     ',
      '     -    ',
      '   -   -  ',
      '      -   ',
      '   -      ',
      ' -  - -   ',
      '    -     ',
      '----------']
l5 = ['----------',
      '        . ',
      '-     --  ',
      '     -    ',
      '-     --  ',
      '   --    -',
      '-    --   ',
      ' -      - ',
      '-         ',
      '----------']
l6 = ['----------',
      '----- ---.',
      '--------- ',
      '--- --- --',
      '----- ----',
      '  --------',
      ' -  ------',
      '-------   ',
      '     -----',
      '----------']
l7 = ['----------',
      '-- ------ ',
      '  .      -',
      '---       ',
      '  -  -    ',
      ' -     -  ',
      '     ---- ',
      '  -   -   ',
      '  -----   ',
      '----------']
l8 = ['----------',
      '    ---.- ',
      '  -       ',
      '    --  - ',
      '  -  - -  ',
      ' -        ',
      '   - -    ',
      '   -    - ',
      '      ----',
      '----------']
l9 = ['----------',
      '    .-  - ',
      '  -   -   ',
      '        - ',
      '    ---   ',
      ' -        ',
      '   - -    ',
      '        - ',
      '        --',
      '----------']
