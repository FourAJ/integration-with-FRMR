from sqlalchemy.orm import Session
from sqlalchemy import column


def getDatabaseObj(model, filter_name, filter_param, data, db: Session):
    obj = db.query(model).filter(column(filter_name) == filter_param).first()
    if obj:
        db.query(model).filter(column(filter_name) == filter_param).update(data)
    else:
        obj = model(**data)
        db.add(obj)
    return obj
