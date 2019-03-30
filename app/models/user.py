from werkzeug.security import generate_password_hash, check_password_hash
from py2neo import Graph


class User:
    search_userid_pattern = 'MATCH (user:User{user_id:"%s"}) RETURN user.user_id, user.password'
    create_user_pattern = 'CREATE (a:User{user_id:"%s",password:"%s"}) RETURN a'

    def __init__(self, graph, user_id, password, register=False):
        self.id = user_id
        self.graph = graph
        self.register = register
        self._password = password

    def check_user(self):
        cypher = self.search_userid_pattern % self.id
        res = self.graph.run(cypher).data()
        print(res)
        return res

    def create_user(self):
        password = generate_password_hash(self._password)
        # 先要检查该id是否存在
        if not self.check_user():
            cypher = self.create_user_pattern % (self.id, password)
            res = self.graph.run(cypher).data()
            print(res)
            if res:
                return True
        else:
            return False

    @property
    def check_password(self):
        res = self.check_user()
        if res and not self.register:
            real_password = res[0]['user.password']
        else:
            raise Exception
        return check_password_hash(real_password, self._password)