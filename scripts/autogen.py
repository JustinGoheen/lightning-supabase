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


import os
import shutil
from pathlib import Path

from keras_autodoc import DocumentationGenerator

FILEPATH = Path(__file__)
project = FILEPATH.parents[1]
DOCSDIR = os.path.join(project, "docs")


class DocsGenerator:
    def build():

        pages = {
            "storage.SupabaseStorage.md": [
                "lightning_supabase.storage.component.SupabaseStorage",
                # "lightning_supabase.storage.component.SupabaseStorage.available_buckets",
                "lightning_supabase.storage.component.SupabaseStorage.create_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.retrieve_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.create_signed_url",
                "lightning_supabase.storage.component.SupabaseStorage.retrieve_public_url",
                "lightning_supabase.storage.component.SupabaseStorage.list_bucket_files",
                "lightning_supabase.storage.component.SupabaseStorage.delete_files_from_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.move_files",
                "lightning_supabase.storage.component.SupabaseStorage.delete_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.empty_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.upload_to_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.download_from_bucket",
                "lightning_supabase.storage.component.SupabaseStorage.mount",
                "lightning_supabase.storage.component.SupabaseStorage.run",
            ]
        }

        doc_generator = DocumentationGenerator(pages)
        doc_generator.generate(DOCSDIR)

        root_readme = os.path.join(project, "README.md")
        docs_intro = os.path.join(DOCSDIR, "index.md")

        shutil.copyfile(src=root_readme, dst=docs_intro)


if __name__ == "__main__":

    docgen = DocsGenerator
    docgen.build()
