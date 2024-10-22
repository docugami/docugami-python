# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.types import Project
from docugami.pagination import SyncProjectsPage, AsyncProjectsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        project = client.projects.retrieve(
            "id",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.projects.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.projects.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.projects.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        project = client.projects.list()
        assert_matches_type(SyncProjectsPage[Project], project, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        project = client.projects.list(
            cursor="cursor",
            docset={"id": "id"},
            limit=1,
            name="name",
            type="TabularReport",
        )
        assert_matches_type(SyncProjectsPage[Project], project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncProjectsPage[Project], project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncProjectsPage[Project], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        project = client.projects.delete(
            "id",
        )
        assert project is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.projects.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.projects.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.projects.with_raw_response.delete(
                "",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        project = await async_client.projects.retrieve(
            "id",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.projects.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        project = await async_client.projects.list()
        assert_matches_type(AsyncProjectsPage[Project], project, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        project = await async_client.projects.list(
            cursor="cursor",
            docset={"id": "id"},
            limit=1,
            name="name",
            type="TabularReport",
        )
        assert_matches_type(AsyncProjectsPage[Project], project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncProjectsPage[Project], project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncProjectsPage[Project], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        project = await async_client.projects.delete(
            "id",
        )
        assert project is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.projects.with_raw_response.delete(
                "",
            )
