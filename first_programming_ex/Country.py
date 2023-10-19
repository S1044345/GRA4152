
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
        self.country = country
        self.population = population
        self.area = area
        self.density = self.population / self.area

        Country._arealist.append(self.area)
        Country._countrylist.append(self.country)
        Country._poplist.append(self.population)
        Country._denselist.append(self.density)
        Country._countrydictarea[self.country] = self.area
        Country._countrydictpop[self.country] = self.population
        Country._countrydictdense[self.country] = self.density

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
    

canada = Country("Canada",1200000,1500)
philippines = Country("Philippines",1000000,1200)
us = Country("USA",20000000,1000)


largest_area_country_list = Country.largestArea_list()
largest_area_country_dict = Country.largestArea_dict()
print(largest_area_country_list,largest_area_country_dict)

largest_pop_country_list = Country.largestPop_list()
largest_pop_country_dict = Country.largestPop_dict()
print(largest_pop_country_list,largest_pop_country_dict)

largest_dense_country_list = Country.largestDen_list()
largest_dense_country_dict = Country.largestDen_dict()
print(largest_dense_country_list,largest_dense_country_dict)