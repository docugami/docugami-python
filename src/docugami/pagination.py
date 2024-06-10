# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

import httpx

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncDocumentsPage",
    "AsyncDocumentsPage",
    "SyncDocsetsPage",
    "AsyncDocsetsPage",
    "SyncPagesPage",
    "AsyncPagesPage",
    "SyncProjectsPage",
    "AsyncProjectsPage",
    "SyncWebhooksPage",
    "AsyncWebhooksPage",
    "SyncArtifactsPage",
    "AsyncArtifactsPage",
]

_T = TypeVar("_T")


class SyncDocumentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncDocumentsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class SyncDocsetsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    docsets: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        docsets = self.docsets
        if not docsets:
            return []
        return docsets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncDocsetsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    docsets: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        docsets = self.docsets
        if not docsets:
            return []
        return docsets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class SyncPagesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        pages = self.pages
        if not pages:
            return []
        return pages

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncPagesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        pages = self.pages
        if not pages:
            return []
        return pages

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class SyncProjectsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    projects: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncProjectsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    projects: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class SyncWebhooksPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    webhooks: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        webhooks = self.webhooks
        if not webhooks:
            return []
        return webhooks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncWebhooksPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    webhooks: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        webhooks = self.webhooks
        if not webhooks:
            return []
        return webhooks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class SyncArtifactsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    artifacts: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        artifacts = self.artifacts
        if not artifacts:
            return []
        return artifacts

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncArtifactsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    artifacts: List[_T]
    next: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        artifacts = self.artifacts
        if not artifacts:
            return []
        return artifacts

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = self.next
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))
