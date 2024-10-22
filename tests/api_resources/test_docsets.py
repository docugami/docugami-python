# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Docset
from docugami.pagination import SyncDocsetsPage, AsyncDocsetsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocsets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Docugami) -> None:
        docset = client.docsets.create(
            name="Loss Runs",
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Docugami) -> None:
        docset = client.docsets.create(
            name="Loss Runs",
            documents=["bn0px5iaym7z", "bn0px5iaym7z", "bn0px5iaym7z"],
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Docugami) -> None:
        response = client.docsets.with_raw_response.create(
            name="Loss Runs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = response.parse()
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Docugami) -> None:
        with client.docsets.with_streaming_response.create(
            name="Loss Runs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = response.parse()
            assert_matches_type(Docset, docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        docset = client.docsets.retrieve(
            "id",
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.docsets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = response.parse()
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.docsets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = response.parse()
            assert_matches_type(Docset, docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.docsets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        docset = client.docsets.list()
        assert_matches_type(SyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        docset = client.docsets.list(
            cursor="cursor",
            limit=1,
            max_documents=0,
            min_documents=0,
            name="name",
            samples=True,
        )
        assert_matches_type(SyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.docsets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = response.parse()
        assert_matches_type(SyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.docsets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = response.parse()
            assert_matches_type(SyncDocsetsPage[Docset], docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        docset = client.docsets.delete(
            "id",
        )
        assert docset is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.docsets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = response.parse()
        assert docset is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.docsets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = response.parse()
            assert docset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.docsets.with_raw_response.delete(
                "",
            )


class TestAsyncDocsets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.create(
            name="Loss Runs",
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.create(
            name="Loss Runs",
            documents=["bn0px5iaym7z", "bn0px5iaym7z", "bn0px5iaym7z"],
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.with_raw_response.create(
            name="Loss Runs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = await response.parse()
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.with_streaming_response.create(
            name="Loss Runs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = await response.parse()
            assert_matches_type(Docset, docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.retrieve(
            "id",
        )
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = await response.parse()
        assert_matches_type(Docset, docset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = await response.parse()
            assert_matches_type(Docset, docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.docsets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.list()
        assert_matches_type(AsyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.list(
            cursor="cursor",
            limit=1,
            max_documents=0,
            min_documents=0,
            name="name",
            samples=True,
        )
        assert_matches_type(AsyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = await response.parse()
        assert_matches_type(AsyncDocsetsPage[Docset], docset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = await response.parse()
            assert_matches_type(AsyncDocsetsPage[Docset], docset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        docset = await async_client.docsets.delete(
            "id",
        )
        assert docset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.docsets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docset = await response.parse()
        assert docset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.docsets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docset = await response.parse()
            assert docset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.docsets.with_raw_response.delete(
                "",
            )
