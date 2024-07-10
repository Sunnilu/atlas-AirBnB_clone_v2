#!/usr/bin/python3

from models.city import City  

class State(BaseModel):  #  State inherits from BaseModel
    # Other attributes and methods...

    @property
    def cities(self):
        # a relationship set up between State and City
        # This method returns a list of City objects associated with the current State instance
        return [city for city in self.__session.query(City).filter(City.state_id == self.id)]
