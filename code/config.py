import json
from datetime import datetime, timedelta
import pytz
from croniter import croniter
import asyncio
import subprocess


def getScript(mins):
    scripts = []
    with open("config.json") as f:
        cron = json.load(f)
    beijing_timezone = pytz.timezone("Asia/Shanghai")
    now_beijing = datetime.now(beijing_timezone)
    for name, expr in cron.items():
        it = croniter(expr, now_beijing)
        prev = it.get_prev(datetime)
        if now_beijing - prev < timedelta(minutes=mins):
            print(f"{name} is due")
            scripts.append(name)

    return scripts


async def run_scripts(scripts, max_concurrent):
    tasks = []
    count = max_concurrent
    for i, script in enumerate(scripts):
        if i > count:
            await tasks[i - count]
            del tasks[i - count]
        print(f"run script: {script}")
        name = "./" + script
        tasks.append(run_script(name))

    await asyncio.gather(*tasks)


async def run_script(name):
    process = await asyncio.create_subprocess_exec(
        process.executable,
        name,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    while True:
        stdout_line = await process.stdout.readline()
        if not stdout_line:
            break
        print(stdout_line.decode().strip())

    await process.wait()
    print(f"{name} finished")


if __name__ == "__main__":
    scripts = getScript(60)
    count = 4
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_scripts(scripts, count))
    loop.close()

    print("执行完毕")
