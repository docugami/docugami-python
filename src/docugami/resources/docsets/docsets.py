# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...types import docset_list_params, docset_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDocsetsPage, AsyncDocsetsPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.docset import Docset

__all__ = ["DocsetsResource", "AsyncDocsetsResource"]


class DocsetsResource(SyncAPIResource):
    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocsetsResourceWithRawResponse:
        return DocsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsetsResourceWithStreamingResponse:
        return DocsetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        documents: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Docset:
        """
        Create a docset

        Args:
          name: The name of the docset.

          documents: Optional collection of document ids to include in the new docset. Documents will
              be moved if they already belong to a docset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/docsets",
            body=maybe_transform(
                {
                    "name": name,
                    "documents": documents,
                },
                docset_create_params.DocsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Docset,
        )

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
    ) -> Docset:
        """
        Get a docset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/docsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Docset,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_documents: int | NotGiven = NOT_GIVEN,
        min_documents: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        samples: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDocsetsPage[Docset]:
        """
        List docsets

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          limit: Maximum number of items to return.

          max_documents: Filters docsets by maximum number of documents in the set.

          min_documents: Filters docsets by minimum number of documents in the set.

          name: Filters docsets by name.

          samples: Whether or not to return sample docsets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/docsets",
            page=SyncDocsetsPage[Docset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "max_documents": max_documents,
                        "min_documents": min_documents,
                        "name": name,
                        "samples": samples,
                    },
                    docset_list_params.DocsetListParams,
                ),
            ),
            model=Docset,
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
        Deleting a docset does _not_ delete any documents it contains.

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
            f"/docsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDocsetsResource(AsyncAPIResource):
    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocsetsResourceWithRawResponse:
        return AsyncDocsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsetsResourceWithStreamingResponse:
        return AsyncDocsetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        documents: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Docset:
        """
        Create a docset

        Args:
          name: The name of the docset.

          documents: Optional collection of document ids to include in the new docset. Documents will
              be moved if they already belong to a docset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/docsets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "documents": documents,
                },
                docset_create_params.DocsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Docset,
        )

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
    ) -> Docset:
        """
        Get a docset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/docsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Docset,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_documents: int | NotGiven = NOT_GIVEN,
        min_documents: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        samples: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Docset, AsyncDocsetsPage[Docset]]:
        """
        List docsets

        Args:
          cursor: Opaque continuation token used to get additional items when a previous query
              returned more than `limit` items.

          limit: Maximum number of items to return.

          max_documents: Filters docsets by maximum number of documents in the set.

          min_documents: Filters docsets by minimum number of documents in the set.

          name: Filters docsets by name.

          samples: Whether or not to return sample docsets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/docsets",
            page=AsyncDocsetsPage[Docset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "max_documents": max_documents,
                        "min_documents": min_documents,
                        "name": name,
                        "samples": samples,
                    },
                    docset_list_params.DocsetListParams,
                ),
            ),
            model=Docset,
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
        Deleting a docset does _not_ delete any documents it contains.

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
            f"/docsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DocsetsResourceWithRawResponse:
    def __init__(self, docsets: DocsetsResource) -> None:
        self._docsets = docsets

        self.create = to_raw_response_wrapper(
            docsets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            docsets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            docsets.list,
        )
        self.delete = to_raw_response_wrapper(
            docsets.delete,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._docsets.documents)


class AsyncDocsetsResourceWithRawResponse:
    def __init__(self, docsets: AsyncDocsetsResource) -> None:
        self._docsets = docsets

        self.create = async_to_raw_response_wrapper(
            docsets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            docsets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            docsets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            docsets.delete,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._docsets.documents)


class DocsetsResourceWithStreamingResponse:
    def __init__(self, docsets: DocsetsResource) -> None:
        self._docsets = docsets

        self.create = to_streamed_response_wrapper(
            docsets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            docsets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            docsets.list,
        )
        self.delete = to_streamed_response_wrapper(
            docsets.delete,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._docsets.documents)


class AsyncDocsetsResourceWithStreamingResponse:
    def __init__(self, docsets: AsyncDocsetsResource) -> None:
        self._docsets = docsets

        self.create = async_to_streamed_response_wrapper(
            docsets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            docsets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            docsets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            docsets.delete,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._docsets.documents)
