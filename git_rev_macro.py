import subprocess

projectTag = (
    subprocess.run(['git', 'describe','--tags','--abbrev=0'], capture_output=True, text=True).stdout
)
revision = (
    subprocess.run(['git', 'rev-parse','HEAD','--short=10'], capture_output=True, text=True).stdout
)
gitDescribeOutput = (
    subprocess.run(['git', 'describe','--tags'], capture_output=True, text=True).stdout
)
info = gitDescribeOutput.split('-')
projectTagNumber = projectTag.replace('.','0')


Import("env")

print(env)

env.Append(CPPDEFINES=[
  ("GIT_REV", "\"%s\""%revision.strip()),
  ("MEEZANI_VERSION", "\"%s\"" % projectTag),
  ("MEEZANI_VERSION_NO", projectTagNumber),
  ("AHEAD_COMMITS", info[1])
])

