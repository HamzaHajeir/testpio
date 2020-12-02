import subprocess

projectTag = (
    subprocess.run(['git', 'describe','--tags','--abbrev=0'], capture_output=True, text=True).stdout
)
revision = (
    subprocess.run(['git', 'rev-parse','HEAD','--short=10'], capture_output=True, text=True).stdout
)
gitDescribeOutput = (
    subprocess.run(['git', 'describe','--tags','--abbrev=10'], capture_output=True, text=True).stdout
)
info = gitDescribeOutput.split('-')


Import("env")

print(env)

env.Append(CPPDEFINES=[
  ("GIT_REV", "\"%s\""%revision.strip()),
  ("GIT_REV_NO", "0x%s"%revision),
  ("MEEZANI_VERSION", projectTag),
  ("AHEAD_COMMITS", info[1])
])

