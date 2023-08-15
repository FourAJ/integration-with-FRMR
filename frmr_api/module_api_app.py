import uvicorn

from fastapi import FastAPI

from frmr_api.database.database import engine, Base
from frmr_api.endpoints.FRMR.person import routers as PersonRouter
from frmr_api.endpoints.FRMR.cert import routers as CertRouter
from frmr_api.endpoints.FRMR.organization import routers as OrganizationRouter
from frmr_api.endpoints.FRMR.nomination import routers as NomRouter
from frmr_api.endpoints.FRMR.qualification import routers as QualificationRouter
from frmr_api.endpoints.FRMR.ext import routers as ExtRouter
from frmr_api.endpoints.FRMR.postgraduate import routers as PostgraduateRouter
from frmr_api.endpoints.FRMR.common import routers as CommonRouter
from frmr_api.endpoints.FRMR.prof import routers as ProfRouter
from frmr_api.endpoints.FRMR.card import routers as CardRouter
from frmr_api.endpoints.FRMR.accreditation import routers as AccreditationRouter


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(PersonRouter.router)
app.include_router(CertRouter.router)
app.include_router(OrganizationRouter.router)
app.include_router(NomRouter.router)
app.include_router(QualificationRouter.router)
app.include_router(ExtRouter.router)
app.include_router(PostgraduateRouter.router)
app.include_router(CommonRouter.router)
app.include_router(ProfRouter.router)
app.include_router(CardRouter.router)
app.include_router(AccreditationRouter.router)


if __name__ == '__main__':
    uvicorn.run(app, port=8002)
