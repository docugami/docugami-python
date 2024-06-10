# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Webhook
from docugami.pagination import SyncWebhooksPage, AsyncWebhooksPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Docugami) -> None:
        webhook = client.webhooks.create(
            target="Project",
            url="https://example.com/docugami-callback",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Docugami) -> None:
        webhook = client.webhooks.create(
            target="Project",
            url="https://example.com/docugami-callback",
            events=["Documents.Create", "Documents.Delete", "Docset.Document.Add"],
            secret="string",
            target_id="0gjiwhvpeqcg",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Docugami) -> None:
        response = client.webhooks.with_raw_response.create(
            target="Project",
            url="https://example.com/docugami-callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Docugami) -> None:
        with client.webhooks.with_streaming_response.create(
            target="Project",
            url="https://example.com/docugami-callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        webhook = client.webhooks.retrieve(
            "string",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(SyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        webhook = client.webhooks.list(
            cursor="string",
            limit=1,
            target="Project",
            target_id="0gjiwhvpeqcg",
        )
        assert_matches_type(SyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncWebhooksPage[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        webhook = client.webhooks.delete(
            "string",
        )
        assert webhook is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.webhooks.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.webhooks.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.create(
            target="Project",
            url="https://example.com/docugami-callback",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.create(
            target="Project",
            url="https://example.com/docugami-callback",
            events=["Documents.Create", "Documents.Delete", "Docset.Document.Add"],
            secret="string",
            target_id="0gjiwhvpeqcg",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDocugami) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            target="Project",
            url="https://example.com/docugami-callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDocugami) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            target="Project",
            url="https://example.com/docugami-callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.retrieve(
            "string",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(AsyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.list(
            cursor="string",
            limit=1,
            target="Project",
            target_id="0gjiwhvpeqcg",
        )
        assert_matches_type(AsyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncWebhooksPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncWebhooksPage[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        webhook = await async_client.webhooks.delete(
            "string",
        )
        assert webhook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )
