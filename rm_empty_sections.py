"""

    """

import asyncio
from pathlib import Path

import pandas as pd
from todoist_api_python.api_async import TodoistAPIAsync

from models import Todoist
from models import TodoistSection
from models import TodoistTask
from util import del_sections
from util import get_all_sections
from util import get_daily_routine_project_id
from util import ret_not_special_items_of_a_class as rnsioac

to = Todoist()
tt = TodoistTask()
ttd = rnsioac(TodoistTask)
ts = TodoistSection()

async def get_all_tasks_async() :
    api = TodoistAPIAsync(to.tok)
    tsks = await api.get_tasks()
    return tsks

def get_all_tasks() :
    tsks = asyncio.run(get_all_tasks_async())
    df = pd.DataFrame()
    for col in ttd :
        df[col] = [getattr(x , col) for x in tsks]
    return df

def main() :
    pass

    ##
    dfs = get_all_sections()

    ##
    dft = get_all_tasks()

    ##
    inbox_id = '2266805950'

    msk = dft[tt.project_id].eq(inbox_id)
    dft = dft[~ msk]

    ##
    if False :
        pass

        ##
        to.proj_id = get_daily_routine_project_id()

    ##
    try :
        to.proj_id = get_daily_routine_project_id()

    # except the daily routine project does not exist
    except IndexError :
        return

    ##
    msk = dfs[ts.project_id].eq(to.proj_id)

    print('All sections count in the project: ' , len(msk[msk]))

    ##
    msk &= ~ dfs[ts.id].isin(dft[tt.section_id])

    print('Empty sections: ' , len(msk[msk]))

    ##
    msk &= ~ dfs[ts.name].str.contains('📌')

    print('Not pinned (!📌) and empty sections: ' , len(msk[msk]))

    ##
    del_sections(dfs.loc[msk , ts.id])

##


if __name__ == '__main__' :
    main()
    print(f'{Path(__file__).name} Done!')

##

if False :
    pass

    ##

    ##
