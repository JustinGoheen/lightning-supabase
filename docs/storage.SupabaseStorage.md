### SupabaseStorage


```python
lightning_supabase.storage.component.SupabaseStorage(
    parallel=False,
    cache_calls=True,
    raise_exception=True,
    host="127.0.0.1",
    port=None,
    local_build_config=None,
    cloud_build_config=None,
    start_with_flow=True,
    cloud_compute_name="default",
    cloud_compute_disk_size=0,
    cloud_compute_idle_timeout=60,
    cloud_compute_shm_size=0,
    cloud_compute_interruptible=False,
    cloud_compute_internal_id=None,
)
```


A custom LightningWork to Drive Supabase Bucket Operations

__Notes__

- LightningWork [docs](https://lightning.ai/docs/app/stable/core_api/lightning_work/lightning_work.html).
- CloudCompute [docs](https://lightning.ai/docs/app/stable/core_api/lightning_work/compute.html#cloudcompute).
- Supabase-Py [docs](https://supabase.com/docs/reference/python/initializing).


----

### create_bucket


```python
SupabaseStorage.create_bucket(bucket_name)
```


creates a bucket

__Arguments__

- __bucket_name__ `str`: the name to use when creating the bucket

__Notes__

see: https://supabase.com/docs/reference/python/storage-createbucket


----

### retrieve_bucket


```python
SupabaseStorage.retrieve_bucket(bucket_name)
```


retrieves a bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket to retrieve

__Notes__

see: https://supabase.com/docs/reference/python/storage-getbucket


----

### create_signed_url


```python
SupabaseStorage.create_signed_url(bucket_name, destination, expiry_duration)
```


creates a signed url

__Arguments__

- __bucket_name__ `str`:
- __destination__ `pathlib.Path | str`:
- __expiray_duration__: the length of time in seconds to keep the url alive

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-createsignedurl


----

### retrieve_public_url


```python
SupabaseStorage.retrieve_public_url(bucket_name, source)
```


Returns the URL for an asset in a public bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket
- __source__ `pathlib.Path | str`:

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-getpublicurl


----

### list_bucket_files


```python
SupabaseStorage.list_bucket_files(bucket_name)
```


lists files in a user defined bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket to show the contents of

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-list


----

### delete_files_from_bucket


```python
SupabaseStorage.delete_files_from_bucket(bucket_name, files)
```


deletes user defined files from specified bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket where the files are located
- __files__ `List[pathlib.Path | str]`: a Python list of files, including file format ending

__Notes__

see: https://supabase.com/docs/reference/python/storage-deletebucket


----

### move_files


```python
SupabaseStorage.move_files(bucket_name, files)
```


moves a list of user defined files

__Arguments__

- __bucket_name__ `str`: the name of the bucket where the files are located
- __files__ `List[pathlib.Path | str]`: a Python list of files, including file format ending

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-move


----

### delete_bucket


```python
SupabaseStorage.delete_bucket(bucket_name)
```


deletes a user defined bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket to delete

__Notes__

see: https://supabase.com/docs/reference/python/storage-deletebucket


----

### empty_bucket


```python
SupabaseStorage.empty_bucket(bucket_name)
```


empties a user defined bucket

__Arguments__

- __bucket_name__ `str`: the name of the bucket to empty

__Notes__

see: https://supabase.com/docs/reference/python/storage-emptybucket


----

### upload_to_bucket


```python
SupabaseStorage.upload_to_bucket(source, destination, bucket_name)
```


uploads a file to bucket

__Arguments__

- __source__ `pathlib.Path | str`:
- __destination__ `pathlib.Path | str`:
- __bucket_name__ `str`:

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-upload


----

### download_from_bucket


```python
SupabaseStorage.download_from_bucket(source, bucket_name)
```


downloads a file from bucket to a destination

__Arguments__

- __source__ `pathlib.Path | str`: the object to download
- __bucket_name__ `str`: the name of the bucket where source is located

__Notes__

see: https://supabase.com/docs/reference/python/storage-from-download


----

### mount


```python
SupabaseStorage.mount()
```


Abstract method that must be overidden to mount Supabase bucket to Lightning


----

### run


```python
SupabaseStorage.run()
```


Abstract method that must be overidden to define LightningWork.run flow


----
