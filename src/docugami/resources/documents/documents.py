# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from ...types import document_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from .contents import (
    ContentsResource,
    AsyncContentsResource,
    ContentsResourceWithRawResponse,
    AsyncContentsResourceWithRawResponse,
    ContentsResourceWithStreamingResponse,
    AsyncContentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDocumentsPage, AsyncDocumentsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.document import Document

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def contents(self) -> ContentsResource:
        return ContentsResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/docugami/docugami-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/docugami/docugami-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Get a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        docset: document_list_params.Docset | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_pages: int | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        min_pages: int | NotGiven = NOT_GIVEN,
        min_size: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        samples: bool | NotGiven = NOT_GIVEN,
        status: Literal["New", "Ingesting", "Ingested", "Processing", "Ready", "Error"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDocumentsPage[Document]:
        """
        List documents

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          limit: Maximum number of items to return.

          max_pages: Filters documents by maximum number of pages in the document.

          max_size: Filters documents by maximum file size in bytes.

          min_pages: Filters documents by minimum number of pages in the document.

          min_size: Filters documents by minimum file size in bytes.

          name: Filters documents by name, excluding any prefix.

          prefix: Filters documents by `name` beginning with this prefix.

          samples: Whether or not to return sample documents.

          status: Filters documents by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents",
            page=SyncDocumentsPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "docset": docset,
                        "limit": limit,
                        "max_pages": max_pages,
                        "max_size": max_size,
                        "min_pages": min_pages,
                        "min_size": min_size,
                        "name": name,
                        "prefix": prefix,
                        "samples": samples,
                        "status": status,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def contents(self) -> AsyncContentsResource:
        return AsyncContentsResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/docugami/docugami-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/docugami/docugami-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Get a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        docset: document_list_params.Docset | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_pages: int | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        min_pages: int | NotGiven = NOT_GIVEN,
        min_size: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        samples: bool | NotGiven = NOT_GIVEN,
        status: Literal["New", "Ingesting", "Ingested", "Processing", "Ready", "Error"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncDocumentsPage[Document]]:
        """
        List documents

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          limit: Maximum number of items to return.

          max_pages: Filters documents by maximum number of pages in the document.

          max_size: Filters documents by maximum file size in bytes.

          min_pages: Filters documents by minimum number of pages in the document.

          min_size: Filters documents by minimum file size in bytes.

          name: Filters documents by name, excluding any prefix.

          prefix: Filters documents by `name` beginning with this prefix.

          samples: Whether or not to return sample documents.

          status: Filters documents by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents",
            page=AsyncDocumentsPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "docset": docset,
                        "limit": limit,
                        "max_pages": max_pages,
                        "max_size": max_size,
                        "min_pages": min_pages,
                        "min_size": min_size,
                        "name": name,
                        "prefix": prefix,
                        "samples": samples,
                        "status": status,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithRawResponse:
        return ContentsResourceWithRawResponse(self._documents.contents)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._documents.pages)


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithRawResponse:
        return AsyncContentsResourceWithRawResponse(self._documents.contents)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._documents.pages)


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )

    @cached_property
    def contents(self) -> ContentsResourceWithStreamingResponse:
        return ContentsResourceWithStreamingResponse(self._documents.contents)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._documents.pages)


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )

    @cached_property
    def contents(self) -> AsyncContentsResourceWithStreamingResponse:
        return AsyncContentsResourceWithStreamingResponse(self._documents.contents)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._documents.pages)
