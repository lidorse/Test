class Shape:
    def __init__(self,area,hekef):
        self.__area = area
        self.__hekef = hekef

    def __str__(self):
        return f'The class Shape returns {self.__area} and {self.__hekef}'

    def __repr__(self):
        return f'Shape{self.__area,self.__hekef}'

    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self,value):
        if value > 0:
            self.__area = value

    @property
    def hekef(self):
        return self.__hekef
    @hekef.setter
    def hekef(self,value):
        if value > 0:
            self.__hekef = value
