# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docugami import Docugami, AsyncDocugami
from tests.utils import assert_matches_type
from docugami.pagination import SyncArtifactsPage, AsyncArtifactsPage
from docugami.types.projects import Artifact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Docugami) -> None:
        artifact = client.projects.artifacts.retrieve(
            "string",
            project_id="string",
            version="1",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Docugami) -> None:
        response = client.projects.artifacts.with_raw_response.retrieve(
            "string",
            project_id="string",
            version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Docugami) -> None:
        with client.projects.artifacts.with_streaming_response.retrieve(
            "string",
            project_id="string",
            version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.artifacts.with_raw_response.retrieve(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.projects.artifacts.with_raw_response.retrieve(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.projects.artifacts.with_raw_response.retrieve(
                "",
                project_id="string",
                version="1",
            )

    @parametrize
    def test_method_list(self, client: Docugami) -> None:
        artifact = client.projects.artifacts.list(
            "1",
            project_id="string",
        )
        assert_matches_type(SyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Docugami) -> None:
        artifact = client.projects.artifacts.list(
            "1",
            project_id="string",
            cursor="string",
            document={"id": "string"},
            is_read_only=True,
            limit=1,
            max_size=0,
            min_size=0,
            name="string",
        )
        assert_matches_type(SyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Docugami) -> None:
        response = client.projects.artifacts.with_raw_response.list(
            "1",
            project_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(SyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Docugami) -> None:
        with client.projects.artifacts.with_streaming_response.list(
            "1",
            project_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(SyncArtifactsPage[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.artifacts.with_raw_response.list(
                "1",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.projects.artifacts.with_raw_response.list(
                "",
                project_id="string",
            )

    @parametrize
    def test_method_delete(self, client: Docugami) -> None:
        artifact = client.projects.artifacts.delete(
            "string",
            project_id="string",
            version="1",
        )
        assert artifact is None

    @parametrize
    def test_raw_response_delete(self, client: Docugami) -> None:
        response = client.projects.artifacts.with_raw_response.delete(
            "string",
            project_id="string",
            version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert artifact is None

    @parametrize
    def test_streaming_response_delete(self, client: Docugami) -> None:
        with client.projects.artifacts.with_streaming_response.delete(
            "string",
            project_id="string",
            version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert artifact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.artifacts.with_raw_response.delete(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.projects.artifacts.with_raw_response.delete(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.projects.artifacts.with_raw_response.delete(
                "",
                project_id="string",
                version="1",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocugami) -> None:
        artifact = await async_client.projects.artifacts.retrieve(
            "string",
            project_id="string",
            version="1",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.artifacts.with_raw_response.retrieve(
            "string",
            project_id="string",
            version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.artifacts.with_streaming_response.retrieve(
            "string",
            project_id="string",
            version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.artifacts.with_raw_response.retrieve(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.projects.artifacts.with_raw_response.retrieve(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.projects.artifacts.with_raw_response.retrieve(
                "",
                project_id="string",
                version="1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDocugami) -> None:
        artifact = await async_client.projects.artifacts.list(
            "1",
            project_id="string",
        )
        assert_matches_type(AsyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocugami) -> None:
        artifact = await async_client.projects.artifacts.list(
            "1",
            project_id="string",
            cursor="string",
            document={"id": "string"},
            is_read_only=True,
            limit=1,
            max_size=0,
            min_size=0,
            name="string",
        )
        assert_matches_type(AsyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.artifacts.with_raw_response.list(
            "1",
            project_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(AsyncArtifactsPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.artifacts.with_streaming_response.list(
            "1",
            project_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(AsyncArtifactsPage[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.artifacts.with_raw_response.list(
                "1",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.projects.artifacts.with_raw_response.list(
                "",
                project_id="string",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDocugami) -> None:
        artifact = await async_client.projects.artifacts.delete(
            "string",
            project_id="string",
            version="1",
        )
        assert artifact is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.artifacts.with_raw_response.delete(
            "string",
            project_id="string",
            version="1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert artifact is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.artifacts.with_streaming_response.delete(
            "string",
            project_id="string",
            version="1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert artifact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.artifacts.with_raw_response.delete(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.projects.artifacts.with_raw_response.delete(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.projects.artifacts.with_raw_response.delete(
                "",
                project_id="string",
                version="1",
            )
