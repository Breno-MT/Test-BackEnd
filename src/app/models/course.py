from src.app import DB, MA 


class Course(DB.Model):
    __tablename__ = "course"

    id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
    name = DB.Column(DB.String(84), nullable = False)
    description = DB.Column(DB.String(84), nullable = False)
    # Colocar holder_image, por hora não sei fazer, vou estudar sobre.
    duration = DB.Column(DB.Integer, nullable = False)
    date_created = DB.Column(DB.DateTime, nullable = False)
    date_updated = DB. Column(DB.DateTime, nullable = True)

class CourseSchema(MA.Schema):
    # Adicionar nested de outras models

    class Meta:
        fields = ("id", "name", "description", "duration", "date_created", "date_updated")


course_share_schema = CourseSchema()
courses_share_schema = CourseSchema(many = True)

