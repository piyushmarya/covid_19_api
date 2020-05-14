from flask_Restful import Resource

class DocumentationResource(Resource):
    def get(self):
        return """
        <h2>Basic Documentation of routes</h2>
        <p>"http://corona-covid-api.herokuapp.com/total" to get the total patients worldwide</p>.
        <p>"http://corona-covid-api.herokuapp.com/world" to get the count of all patients country wise</p>
        <p>"http://corona-covid-api.herokuapp.com/country/<name>" to get the patient count of a particular country</p>
        """
