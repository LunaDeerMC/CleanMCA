[中文版 (Chinese Version)](README_zh.md)

# CleanMCA

CleanMCA is a Bash script for cleaning up unnecessary files in the `region`, `poi`, and `entities` directories of a Minecraft world save. By providing a whitelist file, the script will automatically delete any `.mca` files not listed, helping you reduce world size and free up space.

## Features
- Keeps only the `.mca` files specified in the whitelist.
- Processes the `region`, `poi`, and `entities` directories simultaneously.
- Checks parameters and paths before operation to prevent mistakes.
- **Irreversible operation**—please back up your world before use.

## Usage

### 1. Prepare the Whitelist File
The whitelist is a plain text file, with one `.mca` filename per line, for example:
```
r.0.0.mca
r.0.1.mca
r.1.0.mca
```

You can use the [Dominion](https://dominion.lunadeer.cn/) plugin to generate a whitelist based on land claims.

### 2. Run the Script
In your terminal, execute:

```bash
bash CleanMCA.sh --mca <whitelist_file_path> --region <region_directory_path>
```
Or use short options:
```bash
bash CleanMCA.sh -m <whitelist_file_path> -r <region_directory_path>
```

Parameter description:
- `--mca` or `-m`: Path to the whitelist file.
- `--region` or `-r`: Path to the Minecraft world's `region` directory.

### 3. Example
```bash
bash CleanMCA.sh -m whitelist.txt -r /path/to/world/region
```

The script will process the `region`, `poi`, and `entities` directories, deleting files not in the whitelist.

## Notes
- **This operation is irreversible. Please back up your world before running the script!**
- Requires a Bash-compatible environment (Linux, WSL, Git Bash, etc.).
- Requires common command-line tools: `getopt`, `realpath`, `grep`, etc.

## License

This project is licensed under the MIT License.
