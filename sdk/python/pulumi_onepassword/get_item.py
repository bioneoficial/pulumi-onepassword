# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetItemResult',
    'AwaitableGetItemResult',
    'get_item',
    'get_item_output',
]

@pulumi.output_type
class GetItemResult:
    """
    A collection of values returned by getItem.
    """
    def __init__(__self__, category=None, credential=None, database=None, files=None, hostname=None, id=None, note_value=None, password=None, port=None, private_key=None, public_key=None, sections=None, tags=None, title=None, type=None, url=None, username=None, uuid=None, vault=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if credential and not isinstance(credential, str):
            raise TypeError("Expected argument 'credential' to be a str")
        pulumi.set(__self__, "credential", credential)
        if database and not isinstance(database, str):
            raise TypeError("Expected argument 'database' to be a str")
        pulumi.set(__self__, "database", database)
        if files and not isinstance(files, list):
            raise TypeError("Expected argument 'files' to be a list")
        pulumi.set(__self__, "files", files)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if note_value and not isinstance(note_value, str):
            raise TypeError("Expected argument 'note_value' to be a str")
        pulumi.set(__self__, "note_value", note_value)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if port and not isinstance(port, str):
            raise TypeError("Expected argument 'port' to be a str")
        pulumi.set(__self__, "port", port)
        if private_key and not isinstance(private_key, str):
            raise TypeError("Expected argument 'private_key' to be a str")
        pulumi.set(__self__, "private_key", private_key)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if sections and not isinstance(sections, list):
            raise TypeError("Expected argument 'sections' to be a list")
        pulumi.set(__self__, "sections", sections)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if vault and not isinstance(vault, str):
            raise TypeError("Expected argument 'vault' to be a str")
        pulumi.set(__self__, "vault", vault)

    @property
    @pulumi.getter
    def category(self) -> str:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def credential(self) -> str:
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter
    def database(self) -> str:
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def files(self) -> Optional[Sequence['outputs.GetItemFileResult']]:
        return pulumi.get(self, "files")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="noteValue")
    def note_value(self) -> str:
        return pulumi.get(self, "note_value")

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> str:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> str:
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def sections(self) -> Optional[Sequence['outputs.GetItemSectionResult']]:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> str:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def vault(self) -> str:
        return pulumi.get(self, "vault")


class AwaitableGetItemResult(GetItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetItemResult(
            category=self.category,
            credential=self.credential,
            database=self.database,
            files=self.files,
            hostname=self.hostname,
            id=self.id,
            note_value=self.note_value,
            password=self.password,
            port=self.port,
            private_key=self.private_key,
            public_key=self.public_key,
            sections=self.sections,
            tags=self.tags,
            title=self.title,
            type=self.type,
            url=self.url,
            username=self.username,
            uuid=self.uuid,
            vault=self.vault)


def get_item(files: Optional[Sequence[Union['GetItemFileArgs', 'GetItemFileArgsDict']]] = None,
             note_value: Optional[str] = None,
             sections: Optional[Sequence[Union['GetItemSectionArgs', 'GetItemSectionArgsDict']]] = None,
             title: Optional[str] = None,
             uuid: Optional[str] = None,
             vault: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetItemResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['files'] = files
    __args__['noteValue'] = note_value
    __args__['sections'] = sections
    __args__['title'] = title
    __args__['uuid'] = uuid
    __args__['vault'] = vault
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('onepassword:index/getItem:getItem', __args__, opts=opts, typ=GetItemResult).value

    return AwaitableGetItemResult(
        category=pulumi.get(__ret__, 'category'),
        credential=pulumi.get(__ret__, 'credential'),
        database=pulumi.get(__ret__, 'database'),
        files=pulumi.get(__ret__, 'files'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        note_value=pulumi.get(__ret__, 'note_value'),
        password=pulumi.get(__ret__, 'password'),
        port=pulumi.get(__ret__, 'port'),
        private_key=pulumi.get(__ret__, 'private_key'),
        public_key=pulumi.get(__ret__, 'public_key'),
        sections=pulumi.get(__ret__, 'sections'),
        tags=pulumi.get(__ret__, 'tags'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'),
        url=pulumi.get(__ret__, 'url'),
        username=pulumi.get(__ret__, 'username'),
        uuid=pulumi.get(__ret__, 'uuid'),
        vault=pulumi.get(__ret__, 'vault'))


@_utilities.lift_output_func(get_item)
def get_item_output(files: Optional[pulumi.Input[Optional[Sequence[Union['GetItemFileArgs', 'GetItemFileArgsDict']]]]] = None,
                    note_value: Optional[pulumi.Input[Optional[str]]] = None,
                    sections: Optional[pulumi.Input[Optional[Sequence[Union['GetItemSectionArgs', 'GetItemSectionArgsDict']]]]] = None,
                    title: Optional[pulumi.Input[Optional[str]]] = None,
                    uuid: Optional[pulumi.Input[Optional[str]]] = None,
                    vault: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetItemResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
