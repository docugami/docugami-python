# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Docset, Document
from docugami.pagination import SyncDocumentsPage, AsyncDocumentsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        document = client.docsets.documents.retrieve(
            "string",
            docset_id="string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.docsets.documents.with_raw_response.retrieve(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.docsets.documents.with_streaming_response.retrieve(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            client.docsets.documents.with_raw_response.retrieve(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.docsets.documents.with_raw_response.retrieve(
                "",
                docset_id="string",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        document = client.docsets.documents.list(
            "string",
        )
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        document = client.docsets.documents.list(
            "string",
            cursor="string",
            limit=1,
            max_pages=0,
            max_size=0,
            min_pages=0,
            min_size=0,
            prefix="string",
            status="Ready",
        )
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.docsets.documents.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.docsets.documents.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncDocumentsPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.docsets.documents.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        document = client.docsets.documents.delete(
            "string",
            docset_id="string",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.docsets.documents.with_raw_response.delete(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.docsets.documents.with_streaming_response.delete(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            client.docsets.documents.with_raw_response.delete(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.docsets.documents.with_raw_response.delete(
                "",
                docset_id="string",
            )

    @parametrize
    def test_method_add(self, client: Docugami) -> None:
        document = client.docsets.documents.add(
            "string",
            docset_id="string",
        )
        assert_matches_type(Docset, document, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Docugami) -> None:
        response = client.docsets.documents.with_raw_response.add(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Docset, document, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Docugami) -> None:
        with client.docsets.documents.with_streaming_response.add(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Docset, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            client.docsets.documents.with_raw_response.add(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.docsets.documents.with_raw_response.add(
                "",
                docset_id="string",
            )

    @parametrize
    def test_method_dgml(self, client: Docugami) -> None:
        document = client.docsets.documents.dgml(
            "string",
            docset_id="string",
        )
        assert_matches_type(str, document, path=["response"])

    @parametrize
    def test_raw_response_dgml(self, client: Docugami) -> None:
        response = client.docsets.documents.with_raw_response.dgml(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(str, document, path=["response"])

    @parametrize
    def test_streaming_response_dgml(self, client: Docugami) -> None:
        with client.docsets.documents.with_streaming_response.dgml(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(str, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dgml(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            client.docsets.documents.with_raw_response.dgml(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.docsets.documents.with_raw_response.dgml(
                "",
                docset_id="string",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.retrieve(
            "string",
            docset_id="string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.documents.with_raw_response.retrieve(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.documents.with_streaming_response.retrieve(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.retrieve(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.retrieve(
                "",
                docset_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.list(
            "string",
        )
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.list(
            "string",
            cursor="string",
            limit=1,
            max_pages=0,
            max_size=0,
            min_pages=0,
            min_size=0,
            prefix="string",
            status="Ready",
        )
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.documents.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.documents.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncDocumentsPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.docsets.documents.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.delete(
            "string",
            docset_id="string",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.documents.with_raw_response.delete(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.documents.with_streaming_response.delete(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.delete(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.delete(
                "",
                docset_id="string",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.add(
            "string",
            docset_id="string",
        )
        assert_matches_type(Docset, document, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.documents.with_raw_response.add(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Docset, document, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.documents.with_streaming_response.add(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Docset, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.add(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.add(
                "",
                docset_id="string",
            )

    @parametrize
    async def test_method_dgml(self, async_client: AsyncDocugami) -> None:
        document = await async_client.docsets.documents.dgml(
            "string",
            docset_id="string",
        )
        assert_matches_type(str, document, path=["response"])

    @parametrize
    async def test_raw_response_dgml(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.documents.with_raw_response.dgml(
            "string",
            docset_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(str, document, path=["response"])

    @parametrize
    async def test_streaming_response_dgml(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.documents.with_streaming_response.dgml(
            "string",
            docset_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(str, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dgml(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `docset_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.dgml(
                "string",
                docset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.docsets.documents.with_raw_response.dgml(
                "",
                docset_id="string",
            )
