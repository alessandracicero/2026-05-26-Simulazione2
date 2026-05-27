from database.DB_connect import DBConnect
from model.names import Names


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getRatings():
        cnx=DBConnect.get_connection()
        cursor= cnx.cursor(dictonary=True)
        res = []

        query = """ select distinct avg_rating
                    from ratings
                    order by avg_rating """

        cursor.execute(query)

        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getActor(r1,r2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """ select n.id, n.name, n.height, n.date_of_birth, n.known_for_movies
                    from ratings r , movie m ,role_mapping rm ,names n 
                    where r.avg_rating >= %s
                     and r.avg_rating <=%s and
                    r.movie_id = m.id and m.id =rm.movie_id
                     and rm.name_id =n.id and n.date_of_birth is not null   """

        cursor.execute(query,(r1,r2))

        for row in cursor:
            res.append(Names(**row))

        cursor.close()
        cnx.close()

        return res
    @staticmethod
    def getAllActors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """ select *
                    from names"""

        cursor.execute(query)

        for row in cursor:
            res.append(Names(**row))

        cursor.close()
        cnx.close()

        return res
    @staticmethod
    def getCollegamenti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        res = []

        query = """ select n.id,n2.id as id2, m.worlwide_gross_income as income
                    from (select n.id, n.name, n.height, n.date_of_birth, n.known_for_movies
                     from ratings r , movie m ,role_mapping rm ,names n 
                     where r.avg_rating >= 1.2 and r.avg_rating <=2.7 and
                    r.movie_id = m.id and m.id =rm.movie_id
                     and rm.name_id =n.id and n.date_of_birth is not null ) as n, role_mapping rm , role_mapping rm2 ,(select n.id, n.name, n.height, n.date_of_birth, n.known_for_movies
                    from ratings r , movie m ,role_mapping rm ,names n 
                    where r.avg_rating >= 1.2
                     and r.avg_rating <= 2.7 and
                    r.movie_id = m.id and m.id =rm.movie_id
                     and rm.name_id =n.id and n.date_of_birth is not null) as n2 ,movie m 
                    where n.id = rm.name_id and	rm.movie_id = rm2.movie_id 
                    and   rm2.name_id = n2.id and n.id>n2.id and rm2.movie_id =m.id and worlwide_gross_income is not null  """

        cursor.execute(query)

        for row in cursor:
            res.append((row["id"], row["id2"], row["income"]))

        cursor.close()
        cnx.close()

        return res
