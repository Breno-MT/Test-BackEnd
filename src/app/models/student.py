from src.app import DB, MA 


class Student(DB.Model):
    __tablename__ = "student"

    id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
    name = DB.Column(DB.String(84), nullable = False)
    nicknamme = DB.Column(DB.String(84), nullable = True)
    phone = DB.Column(DB.String(84), nullable = False)
    # Questão de imagem da column "avatar", preciso estudar sobre
    date_created = DB.Column(DB.DateTime, nullable = False)
    date_updated = DB.Column(DB.DateTime, nullable = True)


class StudentSchema(MA.Schema):
    # Colocar suas nested aqui

    class Meta:
        fields = ("id", "name", "nickname", "phone", "date_created", "date_updated")


student_share_schema = StudentSchema()
students_share_schema = StudentSchema(many = True)
