# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PageListResponse", "Document"]


class Document(BaseModel):
    id: str

    download_url: str = FieldInfo(alias="downloadUrl")

    url: str


class PageListResponse(BaseModel):
    download_url: str = FieldInfo(alias="downloadUrl")

    height: int
    """The height of the source page image in pixels."""

    number: int

    url: str

    width: int
    """The width of the source page image in pixels."""

    document: Optional[Document] = None
