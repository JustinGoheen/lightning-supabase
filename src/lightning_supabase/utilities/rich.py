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


import click
from rich import print as rprint
from rich.console import Console
from rich.table import Table


def show_table(command_name: str, asset_type: str, assets: list) -> None:
    # TITLE
    table = Table(title=f"{asset_type.title()} To Be {command_name.title()}")
    # COLUMNS
    table.add_column(f"{asset_type.title()}", justify="right", style="cyan", no_wrap=True)
    table.add_column(f"{asset_type.title()} Name", style="magenta")
    # ROWS
    for asset in assets:
        table.add_row(asset_type, asset)
    # SHOW
    console = Console()
    console.print(table)


def show_destructive_behavior_warning(command_name, asset_type, assets) -> None:
    """
    uses rich console markup

    notes: https://rich.readthedocs.io/en/stable/markup.html
    """
    print()
    rprint(":warning: [bold red]Alert![/bold red] This action has destructive behavior! :warning: ")
    print()
    rprint("The following directories will be [bold red]purged[/bold red]")
    print()
    show_table(command_name, asset_type, assets)
    print()


def common_destructive_flow(command, command_name: str, asset_type: str, assets: list) -> None:
    show_destructive_behavior_warning(command_name, asset_type, assets)
    if click.confirm("Do you want to continue"):
        command()
        print()
        rprint(f"[bold green]{command_name.title()} complete[bold green]")
        print()
    else:
        print()
        rprint("[bold green]No Action Taken[/bold green]")
        print()
