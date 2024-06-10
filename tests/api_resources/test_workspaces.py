# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Workspace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Docugami) -> None:
        workspace = client.workspaces.get()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Docugami) -> None:
        response = client.workspaces.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Docugami) -> None:
        with client.workspaces.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncDocugami) -> None:
        workspace = await async_client.workspaces.get()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncDocugami) -> None:
        response = await async_client.workspaces.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncDocugami) -> None:
        async with async_client.workspaces.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True
