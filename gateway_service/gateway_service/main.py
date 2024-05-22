from typing import Annotated, Dict

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from httpx import AsyncClient

from gateway_service.api.categories_api import router as categories_router
from gateway_service.api.identity_provider_api import router as users_router
from gateway_service.api.namespaces_api import router as namespace_router
from gateway_service.api.notes_api import router as notes_router
from gateway_service.api.statistics_api import router as statistics_router
from gateway_service.exceptions import NotFoundError, ServiceNotAvailableError, UnauthorizedError, AccessDenied

app = FastAPI()
app.include_router(categories_router, prefix='http://158.160.164.167/api/category-service/', tags=['Categories'])
app.include_router(users_router, prefix='http://158.160.164.167/api/identity-provider/', tags=['Users'])
app.include_router(namespace_router, prefix='http://158.160.164.167/api/namespace-service/', tags=['Namespaces'])
app.include_router(notes_router, prefix='http://158.160.164.167/api/notes-service/', tags=['Notes'])
app.include_router(statistics_router, prefix='http://158.160.164.167/api/statistic-service/', tags=['Statistics'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/gateway-service/login')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> RedirectResponse:
    return RedirectResponse(
        url=f'http://158.160.164.167/api/identity-provider/token?client_id=gateway',
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    )


@app.get('/api/gateway-service/code')
async def code_handler(code: str) -> Dict:
    async with AsyncClient(base_url='http://158.160.164.167/api/identity-provider/') as ac:
        response = await ac.post('/access_token', params={'code': code})
    return response.json()


# @app.exception_handler(ServiceNotAvailableError)
# async def not_available_exception_handler(request: Request, exc: ServiceNotAvailableError) -> JSONResponse:
#     return JSONResponse(
#         status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
#         content={'message': 'Notes System unavailable'},
#     )


# @app.exception_handler(NotFoundError)
# async def not_found_error_handler(request: Request, exc: NotFoundError) -> JSONResponse:
#     return JSONResponse(
#         status_code=status.HTTP_404_NOT_FOUND,
#         content=exc.content,
#     )


@app.exception_handler(UnauthorizedError)
async def unauthorized_error_handler(request: Request, exc: UnauthorizedError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=exc.details,
    )


@app.exception_handler(AccessDenied)
async def access_denied_error_handler(request: Request, exc: AccessDenied) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={'message': 'Access denied'},
    )


@app.get('/api/gateway-service/manage/health', status_code=status.HTTP_200_OK)
async def check_health() -> Dict:
    return {'Service': 'Gateway'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
