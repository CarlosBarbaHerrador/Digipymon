import random
class ListaNombres:
    def __init__(self):
        self.lista_nombre_digipymon = ["Antoniopymon", "Paupymon", "Estebanpymon", "Alexpymon", "Becapymon", "Charpymon", "Bulbapymon", "Squirtlepymon", "Pikapymon", "Jigglypuffpymon", "Geodudepymon", "Eeveepymon", "Snorlaxpymon", "Psyduckpymon", "Gengarpymon", "Lucariopymon", "Mewtwopymon", "Torchicpymon", "Mudkipymon", "Pipluppymon", "Chimcharpymon", "Turtwigpymon", "Treeckopymon", "Torchpymon", "Mudpymon", "Leafeonpymon", "Glaceonpymon", "Vaporeonpymon", "Jolteonpymon", "Flareonpymon", "Sylveonpymon", "Espeopymon", "Umbreopymon", "Jolteopymon", "Glacpymon", "Flareopymon", "Sylveopymon", "Espypymon", "Umbrepymon", "Joltapymon", "Glacipymon", "Flarepymon", "Sylveepymon", "Espypymon", "Umbreonpymon", "Garchompymon", "Rayquazapymon", "Kyogrepymon", "Groudopymon", "Dialgapymon"]
        self.lista_nombre_entrenador = [
            "Walter White", "Tony Stark", "Dexter Morgan", "Daenerys Targaryen", "Michael Scott", "Buffy Summers",
            "Sherlock Holmes", "Eleven Byers", "Jack Sparrow", "Leia Organa", "Bruce Wayne", "Rick Grimes",
            "Hermione Granger", "Jon Snow", "Ellen Ripley", "Frodo Baggins", "Luke Skywalker", "Albus Dumbledore",
            "Carrie Bradshaw", "Lisbeth Salander", "Peter Parker", "Katniss Everdeen", "Rick Sanchez",
            "Marty McFly", "Jesse Pinkman", "Cersei Lannister", "Dr. Strange", "Sarah Connor", "Indiana Jones",
            "Negan Smith", "Sansa Stark", "Ellen Ripley", "Maggie Greene", "Tony Stark", "Arya Stark",
            "James Bond", "Holly Golightly", "Gandalf Grey", "Princess Leia", "Hannibal Lecter", "Clarice Starling",
            "Jack Sparrow", "Bella Swan", "Harvey Specter", "Cersei Lannister", "Doctor Who", "Wendy Torrance",
            "Jim Halpert", "Lucy Ricardo", "Danny Zuko", "Nancy Wheeler", "Tyrion Lannister", "Juno MacGuff",
            "Sheldon Cooper", "Bruce Wayne", "Jack Dawson", "Skyler White", "Juno MacGuff", "Maggie Greene",
            "Ted Mosby", "Olivia Pope", "Gandalf Grey", "Rose DeWitt Bukater", "Mike Ross", "Holly Golightly",
            "Indiana Jones", "Jon Snow", "Bruce Wayne", "Eleven Byers", "Marty McFly", "Daenerys Targaryen",
            "Phil Dunphy", "Rose DeWitt Bukater"]


    
    def obtener_nombre_digipymon(self):
        return random.choice(self.lista_nombre_digipymon)
    
    def obtener_nombre_entrenador(self):
        return random.choice(self.lista_nombre_entrenador)