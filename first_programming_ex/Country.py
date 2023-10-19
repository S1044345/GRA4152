
# Creates a class Country that stores the name of a country, its populations, and its area.
# This will have three parameters: country, population, and area

class Country:
    _countrylist = []
    _arealist = []
    _poplist = []
    _denselist = []
    _countrydictarea = {}
    _countrydictpop = {}
    _countrydictdense = {}
    

    #Constructs a country class with three parameters.
    def __init__(self, country, population, area):
        self._country = country
        self._population = population
        self._area = area
        self._density = self._population / self._area

        Country._arealist.append(self._area)
        Country._countrylist.append(self._country)
        Country._poplist.append(self._population)
        Country._denselist.append(self._density)
        Country._countrydictarea[self._country] = self._area
        Country._countrydictpop[self._country] = self._population
        Country._countrydictdense[self._country] = self._density

    #a class method that will find the country with the largest area in a list
    @classmethod
    def largestArea_list (cls):
        _zipped = zip(cls._countrylist,cls._arealist)
        return max(_zipped, key = lambda x: x[1])
    
    #a class method that will find the country with the largest area in a dictionary
    @classmethod
    def largestArea_dict (cls):
        return max(cls._countrydictarea, key = lambda x: cls._countrydictarea[x])
    
    #a class method that will find the country with the largest population in a list
    @classmethod
    def largestPop_list (cls):
        _zipped = zip(cls._countrylist,cls._poplist)
        return max(_zipped, key = lambda x: x[1])
    
    #a class method that will find the country with the largest population in a dictionary
    @classmethod
    def largestPop_dict (cls):
        return max(cls._countrydictpop, key = lambda x: cls._countrydictpop[x])
    
    #a class method that will find the country with the largest density in a list
    @classmethod
    def largestDen_list (cls):
        _zipped = zip(cls._countrylist,cls._denselist)
        return max(_zipped, key = lambda x: x[1])
    
    #a class method that will find the country with the largest density in a dictionary
    @classmethod
    def largestDen_dict (cls):
        return max(cls._countrydictdense, key = lambda x: cls._countrydictdense[x])
    