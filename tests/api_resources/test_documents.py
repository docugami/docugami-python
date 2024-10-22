# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Document
from docugami.pagination import SyncDocumentsPage, AsyncDocumentsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        document = client.documents.retrieve(
            "id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.documents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.documents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        document = client.documents.list()
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        document = client.documents.list(
            cursor="cursor",
            docset={"id": "id"},
            limit=1,
            max_pages=0,
            max_size=0,
            min_pages=0,
            min_size=0,
            name="name",
            prefix="prefix",
            samples=True,
            status="New",
        )
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        document = client.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.delete(
                "",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        document = await async_client.documents.retrieve(
            "id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.documents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.documents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        document = await async_client.documents.list()
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        document = await async_client.documents.list(
            cursor="cursor",
            docset={"id": "id"},
            limit=1,
            max_pages=0,
            max_size=0,
            min_pages=0,
            min_size=0,
            name="name",
            prefix="prefix",
            samples=True,
            status="New",
        )
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        document = await async_client.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.delete(
                "",
            )
