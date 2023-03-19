# Copyright Justin R. Goheen.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import os
from pathlib import Path
from typing import Any, List

import supabase
from lightning import CloudCompute, LightningWork


class SupabaseStore(LightningWork, abc.ABC):
    def __init__(
        self,
        parallel=False,
        cloud_compute=CloudCompute(name="default", idle_timeout=15),
    ):
        super().__init__(parallel=parallel, cloud_compute=cloud_compute)

    @property
    def available_buckets(self):
        return supabase.storage().list_buckets()

    def create_bucket(self, bucket_name: str, create_only: bool = False):
        if create_only:
            supabase.storage().create_bucket(bucket_name)
        else:
            return supabase.storage().create_bucket(bucket_name)

    def retrieve_bucket(self, bucket_name: str):
        return supabase.storage().get_bucket(bucket_name)

    def create_signed_url(self, bucket_name: str, destination: Path | str, expiry_duration: int):
        supabase.storage().from_(bucket_name).create_signed_url(destination, expiry_duration)

    def retrieve_signed_url(self, bucket_name: str, source: Path | str):
        supabase.storage().from_(bucket_name).get_public_url(source)

    def list_bucket_files(self, bucket_name: str) -> List[str]:
        return supabase.storage().from_(bucket_name).list()

    def delete_files_from_bucket(self, bucket_name: str, files: List[Path | str]) -> None:
        supabase.storage().from_(bucket_name).move(*files)

    def move_files(self, bucket_name: str, files: List[Path | str]) -> None:
        supabase.storage().from_(bucket_name).move(*files)

    def delete_bucket(self, bucket_name: str) -> None:
        supabase.storage().delete_bucket(bucket_name)

    def empty_bucket(self, bucket_name: str) -> None:
        supabase.storage().empty_bucket(bucket_name)

    def upload_to_bucket(self, source: Path | str, destination: Path | str, bucket_name: str) -> None:
        """uploads a file to bucket

        # Notes
            see: https://supabase.com/docs/reference/python/storage-from-upload
        """
        with open(source, "rb+"):
            supabase.storage().from_(bucket_name).upload(destination, os.path.abspath(source))

    def download_from_bucket(self, source: Path | str, bucket_name: str) -> Any:
        """downloads a file from bucket to a destination

        # Notes
            see: https://supabase.com/docs/reference/python/storage-from-download
        """

        with open(bucket_name, "wb+") as f:
            res = supabase.storage().from_(bucket_name).download(source)
            f.write(res)

    @abc.abstractmethod
    def mount(self) -> None:
        ...

    @abc.abstractmethod
    def run(self) -> None:
        ...
