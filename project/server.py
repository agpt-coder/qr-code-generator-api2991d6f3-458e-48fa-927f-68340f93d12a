import logging
from contextlib import asynccontextmanager
from typing import Optional

import project.generate_qr_code_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="QR Code Generator API",
    lifespan=lifespan,
    description="Based on the information gathered from the interviews, the task involves creating an endpoint that fulfills the following requirements: - Accepts input data which can vary from URLs, text, contact information, etc. This signifies the endpoint needs to be flexible enough to encode different types of data into a QR code. - Generates a QR code image from the input data. This process will involve converting the supplied data into a format that can be encoded into a QR code image. - Allows for customization of the generated QR code. This includes adjustments to the size, color, and error correction level. Each of these customizations serves a purpose; size ensures the QR code fits within various designs, color alignment with brand guidelines, and error correction level for maintaining scannability under damage or obstruction. - Returns the QR code image in a specified format as requested by the user, for example in SVG format. This demands the system to be capable of generating and providing the QR code in multiple image formats to meet diverse user preferences or requirements. The tech stack selected for implementing this solution includes Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. This stack is suitable for creating a performant, scalable, and maintainable application capable of handling the specified functionalities efficiently.",
)


@app.post(
    "/generate", response_model=project.generate_qr_code_service.GenerateQRCodeResponse
)
async def api_post_generate_qr_code(
    data: str,
    size: Optional[int],
    color: Optional[str],
    background_color: Optional[str],
    error_correction: str,
    format: str,
) -> project.generate_qr_code_service.GenerateQRCodeResponse | Response:
    """
    Takes various input data and generates a QR code based on user customizations.
    """
    try:
        res = await project.generate_qr_code_service.generate_qr_code(
            data, size, color, background_color, error_correction, format
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
