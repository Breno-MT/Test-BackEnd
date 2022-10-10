from src.app import DB, MA 

from src.app.models.student import Student, student_share_schema
from src.app.models.course import Course, course_share_schema


class Enrollment(DB.Model):
    __tablename__ = "enrollment"

    id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
    student_id = DB.Column(DB.Integer, DB.ForeignKey(Student.id), nullable = True)
    course_id = DB.Column(DB.Integer, DB.ForeignKey(Course.id), nullable = True)
    date_enroll = DB.Column(DB.DateTime, nullable = True)
    date_close = DB.Column(DB.DateTime, nullable = True)
    score = DB.Column(DB.Integer, nullable = True)
    status = DB.Column(DB.String(84), nullable = False)
    student = DB.relationship("Student", foreign_keys=[student_id])
    course = DB.relationship("Course", foreign_keys=[course_id])



class EnrollmentSchema(MA.Schema):
    student = MA.Nested(student_share_schema)
    course = MA.Nested(course_share_schema)

    class Meta:
        fields = ("id", "student_id", "course_id", "date_enroll", "date_close", "score", "status")


enrollment_share_schema = EnrollmentSchema()
enrollments_share_schema = EnrollmentSchema(many = True)


