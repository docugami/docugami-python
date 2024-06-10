# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .contents import (
    ContentsResource,
    AsyncContentsResource,
    ContentsResourceWithRawResponse,
    AsyncContentsResourceWithRawResponse,
    ContentsResourceWithStreamingResponse,
    AsyncContentsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncArtifactsPage, AsyncArtifactsPage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.projects import artifact_list_params
from ....types.projects.artifact import Artifact

__all__ = ["ArtifactsResource", "AsyncArtifactsResource"]


class ArtifactsResource(SyncAPIResource):
    @cached_property
    def contents(self) -> ContentsResource:
        return ContentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        artifact_id: str,
        *,
        project_id: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Artifact:
        """
        Get an artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return self._get(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )

    def list(
        self,
        version: str | NotGiven = NOT_GIVEN,
        *,
        project_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        document: artifact_list_params.Document | NotGiven = NOT_GIVEN,
        is_read_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        min_size: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncArtifactsPage[Artifact]:
        """
        List artifacts

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          is_read_only: Filters artifacts by read-only status.

          limit: Maximum number of items to return.

          max_size: Filters artifacts by maximum file size in bytes

          min_size: Filters artifacts by minimum file size in bytes.

          name: Filters artifacts by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get_api_list(
            f"/projects/{project_id}/artifacts/{version}",
            page=SyncArtifactsPage[Artifact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "document": document,
                        "is_read_only": is_read_only,
                        "limit": limit,
                        "max_size": max_size,
                        "min_size": min_size,
                        "name": name,
                    },
                    artifact_list_params.ArtifactListParams,
                ),
            ),
            model=Artifact,
        )

    def delete(
        self,
        artifact_id: str,
        *,
        project_id: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Read-only artifacts cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncArtifactsResource(AsyncAPIResource):
    @cached_property
    def contents(self) -> AsyncContentsResource:
        return AsyncContentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        artifact_id: str,
        *,
        project_id: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Artifact:
        """
        Get an artifact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return await self._get(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )

    def list(
        self,
        version: str | NotGiven = NOT_GIVEN,
        *,
        project_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        document: artifact_list_params.Document | NotGiven = NOT_GIVEN,
        is_read_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        min_size: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Artifact, AsyncArtifactsPage[Artifact]]:
        """
        List artifacts

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          is_read_only: Filters artifacts by read-only status.

          limit: Maximum number of items to return.

          max_size: Filters artifacts by maximum file size in bytes

          min_size: Filters artifacts by minimum file size in bytes.

          name: Filters artifacts by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get_api_list(
            f"/projects/{project_id}/artifacts/{version}",
            page=AsyncArtifactsPage[Artifact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "document": document,
                        "is_read_only": is_read_only,
                        "limit": limit,
                        "max_size": max_size,
                        "min_size": min_size,
                        "name": name,
                    },
                    artifact_list_params.ArtifactListParams,
                ),
            ),
            model=Artifact,
        )

    async def delete(
        self,
        artifact_id: str,
        *,
        project_id: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Read-only artifacts cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.retrieve = to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            artifacts.list,
        )
        self.delete = to_raw_response_wrapper(
            artifacts.delete,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithRawResponse:
        return ContentsResourceWithRawResponse(self._artifacts.contents)


class AsyncArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.retrieve = async_to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            artifacts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            artifacts.delete,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithRawResponse:
        return AsyncContentsResourceWithRawResponse(self._artifacts.contents)


class ArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.retrieve = to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            artifacts.list,
        )
        self.delete = to_streamed_response_wrapper(
            artifacts.delete,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithStreamingResponse:
        return ContentsResourceWithStreamingResponse(self._artifacts.contents)


class AsyncArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.retrieve = async_to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            artifacts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            artifacts.delete,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithStreamingResponse:
        return AsyncContentsResourceWithStreamingResponse(self._artifacts.contents)
