from os import name
from orm import Database
from models import * 

if __name__ == "__main__":
    Database.create_database()
    with Database.session() as session:
        sonek = session.query(Jitel).filter(Jitel.id == 1).one()
        donek = session.query(Jitel).filter(Jitel.id == 2).one()

        print(*[x.address for x in session.query(House).all()])



        sonek.name = 'Троян Александр Васильевич'
        donek.name = 'Матюшев Данила Сергеевич'
        
        # sonek = Jitel(id=1, name='Сонек')
        # donek = Jitel(id=2, name='Донек')

        # peleleta = House(id=1,address="Перетела")
        # fedoseeva = House(id=2, address="Федосеева")

        # sonek.house = peleleta
        # donek.house = fedoseeva

        sonek.house_id = 1
        donek.house_id = 2
        # session.add(sonek)
        # session.add(donek)

        session.commit()

