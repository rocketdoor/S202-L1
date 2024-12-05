class IdolDatabase:
    def __init__(self, database):
        self.db = database

    ## CREATE

    def create_idol(self, name, age, country, full_name, idol_id):
        query = "CREATE (:Idol {name: $name, age: $age, country: $country, full_name: $full_name, idol_id: $idol_id})"
        parameters = {"name": name, "age":age, "country":country, "full_name": full_name, "idol_id": idol_id}
        self.db.execute_query(query, parameters)

    def create_group(self, name, debut, group_id):
        query = "CREATE (:Group {name: $name, debut: $debut, group_id: $group_id})"
        parameters = {"name": name, "debut": debut, "group_id": group_id}
        self.db.execute_query(query, parameters)

    def create_company(self, name, company_id):
        query = "CREATE (:Company {name: $name, company_id: $company_id})"
        parameters = {"name": name, "company_id": company_id}
        self.db.execute_query(query, parameters)

    def create_show(self, name, weekday, show_id):
        query = "CREATE (:Show {name: $name, weekday: $weekday, show_id: $show_id})"
        parameters = {"name": name, "weekday": weekday, "show_id": show_id}
        self.db.execute_query(query, parameters)


    def insert_idol_group(self, idol_id, group_id):
        query = "MATCH (i:Idol {idol_id: $idol_id}) MATCH (g:Group {group_id: $group_id}) CREATE (i)-[:IS_MEMBER]->(g)"
        parameters = {"idol_id": idol_id, "group_id": group_id}
        self.db.execute_query(query, parameters)

    def insert_group_company(self, group_id, company_id):
        query = "MATCH (g:Group {group_id: $group_id}) MATCH (c:Company {company_id: $company_id})  CREATE (c)-[:MANAGES]->(g)"
        parameters = {"group_id": group_id, "company_id": company_id}
        self.db.execute_query(query, parameters)

    def insert_group_show(self, group_id, show_id):
        query = "MATCH (g:Group {group_id: $group_id}) MATCH (s:Show {show_id: $show_id})  CREATE (g)-[:PERFORMS_AT]->(s)"
        parameters = {"group_id": group_id, "show_id": show_id}
        self.db.execute_query(query, parameters)

    def insert_idol_show(self, idol_id, show_id):
        query = "MATCH (i:Idol {idol_id: $idol_id}) MATCH (s:Show {show_id: $show_id}) CREATE (i)-[:MC]->(s)"
        parameters = {"idol_id": idol_id, "show_id": show_id}
        self.db.execute_query(query, parameters)



    # READ

    def get_idol(self, idol_id):
        query = "MATCH (i:Idol{idol_id: $idol_id}) RETURN i.name AS name, i.age AS age, i.country AS country, i.full_name AS full_name"
        parameters = {"idol_id": idol_id}
        results = self.db.execute_query(query, parameters)
        name = [result["name"] for result in results]
        age = [result["age"] for result in results]
        full_name = [result["full_name"] for result in results]
        country = [result["country"] for result in results]
        return name, age, full_name, country

    def get_group(self, group_id):
        query = "MATCH (g:Group{group_id: $group_id}) RETURN g.name AS name, g.debut AS debut"
        parameters = {"group_id": group_id}
        results = self.db.execute_query(query, parameters)
        name = [result["name"] for result in results]
        debut = [result["debut"] for result in results]
        return name, debut

    def get_company(self, company_id):
        query = "MATCH (c:Company{company_id: $company_id}) RETURN c.name AS name"
        parameters = {"company_id": company_id}
        results = self.db.execute_query(query, parameters)
        name = [result["name"] for result in results]
        return name

    def get_show(self, show_id):
        query = "MATCH (s:Show{show_id: $show_id}) RETURN s.name AS name, s.weekday AS weekday"
        parameters = {"show_id": show_id}
        results = self.db.execute_query(query, parameters)
        name = [result["name"] for result in results]
        weekday = [result["weekday"] for result in results]
        return name, weekday



    # UPDATE

    def update_idol(self, old_id, new_id, new_name, new_age, new_country, new_full_name):
        query = "MATCH (i:Idol {idol_id: $old_id}) SET i.idol_id = $new_id SET i.name = $new_name SET i.age = $new_age SET i.country = $new_country SET i.full_name = $new_full_name"
        parameters = {"old_id": old_id, "new_id": new_id, "new_name": new_name, "new_age": new_age, "new_country": new_country, "new_full_name": new_full_name}
        self.db.execute_query(query, parameters)

    def update_group(self, old_id, new_id, new_name, new_debut):
        query = "MATCH (g:Group {group_id: $old_id}) SET g.group_id = $new_id SET g.name = $new_name SET g.debut = $new_debut"
        parameters = {"old_id": old_id, "new_id": new_id, "new_name": new_name, "new_debut": new_debut}
        self.db.execute_query(query, parameters)

    def update_company(self, old_id, new_id, new_name):
        query = "MATCH (c:Company {company_id: $old_id}) SET c.company_id = $new_id SET c.name = $new_name"
        parameters = {"old_id": old_id, "new_id": new_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_show(self, old_id, new_id, new_name, new_day):
        query = "MATCH (s:Show {show_id: $old_id}) SET s.show_id = $new_id SET s.name = $new_name SET s.weekday = $new_day"
        parameters = {"old_id": old_id, "new_id": new_id, "new_name": new_name, "new_day": new_day}
        self.db.execute_query(query, parameters)



    # DELETE

    def delete_idol(self,idol_id):
        query = "MATCH (i:Idol {idol_id: $idol_id}) DETACH DELETE i"
        parameters = {"idol_id": idol_id}
        self.db.execute_query(query, parameters)

    def delete_group(self, group_id):
        query = "MATCH (g:Group {group_id: $group_id}) DETACH DELETE g"
        parameters = {"group_id": group_id}
        self.db.execute_query(query, parameters)

    def delete_company(self,company_id):
        query = "MATCH (c:Company {company_id: $company_id}) DETACH DELETE c"
        parameters = {"company_id": company_id}
        self.db.execute_query(query, parameters)

    def delete_show(self,show_id):
        query = "MATCH (s:Show {show_id: $show_id}) DETACH DELETE s"
        parameters = {"show_id": show_id}
        self.db.execute_query(query, parameters)

