# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.projects.artifact import Artifact
from ....types.projects.artifacts import content_upload_params

__all__ = ["ContentsResource", "AsyncContentsResource"]


class ContentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/docugami/docugami-python#accessing-raw-response-data-eg-headers
        """
        return ContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/docugami/docugami-python#with_streaming_response
        """
        return ContentsResourceWithStreamingResponse(self)

    def download(
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
    ) -> BinaryAPIResponse:
        """
        Downloads an artifact

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
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        version: str,
        *,
        project_id: str,
        file: FileTypes,
        document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Artifact:
        """The maximum request size is 150 MB.

        The allowed file extensions are: .xml,
        .json, .csv, .xlsx, .pdf, and .docx.

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
        body = deepcopy_minimal(
            {
                "file": file,
                "document_id": document_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/projects/{project_id}/artifacts/{version}/content",
            body=maybe_transform(body, content_upload_params.ContentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )


class AsyncContentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/docugami/docugami-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/docugami/docugami-python#with_streaming_response
        """
        return AsyncContentsResourceWithStreamingResponse(self)

    async def download(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads an artifact

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
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/projects/{project_id}/artifacts/{version}/{artifact_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        version: str,
        *,
        project_id: str,
        file: FileTypes,
        document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Artifact:
        """The maximum request size is 150 MB.

        The allowed file extensions are: .xml,
        .json, .csv, .xlsx, .pdf, and .docx.

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
        body = deepcopy_minimal(
            {
                "file": file,
                "document_id": document_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/projects/{project_id}/artifacts/{version}/content",
            body=await async_maybe_transform(body, content_upload_params.ContentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )


class ContentsResourceWithRawResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.download = to_custom_raw_response_wrapper(
            contents.download,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            contents.upload,
        )


class AsyncContentsResourceWithRawResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.download = async_to_custom_raw_response_wrapper(
            contents.download,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            contents.upload,
        )


class ContentsResourceWithStreamingResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.download = to_custom_streamed_response_wrapper(
            contents.download,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            contents.upload,
        )


class AsyncContentsResourceWithStreamingResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.download = async_to_custom_streamed_response_wrapper(
            contents.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            contents.upload,
        )
