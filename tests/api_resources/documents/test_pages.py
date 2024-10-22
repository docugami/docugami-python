# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from docugami.pagination import SyncPagesPage, AsyncPagesPage
from docugami.types.documents import PageListResponse, PageRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        page = client.documents.pages.retrieve(
            page_number=0,
            id="id",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.documents.pages.with_raw_response.retrieve(
            page_number=0,
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.documents.pages.with_streaming_response.retrieve(
            page_number=0,
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.pages.with_raw_response.retrieve(
                page_number=0,
                id="",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        page = client.documents.pages.list(
            "id",
        )
        assert_matches_type(SyncPagesPage[PageListResponse], page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.documents.pages.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(SyncPagesPage[PageListResponse], page, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.documents.pages.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(SyncPagesPage[PageListResponse], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.pages.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        page = client.documents.pages.download(
            page_number=0,
            id="id",
        )
        assert page.is_closed
        assert page.json() == {"foo": "bar"}
        assert cast(Any, page.is_closed) is True
        assert isinstance(page, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        page = client.documents.pages.with_raw_response.download(
            page_number=0,
            id="id",
        )

        assert page.is_closed is True
        assert page.http_request.headers.get("X-Stainless-Lang") == "python"
        assert page.json() == {"foo": "bar"}
        assert isinstance(page, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.documents.pages.with_streaming_response.download(
            page_number=0,
            id="id",
        ) as page:
            assert not page.is_closed
            assert page.http_request.headers.get("X-Stainless-Lang") == "python"

            assert page.json() == {"foo": "bar"}
            assert cast(Any, page.is_closed) is True
            assert isinstance(page, StreamedBinaryAPIResponse)

        assert cast(Any, page.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.pages.with_raw_response.download(
                page_number=0,
                id="",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        page = await async_client.documents.pages.retrieve(
            page_number=0,
            id="id",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.documents.pages.with_raw_response.retrieve(
            page_number=0,
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.documents.pages.with_streaming_response.retrieve(
            page_number=0,
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.pages.with_raw_response.retrieve(
                page_number=0,
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        page = await async_client.documents.pages.list(
            "id",
        )
        assert_matches_type(AsyncPagesPage[PageListResponse], page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.documents.pages.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(AsyncPagesPage[PageListResponse], page, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.documents.pages.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(AsyncPagesPage[PageListResponse], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.pages.with_raw_response.list(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        page = await async_client.documents.pages.download(
            page_number=0,
            id="id",
        )
        assert page.is_closed
        assert await page.json() == {"foo": "bar"}
        assert cast(Any, page.is_closed) is True
        assert isinstance(page, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        page = await async_client.documents.pages.with_raw_response.download(
            page_number=0,
            id="id",
        )

        assert page.is_closed is True
        assert page.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await page.json() == {"foo": "bar"}
        assert isinstance(page, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/id/pages/0/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.documents.pages.with_streaming_response.download(
            page_number=0,
            id="id",
        ) as page:
            assert not page.is_closed
            assert page.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await page.json() == {"foo": "bar"}
            assert cast(Any, page.is_closed) is True
            assert isinstance(page, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, page.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.pages.with_raw_response.download(
                page_number=0,
                id="",
            )
