class Player:
    __table__ = 'players'
    columns = ['id', 'name', 'age', 'height', 'weight', 'shot', 'birth_place', 'birthdate', 'number', 'created_at']

    def __init__(self, kwargs):
        # make sure all of the keys match column names
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')

        # set the Player attributes
        for k, v in kwargs.items():
            setattr(self, k, v)
