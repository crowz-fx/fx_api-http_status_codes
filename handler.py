from flask import abort
from sqlalchemy import Table
from server import Session, generate_new_session_connector, marsh, Base, post_to_analytics

class StatusCode(Base):
    __tablename__ = "status_codes"
    __table_args__ = { "autoload" : True }

class StatusCodeSchema(marsh.ModelSchema):
    class Meta:
        model = StatusCode
        sqla_session = Session

def return_one_code(code):
    status = generate_new_session_connector().query(StatusCode).filter(StatusCode.code == code).one_or_none()

    if status is not None:
        post_to_analytics("/code/{code}".format(code = code))
        status_schema = StatusCodeSchema()
        return status_schema.dump(status)
    else:
        post_to_analytics("/code/error")
        abort(404, "HTTP Status code for [{status_code}] was not found!".format(status_code = code))

def return_all_codes():
    post_to_analytics("/all")
    codes = generate_new_session_connector().query(StatusCode).order_by(StatusCode.code).all()
    status_schema = StatusCodeSchema(many = True)
    return status_schema.dump(codes)