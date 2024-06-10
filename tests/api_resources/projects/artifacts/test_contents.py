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
from docugami.types.projects import Artifact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        content = client.projects.artifacts.contents.download(
            "string",
            project_id="string",
            version="1",
        )
        assert content.is_closed
        assert content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        content = client.projects.artifacts.contents.with_raw_response.download(
            "string",
            project_id="string",
            version="1",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert content.json() == {"foo": "bar"}
        assert isinstance(content, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Docugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.projects.artifacts.contents.with_streaming_response.download(
            "string",
            project_id="string",
            version="1",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, StreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.artifacts.contents.with_raw_response.download(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.projects.artifacts.contents.with_raw_response.download(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.projects.artifacts.contents.with_raw_response.download(
                "",
                project_id="string",
                version="1",
            )

    @parametrize
    def test_method_upload(self, client: Docugami) -> None:
        content = client.projects.artifacts.contents.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        )
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Docugami) -> None:
        content = client.projects.artifacts.contents.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
            document_id="string",
        )
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Docugami) -> None:
        response = client.projects.artifacts.contents.with_raw_response.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Docugami) -> None:
        with client.projects.artifacts.contents.with_streaming_response.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(Artifact, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Docugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.artifacts.contents.with_raw_response.upload(
                "1",
                project_id="",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.projects.artifacts.contents.with_raw_response.upload(
                "",
                project_id="string",
                file=b"raw file contents",
            )


class TestAsyncContents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        content = await async_client.projects.artifacts.contents.download(
            "string",
            project_id="string",
            version="1",
        )
        assert content.is_closed
        assert await content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        content = await async_client.projects.artifacts.contents.with_raw_response.download(
            "string",
            project_id="string",
            version="1",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await content.json() == {"foo": "bar"}
        assert isinstance(content, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncDocugami, respx_mock: MockRouter) -> None:
        respx_mock.get("/projects/string/artifacts/1/string/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.projects.artifacts.contents.with_streaming_response.download(
            "string",
            project_id="string",
            version="1",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.artifacts.contents.with_raw_response.download(
                "string",
                project_id="",
                version="1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.projects.artifacts.contents.with_raw_response.download(
                "string",
                project_id="string",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.projects.artifacts.contents.with_raw_response.download(
                "",
                project_id="string",
                version="1",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncDocugami) -> None:
        content = await async_client.projects.artifacts.contents.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        )
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncDocugami) -> None:
        content = await async_client.projects.artifacts.contents.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
            document_id="string",
        )
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncDocugami) -> None:
        response = await async_client.projects.artifacts.contents.with_raw_response.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(Artifact, content, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncDocugami) -> None:
        async with async_client.projects.artifacts.contents.with_streaming_response.upload(
            "1",
            project_id="string",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(Artifact, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncDocugami) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.artifacts.contents.with_raw_response.upload(
                "1",
                project_id="",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.projects.artifacts.contents.with_raw_response.upload(
                "",
                project_id="string",
                file=b"raw file contents",
            )
